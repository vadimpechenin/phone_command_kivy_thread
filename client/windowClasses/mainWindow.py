# Клиент для запуска сервисов
from client.applicationEnvironment import appEnvironment
from kivy.uix.popup import Popup
#import socket

#Библиотеки для многих страниц
from kivy.uix.screenmanager import Screen
import threading

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import time

#from client.common.socketHelper import SocketHelper
# Библиотеки для формирования структуры пересылаемого сообщения
from client.message.messageStructure import MessageStructure
from client.message.messageStructureParameter import MessageStructureParameter
from client.message.messageResponceParameter import MessageResponceParameter

from client.clientModule import MySocket

class MainWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.koef = appEnvironment.koef
        self.host = ''
        self.port = 8888
        self.title = 'Предупреждение'
        self.text = 'Не верный IP адрес или не запущен сервер'
        # Объект - запрос на сервер
        self.messageParameter = MessageStructureParameter()
        # Объект - ответ с сервера
        self.messageResponce = MessageResponceParameter()
        self.send_data = 0
        threading.Thread(target=self.recv_msg).start()

    def recv_msg(self):
        #self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            time.sleep(0.3)
            if (self.send_data==1):
                self.sock = MySocket(host = self.host, port = self.port)
                self.sendData()
                self.send_data = 2
            if (self.send_data==2):
                self.messageResponce = self.sock.get_data()
                self.send_data = 0
                self.Responce_popup(self.messageResponce.message)
        #self.client.connect(('127.0.0.1', self.port))

    def hostAdress(self):
        self.host =self.ids.text_input.text
        self.port = int(self.ids.text_input1.text)

    def triggerForYoutube(self):
        self.messageParameter.codeString = "youtube"
        self.send_data = 1
        #self.sendData()

    def triggerForGoogle(self):

        self.messageParameter.codeString = "google"
        self.send_data = 1
        #self.sendData()

    def triggerForVK(self):

        self.messageParameter.codeString = "vk"
        #self.sendData()
        self.send_data = 1

    def triggerForFile(self):

        self.messageParameter.codeString = "фильм"
        #self.sendData()
        self.send_data = 1

    def triggerForProgramm(self):

        self.messageParameter.codeString = "steam"
        #self.sendData()
        self.send_data = 1

    def sendData(self):
        #Одинаковая часть кода по отправке сообщений
        try:
            #self.client.connect((self.host, self.port))
            #self.client.sendall(self.messageParameter.codeString.encode("utf-8"))
            #self.client.close()
            print('Зашел в отправку сообщения')
            self.sock.send_data(self.messageParameter)
            #self.messageParameter = MessageStructure.ClearObject(self.messageParameter)
        except:

            self.popupForFilter(self.title, self.text)

    def popupForFilter(self, title, text):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text=text))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        popup = Popup(title=title, content=PopupGrid,
                      auto_dismiss=False, size_hint=(None, None), size=(int(300 * self.koef), int(200 * self.koef)))

        content.bind(on_press=popup.dismiss)
        popup.open()

    def Responce_popup(self, text):
        PopupGrid = GridLayout(rows=2, size_hint_y=None)
        PopupGrid.add_widget(Label(text=text))
        content = Button(text='Закрыть')
        PopupGrid.add_widget(content)
        popup = Popup(title = 'Ответ сервера', content=PopupGrid,
                      auto_dismiss=False, size_hint=(None, None), size=(int(300 * self.koef), int(200 * self.koef)))

        content.bind(on_press=popup.dismiss)
        popup.open()