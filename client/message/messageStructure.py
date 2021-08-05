import pickle

class MessageStructure:
    #Класс для упаковки данных в сообщении для сокетов (коды, картинки, сообщения)
    def __init__(self):
        pass

    @staticmethod
    def SaveToBytes(parameter):
        result = pickle.dumps(parameter, pickle.HIGHEST_PROTOCOL)
        return result

    @staticmethod
    def RestoreFromBytes(parameterAsBytes):
        result = pickle.loads(parameterAsBytes)
        return result

    @staticmethod
    def ClearObject(parameter):
        parameter.codeString = ''