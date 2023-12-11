money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

increase += 1
months=0
while True:
    money_capital -= spend-salary
    if money_capital < 0:
        break
    months += 1
    spend *= increase

print("Количество месяцев, которое можно протянуть без долгов:", months)
