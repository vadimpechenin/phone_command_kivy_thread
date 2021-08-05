#Использование сокетов через классы
import socketserver
import webbrowser
import os

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #Главный метод, который мы переопределяем
        #data = self.request.recv(1024).strip() #Получение информации и ip адреса клиента
        data = self.request.recv(1024).decode("utf-8").lower()
        print(data)
        # URL ссылки
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
        #self.request.sendall(data)

if __name__=='__main__':
    #На получение каждого нового сообщения создается экземпляр класса
    host = ''
    host = '192.168.0.103'
    host = '127.0.0.1'
    with socketserver.TCPServer((host,8888), EchoTCPHandler) as server:
        #Запуск бесконечного цикла и чтение нового клиента
        server.serve_forever()