from client.applicationEnvironment import appEnvironment
from client.clientModule import MySocket
from kivy.lang import Builder

# Для размера окна
from kivy.core.window import Window

from client.windowClasses.console import Console
from client.windowClasses.windowManager import WindowManager
from client.windowClasses.mainWindow import MainWindow

class Bootstrap():

    @staticmethod
    def initEnviroment():
        #appEnvironment.sock = MySocket()
        appEnvironment.koef = 1
        if (appEnvironment.koef == 1):
            Window.size = (420, 800)
        else:
            Window.size = (1100, 2300)

        appEnvironment.kv = Builder.load_file("kvfiles/my.kv")

        appEnvironment.ConsoleObj = Console()

    @staticmethod
    def run():
        appEnvironment.ConsoleObj.run()