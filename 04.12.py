import datetime

year = datetime.datetime.now().year

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except:
        print("Please, enter a number")

print(f"You were born in {year-age} year")
