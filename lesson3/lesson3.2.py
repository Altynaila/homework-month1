name = input()
age = int(input())
hobby = input()
if name == "Ali" and age > 17 and hobby == "tiktok":
    print("Вы сила")
else:
    print("Ты не сила")

if name == "Ali" or age > 17 or hobby == "tiktok":
    print("Ты либо сила, либоты старше 17, либо твое хобби ТИКТОК")
else:
    print("Ты вообще не подходишь под эти условия!")