import socket

# 生成socket实例对象
sk = socket.socket()
# 绑定IP和端口
sk.bind(("127.0.0.1", 8000))
# 监听
sk.listen()

# 定义一个处理/yimi/的函数
def yimi(url):
    with open('yimi.html', 'rb') as f:
        ret = f.read()
        return ret
# 定义一个处理/xiaohei/的函数
def xiaohei(url):
    with open('xiaohei.html', 'rb') as f:
        ret = f.read()
        return ret

url_func = [
    ('/yimi/', yimi),
    ('/xiaohei/', xiaohei),
]

# 写一个死循环，一直等待客户端连接
while 1:
    # 获取与客户端的连接
    conn, _ = sk.accept()
    # 接受客户端发来的消息
    data = conn.recv(8096)
    # 把收到的数据转化成字符串类型
    data_str = str(data, encoding="utf-8")
    # 用\r\n去切割上面的字符串
    l1 = data_str.split("\r\n")
    # 按照空格切割上面的字符串
    l2 = l1[0].split()
    url = l2[1]
    # 给客户端回复消息
    conn.send(b'qnmd')
    # 关闭
    conn.close()
    sk.close()