'''Write a program that simulates a video game system. 
The program should have classes for games, players, and consoles. 
Games should have attributes such as title, genre, and release date. 
Players should have attributes such as name and contact information. 
Consoles should have attributes such as console type (e.g., Xbox, PlayStation) 
and games installed. The program should allow players to play games, save game progress, 
and compete with other players. 
Use inheritance to implement classes for different types of games 
(e.g., sports, adventure) and abstract classes for gaming operations.'''
from abc import ABC, abstractmethod
class Game(ABC):
    def __init__(self, title, genre, release_date) -> None:
        self.tite = title
        self.genre = genre
        self.release_date = release_date
    @abstractmethod
    def get_type(self):
        pass
class SportGame(Game):
    def get_type(self):
        return 'Sport'
class AdventureGame(Game):
    def get_type(self):
        return 'Adventur'
class Player:
    def __init__(self, name, contact_info) -> None:
        self.name = name
        self.contact_info = contact_info
        self.played_games = []
        self.progress = []
        self.total = sum([i[-1] for i in self.progress])
    
    def play_game(self, game):
        self.played_games.append(game)
    
    def save_progress(self, game, progress: int):
        self.progress.append((game.name, progress))
        
    def compete(self, other):
        if self.total > other.total:
            print("You won!")
        elif self.total == other.total:
            print("Equal!")
        else: print('He won!')
        
class Console:
    def __init__(self, console_type, installed_games) -> None:
        self.cosole_type = console_type
        self.installed_games = installed_games

game = SportGame('bjhbh', 'jshndn', 'bwb')
user = Player('MAne', 'hbgui')
user2 = Player('MAne', 'hbgui')
user.progress.append(7)
user.progress.append(('Game', 7))
user.play_game(game)
print(user.total)
print(user2.total)
user.compete(user2)