#Homework10 task2
"""
Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.
"""

import matplotlib.pyplot as plt
import numpy as np
import random 


def monte_carlo_pi(num_samples):
    # 1. Визначення моделі або системи.
    inside_integral = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    # 2. Генерація випадкових вхідних даних
    for _ in range(num_samples):
        x = random.uniform(0, 2)
        y = random.uniform(0, 4)
        # 3. Виконання обчислень
        if y <= x**2:
            inside_integral += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # 4. Агрегування та аналіз результатів
    # S = (M/N)*S_1 
    pi_estimate = 2 * 4 * inside_integral / num_samples
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Задаємо кількість випадкових точок
num_samples = 10000

# Запускаємо метод Монте-Карло для обчислення π
pi_estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(num_samples)

# Виводимо результат
print(f"Оцінка значення π за методом Монте-Карло з {num_samples} випадкових точок: {pi_estimate}")


# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

# Візуалізація результатів
ax.scatter(x_inside, y_inside, color='blue', s=1, label='Точки всередині функції')
ax.scatter(x_outside, y_outside, color='red', s=1, label='Точки поза функцією')


plt.grid()
plt.title(f"Метод Монте-Карло: {num_samples}\nОцінка: {pi_estimate}")
plt.legend()
plt.show()


