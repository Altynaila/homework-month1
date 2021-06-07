to_do_list = ["зарядка","завтрак","ехать на работу","позвонить лпр","сделать норму 75","спать"]
for i in to_do_list:
    print(i)
    n = input("ответ: ")
    if n.strip() == "да":
        continue
    else:
        print("не прошел")
        break