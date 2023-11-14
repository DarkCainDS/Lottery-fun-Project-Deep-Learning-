import calendar
from datetime import date, timedelta

def generate_endpoints(start_date, end_date, starting_sorteo, ending_sorteo):
    months = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
        7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    endpoints = []

    sorteo_number = starting_sorteo
    current_date = start_date

    while current_date <= end_date and sorteo_number <= ending_sorteo:
        # Determinamos el día de la semana (0: Lunes, 1: Martes,..., 6: Domingo)
        day_of_week = current_date.weekday()
        
        if day_of_week in {1, 4, 6}:  # Si es martes (1), viernes (4) o domingo (6)
            fecha = f"{current_date.day}-de-{months[current_date.month]}"
            print(f"({sorteo_number}, '{fecha}-de-{current_date.year}'),")
            sorteo_number += 1  # Incrementa el número de sorteo

        current_date += timedelta(days=1)

start_date = date(2017, 4, 6)  # 6/04/2017
end_date = date(2023, 10, 1)  # 01 de octubre de 2023
starting_sorteo = 4000
ending_sorteo = 5015

generate_endpoints(start_date, end_date, starting_sorteo, ending_sorteo)
