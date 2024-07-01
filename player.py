class Player():
    team = ""
    def __init__(self, name, health, score):
        self.full_name = name
        self.health = health
        self.score = score
    
    def __str__(self) -> str:
        return f"{self.full_name} {self.health}"

    def game_over(self):
        if self.health == False : # not self.health / self.health != True
            print("Game Over")
player = Player(name="Rym", health=False, score=0)
print(player.full_name)
player.game_over()
