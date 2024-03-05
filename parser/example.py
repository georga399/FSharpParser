# example of using my FParserTable

from FParserTable import FParserTable

parseTable = FParserTable()
with open('samples/test1.fs') as f:
    text = f.read()
    parseTable.SetText(text)
    print(parseTable.GetOperands())
    print(parseTable.GetOperators())
