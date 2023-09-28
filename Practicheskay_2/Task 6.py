def Uppercase(string) -> bool:
    if (any(pasword.isupper() for pasword in string)):
        return True
    return False

def Lowercase(string) -> bool:
    if (any(pasword.islower() for pasword in string)):
        return True
    return False

def isNumber(string) -> bool:
    if(any(pasword.isdigit() for pasword in string)):
        return True
    return False

def checkPassword(pasword):
    txt = ""
    if (Uppercase(pasword) and Lowercase(pasword) and isNumber(pasword) and len(pasword) >= 4 and pasword != ""):
        txt += "Пароль верный"

    if (not pasword != ""):
        txt += "\nВы ничего не ввели! "
    if (not Uppercase(pasword)):
        txt += "\nПароль должен содержать заглавные буквы"
    if (not Lowercase(pasword)):
        txt += "\nПароль должен содержать строчеые буквы"
    if (not isNumber(pasword)):
        txt += "\nПароль должен содержать цифры"
    if (not len(pasword) >= 4):
        txt += "\nДлина пароля меньше 4 символов"

    print(txt)

def main():

    checkPassword(pasword = str(input("Введите пароль: ")))

if __name__ == '__main__':
    main()


