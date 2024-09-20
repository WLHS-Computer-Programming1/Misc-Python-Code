# going through two different size lists in one loop
import turtle

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('blue')
timmy.pensize(5)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
color = ["blue","red","green","yellow","purple","black"]

#          0       1     2        3

for number in numbers:
    color_index = (number-1) % len(color) #number-1 to start at 0
#                                         # %len(color) to make it repeat 0,1,2,...,length-1
    timmy.forward(number*5)
    timmy.left(20)
    timmy.color(color[color_index])

turtle.Screen().exitonclick()
################################################
def draw_sky(num_stars):
    pass

# ask user repeatedly until they choose not to

while True:
    num_stars = int(input("How many stars do you want want? "))
    draw_sky(num_stars)
    draw_again = input("Would you like to make another picture(y/n): ")
    if draw_again == 'y':
        continue #send to top of loop
    else:
        print("Thanks for your beautiful art!")
        break #send out of while loop
