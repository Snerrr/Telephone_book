# Фунции достать, преобразовать
path = r"Number_directory/phone.txt"
import text
phone_book = []
iznachalniy_book = []

def zagolovok():
    print(f"{text.u:<10} {text.n:<25} {text.p:<15} {text.c:<50}")

def open_file(): 
    global phone_book
    if len(phone_book) > 0:
        return False
    else:
        with open(path, "r", encoding="UTF-8") as file:
            ludi = file.readlines()
            for element in ludi:
                user_id, name, phone, comment = element.strip().split(":")
                phone_book.append({"id": user_id, "name": name, "phone": phone, "comment": comment})
                iznachalniy_book.append({"id": user_id, "name": name, "phone": phone, "comment": comment})


def dobavlenie():
    new_contact = []
    all_id = []
    for element in phone_book:
            all_id.append(element.get("id"))
    id = input(text.id_users)
    if id.isdigit() == 0 or id in all_id:
        while id.isdigit() == 0 and len(id) > 0 or id in all_id:
            print(text.not_isdigit)
            id = input(text.id_users)           
    name = input(text.name_users)
    phone = input(text.number_users)
    comment = input(text.comment_users)
    if len(id) > 0 and len(name) > 0 and len(phone) > 0 and len(comment) > 0:
        phone_book.append({"id": id, "name": name, "phone": phone, "comment": comment})
        new_contact.append({"id": id, "name": name, "phone": phone, "comment": comment})
        print()
        print(text.dobavleny_true)
        print()
        zagolovok()
        print()
        for item in new_contact:
            id = item.get("id")
            name = item.get("name")
            phone = item.get("phone")
            comment = item.get("comment")
            print(f"{id:<10} {name:<25} {phone:<15} {comment:<50}")
    else:
        print()
        print(text.dobavleny_false)

def poisc():
    nachlos = []
    print()
    search = input(text.name_search)
    print()
    for element in phone_book:
        for key, value in element.items():
            if search.lower() in value.lower():
                nachlos.append(element)
                break     
    return(nachlos)

def save_file():
    book_posle = []
    with open("Number_directory/phone.txt", "w", encoding = "UTF-8") as file:
        for item in phone_book:
          id = item.get("id")
          name = item.get("name")
          phone = item.get("phone")
          comment = item.get("comment")
          file.write(f"{id}:{name}:{phone}:{comment}\n")
    with open(path, "r", encoding="UTF-8") as file:
        contacty = file.readlines()
        for element in contacty:
            user_id, name, phone, comment = element.strip().split(":")
            book_posle.append({"id": user_id, "name": name, "phone": phone, "comment": comment})
        global iznachalniy_book
        iznachalniy_book = book_posle
        

def proverka_save():
    do_izmenenia = list.copy(iznachalniy_book)
    posle_izmenenia = []
    for item in phone_book:
          posle_izmenenia.append(item)
    if do_izmenenia == posle_izmenenia:
         return False

def redact():
    id_poisc = input(text.redact_contact)
    izmenenniy_contanct = []
    all_id = []
    for element in phone_book:
            all_id.append(element.get("id"))
    kol = 1
    kol_1 = 0
    for element in phone_book:
        if id_poisc == element.get("id"):
            kol -= 1
            print(text.izmenit)
            print()
            id_novoe = input(text.id_users)
            if not id_novoe.isdigit() and len(id_novoe) > 0 or id_novoe in all_id:
              while id_novoe.isdigit() == 0 and len(id_novoe) > 0 or id_novoe in all_id:
                  print(text.not_isdigit_red)
                  id_novoe = input(text.id_users)
            name_novoe = input(text.name_users)
            phone_novoe = input(text.number_users)
            comment_novoe = input(text.comment_users)
            if not id_novoe:
                id_novoe = element.get("id")
                kol_1 += 1
            if not name_novoe:
                name_novoe = element.get("name")
                kol_1 += 1
            if not phone_novoe:
                phone_novoe = element.get("phone")
                kol_1 += 1
            if not comment_novoe:
                comment_novoe = element.get("comment")
                kol_1 += 1
            if kol_1 == 4:
                print()
                print(text.izmenit_nichego)
            else:
                element["id"] = id_novoe
                element["name"] = name_novoe
                element["phone"] = phone_novoe
                element["comment"] = comment_novoe
                print()
                print(text.izmenit_true)
                print()
                izmenenniy_contanct.append({"id": id_novoe, "name": name_novoe,
                                             "phone": phone_novoe, "comment": comment_novoe})
                for item in izmenenniy_contanct:
                    id = item.get("id")
                    name = item.get("name")
                    phone = item.get("phone")
                    comment = item.get("comment")
                    print(f"{id:<10} {name:<25} {phone:<15} {comment:<50}")
            break
    if kol == 1:
        print()
        print(text.izmenit_false)

def deleted():
    kol = 1
    global phone_book
    number_deleted = input(text.delet_user)
    if number_deleted.isdigit() == 0:
        while number_deleted.isdigit() == 0:
            print(text.delet_notisdidget)
            number_deleted = input(text.delet_user) 
    for i in range(len(phone_book)):
        if number_deleted == phone_book[i].get("id"):
            kol -= 1
            element_deleted = phone_book.pop(i)
            print()
            print(text.deleted_true)
            id = element_deleted.get("id")
            name = element_deleted.get("name")
            phone = element_deleted.get("phone")
            comment = element_deleted.get("comment")
            print(f"{id:<10} {name:<25} {phone:<15} {comment:<50}")
            break
    if kol == 1:
        print()
        print(text.izmenit_false)

    

    
    