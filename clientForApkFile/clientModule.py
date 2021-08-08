"""
Реализация socket клиент, передача сообщения и картинки
"""
import socket

from clientForApkFile.common.socketHelper import SocketHelper

from clientForApkFile.message.messageStructure import MessageStructure
from clientForApkFile.message.messageResponceParameter import MessageResponceParameter

from threading import Lock

class MySocket:
    HOST = '192.168.0.103'
    #HOST = '127.0.0.1'
    PORT = 8888
    BUFFER_LENGTH = 2048
    # Объект - ответ с сервера
    messageResponce = MessageResponceParameter()

    def __init__(self, serverClient = 1, host=HOST, port=PORT):
        self.sock = socket.socket()

        if (serverClient==1):
            self.sock.connect((host, port))
        else:
            self.sock.bind((host, port))
            #self.sock.listen(1)
            print("Server is listening", '\n')
            #clientsocket, addr = self.sock .accept()
            #print("got a connection from %s" % str(addr))

        self.helper = SocketHelper(self.sock)
        self.messageResponce = MessageResponceParameter()
        self.mutex_write = Lock()
        self.mutex_read = Lock()

    def send_data(self,messageParameter):

        messageParameterAsBytes = MessageStructure.SaveToBytes(messageParameter)

        self.mutex_write.acquire()

        self.helper.writeInt(len(messageParameterAsBytes))
        print("Размер отсылаемого сообщения:", len(messageParameterAsBytes))

        self.helper.writeBytesArray(messageParameterAsBytes)
        print("Сообщение отправлено")
        self.mutex_write.release()
        #time.sleep(0.5)

    def get_data(self):

        self.mutex_read.acquire()

        sizeOfResponce = self.helper.readInt()
        print("Размер принимаемого сообщения: " + str(sizeOfResponce))
        messageResponcetAsBytes = self.helper.readBytesArray(sizeOfResponce)
        self.messageResponce = MessageStructure.RestoreFromBytes(messageResponcetAsBytes)

        print("Ответ получен")
        self.mutex_read.release()

        return self.messageResponce
        #time.sleep(0.5)