#Запуск сервисов с телефона
# https://www.youtube.com/watch?v=0P1gtxRWh-s
import socket
import webbrowser
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Берем название рабочей машины и по ее имени ip
print(socket.gethostbyname_ex(socket.gethostname()))

host = '192.168.1.60'
host = '127.0.0.1'
port = 8888

server.bind((host, port))

server.listen(1)



while True:
    try:
        print("Server is listening", '\n')
        #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        user, adres = server.accept()
    except KeyboardInterrupt:
        server.close()
        break
    else:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)
        #URL ссылки
        if data == "youtube":
            webbrowser.open("https://www.youtube.com/")
        elif data == "google":
            webbrowser.open("https://www.google.com/")
        elif data == "vk":
            webbrowser.open("https://www.vk.com/")

        # Запуск приложения
        elif data == "steam":
            os.startfile("C:/Users/User/AppData/Local/FreeCAD 0.18/bin/FreeCAD.exe")
        elif data == "фильм":
            os.startfile("D:/Фильмы/Призрак в доспехах/Ghost in shell.avi")
        else:
            print('Неверный ввод')
