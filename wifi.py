import time
import network
import socket
import ScreenTool


ssid = "bingku"
password = "bingkuhouse"

port = 10000 #端口

ScreenTool.Init()
ScreenTool.InitFont()

# 创建WIFI连接对象
wlan = network.WLAN(network.STA_IF)
# 激活接口
wlan.active(True)

# 连接WIFI
print("正在尝试连接到WIFI: " + ssid + "")
wlan.connect(ssid,password)

while not wlan.isconnected():
    print('.',end='')
    time.sleep(0.5)
    
print('\n连接成功!')


#socket通信

try:
    ip = wlan.ifconfig()[0]   #获取IP地址

    listenSocket = socket.socket()   #创建套接字
    listenSocket.bind((ip, port))   #绑定地址和端口号
    listenSocket.listen(1)   #监听套接字
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #设置套接字
    print('tcp waiting...')
    print("单片机IP: "+ str(ip))

    while True:
        ScreenTool.Show("等待上位机连接.....")  
        conn, addr = listenSocket.accept()   #接收连接请求，返回收发数据的套接字对象和客户端地址
        print("接收到连接请求: ")
        print(addr)
        ScreenTool.Show("连接到电脑")          
        while True:
            data = conn.recv(1024)   #接收数据（1024字节大小）
            if(len(data) == 0):   #判断客户端是否断开连接
                ScreenTool.Show("连接断开")
                conn.close()   #关闭套接字
                break
            print(data)
            data_str = data.decode('utf-8')
            ScreenTool.Show(data_str)
except Exception as e:
    print(f'An error occurred: {e}')
    if(listenSocket):   #判断套接字是否为空
        listenSocket.close()   #关闭套接字
    wlan.disconnect()   #断开WiFi
    wlan.active(False)   #冻结网络
    ScreenTool.Show("发生错误连接断开")