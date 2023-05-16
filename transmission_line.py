class TransmissionLine:
    def __init__(self, l, x_per_km, r_per_km):
        self.__l = l
        self.__x_per_km = x_per_km
        self.__r_per_km = r_per_km

    def get_l(self):
        return self.__l
    
    def get_x_per_km(self):
        return self.__x_per_km
    
    def get_r_per_km(self):
        return self.__r_per_km
    