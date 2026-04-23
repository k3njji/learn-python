import tkinter as tk
import random

class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 40
        self.height = 20
        self.x = 250
        self.y = 450
        self.speed = 20

        self.id = canvas.create_rectangle(
            self.x, self.y,
            self.x + self.width,
            self.y + self.height,
            fill="green"
        )

    def move_left(self, event=None):
        if self.x > 0:
            self.x -= self.speed
            self.canvas.move(self.id, -self.speed, 0)

    def move_right(self, event=None):
        if self.x < 460:
            self.x += self.speed
            self.canvas.move(self.id, self.speed, 0)

    def shoot(self):
        return Bullet(self.canvas, self.x + self.width // 2, self.y)


class Bullet:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.speed = 10
        self.id = canvas.create_rectangle(
            x - 2, y - 10, x + 2, y,
            fill="yellow"
        )

    def move(self):
        self.canvas.move(self.id, 0, -self.speed)

    def get_position(self):
        return self.canvas.coords(self.id)


class Enemy:
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 30
        self.x = random.randint(0, 470)
        self.y = 0
        self.speed = 3

        self.id = canvas.create_rectangle(
            self.x, self.y,
            self.x + self.size,
            self.y + self.size,
            fill="red"
        )

    def move(self):
        self.canvas.move(self.id, 0, self.speed)

    def get_position(self):
        return self.canvas.coords(self.id)


class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Space Invaders")

        self.canvas = tk.Canvas(root, width=500, height=500, bg="black")
        self.canvas.pack()

        self.player = Player(self.canvas)

        self.bullets = []
        self.enemies = []

        self.running = True

        # Controls
        self.root.bind("<Left>", self.player.move_left)
        self.root.bind("<Right>", self.player.move_right)
        self.root.bind("<space>", self.shoot)

        self.spawn_enemy()
        self.update()

    def shoot(self, event=None):
        self.bullets.append(self.player.shoot())

    def spawn_enemy(self):
        if self.running:
            self.enemies.append(Enemy(self.canvas))
            self.root.after(1000, self.spawn_enemy)

    def check_collision(self, obj1, obj2):
        x1, y1, x2, y2 = obj1
        a1, b1, a2, b2 = obj2
        return not (x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2)

    def update(self):
        if not self.running:
            return

        for bullet in self.bullets[:]:
            bullet.move()
            pos = bullet.get_position()

            if pos[1] < 0:
                self.canvas.delete(bullet.id)
                self.bullets.remove(bullet)

        for enemy in self.enemies[:]:
            enemy.move()
            pos = enemy.get_position()

            if pos[3] > 500:
                self.canvas.delete(enemy.id)
                self.enemies.remove(enemy)
                continue

            for bullet in self.bullets[:]:
                if self.check_collision(bullet.get_position(), enemy.get_position()):
                    self.canvas.delete(bullet.id)
                    self.canvas.delete(enemy.id)
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    break

        self.root.after(30, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()