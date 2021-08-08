#Запуск сервисов с телефона
# https://www.youtube.com/watch?v=0P1gtxRWh-s
import socket
import webbrowser
import os

from client.common.socketHelper import SocketHelper

from client.message.messageStructure import MessageStructure
from client.message.messageStructureParameter import MessageStructureParameter
from client.message.messageResponceParameter import MessageResponceParameter

# Объект - запрос на сервер
messageParameter = MessageStructureParameter()
#Объект - ответ с сервера
messageResponce = MessageResponceParameter()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Берем название рабочей машины и по ее имени ip
print(socket.gethostbyname_ex(socket.gethostname()))

host = '192.168.0.103'
#host = '127.0.0.1'
port = 8888

server.bind((host, port))

server.listen(1)

print("Server is listening", '\n')



while True:
    try:
        user, adres = server.accept()
        helper = SocketHelper(user)
        print("got a connection from %s" % str(adres))

    except KeyboardInterrupt:
        server.close()
        break
    else:
        sizeOfRequest = helper.readInt()
        print("Размер принимаемого сообщения: " + str(sizeOfRequest))
        messageParameterAsBytes = helper.readBytesArray(sizeOfRequest)
        messageParameter = MessageStructure.RestoreFromBytes(messageParameterAsBytes)

        #data = user.recv(1024).decode("utf-8").lower()
        print(messageParameter.codeString)
        #URL ссылки
        if messageParameter.codeString == "youtube":
            messageResponce.message = "Запущен https://www.youtube.com/"
            webbrowser.open("https://www.youtube.com/")
        elif messageParameter.codeString == "google":
            messageResponce.message = "Запущен https://www.google.com/"
            webbrowser.open("https://www.google.com/")
        elif messageParameter.codeString == "vk":
            messageResponce.message = "Запущен https://www.vk.com/"
            webbrowser.open("https://www.vk.com/")

        # Запуск приложения
        elif messageParameter.codeString == "steam":
            messageResponce.message = "Запущен FreeCAD.exe"
            os.startfile("C:/Users/User/AppData/Local/FreeCAD 0.18/bin/FreeCAD.exe")
        elif messageParameter.codeString == "фильм":
            messageResponce.message = "Запущен Ghost in shell.avi"
            os.startfile("D:/Фильмы/Призрак в доспехах/Ghost in shell.avi")
        else:
            messageResponce.message = "Неверный ввод"
            print('Неверный ввод')

        messageResponceAsBytes = MessageStructure.SaveToBytes(messageResponce)

        helper.writeInt(len(messageResponceAsBytes))
        print("Размер отсылаемого ответа:", len(messageResponceAsBytes))

        helper.writeBytesArray(messageResponceAsBytes)
        print("Ответ отправлен")

