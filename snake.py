import curses
import random

# basic snake game for python3. How fitting
# Setup the screen
screen = curses.initscr()
curses.curs_set(0)
sh, sw = screen.getmaxyx()
window = curses.newwin(sh, sw, 0, 0)
window.keypad(1)
window.timeout(100)

# Setup snake
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Food setup
food = [sh // 2, sw // 2]
window.addch(food[0], food[1], curses.ACS_BULLET)

key = curses.KEY_RIGHT

# Move the snake
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[1][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit(0)

    # Make new head from the original
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_BULLET)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], curses.ACS_BULLET)
