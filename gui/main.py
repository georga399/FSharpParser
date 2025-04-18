import os
import sys
import time
import locale
import json
from math import log2

import gi

import parser.FParserTable

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk, Gdk, GObject, Pango


class EditorWindow(Gtk.ApplicationWindow):
    # A sentence with more than SENTENCE_SHORT characters is not short.
    SENTENCE_SHORT = 50
    # A sentence with more than SENTENCE_LONG characters is long.
    SENTENCE_LONG = 60

    def __init__(self, app, file=None):
        content = ""

        self.title = _("TextView Editor")
        self.user_action = False
        self.undo = []  # undo buffer
        self.redo = []  # redo buffer

        if file:
            try:
                [success, content, etags] = file.load_contents(None)
                content = content.decode("utf-8", "ignore")
            except GObject.GError as e:
                file = None
                print("Error: " + e.message)
        super().__init__(application=app)
        self.set_default_size(720, 400)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        grid = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(grid)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        self.textview = Gtk.TextView()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textview.set_monospace(True)

        scrolled_window.add(self.textview)
        grid.pack_start(scrolled_window, True, True, 0)

        self.searchbar = Gtk.SearchBar()
        # We use Gtk.Entry since Gtk.SearchEntry does not support IME
        # at this point.
        self.search_entry = Gtk.Entry()
        self.searchbar.add(self.search_entry)
        self.searchbar.connect_entry(self.search_entry)
        grid.pack_start(self.searchbar, False, False, 0)
        self.searchbar.set_search_mode(False)
        self.search_entry.connect("activate", self.on_find)

        self.replacebar = Gtk.SearchBar()
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.replacebar.add(box)
        self.replace_from = Gtk.Entry()
        box.pack_start(self.replace_from, False, False, 1)
        self.replace_to = Gtk.Entry()
        box.pack_start(self.replace_to, False, False, 1)
        self.replacebar.connect_entry(self.replace_from)
        grid.pack_start(self.replacebar, False, False, 0)
        self.replacebar.set_search_mode(False)
        self.replace_from.connect("activate", self.on_find)
        self.replace_to.connect("activate", self.on_replace)

        self.connect("key-press-event", self.on_key_press_event)

        self.buffer = self.textview.get_buffer()
        if content:
            self.buffer.set_text(content)
            self.buffer.set_modified(False)
            self.buffer.place_cursor(self.buffer.get_start_iter())
        self.buffer.connect("insert_text", self.on_insert)
        self.buffer.connect("delete_range", self.on_delete)
        self.buffer.connect("begin_user_action", self.on_begin_user_action)
        self.buffer.connect("end_user_action", self.on_end_user_action)
        self.buffer.connect_after("insert_text", self.on_inserted)
        self.buffer.connect_after("delete_range", self.on_deleted)

        actions = {
            "new": self.new_callback,
            "open": self.open_callback,
            "save": self.save_callback,
            "saveas": self.save_as_callback,
            "close": self.close_callback,
            "closeall": self.close_all_callback,
            "undo": self.undo_callback,
            "redo": self.redo_callback,
            "cut": self.cut_callback,
            "copy": self.copy_callback,
            "paste": self.paste_callback,
            "find": self.find_callback,
            "replace": self.replace_callback,
            "selectall": self.select_all_callback,
            "font": self.font_callback,
            "about": self.about_callback,
            "parse": self.parse_callback
        }
        for name, method in actions.items():
            action = Gio.SimpleAction.new(name, None)
            action.connect("activate", method)
            self.add_action(action)
        self.connect("delete-event", self.on_delete_event)

        action = Gio.SimpleAction.new_stateful(
            "wordwrap", None, GLib.Variant.new_boolean(True))
        action.connect("activate", self.wordwrap_callback)
        self.add_action(action)

        self.highlightlongsentences_action = Gio.SimpleAction.new_stateful(
            "highlightlongsentences", None, GLib.Variant.new_boolean(False))
        self.highlightlongsentences_action.connect(
            "activate", self.highlightlongsentences_callback)
        self.add_action(self.highlightlongsentences_action)

        self.set_file(file)

        self.tag_yellow = self.buffer.create_tag(
            "yellow", background="light yellow")
        self.tag_red = self.buffer.create_tag(
            "red", background="light pink")
        self.check_sentences(self.highlightlongsentences_action.get_state())

    def check_sentences(self, highlight):
        if not highlight:
            return
        bounds = self.buffer.get_bounds()
        self.buffer.remove_all_tags(bounds[0], bounds[1])
        text = self.buffer.get_text(bounds[0], bounds[1], False)
        start = end = 0
        text_length = len(text)
        for i in range(text_length):
            c = text[i]
            if start == end:
                if c in "\n\r\t 　":
                    start += 1
                    end = start
                    continue
            end = i + 1
            if c in "\n\r　 。．？！" or text_length <= end:
                if c in "\n\r　 ":
                    end -= 1
                count = end - start
                if self.SENTENCE_SHORT < count:
                    s = self.buffer.get_iter_at_offset(start)
                    e = self.buffer.get_iter_at_offset(end)
                    if self.SENTENCE_LONG < count:
                        self.buffer.apply_tag(self.tag_red, s, e)
                    else:
                        self.buffer.apply_tag(self.tag_yellow, s, e)
                start = end = i + 1

    def on_key_press_event(self, widget, event):
        # Control focus around search bars by checking keys typed into the
        # main window
        if self.search_entry.is_focus():
            if event.keyval == Gdk.KEY_Escape:
                self.searchbar.set_search_mode(False)
                self.textview.grab_focus()
                return True
        if self.replace_to.is_focus() or self.replace_from.is_focus():
            if event.keyval == Gdk.KEY_Tab or event.keyval == Gdk.KEY_ISO_Left_Tab:
                if self.replace_to.is_focus():
                    self.replacebar.connect_entry(self.replace_from)
                    self.replace_from.grab_focus()
                elif self.replace_from.is_focus():
                    self.replacebar.connect_entry(self.replace_to)
                    self.replace_to.grab_focus()
                return True
            if event.keyval == Gdk.KEY_Escape:
                self.replacebar.set_search_mode(False)
                self.textview.grab_focus()
                return True
        return False

    def set_file(self, file):
        self.file = file
        if self.file:
            self.buffer.set_modified(False)
            self.undo = []
            self.redo = []
            self.set_title(file.get_basename() + " ― " + self.title)
            return False
        else:
            self.set_title(self.title)
            return True

    def is_opened(self, file):
        windows = self.get_application().get_windows()
        for window in windows:
            if window.file and window.file.equal(file):
                return window
        return None

    def on_insert(self, textbuffer, iter, text, length):
        if self.user_action:
            self.undo.append(["insert_text", iter.get_offset(), text,
                              time.perf_counter()])
            self.redo.clear()

    def on_inserted(self, textbuffer, iter, text, length):
        self.check_sentences(self.highlightlongsentences_action.get_state())

    def on_delete(self, textbuffer, start, end):
        if self.user_action:
            text = self.buffer.get_text(start, end, True)
            self.undo.append(["delete_range", start.get_offset(), text,
                              time.perf_counter()])
            self.redo.clear()

    def on_deleted(self, textbuffer, start, end):
        self.check_sentences(self.highlightlongsentences_action.get_state())

    def on_begin_user_action(self, textbuffer):
        self.user_action = True

    def on_end_user_action(self, textbuffer):
        self.user_action = False

    def new_callback(self, action, parameter):
        win = EditorWindow(self.get_application())
        win.show_all()

    def open_callback(self, action, parameter):
        open_dialog = Gtk.FileChooserDialog(
            _("Open File"), self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))
        self.add_filters(open_dialog)
        open_dialog.set_local_only(False)
        open_dialog.set_modal(True)
        open_dialog.connect("response", self.open_response_cb)
        open_dialog.show()

    def open_response_cb(self, dialog, response):
        file = None
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
        dialog.destroy()
        # open new window after closing dialog to raise the new window
        # in the stacking order.
        if file:
            win = self.is_opened(file)
            if win:
                win.present()
                return
            win = EditorWindow(self.get_application(), file=file)
            win.show_all()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name(_("Text files"))
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name(_("Python files"))
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name(_("Any files"))
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def save(self):
        [start, end] = self.buffer.get_bounds()
        current_contents = self.buffer.get_text(start, end, False)
        if current_contents:
            try:
                current_contents = current_contents.encode()
                self.file.replace_contents(current_contents, None, False, Gio.FileCreateFlags.NONE, None)
            except GObject.GError as e:
                self.file = None
        else:
            try:
                self.file.replace_readwrite(None, False, Gio.FileCreateFlags.NONE, None)
            except GObject.GError as e:
                self.file = None
        return self.set_file(self.file)

    def save_as(self):
        dialog = Gtk.FileChooserDialog(
            _("Save File"), self,
            Gtk.FileChooserAction.SAVE,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        dialog.set_do_overwrite_confirmation(True)
        dialog.set_modal(True)
        if self.file is not None:
            try:
                dialog.set_file(self.file)
            except GObject.GError as e:
                print("Error: " + e.message)
        response = dialog.run()
        if response == Gtk.ResponseType.ACCEPT:
            self.file = dialog.get_file()
            dialog.destroy()
            return self.save()
        dialog.destroy()
        return self.set_file(None)

    def confirm_save_changes(self):
        if not self.buffer.get_modified():
            return False
        dialog = Gtk.MessageDialog(
            self, 0, Gtk.MessageType.QUESTION,
            Gtk.ButtonsType.NONE, _("Save changes to this document?"))
        dialog.format_secondary_text(
            _("If you don't, changes will be lost."))
        dialog.add_button(_("Close _Without Saving"), Gtk.ResponseType.NO)
        dialog.add_button(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
        dialog.add_button(Gtk.STOCK_SAVE, Gtk.ResponseType.YES)
        dialog.set_default_response(Gtk.ResponseType.YES)
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.NO:
            return False
        elif response == Gtk.ResponseType.YES:
            # close the window after saving changes
            self.close_after_save = True
            if self.file is not None:
                return self.save()
            else:
                return self.save_as()
        else:
            return True

    def save_callback(self, action, parameter):
        if self.file is not None:
            self.save()
        else:
            self.save_as()

    def save_as_callback(self, action, parameter):
        self.save_as()

    def close_callback(self, action, parameter):
        if not self.confirm_save_changes():
            self.destroy()

    def close_all_callback(self, action, parameter):
        windows = self.get_application().get_windows()
        for window in windows:
            window.lookup_action("close").activate()

    def on_delete_event(self, widget, event):
        return self.confirm_save_changes()

    def undo_callback(self, action, parameter):
        if not self.undo or not self.textview.is_focus():
            return
        action = self.undo.pop()
        if action[0] == "insert_text":
            start = self.buffer.get_iter_at_offset(action[1])
            end = self.buffer.get_iter_at_offset(action[1] + len(action[2]))
            self.buffer.delete(start, end)
            # undo previous delete_range that issued within 1 msec
            # to cope with ibus-replace-with-kanji smoothly
            if self.undo:
                prev = self.undo[-1]
                if prev[0] == "delete_range" and action[3] - prev[3] < 0.001:
                    self.redo.append(action)
                    action = self.undo.pop()
                    start = self.buffer.get_iter_at_offset(action[1])
                    self.buffer.insert(start, action[2])
        elif action[0] == "delete_range":
            start = self.buffer.get_iter_at_offset(action[1])
            self.buffer.insert(start, action[2])
        self.redo.append(action)

    def redo_callback(self, action, parameter):
        if not self.redo or not self.textview.is_focus():
            return
        action = self.redo.pop()
        if action[0] == "insert_text":
            start = self.buffer.get_iter_at_offset(action[1])
            self.buffer.insert(start, action[2])
        elif action[0] == "delete_range":
            start = self.buffer.get_iter_at_offset(action[1])
            end = self.buffer.get_iter_at_offset(action[1] + len(action[2]))
            self.buffer.delete(start, end)
            # redo previous insert_text that issued within 1 msec
            # to cope with ibus-replace-with-kanji smoothly
            if self.redo:
                prev = self.redo[-1]
                if prev[0] == "insert_text" and action[3] - prev[3] < 0.001:
                    self.undo.append(action)
                    action = self.redo.pop()
                    start = self.buffer.get_iter_at_offset(action[1])
                    self.buffer.insert(start, action[2])
        self.undo.append(action)

    def cut_callback(self, action, parameter):
        self.buffer.cut_clipboard(self.clipboard, self.textview.get_editable())
        self.textview.scroll_mark_onscreen(self.buffer.get_insert())

    def copy_callback(self, action, parameter):
        self.buffer.copy_clipboard(self.clipboard)

    def paste_callback(self, action, parameter):
        text = self.clipboard.wait_for_text()
        if text is not None:
            self.buffer.begin_user_action()
            self.buffer.insert_at_cursor(text)
            self.buffer.end_user_action()

    def find_callback(self, action, parameter):
        self.searchbar.set_search_mode(True)

    def select_text(self, text):
        cursor_mark = self.buffer.get_insert()
        start = self.buffer.get_iter_at_mark(cursor_mark)
        selecton_mark = self.buffer.get_selection_bound()
        selected = self.buffer.get_iter_at_mark(selecton_mark)
        if start.get_offset() < selected.get_offset():
            start = selected
        match = start.forward_search(text, 0, None)
        if match is None:
            start = self.buffer.get_start_iter()
            match = start.forward_search(text, 0, None)
        if match is not None:
            match_start, match_end = match
            self.buffer.select_range(match_start, match_end)
            self.textview.scroll_mark_onscreen(self.buffer.get_insert())
        return match

    def on_find(self, entry):
        self.select_text(entry.get_text())

    def replace_callback(self, action, parameter):
        self.replacebar.set_search_mode(True)

    def on_replace(self, entry):
        match = self.select_text(self.replace_from.get_text())
        if match is None:
            return
        self.buffer.begin_user_action()
        self.buffer.delete(match[0], match[1])
        text = self.replace_to.get_text()
        if text is not None:
            self.buffer.insert_at_cursor(text)
            cursor_mark = self.buffer.get_insert()
            end = self.buffer.get_iter_at_mark(cursor_mark)
            start = end.copy()
            start.backward_chars(len(text))
            self.textview.scroll_mark_onscreen(cursor_mark)
            self.buffer.select_range(start, end)
        self.buffer.end_user_action()

    def select_all_callback(self, action, parameter):
        start, end = self.buffer.get_bounds()
        self.buffer.select_range(start, end)

    def font_callback(self, action, parameter):
        dialog = Gtk.FontChooserDialog(_("Font"), self)
        dialog.props.preview_text = _("The quick brown fox jumps over the lazy dog.")
        style = self.textview.get_style()
        dialog.set_font_desc(style.font_desc)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            font = dialog.get_font()
            if font:
                self.textview.modify_font(
                    Pango.font_description_from_string(font))
        dialog.destroy()

    def wordwrap_callback(self, action, parameter):
        wordwrap = not action.get_state()
        action.set_state(GLib.Variant.new_boolean(wordwrap))
        if wordwrap:
            self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        else:
            self.textview.set_wrap_mode(Gtk.WrapMode.NONE)

    def highlightlongsentences_callback(self, action, parameter):
        highlight = not action.get_state()
        action.set_state(GLib.Variant.new_boolean(highlight))
        if highlight:
            self.check_sentences(highlight)
        else:
            bounds = self.buffer.get_bounds()
            self.buffer.remove_all_tags(bounds[0], bounds[1])

    def about_callback(self, action, parameter):
        dialog = Gtk.AboutDialog()
        dialog.set_transient_for(self)

        authors = ["Nikita Senko", "Egor Azarov"]

        dialog.set_program_name(self.title)
        dialog.set_copyright("Copyright 2025 Pasechnik Ink.")
        dialog.set_authors(authors)
        dialog.set_logo_icon_name("textview-editor")

        # to close the dialog when "close" is clicked, e.g. on RPi,
        # we connect the "response" signal to about_response_callback
        dialog.connect("response", self.about_response_callback)
        dialog.show()

    def about_response_callback(self, dialog, response):
        dialog.destroy()

    def parse_callback(self, action, parameter):
        parser_table = parser.FParserTable.FParserTable()
        buf = self.textview.get_buffer()
        parser_table.SetText(
            text=buf.get_text(start=buf.get_start_iter(), end=buf.get_end_iter(), include_hidden_chars=False))

        window = Gtk.Window()
        window.set_default_size(1000, 500)
        window.set_title("FParser Table")
        window.connect("destroy", Gtk.main_quit)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        window.add(scrolled_window)

        # Create a table to hold the labels
        table = Gtk.Table(5, 2, True)
        scrolled_window.add(table)

        row = 0

        label_tmp = Gtk.Label()
        label_tmp.set_markup("<b>Operators:</b>")
        table.attach(label_tmp, 0, 1, row, row + 1)
        row += 1

        # Add labels for the operator dictionary
        for operator, info in parser_table.GetOperators().items():
            label_operator = Gtk.Label(operator)
            label_info = Gtk.Label(info)
            table.attach(label_operator, 0, 1, row, row + 1)
            table.attach(label_info, 1, 2, row, row + 1)
            row += 1

        label_tmp = Gtk.Label()
        label_tmp.set_markup("<b>Operands:</b>")
        table.attach(label_tmp, 0, 1, row, row + 1)
        row += 1
        # Add labels for the operand dictionary
        for operand, info in parser_table.GetOperands().items():
            label_operand = Gtk.Label(operand)
            label_info = Gtk.Label(info)
            table.attach(label_operand, 0, 1, row, row + 1)
            table.attach(label_info, 1, 2, row, row + 1)
            row += 1

        button = Gtk.Button(label="Open Holsted Metrics")
        button.connect("clicked", self.open_holsted_metrics)

        # Attach the button to the table
        table.attach(button, 0, 2, row, row + 1)

        # Show the window and start the GTK main loop
        window.show_all()

    def open_holsted_metrics(self, button):
        parser_table = parser.FParserTable.FParserTable()
        buf = self.textview.get_buffer()
        parser_table.SetText(
            text=buf.get_text(start=buf.get_start_iter(), end=buf.get_end_iter(), include_hidden_chars=False))

        metrics_window = Gtk.Window()
        metrics_window.set_default_size(800, 600)
        metrics_window.set_title("Holsted Metrics")
        metrics_window.connect("destroy", Gtk.main_quit)

        # Create a box to hold the metrics labels
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        metrics_window.add(box)

        # Общее число операторов программы N1
        N1 = 0
        for operator in parser_table.GetOperators().values():
            N1 += operator

        # Общее число операндов программы N2
        N2 = 0
        for operand in parser_table.GetOperands().values():
            N2 += operand

        # Длина программы N
        N = N1 + N2

        # Число уникальных операторов программы(ɳ1)
        n1 = len(parser_table.GetOperators().values())

        # Число уникальных операндов программы(ɳ2)
        n2 = len(parser_table.GetOperands().values())

        # Словарь программы(ɳ)
        n = n1 + n2

        # Объем программы(V)
        V = N * log2(n)

        # Теоретическая длина программы (C)
        С = (n1 * log2(n1)) + (n2 * log2(n2))

        # Сложность программы
        D = (n1 / 2) * (N2 / n2)

        # Усилие для написания
        E = D * V

        # Время для программирования
        T = E / 18

        # Количество ожидаемых ошибок
        B = V / 3000

        # Create labels for each metric and add them to the box
        metrics_labels = [
            f"Общее число операторов программы (N1): {N1}",
            f"Общее число операндов в программе (N2): {N2}",
            f"Длина программы (N): {N}",
            f"Число уникальных операторов программы (ɳ1): {n1}",
            f"Число уникальных операндов программы (ɳ2): {n2}",
            f"Cловарь программы (ɳ): {n}",
            f"Объем программы (V): {V:.2f}",
            f"Теоретическая длина программы (C): {С:.2f} - в идеале N > C не более 10%",
            f"Сложность программы (D): {D:.2f}",
            f"Усилие для написания (E): {E:.2f}",
            f"Время для программирования (T): {T:.2f}",
            f"Количество ожидаемых ошибок (B): {B:.5f}"
        ]

        for metric_label in metrics_labels:
            label = Gtk.Label(label=metric_label)
            box.pack_start(label, True, True, 0)

        # Show the window and start the GTK main loop
        metrics_window.show_all()


class EditorApplication(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         flags=Gio.ApplicationFlags.HANDLES_OPEN,
                         **kwargs)

        self.resourcedir = os.path.dirname(sys.argv[0])
        if not sys.argv[0].endswith(".py"):
            # application has been installed
            self.resourcedir = os.path.dirname(self.resourcedir)
            self.resourcedir += '/share/textview-editor'

        self.lang = locale.getlocale()[0]
        filename = self.resourcedir + "/textview-editor." + self.lang + ".json"
        try:
            with open(filename, 'r') as file:
                self.uitexts = json.load(file)
        except OSError as e:
            self.uitexts = {}

    def do_activate(self):
        win = EditorWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        builder = Gtk.Builder()
        filename = self.resourcedir + "/textview-editor.menu." + self.lang + ".ui"
        try:
            builder.add_from_file(filename)
        except GLib.GError as e:
            try:
                filename = self.resourcedir + "/textview-editor.menu.ui"
                builder.add_from_file(filename)
            except GLib.GError as e:
                print("Error: " + e.message)
                sys.exit()
        self.set_menubar(builder.get_object("menubar"))

    def do_open(self, files, *hint):
        for file in files:
            win = EditorWindow(self, file=file)
            win.show_all()

    def get_text(self, string):
        if string in self.uitexts:
            return self.uitexts[string]
        return string


# i18n
def _(string):
    return app.get_text(string)


if __name__ == "__main__":
    app = EditorApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
