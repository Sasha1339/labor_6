from power_system import PowerSystem
from power_transformer import PowerTransformer
from transmission_line import TransmissionLine
import xml.etree.ElementTree as ET
import math
import logging


class Service:

    def parsing_xml(self, xml_str):
        self.__transmission_line = []
        root = ET.fromstring(xml_str)
        logging.warning("okokoookoooo")
        for data in root:
            if data.tag == "fault":
                for dat in data:
                    self.__bus = int(dat.text)
            elif data.tag == "power_system":
                skz = 0
                u = 0
                for dat in data:
                    if dat.tag == "skz":
                        skz = float(dat.text)
                    if dat.tag == "u":
                        u = float(dat.text)
                self.__power_system = PowerSystem(skz, u)
            elif data.tag == "transmission_line":
                l = 0
                x_per_km = 0
                r_per_km = 0
                for dat in data:
                    if dat.tag == "l":
                        l = float(dat.text)
                    if dat.tag == "x_per_km":
                        x_per_km = float(dat.text)
                    if dat.tag == "r_per_km":
                        r_per_km = float(dat.text)
                self.__transmission_line.append(TransmissionLine(l, x_per_km, r_per_km))
            elif data.tag == "power_transformer":
                ukz = 0
                pkz = 0
                ratio = 0
                snom = 0
                unom = 0
                for dat in data:
                    if dat.tag == "ukz":
                        ukz = float(dat.text)
                    if dat.tag == "pkz":
                        pkz = float(dat.text)
                    if dat.tag == "ratio":
                        ratio = float(dat.text)
                    if dat.tag == "snom":
                        snom = float(dat.text)
                    if dat.tag == "unom":
                        unom = float(dat.text)
                self.__power_transformer = PowerTransformer(ukz, pkz, ratio, snom, unom)
    

    def calculate(self):
        logging.info('pfitk')
        Ikz = 0
        if self.__bus == 1:
            Xc = self.__power_system.get_u()**2/self.__power_system.get_skz()
            Ikz = self.__power_system.get_u()/(math.sqrt(3)*Xc)
        elif self.__bus == 2:
            Xc = (self.__power_system.get_u()**2/self.__power_system.get_skz())/(self.__power_transformer.get_ratio())**2
            Rt = (self.__power_transformer.get_pkz()*(self.__power_transformer.get_unom()**2))/(self.__power_transformer.get_snom()**2)/(self.__power_transformer.get_ratio())**2
            Xt = (self.__power_transformer.get_ukz()/100)*(self.__power_transformer.get_unom()**2/self.__power_transformer.get_snom())/(self.__power_transformer.get_ratio()**2)
            Xt = math.sqrt(Rt**2+Xt**2)
            Ikz = self.__power_system.get_u()/(math.sqrt(3)*(Xc+Xt))
        elif self.__bus == 3:
            Xc = (self.__power_system.get_u()**2/self.__power_system.get_skz())/(self.__power_transformer.get_ratio())**2
            Rt = (self.__power_transformer.get_pkz()*(self.__power_transformer.get_unom()**2))/(self.__power_transformer.get_snom()**2)/(self.__power_transformer.get_ratio())**2
            Xt = (self.__power_transformer.get_ukz()/100)*(self.__power_transformer.get_unom()**2/self.__power_transformer.get_snom())/(self.__power_transformer.get_ratio()**2)
            Xt = math.sqrt(Rt**2+Xt**2)
            Xl = 0
            X_l = []
            for line in self.__transmission_line:
                X_l.append(math.sqrt((line.get_l()*line.get_x_per_km())**2+(line.get_l()*line.get_r_per_km())**2))
            Xl = (X_l[0]*X_l[1])/(X_l[0]+X_l[1])
            Ikz = self.__power_system.get_u()/(math.sqrt(3)*(Xc+Xt+Xl))
        elif self.__bus == 4:
            Xc = (self.__power_system.get_u()**2/self.__power_system.get_skz())/(self.__power_transformer.get_ratio())**2
            Rt = (self.__power_transformer.get_pkz()*(self.__power_transformer.get_unom()**2))/(self.__power_transformer.get_snom()**2)/(self.__power_transformer.get_ratio())**2
            Xt = (self.__power_transformer.get_ukz()/100)*(self.__power_transformer.get_unom()**2/self.__power_transformer.get_snom())/(self.__power_transformer.get_ratio()**2)
            Xt = math.sqrt(Rt**2+Xt**2)
            Xl = 0
            X_l = []
            for line in self.__transmission_line:
                X_l.append(math.sqrt((line.get_l()*line.get_x_per_km())**2+(line.get_l()*line.get_r_per_km())**2))
            Xl = (X_l[0]*X_l[1])/(X_l[0]+X_l[1])+X_l[2]
            Ikz = self.__power_system.get_u()/(math.sqrt(3)*(Xc+Xt+Xl))
        return Ikz
