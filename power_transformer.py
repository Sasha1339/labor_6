class PowerTransformer:
    def __init__(self, ukz, pkz, ratio, snom, unom):
        self.__ukz = ukz
        self.__pkz = pkz
        self.__ratio = ratio
        self.__snom = snom
        self.__unom = unom

    def get_ukz(self):
        return self.__ukz
    
    def get_pkz(self):
        return self.__pkz
    
    def get_ratio(self):
        return self.__ratio
    
    def get_snom(self):
        return self.__snom
    
    def get_unom(self):
        return self.__unom
