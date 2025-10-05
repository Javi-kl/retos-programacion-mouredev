from datetime import datetime, date, timedelta

# 0.1 fecha de hoy
now_date_hour = datetime.now()
print(f"Fecha y hora actual: {now_date_hour}")

# 0.2 Solo fecha
now_date = date.today()
print(f"Fecha actual: {now_date}")

# 0.3 fecha de nacimiento
born_date = datetime(year=1990, month=11, day=23, hour=1, minute=30, second=34)
print(f"Fecha nacimiento sin formato: {born_date}")

# 0.4formatear fecha
format_born_Date = born_date.strftime(
    "%Y-%m-%d"
)  # strftime aplica un formato y devuelve un string

parsed_date = datetime.strptime(
    format_born_Date, "%Y-%m-%d"
)  # strptime convierte el string a un objeto fecha operable
print(f"Fecha nacimiento: {parsed_date}")


# 0.5 Mostrar edad
def calculate_age(born_date, now_date):
    age = now_date.year - born_date.year
    return age


age = calculate_age(born_date, now_date)
print(f"Edad: {age} años")


"""
Extra
"""
print("\n---- Extra ----")

months_list = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
]


# formatear fecha
def format_born_date(born_date, months_list):
    # 1. formato dia mes año completo
    print(f"Format 1: {born_date.strftime('%d,%m,%Y')}")
    # 2. formato hora minuto segundos
    print(f"Format 2: {born_date.strftime('%H:%M:%S')}")
    # 3. formato año
    print(f"Format 3: {born_date.strftime('%Y')}")
    month = born_date.month
    # 4. formato nombre del mes en español
    print(f"Format 4: {months_list[month-1]}")
    # 5. formato número de la semana
    week_of_month = (born_date.day - 1) // 7 + 1
    print(f"Format 5: {week_of_month} semana del mes")
    # 6. formato dia de la semana en inglés
    day_week = born_date.strftime("%A")
    print(f"Format 6: dia de la semana {day_week}")
    # 7. formato dia del año
    day_of_year = born_date.timetuple().tm_yday
    print(f"Format 7: dia del año {day_of_year}")
    # 8. formato iso
    print(f"Formato 8 - ISO: {born_date.isoformat()}")
    # 9. formato ultimos dos digitos del año
    print(f"Format 9: {born_date.strftime('%y')}")
    # 10. formato segundos desde 1970 !!
    timestamp = born_date.strftime("%s")
    print(f"Format 10: timestamp unix: {timestamp}")


format_born_date(born_date, months_list)
