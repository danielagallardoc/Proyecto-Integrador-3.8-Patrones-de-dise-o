from abc import ABC, abstractmethod
from typing import List

class ConfiguracionGlobal:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionGlobal, cls).__new__(cls)
            cls._instancia.umbrales = {
                "temperatura": 35.0,
                "humedad": 80.0,
                "contaminacion": 150.0
            }
        return cls._instancia


class Sensor(ABC):
    @abstractmethod
    def leer_valor(self):
        pass

class SensorTemperatura(Sensor):
    def leer_valor(self):
        return 36.5  

class SensorHumedad(Sensor):
    def leer_valor(self):
        return 78.0  

class SensorContaminacion(Sensor):
    def leer_valor(self):
        return 160.0  

class SensorFactory(ABC):
    @abstractmethod
    def crear_sensor(self):
        pass

class TemperaturaFactory(SensorFactory):
    def crear_sensor(self):
        return SensorTemperatura()

class HumedadFactory(SensorFactory):
    def crear_sensor(self):
        return SensorHumedad()

class ContaminacionFactory(SensorFactory):
    def crear_sensor(self):
        return SensorContaminacion()


class Observador(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass

class CentroEmergencias(Observador):
    def actualizar(self, mensaje):
        print(f"[Centro de Emergencias] Alerta: {mensaje}")

class MantenimientoCiudad(Observador):
    def actualizar(self, mensaje):
        print(f"[Mantenimiento] Acción requerida: {mensaje}")

class MonitorCiudad:
    def __init__(self):
        self.observadores: List[Observador] = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def verificar_sensor(self, tipo_sensor, valor):
        config = ConfiguracionGlobal()
        umbral = config.umbrales.get(tipo_sensor, None)
        if umbral and valor > umbral:
            mensaje = f"{tipo_sensor.capitalize()} crítico: {valor} (Umbral: {umbral})"
            self.notificar(mensaje)

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)


class ServicioDatosExterno:
    def obtener_datos(self, tipo_sensor):
        print(f"Consultando API externa para {tipo_sensor}...")
        return 123.45 

class DatosAdapter:
    def __init__(self, servicio_externo):
        self.servicio_externo = servicio_externo

    def obtener_datos_sensor(self, tipo_sensor):
        return self.servicio_externo.obtener_datos(tipo_sensor)


def monitorear_ciudad():
    sensores = {
        "temperatura": TemperaturaFactory().crear_sensor(),
        "humedad": HumedadFactory().crear_sensor(),
        "contaminacion": ContaminacionFactory().crear_sensor()
    }

    monitor = MonitorCiudad()
    monitor.agregar_observador(CentroEmergencias())
    monitor.agregar_observador(MantenimientoCiudad())

    servicio_externo = ServicioDatosExterno()
    adapter = DatosAdapter(servicio_externo)
    adapter.obtener_datos_sensor("calidad del aire")

    for tipo, sensor in sensores.items():
        valor = sensor.leer_valor()
        print(f"Sensor {tipo.capitalize()} mide: {valor}")
        monitor.verificar_sensor(tipo, valor)


if __name__ == "__main__":
    print("=== Sistema Smart City: Monitoreo de Sensores ===\n")
    monitorear_ciudad()
