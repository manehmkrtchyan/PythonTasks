'''Write a program that simulates a hotel booking system. 
The program should have classes for rooms, guests, and reservations. 
Rooms should have attributes such as room number, price, and amenities.
Guests should have attributes such as name and contact information. 
Reservations should have attributes such as the guest making the reservation, 
the room being reserved, and the reservation dates. 
The program should allow guests to search for and book available rooms, 
view their reservation history, and leave feedback. 
Use inheritance to implement classes for different types of rooms 
(e.g., standard, deluxe) and abstract classes for reservation operations'''
from abc import ABC, abstractmethod
from datetime import datetime
class Room(ABC):
    def __init__(self, number, price, amentities) -> None:
        self.number = number
        self.price = price
        self.amentities = amentities
        self.state = 'Available'
        self.feedback_list = []
        
    @abstractmethod
    def get_type(self):
        pass    
class StandartRoom(Room):
    def get_type(self):
        return 'Standart'
    
class DeluxeRoom(Room):
    def get_type(self):
        return 'Deluxe'
    
class Guest():
    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
        self.reservations = []
        
    def book_room(self, room):
        reserve = Reservation(self, room, datetime.now)
        self.reservations.append(reserve)
        room.state = 'Reserved'
        print('You booked a room')
        
    def search_room(self, room):
        if room.state == 'Available':
            print('The room is available. You can book it')
        else:print('No you cant book it it is already reserved ')
            
    def view_history(self):
        print(f'your history: {self.reservations}')
        
    def leave_feedback(self, room, feedback):
        room.feedback_list.append(feedback)
        print('Feedback is added')
        
class Reservation:
    def __init__(self, guest, room, date) -> None:
        self.guest = guest
        self.room = room
        self.date = date
        
guest1 = Guest('mane', 'shbckjn')
room1 = StandartRoom(1, 100, 'hjbwjhbj')
guest1.book_room(room1)
guest1.leave_feedback(room1, 'lavn er')
guest1.search_room(room1)