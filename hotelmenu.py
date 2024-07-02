#define the menu of restaturent
#create disnary
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,

}
#Great
print("Welcome to python restaturent")
print("Pizza: Rs40\n Pasta:Rs50\n Burger: Rs60\n Salad:Rs70\n Coffee:Rs80 ")
order_total=0
#90+70=150 
#user order
item1=input("Enter the name of item you want to oreder =")
#use membership operator to check item avaible in menu
if item1 in menu:
    order_total+=menu[item1]#update oredr total:ie:0+50
    print(f"Your item {item1} has been added to your order")

else:
    print(f"Order item {item1}is not available yet")

another_order=input("do yo want to add another item? (Yes/No)")
if another_order=="Yes":
    item2=input("Enter the name of second item =")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"item {item2} has been added to order")
    else:
        print(f"ordered item{item2}is not available!!")    


print(f"The total amount of items to pay is {order_total}")        


