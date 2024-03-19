# example of using FParserTable

from FParserTable import FParserTable

parseTable = FParserTable()
with open('samples/string.fs') as f:
    text = f.read()
    parseTable.SetText(text)
    print(parseTable.GetOperands())
    print(parseTable.GetOperators())
