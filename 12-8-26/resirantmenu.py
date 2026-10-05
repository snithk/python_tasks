print("---- MENU -----")
menu=int(input("""
select the option fron the
1.Biryani
2.Chicken 65
3.Veg Pulao
4.Butter Chicken
5.Paneer Tikka
Enter your choice:
"""))
match menu:
    case 1:
        print("Item: Biryani")
        print("Price      : ₹150")
    case 2:
        print("Item: Chicken 65")
        print("Price      : ₹180")
    case 3:
        print("Item: Veg Pulao")
        print("Price      : ₹120")
    case 4:
        print("Item: .Butter Chicken")
        print("Price      : 200")
    case 5:
        print("Item: paneer Tikka")
        print("Price      : ₹180")

