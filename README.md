
## 功能说明：
封装串口和网口连接硬件
1.实现统一的发送和接收接口， 阻塞接收
2.使用工厂类生成统一的实例
3.数据通过子线程放入到FIFO队列中


## 文件说明
- utils.py: 工具类, BaseConn和DequeWithMaxLen
  - BaseConn 数据入队列和取数
  - DequeWithMaxLen  实现队列
  - log 日志配置，通过配置hander `hard_conn` 修改默认日志格式
- base_serial
    - `BaseSerial` 实现连接和断开
    - `SerialConn` 实现数据接收和发送
- base_socket
    - `BaseSocket` 实现连接和断开
        - send: 发送数据
        - receive： 接收数据
        - send_receive： 发送等待返回数据
    - `SocketConn` 实现数据接收和发送
        - send: 发送数据
        - receive： 接收数据
        - send_receive： 发送等待返回数据
- hard_conn
    - `HardConnSock` 线程方式实现数据接收
    - `HardConnSerial` 线程方式实现数据接收
    - `hard_conn` 工厂方法生成实例  在使用中使用该方法就可以

```python 
# send 命令有配置send_lf参数 ，send的字符串后面会增加结束符再发送到硬件。默认参数是\r\n
# socket连接, 指定log级别，默认是INFO
import logging
hard = HardConnect(conn_type='socket', ip='127.0.0.1', port=60000, logging_level=logging.DEBUG)
# 发送命令, 等待返回； 
received_data = hard.send_receive('send command')  
hard.start()     # 启动线程持续接收数据

# 串口连接
hard = HardConnect(conn_type='serial', device='/dev/tty.usbmodem1202', baud_rate=115200)
hard1.start()   # 启动线程持续接收数据
receive = hard.send_receive('send command')  # 发送命令, 等待返回
val = hard.new_value()  # 获取队列里最后一个值

# with open
with HardConnect(
        conn_type='socket', ip="192.168.0.100", port=60000, 
    ) as socket5001:
        socket5001.start()
```

## v0.2.5
add log config and del print console
optimze receive data put queue
optimze arguments

## V0.2.3
add serial receive bytes

## V0.2.2
add socket receive length

## V0.2.1
add socket timout


## V0.2.0
add send_receive  Don't use sub thread receive data. main thread send command wait for server response
socket add send bytes type. so users can continue to send data as needed.

## V0.1.0
socket & serial connect/disconnect/send/receive
Use thread to receive separately， Send use main thread, receive use sub thread