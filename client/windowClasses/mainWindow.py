# Клиент для запуска сервисов
from client.applicationEnvironment import appEnvironment
from kivy.uix.popup import Popup
import socket

#Библиотеки для многих страниц
from kivy.uix.screenmanager import Screen
import threading

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MainWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.koef = appEnvironment.koef
        self.host = ''
        self.port = 8888
        self.title = 'Предупреждение'
        self.text = 'Не верный IP адрес или не запущен сервер'
        self.hello_label = Label(text="Connecting...", size_hint=(1, 1.7), font_size=20)
        threading.Thread(target=self.recv_msg).start()

    def recv_msg(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.connect(('127.0.0.1', self.port))

    def hostAdress(self):
        self.host =self.ids.text_input.text
        self.port = int(self.ids.text_input1.text)

    def triggerForYoutube(self):
        s = "youtube"
        self.sendData(s)

    def triggerForGoogle(self):

        s = "google"
        self.sendData(s)

    def triggerForVK(self):

        s = "vk"
        self.sendData(s)

    def triggerForFile(self):

        s = "фильм"
        self.sendData(s)

    def triggerForProgramm(self):

        s = "steam"
        self.sendData(s)

    def sendData(self,s):
        #Одинаковая часть кода по отправке сообщений
        try:
            self.client.connect((self.host, self.port))
            self.client.sendall(s.encode("utf-8"))
            self.client.close()
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