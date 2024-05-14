from abc import ABC, abstractmethod

class Membresia(ABC):

    def __init__(self, p_correo: str, p_tarjeta: str, p_costo: int, p_dispositivos: int)
        self.__p_correo = p_correo
        self.__p_tarjeta = p_tarjeta
        self.__p_costo = p_costo
        self.__p_dispositivos = p_dispositivos

    @property
    def get_p_correo(self):
        return self.__p_correo
    
    @property
    def get_p_tarjeta(self):
        return self.__p_tarjeta

    @property
    def get_p_costo(self):
        return self.__p_costo
    
    @property
    def get_p_dispositivos(self):
        return self.__p_dispositivos
    
class Basica(Membresia):
    def __init__(self, p_correo: str, p_tarjeta: str):
        super().__init__(p_correo, p_tarjeta, 0, 1)

    def 
