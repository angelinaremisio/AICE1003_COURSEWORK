def create_runner(x:int =0, y:int =0, orientation:str = "N"):
    runner = [(x,y), orientation]
    return runner

def get_x(runner):
    return runner[0][0] # x

def get_y(runner):
    return runner[0][1] # y

def get_orientation(runner):
    return runner[1] # orientation

def turn(runner, direction:str):
    orientation = get_orientation(runner)
    index = 0
    new_orientation = ""
    compass = ["N", "E", "S", "W"]
    if direction == "Left":
        index = compass.index(orientation) - 1
    elif direction == "Right":
        index = compass.index(orientation) + 1
        if index > len(compass)-1:
            index = 0
    new_orientation = compass[index]
    runner[1] = new_orientation
    return runner

def forward(runner):
    runner[0][1] += 1
    return runner

#tests

lucy = create_runner(5, 2, "N")
amani = create_runner(5, 2, "W")
print(lucy)
print(amani)
turn(lucy, "Left")
turn(amani, "Right")
print(lucy)
print(amani)
