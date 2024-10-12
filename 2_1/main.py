from hitbox import HitBox

hb1 = HitBox(0, 0, 100, 100)
hb2 = HitBox(50, 50, 100, 100)
intersection = hb1.intersects(hb2)
print(intersection)

print(f"верхняя граница hb1: {hb1.top},"
      f"верхняя граница hb2: {hb2.top}")
print(f"")
