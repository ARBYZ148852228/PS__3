from tank import Tank
from tkinter import*

w = Tk()
w.title("Minimal Tank 228.0")
canv = Canvas(w, width = 800, height = 600, bg = "light green")
canv.pack()
player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, model="T-34")

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D  =68


def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()

    if event.keycode == KEY_S:
        player.backward()

    if event.keycode == KEY_A:
        player.left()

    if event.keycode == KEY_D:
        player.right()


w.bind("<KeyPress>", key_press)
w.mainloop()
