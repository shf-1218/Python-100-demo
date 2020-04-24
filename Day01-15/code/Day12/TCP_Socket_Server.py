# encoding: utf-8
"""
@version: 1.0
@author: 
@file: TCP_Socket_Server
@time: 2020-04-02 16:49
"""

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    class FileTransferHandler(Thread):
        def __init__(self, client):
            super().__init__()
            self.client = client

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'txt.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.client.send(json_str.encode('utf-8'))
            self.client.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('127.0.0.1', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('./3058.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()
