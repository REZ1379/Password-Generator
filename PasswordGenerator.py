import random
import turtle as Tur
print("\nCreated by \"Reza Rafiee\".08-Mar-22")
Win = Tur.Screen()
Win.title("Password Generator \U0001F510")
Win.bgcolor("black")
Tur.pencolor("white")
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower = "abcdefghijklmnopqrstuvwxyz"
Number = "0123456789"
Symbol = "!@#$%^&*()_+~{}[](<>?"
All = Upper + Lower + Number + Symbol
Lenght = random.randint(8, 12)
Password = "".join(random.sample(All, Lenght))
Style = ('Arial', 20, 'bold')
Tur.write(
    f"The generated password is  :  {Password}",
    font=Style, align="center")
Tur.hideturtle()
Win.mainloop()
