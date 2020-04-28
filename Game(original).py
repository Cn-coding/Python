# left arrow to go left and right arrow to go right
# forward arrow to speed up and back arrow to slow down
# if you touch a wall you’ll bounce back the way you came
# if you touch a barrier you’ll bounce in a random direction
# you can check the time it took you at the end at the bottom of the python shell page
# The aim is to get 5 circles from one arena and 5 from the other
# once you have 5 circles from the first arena you’ll be teleported to the next one

##shape1 = input("What shape would you like to be? ")
##colour = input("What colour would you like to be? ")





from turtle import *
import turtle
import random
import time
import math
 
target = 0
z = 0
f = 0
p = ["blue","darkred","green","orange","yellow","darkgreen","purple","turquoise"]
wn = turtle.Screen()
wn.bgcolor("lightblue")





 
def isCollision(player, goal):
    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))

    if d<20:
        return True
    else:
        return False


player = turtle.Turtle()
player.color('blue')
player_shape = ((-10,-20),(-5,-13),(-2,-18),(0,-13),(5,-20),(5,-13),(5,0),(-1,0),(-1,-3),(-3,-3),(-3,0),(-10,0),(-3,0),(-3,1),(-1,1),(-1,0),(5,0),(-2,13),(-10,0),(-10,-15))
##player_shape = ((-5,5),(160,5))
print(player_shape)
turtle.register_shape('player', player_shape)
player.shape('player')
player.penup()
player.speed(0)
# should be 330
player.setposition(250,0)
player.lt(90)
 
 
mypen = turtle.Turtle()
mypen.shape('player')
mypen.penup()
mypen.setposition(50,-300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
 
pen1 = Pen()
pen1.color("black")
pen1.penup()
pen1.goto(0,100)




 
 
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.forward(250)
mypen.left(90)
mypen.forward(250)
mypen.right(90)
mypen.forward(50)
mypen.right(90)
mypen.forward(250)
mypen.penup()
mypen.setpos(-650,300)
mypen.pendown()
mypen.fd(600)
mypen.lt(90)
mypen.fd(600)
mypen.lt(90)
mypen.fd(600)
mypen.lt(90)
mypen.fd(600)
for i in range(4):
    mypen.lt(90)
    mypen.fd(285)
    mypen.lt(90)
    mypen.fd(175)
    mypen.rt(90)
    mypen.fd(30)
    mypen.rt(90)
    mypen.fd(175)
    mypen.lt(90)
    mypen.fd(285)
 
goal = turtle.Turtle()
goal.color(random.choice(p))
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(100,-250)
goal.penup()
goal.rt(135)
 
 
speed = 0
def turnleft():
    player.left(22.5)
 
def turnright():
    player.right(22.5)
    
def speedup():
    global speed
    if speed<13:
        speed+=1
    if speed<0:
        speed = 1
def speeddown():
    global speed
    speed-=1
    if speed<-5:
         speed = -5
    
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(speedup,"Up")
turtle.onkey(speeddown,"Down")
 
 
##time.sleep(1)
 
speed = 1
import random
t = time
start = time.time()




h = 0
h9=0
h11=0
h12=0
h14=0

while True:

    h12+=1
    h11+=speed

    total = time.time()-start
    total = int(total)
    round(total)
    total2= total-1
    
    if target == 5:
        h13 = total
        print("Sector 1:",total)
        print("Sector 1 Avg Speed:",round((h11/h12),1))
        h11 = 0
        h12 = 0
        player.setpos(-250,-25)
        target +=15








# Unindent region if you want to display speed


##    if speed != h14:
##        pen1.color("lightblue")
##        pen1.write(h14,False,'center',font=('Candara',18,'bold'))
##        pen1.color("black")
##        pen1.write(speed,False,'center',font=('Candara',18,'bold'))
##        h+=1

    h14 = speed
    
    total = time.time()-start
    r = random.randint(50,300)and random.randint(350,650)
    q = random.randint(-300,300)
    u = random.randint(-650,-50)
    player.forward(speed)
 
 
    #Walls And Out Of Bounds Glitch Fix
    if player.xcor()>670:
        player.setpos(350,0)
    if player.xcor()<-660:
        player.setpos(-350,0)
        
    if player.ycor()>315 and player.xcor()>25:
        player.setpos(350,0)
    if player.ycor()>315 and player.xcor()<25:
        player.setpos(-350,0)
        
    if player.ycor()<-305 and player.xcor()>25:
        player.setpos(350,0)
    if player.ycor()<-305 and player.xcor()<25:
        player.setpos(-350,0)
        
    if player.xcor()>655 or (player.xcor()<55 and player.xcor()>-50):
        player.right(180)
    if player.ycor()>305 or player.ycor()<-295:
        player.right(180)
        
    if player.xcor()<-650:
        player.rt(180)
    if player.xcor()==300 and player.ycor()==-300:
        player.setposition(300,100)
 
    #Arena 1 Barrier
    if player.xcor()>300 and player.xcor()<350 and player.ycor()<-50:
        player.rt(random.randint(0,180))
 
    #Arena 2 Barrier Right
    if player.xcor()>-650 and player.xcor()<-475 and player.ycor()<20 and player.ycor()>-30:
        player.rt(random.randint(0,180))
 
    #Arena 2 Barrier Bottom
    if player.xcor()>-370 and player.xcor()<-340 and player.ycor()<-120:      
        player.rt(random.randint(0,180))
 
    #Arena 2 Barrier Left
    if player.xcor()>-230 and player.xcor()<-55 and player.ycor()<20 and player.ycor()>-30:    
        player.rt(random.randint(0,180))
    #Arena 2 Barrier top
    if player.xcor()>-370 and player.xcor()<-340 and player.ycor()>120:
        player.rt(random.randint(0,180))
 
 
 
    isCollision(player,goal)
    if isCollision(player, goal):
        goal.color(random.choice(p))
        goal.pendown()
        target+=1
        f+=1
        goal.penup()
        if f<5:
            goal.setposition(r,q)           

        if f>4:
            wn.bgcolor("grey")
            player.color("pink")
            goal.setpos(u,q)
    if f == 10:
        break

    





total = int(total)
round(total)
print("Sector 2:",total-h13)
print("Sector 2 Avg Speed:",round((h11/h12),1)) 
print("Total Time:",total)
print(h11/h12) 
f = str(total)
file = open("file1.txt","a")
file.write(f + "\n")
file.close()
