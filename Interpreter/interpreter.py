expression = input("Expression: ").strip()
number_1, operator, number_2 = expression.split(" ")

if operator == "+":
    expression = float(number_1) + float(number_2)
elif operator == "-":
    expression = float(number_1) - float(number_2)
elif operator == "*":
    expression = float(number_1) * float(number_2)
elif operator == "/":
    expression = float(number_1) / float(number_2)

print(round(expression, 2))
