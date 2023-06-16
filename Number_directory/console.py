# Функции для вывода и ввода
import text, model
def prinytie_chisla():
    while True:
        print(text.meny)
        a = input(text.meny_choice)
        if a.isdigit() and 0 < int(a) < 9:
            return int(a)
        else:
           print("\n" + "=" * len(text.no_choice))
           print(text.no_choice)
           print("=" * len(text.no_choice) + "\n")

def otkritie_fila():
    if model.open_file() == 0:
        print("\n" + "=" * len(text.no_choice))
        print(text.false_dvazdy)
        print("=" * len(text.no_choice) + "\n")
    else:
        model.open_file()
        print("\n" + "=" * len(text.telephon_open))
        print(text.telephon_open)
        print("=" * len(text.telephon_open) + "\n")

def vivod_dannih():
  print("\n" + "=" * 110)
  if len(model.phone_book) == 0:
      print(text.otrkoy_meny)
  else:
    model.zagolovok()
    print()
    for item in model.phone_book:
        id = item.get("id")
        name = item.get("name")
        phone = item.get("phone")
        comment = item.get("comment")
        print(f"{id:<10} {name:<25} {phone:<15} {comment:<50}")
  print("=" * 110 + "\n")

def vivod_dopolnenie():
    if len(model.phone_book) == 0:
        print("\n" + "=" * 110)
        print(text.otrkoy_meny)
        print("=" * 110 + "\n")
    else:
      vivod_dannih()
      print("\n" + "=" * 110)
      model.dobavlenie()
      print("=" * 110 + "\n")

def vivod_poisc():
    if len(model.phone_book) == 0:
        print("\n" + "=" * 110)
        print(text.otrkoy_meny)
        print("=" * 110 + "\n")
    else:
        vivod_dannih()
        chto_nachlos = model.poisc()
        print("\n" + "=" * 110)
        if len(chto_nachlos) == 0:
            print(text.res_poisc_false)
        else:
            print(text.res_poisc_true)
            print()
            for item in chto_nachlos:
                id = item.get("id")
                name = item.get("name")
                phone = item.get("phone")
                comment = item.get("comment")
                print(f"{id:<10} {name:<25} {phone:<15} {comment:<50}")
        print("=" * 110 + "\n")

def vivod_save():
    print("\n" + "=" * 110)
    if len(model.phone_book) == 0:
        print(text.otrkoy_meny)
    elif model.proverka_save() == 0:
        print(text.save_false)
    else:
        model.save_file()
        print(text.save_true)
    print("=" * 110 + "\n")

def konec():
    print("\n" + "=" * 110)
    print(text.the_end)
    print("=" * 110 + "\n")

def redactirovanie():
    if len(model.phone_book) == 0:
        print("\n" + "=" * 110)
        print(text.otrkoy_meny)
        print("=" * 110 + "\n")
    else:
        vivod_dannih()
        print("\n" + "=" * 110)
        model.redact()
        print("=" * 110 + "\n")

def vivod_deleted():
    if len(model.phone_book) == 0:
        print("\n" + "=" * 110)
        print(text.otrkoy_meny)
        print("=" * 110 + "\n")
    else:
        vivod_dannih()
        print("\n" + "=" * 110)
        model.deleted()
        print("=" * 110 + "\n")



   
    
    
        