import random

class RockPaperScissor :
    def __init__(self) :
        self.choices = ["rock", "paper", "scissor"]
        self.user_choice = None
        self.computer_choice = None
        self.end_game = False

    def get_user_choice(self) -> str:
        while True :
            user_choice = input("Rock Paper or Scissor?: ").lower()
            if user_choice not in self.choices :
                print("Wrong input, try again!")
            else :
                self.user_choice = user_choice
                return user_choice
            
    def get_computer_choice(self) -> str:
        self.computer_choice = random.choices(self.choices)[0]
        return self.computer_choice
    
    def get_winner(self) -> str :
        user_win_scenarios = [('scissor', 'paper'), ('paper', 'rock'), ('rock', 'scissor')]
        if self.user_choice == self.computer_choice :
            return "Tie"
        elif (self.user_choice, self.computer_choice) in user_win_scenarios :
            self.end_game = True
            return "User wins!"
        else :
            self.end_game = True
            return "Computer wins :("
        
    def play(self) -> str:
        self.get_user_choice()
        self.get_computer_choice()
        return self.get_winner()

    def __call__(self) -> bool:
        return not self.end_game
    

if __name__ == "__main__" :
    game = RockPaperScissor()
    while game() :
        print(game.play())