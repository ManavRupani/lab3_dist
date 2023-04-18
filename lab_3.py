
print("WELCOME TO ALMOND SHOPING SITE")
print("1.Add product to the cart")
print("2.Search the product")
print("3.Delete product from the cart")
print("4.Exit")
my_cart=dict()
count=0
main=True
while(main==True):
    u_input=int(input("Enter your choise: "))
    if u_input==4:
        break
    while(u_input!=4):
        if count==5:
            print("your cart is full ")
            break
        elif u_input==1:
            a1=int(input("Enter number of items you want to add "))
            for i in range(a1):
                if count==5:
                    print("your cart is full ")
                    break
                x=input("Enter an item ")
                y=input("Enter the brand name: ")
                my_cart[x]=y
                count+=1
            print("You entered following items to the cart")
            for key,value in my_cart.items():
                print(key+":"+value)
            print("\n")
            u_input=0
            break
        elif u_input==2:
            a2=input("Ennter item to be searched: ")
            print(a2+" : "+my_cart.get(a2, "not found"))
            u_input=0
            break
        elif u_input==3:
            if len(my_cart)>0:
                a3=input("enter item to be deleted")
                try:
                    my_cart.pop(a3)
                except:
                    print("Item not found")
                count-=1
                u_input=0
                break
            else:
                print("Your Cart is Empty")
                break
        else:
            print("Wrong option Entered")
            u_input=0
            break

        # else:
        #     pass
