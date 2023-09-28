temp = int(input("Введите температуру: "))
humidity = int(input("Введите влажность: "))
txt = ""

if (humidity > 0 and humidity < 100):
    if(humidity>=90):
        txt+="На улице идут осадки"
        if(temp < 0):
            txt+="\n На улице снег"
        else:
            txt+="\n На улице идёт дождь"
    else:
        txt+="Осадков нет"
else:
    txt+="Некоректно указанн процент влажности"

print(txt)
