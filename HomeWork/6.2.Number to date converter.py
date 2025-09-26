day_name1 = 'день'
day_name2 = 'дні'
day_name3 = 'днів'

sec = int(input("Enter Your date: "))
minutes, seconds = divmod(sec, 60)
hours, minutes = divmod(minutes, 60)
day, hours = divmod(hours, 24)

if day % 10 == 1 and day % 100 != 11:
    print(sec, f"-> {day},", day_name1 ,f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
elif day % 10 in (2, 3, 4) and day % 100 not in (12, 13, 14):
    print(sec, f"-> {day},", day_name2, f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
else:
    print(sec, f"-> {day}", day_name3, f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")