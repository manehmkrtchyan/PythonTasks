'''Write a program that simulates a movie theater system. 
The program should have classes for movies, theaters, and showtimes.
Movies should have attributes such as title, genre, and length. 
Theaters should have attributes such as location and seating capacity. 
Showtimes should have attributes such as the movie being shown, 
the theater it is being shown in, and the time/date of the showing. 
The program should allow customers to browse movies and showtimes, 
reserve seats for a particular showing, and purchase tickets. 
Use inheritance to implement classes for different types of theaters 
(e.g., standard, IMAX) and abstract classes for movie theater operations.'''
from abc import ABC, abstractmethod

class Movie:
    def __init__(self, title, genre, length) -> None:
        self.title = title
        self.genre = genre
        self.length = length
    
class Theater:
    def __init__(self, location, seating_capacity) -> None:
        self.location = location
        self.seating_capacity = seating_capacity
        
    @abstractmethod
    def get_type(self):
        pass
    
    @abstractmethod
    def get_ticket_price(self):
        pass
    
class StandartTheater(Theater):
    def get_type(self):
        return 'Standart'
    
    def get_ticket_price(self):
        return 10

class IMAXTheater(Theater):
    def get_type(self):
        return 'IMAX'
    
    def get_ticket_price(self):
        return 20

class Showtime:
    def __init__(self, movie, theater, time_date) -> None:
        self.movie = movie
        self.theatre = theater
        self.time_date = time_date
    
    def reserve(self, customer):
        if self.theatre.seating_capacity > 0:
            self.theatre.seating_capacity -= 1
            print(f'Dear {customer.name }You reserved a ticket for {self.movie.title} movie at {self.theatre.location}')
        else:
            print('No available seats')
            
    def sell(self, customer):
        if self.theatre.seating_capacity > 0:
            self.theatre.seating_capacity -= 1
            print(f'Dear {customer.name }You bought a ticket for {self.movie.title} movie at {self.theatre.location}')
        else:
            print('No available seats')

class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.movies = []
        
    def browse_movie(self, movie):
        self.movies.append(movie)
    
    def buy_tickets(self, showtime):
        return showtime.sell(self)
    
    def reserve_seats(self, showtime):
        return showtime.reserve(self)
    
customer = Customer('Mane')
movie = Movie('Titanic', 'drama', 150)
theater = Theater('Yerevan', 20)
showtime = Showtime(movie, theater, 'today')
customer.buy_tickets(showtime)
