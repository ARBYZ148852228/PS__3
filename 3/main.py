# Перенести код из директории 1_2 файл main
from tank import Tank
from tkinter import*



KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68
FPS =60


def update():
    enemy.update()
    player.update()
    check_collision()
    player.forvard()
    w.after(1000//FPS, update)

def check_collision():
    if player.intersects(enemy):  # 4 Вызвать обертку
        print('Танки столкнулись')

def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    if event.keycode == KEY_S:
        player.backward()
    if event.keycode == KEY_A:
        player.left()
    if event.keycode == KEY_D:
        player.right()
    check_collision()           # 5 вызвать проверку столкновений при событиях нажатия на клавиши
                                   # смоделировать ситуацию столкновения
w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = 800, height = 600, bg = 'alice blue')
canv.pack()

player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed = 1, bot = False)
enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100, speed = 1, bot = True)

enemy.set_target(player)

w.bind('<KeyPress>', key_press)

w.update()
w.mainloop()