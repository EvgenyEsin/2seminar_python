# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input("Сколько монет лежит на столе? "))
reshka = 0  # сюда будем запоминать кол-во монет, лежащих решкой
for i in range(n):
    side = int(input("Если решка, введите  /1/, если герб, то /0/: "))
    if side == 1:
        reshka += 1
if reshka == 0 or reshka == n:
    print("Все монеты лежат одной и той же стороной, ничего переворачивать не надо.")
elif reshka*2 < n:  # если решек меньше половины, то переворачиваем только их
    print(f'Нужно перевернуть {reshka} монет, лежащих решкой')
elif reshka*2 > n:  # иначе будем переворачивать гербы
    print(f'Нужно перевернуть {n-reshka} монет, лежащих гербом')
else:
    print("Все равно, какие монеты переворачивать, так как их поровну")
