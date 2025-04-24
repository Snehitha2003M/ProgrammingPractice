print("*****Besant Hotel*****")

print("menu:\n 1.Biriyani rs:100 \n 2.pizza")

menu_card={"biriyani":100,"pizza":200}

your_order=input("enter your oder").lower()

if your_order in menu_card:
    print(f"yes {your_order} is available")
    quantity=int(input(f"enter how many you want"))
    if your_order=="biriyani":
        total=menu_card[your_order]*quantity
        print(f"your total amount is {total}")
        if total>=1000:
            total-=200
            print(f"you ordered  more than 1000 rs your total amount is {total}")
    elif your_order=="pizza":
        total=menu_card[your_order]*quantity
        print(f"your total amount is {total}")
        if total>=1000:
            total-=200
            print(f"you ordered  more than 1000 rs your total amount is {total}")
else:
    print(f"your order is not available")


