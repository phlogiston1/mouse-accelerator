import mouse

prevposition = mouse.get_position()
inertia = [0,0]
previnertia = [0,0]
resistance = 2
friction = 0.3 #perfect!!!
#frictiondiv = 100
while True:
    position = mouse.get_position()
    useposition = list(position)

    useposition[0] -= previnertia[0]
    useposition[1] -= previnertia[1]
    changeX = ((useposition[0] - list(prevposition)[0])/resistance)
    changeY = ((useposition[1] - list(prevposition)[1])/resistance)
    inertia[0] -= inertia[0]*friction
    inertia[1] -= inertia[1]*friction
    inertia[0] += changeX
    inertia[1] += changeY
    inertia[0] *= 1
    inertia[1] *= 1
    #friction = frictiondiv/(abs(changeX) + abs(changeY)+1)
    prevposition = position
    if useposition[0] == 0 or useposition[1] == 0 or mouse.is_pressed(button='left') or mouse.is_pressed(button='right'):
        inertia = [0,0]
    mouse.move(inertia[0], inertia[1], absolute=False, duration=0.0001)
    previnertia = inertia
