time = int(input("Введите время: "))
txt=""

if(time >= 3 and time <=5):
    txt+="Раннее утро"
elif(time >= 6 and time <=10):
    txt+="Утро"
elif(time >= 11 and time <=15):
    txt+="День"
elif(time >= 16 and time <=21):
    txt+="Вечер"
else: txt+="Ночь"

print("Сейчас " + txt)