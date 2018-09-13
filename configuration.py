class Configuration:

    def __init__(self):
        if hasattr(Configuration, 'instance'):
            raise Exception('Already exists')

    @staticmethod
    def getinstance():
        return Configuration.instance

Configuration.instance = Configuration()
