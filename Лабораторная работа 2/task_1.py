money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
while (salary + money_capital) >= spend:
    money_capital = money_capital + salary - spend
    spend = spend + increase * spend
    months = months + 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
