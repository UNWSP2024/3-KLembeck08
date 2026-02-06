age = int(input("Enter the person's age: "))

if age <= 1:
    print("The person is an infant.")
elif age < 13:
    print("The person is a child.")
elif age < 20:
    print("The person is a teenager.")
else:
    print("The person is an adult.")
