print("Calculate Unit Weight of any steel bar")
print(      " *Simple tool by Mr. Kareer*")
def main():
    x = float(input("Enter Dia Size (In MM): "))
    y = float(input("Length of the steel bar (In Metre): "))
    m = float(input("Total no. of bars: "))

    print("The weight of the bar is",round(((x*x)/162)*y*m,2), "Kgs")

    print("Run Again ?")
    a= input("yes/no: " )
    if a == "yes":
        main()
    elif a == "no":
        print("Press any key to exit")
        input()
        exit()
    else:
        print("Invalid Entry")
        input("Press any key to try again")
        main()

main()