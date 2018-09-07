import numpy as np
import random
import time


class Snake_game():
    move_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def __init__(self, SIZE=10):
        self.SIZE = SIZE
        self.reset()

    def reset(self):
        self.field = np.zeros(shape=(self.SIZE,)*2, dtype=int)
        self.snake = [(5, 5)]
        self.direction = 0

        self.place_goal()
        self.render()
        self.score = 0

    def assign(self, coor: tuple, value: int):
        self.field[coor[1]][coor[0]] = value

    def render(self):
        self.field = np.zeros(shape=(self.SIZE,)*2, dtype=int)
        for index, i in enumerate(self.snake):
            if index == 0:
                self.assign(i, 101)
                continue
            self.assign(i, 100)

        self.assign(self.goal, 666)

    def place_goal(self):
        self.goal = (random.randint(0, self.SIZE-1),
                     random.randint(0, self.SIZE-1))
        if self.goal in self.snake:
            self.place_goal()

    def game_loop(self, control=None):
        # 		1
        #	2		0
        # 		3

        # if direction is not directly backwards or not
        if control is not None:
            if abs(self.direction - control) != 2 or len(self.snake) <= 1:
                self.direction = control

        position_change = self.move_list[self.direction]
        new_position = tuple(map(sum, zip(position_change, self.snake[0])))
        self.snake = [new_position] + self.snake

        if self.goal in self.snake:
            self.score += 1
            self.place_goal()
        else:
            self.snake.pop()

        if len(self.snake) != len(set(self.snake)):
            print("Game Over")
            print(self.score)
            self.reset()
            return

        for item in self.snake:
            if not all([i < self.SIZE and i > -1 for i in item]):
                print("Game Over")
                print(self.score)
                self.reset()
                return

        self.render()


if __name__ == "__main__":
    game = Snake_game()

    test = [1, 0, 3, 0, 2, 1, 2, 3, None, None]
    for i in test:
        game.game_loop(i)
        print(game.snake)
        print(game.field, end="\r")
        time.sleep(0.5)
