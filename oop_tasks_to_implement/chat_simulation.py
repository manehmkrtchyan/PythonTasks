'''Write a program that simulates a messaging application.
The program should have classes for users, conversations,
and messages. 
Users should have attributes such as name and contact
information. Conversations should have attributes such as 
the users involved and the conversation history.
Messages should have attributes such as the user sending the
message, the conversation the message is part of, 
and the message content. The program should allow users to 
create and participate in conversations, 
send and receive messages, and manage their messaging settings. 
Use inheritance to implement classes for different types of messages 
(e.g., text, multimedia) and abstract classes for messaging operations.
'''
from abc import ABC, abstractmethod
class User:
    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
        
    def send_message(self,message, conversation):
        message.send(conversation)
    
    def get_message(self, message):
        print(f'{message.sender}: {message}')
        
    def manage_settings(self, **settings):
        for key, value in settings.items():
            setattr(self, key, value)
        
    def __repr__(self):
        return self.name
        
class Conversation:
    def __init__(self, users: 'list') -> None:
        self.users = users
        self.history = []
        
    def add_user(self, user):
        self.users.append(user)
        
    def remove_user(self, user):
        self.users.remove(user)
        
    def get_history(self):
        print(self.history) 

class Message(ABC):
    def __init__(self, sender, content) -> None:
        self.sender = sender
        self.content = content
        
    def send(self, conversation):
        pass

class TextMessage(Message):
    def send(self, conversation):
        message = f'{self.sender}: {self.content}'
        conversation.history.append(message)

    def __repr__(self):
        return self.content
    
class ImageMessage(Message):
    def __init__(self, sender, content, image) -> None:
        super().__init__(sender, content)
        self.image = image
        
    def send(self, conversation):
        message = f'{self.sender}: {self.content}, {self.image}'
        
    def __repr__(self):
        return (self.content, self.image)
    
    
user1 = User('Mane', 'wugfuywg')
user2 = User('Hovo', 'wugfuywg')
conv = Conversation([user1, user2])
message = TextMessage(user1, 'Bare')
message2 = TextMessage(user1, 'Laves')
user1.get_message(message)
user2.send_message(message2, conv)
conv.get_history()