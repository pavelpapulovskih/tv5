mothers_height = [172, 177, 158, 170, 178, 175, 164, 160, 169, 165]
daughters_height = [173, 175, 162, 174, 175, 168, 155, 170, 160]
n1 = len(mothers_height)
n2 = len(daughters_height)
mean_mothers = sum(mothers_height) / n1
mean_daughters = sum(daughters_height) / n2
var_mothers = sum((x - mean_mothers) ** 2 for x in mothers_height) /(n1 - 1)
var_daughters = sum((x - mean_daughters) ** 2 for x in
daughters_height) / (n2 - 1)
# t-статистика для независимых выборок
pooled_variance = ((n1 - 1) * var_mothers + (n2 - 1) *
var_daughters) / (n1 + n2 - 2)
t_stat_ind = (mean_mothers - mean_daughters) /math.sqrt(pooled_variance * (1 / n1 + 1 / n2))
# Критическое значение для двустороннего теста при α = 0.05 и df =
18
t_crit_ind = 2.100922
print("Задача 3: Статистически значимые различия в росте матерей идочерей")
print(f"t-статистика: {t_stat_ind}")
print(f"Критическое значение: {t_crit_ind}")
if abs(t_stat_ind) > t_crit_ind:print("Есть статистически значимые различия в росте матерей дочерей.")
else:print("Нет статистически значимых различий в росте матерей идочерей.")
print()