import random
import turtle as Tur
print("\nCreated by \"Reza Rafiee\".08-Mar-22")
Win = Tur.Screen()
Win.title("Password Generator \U0001F510")
Win.bgcolor("black")
Txt = Tur.Turtle()
Txt.shapesize(0.01)
Txt.goto(0, 250)
Txt.pencolor("white")
Txt.write("Press \"Space\" to Generate", font=(
    "calibri", 20, "italic"), align="center")
Txt.hideturtle
Tur.Turtle()
Tur.shapesize(0.01)
Tur.pencolor("white")
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower = "abcdefghijklmnopqrstuvwxyz"
Number = "0123456789"
Symbol = "!@#$%^&*()_+~{}[](<>?"
All = Upper + Lower + Number + Symbol
Lenght = random.randint(8, 12)
Password = "".join(random.sample(All, Lenght))
Style = ('Arial', 20, 'bold')


def Generate():
    Tur.write(
        f"The generated password is  :  {Password}",
        font=Style, align="center")


Win.onkey(Generate, "space")
Win.listen()
Tur.hideturtle()
Win.mainloop()
