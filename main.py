# Клиент для запуска сервисов
from kivy.app import App
from kivy.uix.popup import Popup
# Для размера окна
from kivy.core.window import Window
#Библиотеки для многих страниц
from kivy.uix.screenmanager import ScreenManager, Screen
import threading

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


from kivy.lang import Builder
from os.path import dirname, join, basename, isfile
from os import listdir
import socket

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.0.103'
#host = '127.0.0.1'
#port = 8888
if (1==1):
    Window.size = (420, 800)
    koef = 1
else:
    Window.size = (1100, 2300)
    koef = 3


class MainWindow(Screen):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.koef = koef
        self.host = ''
        self.port = 8888
        self.title = 'Предупреждение'
        self.text = 'Не верный IP адрес или не запущен сервер'
        self.hello_label = Label(text="Connecting...", size_hint=(1, 1.7), font_size=20)
        threading.Thread(target=self.recv_msg).start()

    def recv_msg(self):
        self.client = socket.socket()

    def hostAdress(self):

        self.host =self.ids.text_input.text
        self.port = int(self.ids.text_input1.text)

    def triggerForYoutube(self):
        s = "youtube"
        try:
            self.client.connect((self.host, self.port))
            self.client.send(s.encode("utf-8"))
        except:
            #self.hello_label = Label(text="Connecting...", size_hint=(1, 1.7), font_size=20)
            self.popupForFilter(self.title, self.text)

    def triggerForGoogle(self):

        s = "google"
        try:
            self.client.connect((self.host, self.port))
            self.client.send(s.encode("utf-8"))
        except:

            self.popupForFilter(self.title, self.text)

    def triggerForVK(self):

        s = "vk"
        try:
            self.client.connect((self.host, self.port))
            self.client.send(s.encode("utf-8"))
        except:

            self.popupForFilter(self.title, self.text)

    def triggerForFile(self):

        s = "фильм"
        try:
            self.client.connect((self.host, self.port))
            self.client.send(s.encode("utf-8"))
        except:

            self.popupForFilter(self.title, self.text)

    def triggerForProgramm(self):

        s = "steam"
        try:
            self.client.connect((self.host, self.port))
            self.client.send(s.encode("utf-8"))
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

# Менеджер перехода между страницами и передачи данных
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("kvfiles/my.kv")

class Console(App):
    def build(self):
        return kv
        # return CameraClick()

    # Метод для кодировки русских символов в описании
    def load_all_kv_files(self, directory_kv_files):
        for kv_file in listdir(directory_kv_files):
            kv_file = join(directory_kv_files, kv_file)
            if isfile(kv_file) and kv_file.endswith("kv"):
                with open(kv_file, encoding="utf-8") as kv:
                    Builder.load_string(kv.read())
                    #return kv

if __name__ == '__main__':
    directory_kv_files = 'kvfiles'
    Console().run()