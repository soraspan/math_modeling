import numpy as np
import matplotlib.pyplot as plt


x = [3, 4, 5]
y = [40, 10, 30]

plt.plot(x, y, color='g', label='luchte', marker='>', ms=5)

# --- Украшательства ---
plt.xlabel('Coord: x') # Подись оси ОХ
plt.ylabel('Coord: y') # Подпись оси ОУ
plt.legend() # Вызов "легенды"
plt.title('Base') # Общая подпись графика
plt.grid() # Подключение сетки
plt.show()