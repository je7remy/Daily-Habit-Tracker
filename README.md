# 𝒟𝒶𝒾𝓁𝓎 𝐻𝒶𝒷𝒾𝓉 𝒯𝓇𝒶𝒸𝓀𝑒𝓇                                                                         

## Descripción

**Daily Habit Tracker** es un sistema de seguimiento personal desarrollado en Python que te permite monitorear y mejorar tus hábitos diarios. Este programa registra tu progreso en áreas clave como la abstinencia de alcohol, redes sociales y pornografía, el descanso de 8 horas, la meditación, la calidad de tus relaciones sociales, el ejercicio físico y la adherencia a un horario específico denominado "Horario GOD". Además, incluye un seguimiento de las horas dedicadas a certificaciones técnicas como Google, CompTIA y eJPTv2.

El sistema calcula puntos diarios basados en el cumplimiento de estos hábitos, mantiene una racha si sigues el "Horario GOD" de manera consecutiva y te permite avanzar a través de niveles según los puntos acumulados (100 puntos por nivel). Los datos se almacenan en un archivo Markdown (`historial_god.md`) para facilitar su revisión y seguimiento.

## Características

- **Registro diario de hábitos**: Ingresa tus logros diarios respondiendo preguntas simples con `✓` (sí) o `x` (no).
- **Cálculo de puntos**: Obtén puntos por completar hábitos (ej. 10 puntos por seguir el Horario GOD, 3 por ejercicio, etc.) y por meditar (1 punto cada 10 minutos).
- **Racha consecutiva**: Mantén una racha si sigues el "Horario GOD" en días consecutivos; la racha se reinicia si fallas o hay un salto en las fechas.
- **Sistema de niveles**: Sube de nivel al acumular 100 puntos, con notificación en consola al alcanzar un nuevo nivel.
- **Seguimiento de certificaciones**: Registra las horas diarias dedicadas a certificaciones (Google, CompTIA, eJPTv2) y visualiza las horas acumuladas.
- **Historial en Markdown**: Los registros se guardan en `historial_god.md` en formato de tabla, incluyendo las horas diarias de certificaciones.
- **Horas acumuladas**: Muestra el total de horas dedicadas a cada certificación al ingresar datos o visualizar el historial.
- **Validación de entradas**: Asegura que las fechas sean únicas y en formato correcto (`dd/mm/yyyy`), y que las horas sean números positivos.

## Requisitos

- **Python 3.x** instalado en tu sistema.

## Instalación

1. Clona el repositorio desde GitHub (ajusta la URL según tu repositorio):
   ```bash
   git clone https://github.com/tu_usuario/daily-habit-tracker.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd daily-habit-tracker
   ```
3. Verifica que tengas Python instalado ejecutando:
   ```bash
   python --version
   ```
   Si no está instalado, descárgalo desde [python.org](https://www.python.org/).

## Uso

1. Ejecuta el programa principal:
   ```bash
   python main.py
   ```
2. Selecciona una opción del menú interactivo:
   - **1. Ingresar datos del día**: Registra tus hábitos y horas de certificaciones.
   - **2. Visualizar historial**: Consulta todos los registros previos y las horas acumuladas.
   - **3. Salir**: Finaliza el programa.

### Ingresar datos del día

- **Fecha**: Ingresa la fecha en formato `dd/mm/yyyy`. El programa verifica que no exista un registro previo para esa fecha.
- **Hábitos**: Responde con `✓` (sí) o `x` (no) a preguntas sobre:
  - Abstinencia de alcohol.
  - Evitar redes sociales y contenido multimedia.
  - Abstinencia de pornografía.
  - Dormir 8 horas.
  - Rodearte de un buen círculo social.
  - Hacer ejercicio (5:30-5:50 PM).
  - Seguir el "Horario GOD".
- **Meditación**: Indica los minutos meditados (número entero).
- **Certificaciones**: Ingresa las horas dedicadas a cada certificación (Google, CompTIA, eJPTv2) en formato decimal (ej. 2.5).

#### Ejemplo de entrada:
```
Ingresa la fecha (dd/mm/yyyy): 15/10/2023
¿Te abstuviste de alcohol? (✓/x): ✓
¿Evitaste redes sociales y contenido multimedia? (✓/x): ✓
¿Te abstuviste de pornografía? (✓/x): ✓
¿Dormiste 8 horas? (✓/x): ✓
¿Cuántos minutos meditaste?: 20
¿Te rodeaste de un buen círculo? (✓/x): ✓
¿Hiciste ejercicio? (✓/x): ✓
¿Seguiste tu horario GOD? (✓/x): ✓
Ingresa las horas dedicadas a Google hoy (puede ser decimal): 2.5
Ingresa las horas dedicadas a CompTIA hoy (puede ser decimal): 1.0
Ingresa las horas dedicadas a eJPTv2 hoy (puede ser decimal): 0
```

#### Salida en consola:
```
Puntos totales: 27
Racha actual: 1
Nivel: 1
Horas acumuladas en certificaciones:
  Google: 2.5 horas
  CompTIA: 1.0 horas
```

### Visualizar historial

- Muestra el contenido completo de `historial_god.md` en la consola, seguido de las horas acumuladas en certificaciones.

#### Ejemplo de historial en `historial_god.md`:
```
| Fecha      | No Alcohol (0%) | No Media (0%) | No Porno (0%) | 8H Descanso (100%) | Meditación (min) | Buen Círculo (100%) | Ejercicio (5:30-5:50 PM) | Horario GOD | Certificaciones Avanzadas |
|------------|:---------------:|:-------------:|:-------------:|:------------------:|:----------------:|:-------------------:|:------------------------:|:-----------:|:------------------------:|
| 15/10/2023 | ✓              | ✓            | ✓            | ✓                 | 20              | ✓                  | ✓                       | ✓          | Google:2.5h CompTIA:1.0h   |
```

#### Salida en consola al visualizar:
```
| Fecha      | No Alcohol (0%) | No Media (0%) | No Porno (0%) | 8H Descanso (100%) | Meditación (min) | Buen Círculo (100%) | Ejercicio (5:30-5:50 PM) | Horario GOD | Certificaciones Avanzadas |
|------------|:---------------:|:-------------:|:-------------:|:------------------:|:----------------:|:-------------------:|:------------------------:|:-----------:|:------------------------:|
| 15/10/2023 | ✓              | ✓            | ✓            | ✓                 | 20              | ✓                  | ✓                       | ✓          | Google:2.5h CompTIA:1.0h   |

Horas acumuladas en certificaciones:
  Google: 2.5 horas
  CompTIA: 1.0 horas
```

### Salir

- Selecciona la opción **3** para cerrar el programa con un mensaje de despedida: `¡Hasta luego!`.

## Estructura del proyecto

- **`main.py`**: Contiene toda la lógica del programa, incluyendo la clase `GODSystem` para gestionar puntos, rachas, niveles y registros, y el menú interactivo.
- **`historial_god.md`**: Archivo generado automáticamente para almacenar el historial en formato Markdown.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto:

1. Abre un **issue** para discutir tu idea o reportar un problema.
2. Envía un **pull request** con tus cambios.

### Ideas para contribuir:
- Agregar más hábitos personalizables.
- Implementar una interfaz gráfica (GUI) con bibliotecas como Tkinter o PyQt.
- Exportar el historial a otros formatos (CSV, JSON).
- Añadir estadísticas avanzadas (promedios, gráficos).

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Consulta el archivo `LICENSE` para más detalles.
