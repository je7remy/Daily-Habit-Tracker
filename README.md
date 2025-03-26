
# Daily Habit Tracker

## Descripción

**Daily Habit Tracker** es un sistema de seguimiento personal desarrollado en Python que te permite monitorear y mejorar tus hábitos diarios. Este programa registra tu progreso en áreas clave como la abstinencia de alcohol, redes sociales y pornografía, el descanso de 8 horas, la meditación, la calidad de tus relaciones sociales, el ejercicio físico y la adherencia a un horario específico. Además, incluye un seguimiento de progreso en certificaciones técnicas como Google, CompTIA y eJPTv2.

El sistema calcula puntos diarios basados en el cumplimiento de estos hábitos, mantiene una racha si sigues el "Horario GOD" de manera consecutiva y te permite avanzar a través de niveles según los puntos acumulados. Los datos se almacenan en un archivo Markdown para facilitar su revisión.

## Características

- **Registro diario de hábitos**: Ingresa tus logros diarios respondiendo preguntas simples.
- **Cálculo de puntos**: Obtén puntos por completar hábitos y avanzar en certificaciones.
- **Racha consecutiva**: Mantén una racha si sigues el horario establecido sin interrupciones.
- **Sistema de niveles**: Sube de nivel al acumular puntos (100 puntos por nivel).
- **Seguimiento de certificaciones**: Registra el progreso porcentual en certificaciones específicas.
- **Historial en Markdown**: Todos los registros se guardan en un archivo `historial_god.md` con formato de tabla.

## Requisitos

- Python 3.x instalado en tu sistema.

## Instalación

1. Clona el repositorio desde GitHub:
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
   - **1. Ingresar datos del día**: Registra tus hábitos diarios.
   - **2. Visualizar historial**: Consulta todos los registros previos.
   - **3. Salir**: Finaliza el programa.

### Ingresar datos del día

- **Fecha**: Ingresa la fecha en formato `dd/mm/yyyy`.
- **Hábitos**: Responde con `✓` (sí) o `x` (no) a preguntas sobre alcohol, redes sociales, pornografía, descanso, círculo social, ejercicio y horario.
- **Meditación**: Indica los minutos meditados (puntos cada 10 minutos).
- **Certificaciones**: Ingresa el progreso porcentual (0-100%) para cada certificación (Google, CompTIA, eJPTv2).

Ejemplo de entrada:
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
Ingresa el progreso en Google (0-100%): 10
Ingresa el progreso en CompTIA (0-100%): 5
Ingresa el progreso en eJPTv2 (0-100%): 0
```

### Visualizar historial

- Muestra el contenido del archivo `historial_god.md` en la consola, con una tabla que incluye todos los registros.

Ejemplo de historial:
```
| Fecha      | No Alcohol (0%) | No Media (0%) | No Porno (0%) | 8H Descanso (100%) | Meditación (min) | Buen Círculo (100%) | Ejercicio (5:30-5:50 PM) | Horario GOD | Certificaciones Avanzadas |
|------------|:---------------:|:-------------:|:-------------:|:------------------:|:----------------:|:-------------------:|:------------------------:|:-----------:|:------------------------:|
| 15/10/2023 | ✓              | ✓            | ✓            | ✓                 | 20              | ✓                  | ✓                       | ✓          | Google:10% CompTIA:5%    |
```

### Salir

- Selecciona la opción 3 para cerrar el programa.

## Estructura del proyecto

- **`main.py`**: Contiene toda la lógica del programa, incluyendo la clase `GODSystem` y el menú interactivo.
- **`historial_god.md`**: Archivo generado automáticamente para almacenar el historial en formato Markdown.

## Contribuir

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto:

1. Abre un **issue** para discutir tu idea o reportar un problema.
2. Envía un **pull request** con tus cambios.

Algunas ideas para contribuir:
- Agregar más hábitos personalizables.
- Mejorar la interfaz con una GUI.
- Exportar el historial a otros formatos (CSV, JSON).

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE). Consulta el archivo `LICENSE` para más detalles.

---
