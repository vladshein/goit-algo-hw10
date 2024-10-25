# goit-algo-hw10

Завдання 2 потребує порівняння двох методів знаходження
площі функції інтегрування(обрана функція y = x^2).
===============================================
Перший метод використовує рандомізований підхід за методом Монте-Карло.
Результати цього методу досить близкі до реальних починаючи з кількості
експериментів 10000 - результат для вказаних обмежень 2.6532
Результати кожен запуск дещо відрізняються, але наближаються до реальних(2.66).
===============================================
Другий метод - реальний, який використовує scipy.integrate та метод quad.
Результат прогнозований і становить 2.66.
===============================================
Висновок: для покращення результату першого методу потрібно більше
експериментів. Тоді результат стає максимально наближеним до реального.
===============================================