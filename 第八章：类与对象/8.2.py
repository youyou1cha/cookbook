# with语句；上下文管理协议
# 一般网络、数据库等需要打开关闭的清理的动作，都可以用上下文管理
# __enter__() 和__exit__()方法
# AF_INET IPV4和IPV6的网络协议；SOCK_STREAM TCP协议
from socket import socket,AF_INET,SOCK_STREAM

class LazyConnection:

    def __init__(self,address,family=AF_INET,type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not  None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock=None