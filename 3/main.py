from tank import Tank
from tkinter import*


KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D  =68

def chek_collision(enemy):
    if player.intersects(enemy):
        print("!crash!")


def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()

    if event.keycode == KEY_S:
        player.backward()

    if event.keycode == KEY_A:
        player.left()

    if event.keycode == KEY_D:
        player.right()
    chek_collision(Enemy)

w = Tk()
w.title("Minimal Tank 228.0")
canv = Canvas(w, width = 800, height = 600, bg = "light green")
canv.pack()


player = Tank(canvas = canv, x = 100, y = 50, ammo = 100)

Enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100)


w.bind("<KeyPress>", key_press)
w.mainloop()
