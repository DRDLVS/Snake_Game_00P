from turtle import Turtle

X_COR = 0
Y_COR = 275
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(X_COR, Y_COR)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
        self.points = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)



