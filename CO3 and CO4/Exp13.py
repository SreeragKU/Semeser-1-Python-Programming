from datetime import date


def calage(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


print(calage(date(2000, 9, 26)), "years")
