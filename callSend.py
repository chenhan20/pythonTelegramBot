import asyncio

import sendUsaStock
import sendYfinance
import sendCrypto


def callSend():
    asyncio.run(sendYfinance.sendYfinance())
    asyncio.run(sendCrypto.sendCrypto())
    asyncio.run(sendUsaStock.sendUsaStock())


if __name__ == '__main__':
    callSend()
