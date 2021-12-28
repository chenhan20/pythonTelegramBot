import sendUsaStock
import sendYfinance 
import sendCrypto

def callSend():
    sendYfinance.sendYfinance()
    sendCrypto.sendCrypto()
    sendUsaStock.sendUsaStock()


if __name__ == '__main__':
    callSend()