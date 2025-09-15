
sec = int(input("Enter Your date: "))
minutes, seconds = divmod(sec, 60)
hours, minutes = divmod(minutes, 60)
day, hours = divmod(hours, 24)
print(sec, f"-> {day} днів, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

