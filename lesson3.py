#age = False
#print(type(age))
age = int(input())
name = input()
if age > 18:
    print("Вам можно войти!")
else:
    print("Вам нам нельзя")

if name == "Altynai":
    print("Вас зовут Алтынай!")
else:
    print("Вы не Алтынай!")

if name != "Altynai":
    print("Вы не  Алтынай!")
else:
    print("Вас зовут Алтынай")