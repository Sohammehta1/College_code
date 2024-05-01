import turtle as tt 

tom= tt.Turtle()
tom.shape("turtle") #  “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
my_screen = tt.Screen()
#tom.up()
tom.forward(100)
#tom.down()
tom.right(90)
tom.forward(50)
tom.right(90+26.6)# angle in triangle is 63.4d
tom.forward(111.8)


tom.right(63.4)
tom.pencolor("orange")
for i in range(4):
    tom.forward(100)
    tom.right(90)
my_screen.exitonclick()