print("----- ATM MENU -----")
initial_balance=10000
atm=int(input("""
select the option fron the
1.Check Balance
2.Deposit
3.Withdraw
4.Exit
Enter your choice:
"""))
match atm:
    case 1:
        print("initial_balance",initial_balance)
    case 2:
        deposit=int(input("enter the deposit"))
        initial_balance+=deposit
        print("initial_balance",initial_balance)

    case 3:
        withdram=int(input("amount"))
        initial_balance-=withdram
        print("initial_balance",initial_balance)
    case 4:
        print("exit")
