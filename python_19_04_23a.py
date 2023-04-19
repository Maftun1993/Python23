# name= input("What is your name? ")
# print("Your name is ", name)

# age = input("what is your age? ")
# result = 2023 - int(age)
# print("You was born in",result)



# rent = input("Monthly rent = ")
# extra = input("Monthly Water and Electrecity = ")

# yearlyRent = 12 * int(rent)
# yearlyExtra = 12 * int(extra)

# total = str("Your yearly expence: ") + str(yearlyRent + yearlyExtra)
# print(total)


rent, extra = input("What is your rent and water and electrecity expences ").split()

monthlyPayment= int(rent) + int(extra)

print(monthlyPayment)