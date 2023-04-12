Heads = 0
Total = 0

with open("prob.txt", "r+") as file:
    file.truncate()

while True:
    HT = input("Select: ")
    if HT.strip() == 'h':
        with open("prob.txt", "a+") as file:
            file.writelines(HT + "\n")
            Heads += 1
            Total += 1
            Value = (Heads/Total)*100
            print(f"The head percentage is: {Value}%")
    elif HT.strip() == 't':
        with open("prob.txt", "a+") as file:
            file.writelines(HT + "\n")
            Total += 1
            print(f"The head percentage is: {Value}%")
    else:
        break






