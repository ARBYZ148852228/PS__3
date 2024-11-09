from tank import Tank
from tkinter import*
import world


KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40
KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 60
def update():
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_sise()//2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_sise()//2)

    player.update()
    neutral.update()
    enemy.update()
    check_collision()
    w.after(1000//FPS, update)


def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)



def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(0,-5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0,5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5,0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5,0)

w = Tk()
w.title('Танки на минималках 52.0')
# 2 ширина и высота определяются через модуль world
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT,
              bg = 'alice blue')
canv.pack()

player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed=1, bot = False)
enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100, speed=1, bot = True)
neutral = Tank(canvas = canv, x = 500, y = 500, ammo = 100, speed=1 , bot = False)
neutral.stop()


enemy.set_target(player)


w.bind('<KeyPress>', key_press)



update()
w.mainloop()