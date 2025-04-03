import csv
import signal
from datetime import datetime, timedelta

class GODSystem:
    def __init__(self):
        self.points = 0
        self.streak = 0
        self.level = 1
        self.daily_logs = []
        self.certificaciones_horas = {"Google": 0.0, "CompTIA": 0.0, "eJPTv2": 0.0}
        self.load_history()  # Cargar historial al iniciar
        self.calculate_initial_streak()  # Calcular racha inicial

    def load_history(self):
        """Carga los registros pasados desde 'historial_god.md' y calcula las horas acumuladas."""
        self.certificaciones_horas = {"Google": 0.0, "CompTIA": 0.0, "eJPTv2": 0.0}  # Reiniciar horas acumuladas
        try:
            with open('historial_god.md', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) < 1:
                    return  # No hay datos aún
                # Saltar encabezados y separadores (primeras dos líneas)
                for line in lines[2:]:
                    if line.strip():
                        parts = [p.strip() for p in line.split('|')[1:-1]]
                        if len(parts) == 10:
                            self.daily_logs.append({
                                "Fecha": datetime.strptime(parts[0], "%d/%m/%Y"),
                                "No Alcohol (0%)": parts[1],
                                "No Media (0%)": parts[2],
                                "No Porno (0%)": parts[3],
                                "8H Descanso (100%)": parts[4],
                                "Meditación (min)": int(parts[5]) if parts[5] else 0,
                                "Buen Círculo (100%)": parts[6],
                                "Ejercicio (5:30-5:50 PM)": parts[7],
                                "Horario GOD": parts[8],
                                "Certificaciones Avanzadas": parts[9]
                            })
                            # Sumar horas diarias al acumulado
                            certs = parts[9].split()
                            for cert in certs:
                                if ':' in cert:
                                    nombre, horas_str = cert.split(':')
                                    if nombre in self.certificaciones_horas:
                                        horas = float(horas_str.strip('h'))
                                        self.certificaciones_horas[nombre] += horas
        except FileNotFoundError:
            pass  # Si el archivo no existe, comienza vacío

    def calculate_initial_streak(self):
        """Calcula la racha inicial basada en el historial."""
        if not self.daily_logs:
            self.streak = 0
            return
        sorted_logs = sorted(self.daily_logs, key=lambda x: x['Fecha'], reverse=True)
        current_streak = 0
        previous_date = None
        for log in sorted_logs:
            if log['Horario GOD'] != '✓':
                break
            if previous_date is None:
                current_streak += 1
                previous_date = log['Fecha']
            else:
                if log['Fecha'] == previous_date - timedelta(days=1):
                    current_streak += 1
                    previous_date = log['Fecha']
                else:
                    break
        self.streak = current_streak

    def calculate_daily_score(self, fecha_str, no_alcohol, no_media, no_porno, descanso_8h, minutos_meditacion, buen_circulo, ejercicio, horario_god, certificaciones_horas):
        """Calcula puntos, actualiza la racha y las horas acumuladas para un nuevo registro."""
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        daily_points = 0

        if self.daily_logs:
            latest_date = max(log['Fecha'] for log in self.daily_logs)
            consecutive = fecha == latest_date + timedelta(days=1)
        else:
            consecutive = True

        if horario_god == '✓':
            daily_points += 10
            if consecutive:
                self.streak += 1
            else:
                self.streak = 1
        else:
            self.streak = 0

        daily_points += 2 if no_alcohol == '✓' else 0
        daily_points += 2 if no_media == '✓' else 0
        daily_points += 2 if no_porno == '✓' else 0
        daily_points += 3 if descanso_8h == '✓' else 0
        daily_points += minutos_meditacion // 10
        daily_points += 2 if buen_circulo == '✓' else 0
        daily_points += 3 if ejercicio == '✓' else 0

        self.points += daily_points
        self.update_level()

        # Actualizar las horas acumuladas de las certificaciones
        for cert, horas in certificaciones_horas.items():
            if cert in self.certificaciones_horas:
                self.certificaciones_horas[cert] += horas

        # Crear el string con las horas DIARIAS para el historial
        daily_cert_str = " ".join([f"{k}:{horas}h" for k, horas in certificaciones_horas.items() if horas > 0])

        # Guardar en daily_logs
        self.daily_logs.append({
            "Fecha": fecha,
            "No Alcohol (0%)": no_alcohol,
            "No Media (0%)": no_media,
            "No Porno (0%)": no_porno,
            "8H Descanso (100%)": descanso_8h,
            "Meditación (min)": minutos_meditacion,
            "Buen Círculo (100%)": buen_circulo,
            "Ejercicio (5:30-5:50 PM)": ejercicio,
            "Horario GOD": horario_god,
            "Certificaciones Avanzadas": daily_cert_str
        })

        # Guardar en el archivo
        self.save_to_file(fecha_str, no_alcohol, no_media, no_porno, descanso_8h, minutos_meditacion, buen_circulo, ejercicio, horario_god, daily_cert_str)

    def save_to_file(self, fecha, no_alcohol, no_media, no_porno, descanso_8h, minutos_meditacion, buen_circulo, ejercicio, horario_god, certificaciones):
        """Guarda la entrada en 'historial_god.md' con el formato exacto."""
        columns = [fecha, no_alcohol, no_media, no_porno, descanso_8h, str(minutos_meditacion), buen_circulo, ejercicio, horario_god, certificaciones]
        row = "| " + " | ".join(map(str, columns)) + " |\n"
        with open('historial_god.md', 'a', encoding='utf-8') as f:
            if f.tell() == 0:  # Archivo vacío, escribir encabezados
                headers = "| Fecha | No Alcohol (0%) | No Media (0%) | No Porno (0%) | 8H Descanso (100%) | Meditación (min) | Buen Círculo (100%) | Ejercicio (5:30-5:50 PM) | Horario GOD | Certificaciones Avanzadas |\n"
                separator = "| ---------- | :-------------: | :-----------: | :-----------: | :----------------: | :--------------: | :-----------------: | :----------------------: | :---------: | :-------------------------------------------------------------------: |\n"
                f.write(headers)
                f.write(separator)
            f.write(row)

    def update_level(self):
        """Actualiza el nivel basado en los puntos."""
        new_level = 1 + (self.points // 100)
        if new_level != self.level:
            self.level = new_level
            print(f"¡Subiste al nivel {self.level}!")

    def view_history(self):
        """Muestra el historial completo en la consola y las horas acumuladas."""
        try:
            with open('historial_god.md', 'r', encoding='utf-8') as f:
                print(f.read())
            print("\nHoras acumuladas en certificaciones:")
            for cert, horas in self.certificaciones_horas.items():
                if horas > 0:
                    print(f"  {cert}: {horas} horas")
        except FileNotFoundError:
            print("⚠️ No hay historial disponible.")

def get_valid_input(prompt, expected_type=str, allow_spaces=False, allow_volver=False):
    """Obtiene una entrada válida del usuario, con opción de 'volver'."""
    while True:
        value = input(prompt).strip()
        if allow_volver and value.lower() == "volver":
            return "volver"
        if not allow_spaces and ' ' in value:
            print("⚠️ La respuesta no debe contener espacios. Intenta nuevamente.")
            continue
        if expected_type == float:
            try:
                return float(value)
            except ValueError:
                print("⚠️ Debes ingresar un número (puede ser decimal). Intenta nuevamente.")
        elif expected_type == int:
            try:
                return int(value)
            except ValueError:
                print("⚠️ Debes ingresar un número entero. Intenta nuevamente.")
        else:
            return value

def main():
    god_system = GODSystem()

    # Manejador de Ctrl+C
    def signal_handler(sig, frame):
        print("\n¡Hasta luego!")
        exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        print("""
██████╗  █████╗ ██╗██╗  ██╗   ██╗    ██╗  ██╗ █████╗ ██████╗ ██╗████████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║██║  ╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔══██╗██║╚══██╔══╝    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║███████║██║██║   ╚████╔╝     ███████║███████║██████╔╝██║   ██║          ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██╔══██║██║██║    ╚██╔╝      ██╔══██║██╔══██║██╔══██╗██║   ██║          ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝██║  ██║██║███████╗██║       ██║  ██║██║  ██║██████╔╝██║   ██║          ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                                         
""")
        print("\n--- Menú ---\n")
        print("1. Ingresar datos del día")
        print("2. Visualizar historial")
        print("3. Salir\n")
        option = input("Elige una opción (1-3): ").strip()

        if option == '1':
            preguntas = [
                ("Ingresa la fecha (dd/mm/yyyy): ", str, False),
                ("¿Te abstuviste de alcohol? (✓/x): ", str, False),
                ("¿Evitaste redes sociales y contenido multimedia? (✓/x): ", str, False),
                ("¿Te abstuviste de pornografía? (✓/x): ", str, False),
                ("¿Dormiste 8 horas? (✓/x): ", str, False),
                ("¿Cuántos minutos meditaste?: ", int, False),
                ("¿Te rodeaste de un buen círculo? (✓/x): ", str, False),
                ("¿Hiciste ejercicio? (✓/x): ", str, False),
                ("¿Seguiste tu horario GOD? (✓/x): ", str, False),
            ]
            respuestas = []
            i = 0
            while i < len(preguntas):
                prompt, expected_type, allow_spaces = preguntas[i]
                value = get_valid_input(prompt, expected_type, allow_spaces, allow_volver=True)
                if value == "volver":
                    if i > 0:
                        i -= 1
                    continue
                respuestas.append(value)
                i += 1

            fecha_str, no_alcohol, no_media, no_porno, descanso_8h, minutos_meditacion, buen_circulo, ejercicio, horario_god = respuestas

            try:
                fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            except ValueError:
                print("⚠️ Formato de fecha incorrecto. Usa dd/mm/yyyy.")
                continue

            if any(log['Fecha'] == fecha for log in god_system.daily_logs):
                print("⚠️ Ya existe un registro para esta fecha.")
                continue

            # Preguntar por horas dedicadas a certificaciones
            certificaciones_horas = {}
            for cert in god_system.certificaciones_horas:
                while True:
                    horas = get_valid_input(f"Ingresa las horas dedicadas a {cert} hoy (puede ser decimal): ", float, allow_spaces=False)
                    if horas >= 0:
                        if horas > 0:
                            certificaciones_horas[cert] = horas
                        break
                    else:
                        print("⚠️ Las horas deben ser un número positivo.")

            god_system.calculate_daily_score(fecha_str, no_alcohol, no_media, no_porno, descanso_8h, minutos_meditacion, buen_circulo, ejercicio, horario_god, certificaciones_horas)

            print(f"\nPuntos totales: {god_system.points}")
            print(f"Racha actual: {god_system.streak}")
            print(f"Nivel: {god_system.level}")
            print("Horas acumuladas en certificaciones:")
            for cert, horas in god_system.certificaciones_horas.items():
                if horas > 0:
                    print(f"  {cert}: {horas} horas")

        elif option == '2':
            god_system.view_history()

        elif option == '3':
            print("¡Hasta luego!")
            break

        else:
            print("⚠️ Opción inválida. Elige 1, 2 o 3.")

if __name__ == "__main__":
    main()