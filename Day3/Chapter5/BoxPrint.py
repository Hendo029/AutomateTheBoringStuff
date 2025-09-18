def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be one character.')
    if width < 2 or height < 2:
        raise Exception('Width and height need to be greater than 1')
    print(symbol * width)
    for i in range(height -2):
        print(symbol + (' ' * (width -2)) + symbol)
    print(symbol * width)
boxPrint('*', 1, 10)