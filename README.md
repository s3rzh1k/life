# life
Репозиторий с игрой Жизнь

Реализация игры «Жизнь» (Conway's Game of Life) математика Джона Конвея.
Правила:
• Место действия игры - клеточное поле.
• Поколение -это одна итерация изменения поля
• Каждая клетка может иметь два состояния: заполнена(жива), пуста(мертва)
• У каждой клетки есть соседи - 8 соседних клеток
• В пустой клетке, рядом с которой ровно три заполненные клетки, зарождается жизнь
• Если у заполненной клетки три или два заполненных соседа, то она продолжает быть заполненной
• В противном случае, если соседей меньше двух или больше трёх, клетка умирает («от одиночества» или «от перенаселённости»).

Игра написана на языке Python 3.7.
Для запуска игры необходимо: 
1) установить библиотеки "pygame" (v1.9.6) и "numpy" (1.19.2)
2) открыть файл "life_0_2.py"

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Repository with the game Life

Here is the realization of the Conway's Game of Life.
The rules:
• Any live cell with fewer than two live neighbours dies, as if by underpopulation.
• Any live cell with two or three live neighbours lives on to the next generation.
• Any live cell with more than three live neighbours dies, as if by overpopulation.
• Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
• Any live cell with two or three live neighbours survives.
• Any dead cell with three live neighbours becomes a live cell.
• All other live cells die in the next generation. Similarly, all other dead cells stay dead.

This game is written on Python 3.7.
For launching:
1) install "pygame" (v1.9.6) and "numpy" (1.19.2) frameworks
2) open file "life_0_2.py"
