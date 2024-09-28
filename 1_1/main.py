from tank import Tank
t1 = Tank(0,0, "T-14", 100 )
t2 = Tank(100,100, "T-34", 80 )
t1.right()
t1.right()
t1.backward()
t1.backward()
t1.fire()
t1.fire()
t1.info()
t2.info()
print(f"Create Tanks: {Tank.count}")

