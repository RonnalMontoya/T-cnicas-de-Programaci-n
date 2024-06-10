from abc import ABC, abstractmethod

# Abstracción y Encapsulación
class Empleado(ABC):
    def __init__(self, nombre, id_empleado):
        self.__nombre = nombre  # Atributo encapsulado
        self.__id_empleado = id_empleado  # Atributo encapsulado

    @abstractmethod
    def calcular_pago(self):
        pass

    def obtener_nombre(self):
        return self.__nombre

    def obtener_id_empleado(self):
        return self.__id_empleado

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_id_empleado(self, id_empleado):
        self.__id_empleado = id_empleado

# Herencia
class Empleadoasalariado(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.__salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.__salario_mensual

class Empleadoporhora(Empleado):
    def __init__(self, nombre, id_empleado, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado)
        self.__tarifa_hora = tarifa_hora
        self.__horas_trabajadas = horas_trabajadas

    def calcular_pago(self):
        return self.__tarifa_hora * self.__horas_trabajadas

# Polimorfismo
def procesar_pagos(empleados):
    for empleado in empleados:
        print(f"Empleado: {empleado.obtener_nombre()}, ID: {empleado.obtener_id_empleado()}, Pago: {empleado.calcular_pago()}")

# Crear instancias de las clases derivadas
asalariado = Empleadoasalariado("Juan Pérez", 1, 3000)
por_hora = Empleadoporhora("Ana Gómez", 2, 20, 120)

# Lista de empleados
empleados = [asalariado, por_hora]

# Usar la función que demuestra polimorfismo
procesar_pagos(empleados)
