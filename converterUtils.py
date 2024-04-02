def converterNumber(num):
    converterNum = int(num.replace(',', ''))
    numberLength = len(str(converterNum))
    if numberLength > 12:
        converterNum = str(round(converterNum / 1000000000000, 2)) + '兆'
    elif 8 < numberLength <= 12:
        converterNum = str(round(converterNum / 100000000, 2)) + '億'
    elif 4 < numberLength <= 8:
        converterNum = str(round(converterNum / 10000, 2)) + '萬'
    return converterNum
