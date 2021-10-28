import sendYfinance 
import sendCrypto

def callSend():
    sendYfinance.sendYfinance()
    sendCrypto.sendCrypto()


if __name__ == '__main__':
    callSend()