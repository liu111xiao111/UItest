
import time
import requests



class MessageTest():
    pass

if __name__ == "__main__":
    str = 'debug logLine Jan 19 12:22:33 Test-iphone-6s FeiFan[946] <Error>: CGContextSetFillColorWithColor: invalid context 0x0. If you want to see the backtrace, please set CG_CONTEXT_SHOW_BACKTRACE environmental variable.'
    str1 = str.split(':')[3]
    print(str1)