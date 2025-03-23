overtime_hours = 0  # built in biweekly
additional_overtime = 0  # overtime on top of built in overtime and normal work days
hours_worked = 0  # hours worked biweekly
shift_length = float(0)  # in hours
hourly_pay = float(0)  # in dollars
paid_holidays = 0  # calculated using full shift of pay
retirement_percentage = float(0)  # amount you commit to a 401k in decimal
retirement_plan_match = float(
    0
)  # amount your company matches in decimal.  Does not account for federal caps yet
stock_plan_cont = float(0)  # amount you contribute to ESPP in decimal
stock_plan_disc = float(0)  # amount company stock is discounted by in decimal
hsa_yearly = float(0)  # yearly company funded hsa contributions
other_income = float(0)  # other income (holiday pay is counted into this number later)

print("Please enter the following information")
print("1. Built In overtime hours worked biweekly")
print("2. Additional overtime worked biweekly")
print("3. non-overtime hours worked biweekly")
print("4. Length of normal work day")
print("5. non-overtime hourly pay")
print("6. # of paid holidays")
print("7. Percent of pay contributed to retirement")
print("8. Matching percentage of your company")
print("9. Stock purchase plan contribution")
print("10. Stock purchase plan discount")

overtime_hours = float(input())
additional_overtime = float(input())
hours_worked = float(input())
shift_length = float(input())
hourly_pay = float(input())
paid_holidays = float(input())
retirement_percentage = float(input())
retirement_plan_match = float(input())
stock_plan_cont = float(input())
stock_plan_disc = float(input())


print("11. Company HSA yearly contributions?")
print("12. Other monthly income?")

hsa_yearly = float(input())
other_income = float(input())

other_income = other_income * 12 + paid_holidays * shift_length * hourly_pay

gross = 26 * (
    hours_worked * hourly_pay
    + overtime_hours * hourly_pay * 1.5
    + additional_overtime * hourly_pay * 1.5
)
print("from pay")
print(gross)


gross_with_stock = (
    gross * stock_plan_cont * stock_plan_disc + gross
)  # stock plan added to gross

gross_with_stock_and_retirement = (
    gross * retirement_percentage * retirement_plan_match + gross_with_stock
)  # retirement plan added to gross with stock

print("with stock selling")
print(gross_with_stock)

print("with stock selling and retirement plan")
print(gross_with_stock_and_retirement)

print("with ESPP/Retirement/HSA/Other Income")
print(gross_with_stock_and_retirement + hsa_yearly + other_income)
