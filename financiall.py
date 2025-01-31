print("Hello, I am your financial advisor. Let me calculate your income.")

while True:
    print("Do you want to calculate your income by hourly, weekly, biweekly, or yearly?")
    user_input = input().lower()

    if user_input == "hourly":
        hourly_income = float(input("How much do you make an hour? "))
        weekly_hours = float(input("How many hours do you work a week? "))
        weekly_income = weekly_hours * hourly_income
        yearly_income = weekly_income * 52
        print(f"You make ${yearly_income:.2f} a year.")
    elif user_input == "weekly":
        weekly_income = float(input("How much do you make a week? "))
        yearly_income = weekly_income * 52
        print(f"You make ${yearly_income:.2f} a year.")
    elif user_input == "biweekly":
        biweekly_income = float(input("How much do you make every two weeks? "))
        yearly_income = biweekly_income * 26
        print(f"You make ${yearly_income:.2f} a year.")
    else:
        print("Invalid input. Please enter 'hourly', 'weekly', 'biweekly', or 'yearly'.")

    again = input("Do you want to calculate your income in another way? (yes to continue, no to exit): ").lower()
    if again != 'yes':
        print("Thank you for using the financial advisor. Goodbye!")
        break
