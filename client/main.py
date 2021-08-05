# Клиент для запуска сервисов
#Импорт классов, отвечающих за бизнес-логику окон
from client.bootstrap import Bootstrap

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.0.103'
#host = '127.0.0.1'
#port = 8888



if __name__ == '__main__':
    Bootstrap.initEnviroment()
    Bootstrap.run()