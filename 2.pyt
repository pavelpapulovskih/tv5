weights = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
mu_0 = 200
alpha = 0.01
n = len(weights)
mean_weight = sum(weights) / n
s = math.sqrt(sum((x - mean_weight) ** 2 for x in weights) / (n -
1))
# t-статистика
t_stat = (mean_weight - mu_0) / (s / math.sqrt(n))
# Критическое значение для t-распределения с n-1 степенью свободы
t_crit = 3.249835 # Для двустороннего теста при α = 0.01 и df = 9
print("Задача 2: Проверка гипотезы с использованием t-теста")
print(f"t-статистика: {t_stat}")
print(f"Критическое значение: {t_crit}")
# Проверка гипотезы
if abs(t_stat) > t_crit:print("Отвергаем нулевую гипотезу в пользу альтернативнойгипотезы.")
else:print("Нет оснований отвергать нулевую гипотезу.")
print()
