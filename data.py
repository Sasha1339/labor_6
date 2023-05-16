class Data:
    def __init__(self, power_system, transmission_line, power_transformer):
        self.__power_system = power_system
        self.__transmission_line = transmission_line
        self.__power_transformer = power_transformer

    def get_power_system(self):
        return self.__power_system
    
    def get_transmission_line(self):
        return self.__transmission_line
    
    def get_power_transformer(self):
        return self.__power_transformer
    
    def set_power_system(self, power_system):
        self.__power_system = power_system
    
    def set_transmission_line(self, transmission_line):
        self.__transmission_line = transmission_line
    
    def set_power_transformer(self, power_transformer):
        self.__power_transformer = power_transformer