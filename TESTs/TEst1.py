orange_price = 17.5
my_money = 14
tea_price = 14
if my_money > orange_price:
    print("I buy orange")
else:
		# Вкладений умовний оператор if зі своїм блоком else
    if my_money >= tea_price:
        print("Not orange, just tea")
    else:
        print("I buy apple")
print("The end")