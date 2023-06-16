# Главная папка, где все финальные функции
import console
def start():
    while True:
        choise = console.prinytie_chisla()
        match choise:
            case 1:
                console.otkritie_fila()
            case 2:
                console.vivod_save()
            case 3:
                console.vivod_dannih()
            case 4:
                console.vivod_dopolnenie()
            case 5:
                console.vivod_poisc()
            case 6:
                console.redactirovanie()
            case 7:
                console.vivod_deleted()
            case 8:
                console.konec()
                break