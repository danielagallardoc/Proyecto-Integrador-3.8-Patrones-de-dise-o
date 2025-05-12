# Proyecto: Sistema de Monitoreo de Sensores para una Ciudad Inteligente (Smart City)

Este proyecto simula un sistema de monitoreo de sensores ambientales en una ciudad inteligente. Se gestionan sensores de temperatura, humedad y contaminación, notificando a las autoridades si se detectan valores críticos. Además, el sistema integra datos de servicios externos y gestiona la configuración global de umbrales.

El proyecto implementa 4 patrones de diseño solicitados:

- 1 Patrón Creacional
- 1 Patrón Estructural
- 1 Patrón de Comportamiento
- 1 Patrón adicional


#Patrones implementados y justificación
1. Factory Method (Patrón Creacional)
* Problema: Se necesitaba una manera flexible de crear diferentes tipos de sensores (temperatura, humedad, contaminación) sin modificar el código principal.
* Razón: Factory Method permite crear objetos sin exponer la lógica de creación, facilitando la escalabilidad si se agregan más sensores.
* Solución: Se implementaron fábricas concretas (TemperaturaFactory, HumedadFactory, ContaminacionFactory) que crean instancias específicas de sensores. El cliente solo llama a la fábrica sin saber cómo se construye internamente.

2. Adapter (Patrón Estructural)
* Problema: Era necesario obtener datos de una API externa, pero la interfaz de dicha API no era compatible con el resto del sistema.
* Razón: Adapter permite integrar clases con interfaces incompatibles sin modificar su código.
* Solución: Se creó un DatosAdapter que traduce las llamadas de la API externa al formato requerido por el sistema, encapsulando la lógica de comunicación externa.

3. Observer (Patrón de Comportamiento)
* Problema: Al detectar valores críticos en sensores, debía notificarse automáticamente a varias entidades (emergencias, mantenimiento).
* Razón: Observer permite que múltiples objetos (observadores) reaccionen a un cambio en otro objeto (el sujeto).
* Solución: Se implementó la clase MonitorCiudad como sujeto y CentroEmergencias y MantenimientoCiudadcomo observadores. Cuando un valor crítico es detectado, todos los observadores son notificados.

4. Singleton (Patrón adicional)
* Problema: La configuración de umbrales críticos (temperatura, humedad, contaminación) debía ser única y accesible globalmente.
* Razón: Singleton garantiza una única instancia de una clase, facilitando la consistencia de datos.
* Solución: Se implementó la clase ConfiguracionGlobal como Singleton, asegurando que cualquier módulo acceda a la misma configuración.

