import calendar
from datetime import date, timedelta

def generate_endpoints(start_date, end_date, starting_sorteo):
    months = {
        1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
        7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
    }
    endpoints = []

    sorteo_number = starting_sorteo

    current_date = start_date
    while current_date <= end_date:
        # Determinamos el día de la semana (0: Lunes, 1: Martes,..., 6: Domingo)
        day_of_week = current_date.weekday()
        
        if day_of_week in {1, 4, 6}:  # Si es martes (1), viernes (4) o domingo (6)
            day_str = str(current_date.day).zfill(2)
            endpoints.append((sorteo_number, f"{day_str}-de-{months[current_date.month]}"))
            sorteo_number -= 1  # Decrementa el número de sorteo

        current_date += timedelta(days=1)

    return endpoints

start_date = date(2017, 4, 6)  # 6/04/2017
end_date = date(2023, 10, 1)  # 01 de octubre de 2023
starting_sorteo_2017 = 4000  # Sorteo 4000 el 6/04/2017
endpoints = generate_endpoints(start_date, end_date, starting_sorteo_2017)

for endpoint in endpoints:
    print(endpoint)
