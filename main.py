ALIGN="center"
FONT=("Britannic Bold",10,"normal")
from turtle import Turtle,Screen
import pandas
screen=Screen()
screen.title("Indian States Game")
screen.setup(height=750,width=700)
image="IndianMap.gif"
screen.addshape(image)
turtle=Turtle()
turtle.shape(image)

def new_write(x_axis, y_axis, answer):
    new = Turtle()
    new.hideturtle()
    new.penup()
    new.goto(x_axis, y_axis)
    new.write(arg=answer, align=ALIGN,font=FONT)
def winner():
    win=Turtle()
    win.hideturtle()
    win.color("black")
    win.penup()
    win.write(arg="YOU WON!YOU GUESSED IT ALL!",align=ALIGN,font=("Cooper Black",27,"normal"))
# for finding coordinates:
# def get_mouse_click_coordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coordinates)
data=pandas.read_csv("Indian_states.csv")

score=0
already_done=[]
game_on=True
while game_on:
    user_answer=screen.textinput(title="Guess the states of India",prompt=f"Enter the states names({score}/34)")
    for d in data["state"]:
        if user_answer.lower()==d.lower():
            if d not in already_done:
                x=data.loc[data.state == d, "x"].item()
                y = data.loc[data.state == d, "y"].item()
                new_write(x,y,d)
                score+=1
                already_done.append(d)
    if len(already_done)>33:
        game_on=False
        winner()
screen.exitonclick()