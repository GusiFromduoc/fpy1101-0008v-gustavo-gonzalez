# fpy1101-0008v-gustavo-gonzalez
# Laboratorio de Programacion - Estructuras de Control y Validacion

Este repositorio contiene dos soluciones de software desarrolladas en Python enfocadas en el control de flujos iterativos, gestion de excepciones y validacion estricta de datos en consola. Los scripts han sido diseñados bajo los estandares de orden y optimizacion logica (PEP 8).

---

## 1. Sistema de Registro de Personal Medico

Script diseñado para gestionar y clasificar el alta de profesionales de la salud en una plataforma hospitalaria.

### Caracteristicas
* **Control de Iteraciones:** Determina dinamicamente el limite del ciclo principal mediante la entrada inicial de la cantidad de medicos a registrar.
* **Validacion de Cadenas:** Aplica filtros estrictos para la admision de nombres de usuarios (minimo 6 caracteres y exclusion total de espacios en blanco mediante metodos de cadena).
* **Manejo de Excepciones:** Implementa bloques try-except para asegurar que las variables de tipo entero (como los años de experiencia) no interrumpan la ejecucion ante entradas invalidas.
* **Logica de Clasificacion:** Segmenta de forma automatica al personal en dos categorias exclusivas:
  * Especialista Senior: Experiencia estrictamente mayor a 5 años.
  * Residente Junior: Experiencia menor o igual a 5 años.

---

## 2. Sistema de Gestion de Prestamos - Biblioteca Central

Plataforma interactiva que automatiza el control de inventario de una biblioteca mediante una interfaz de menu por consola.

### Caracteristicas
* **Menu de Navegacion:** Estructura basada en una cadena de condicionales enlazados (if-elif-else) que operan dentro de un ciclo principal controlado.
* **Consistencia de Inventario:** Realiza operaciones aritmeticas inversas en tiempo real sobre las variables de stock libre y stock en circulacion.
* **Seguridad Operacional:** * Restringe transacciones si la solicitud de prestamo supera la disponibilidad actual en estanterias.
  * Impide devoluciones que excedan el total de libros prestados activamente de la sesion.
  * Bloquea el procesamiento de valores negativos o nulos (menores a 1).
* **Modulo de Auditoria:** La opcion de historial reporta de forma simultanea los indicadores de stock activo junto con los acumulados historicos de movimientos de la sesion.

---

## Requisitos de Ejecucion

* Entorno de ejecucion: Python 3.x
* Interfaz: Terminal / Consola de comandos
