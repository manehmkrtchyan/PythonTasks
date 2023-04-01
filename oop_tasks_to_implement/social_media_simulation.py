'''Write a program that simulates a social media platform. 
The program should have classes for users, posts, and comments. 
Users should have attributes such as name and contact information.
Posts should have attributes such as the user making the post, 
the post content, and the date/time of the post. 
Comments should have attributes such as the user making the comment, the comment content, 
and the date/time of the comment. The program should allow users to create and share posts, 
comment on posts, and interact with other users.
Use inheritance to implement classes for different types of posts 
(e.g., text, photo) and abstract classes for social media operations.'''
from datetime import datetime
from abc import ABC, abstractmethod
class User:
    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
        self.posts = []
        self.shared = []
        self.followers = []
    
    def create_post(self, content, type):
        if type == 'Text':
            post = TextPost(self, content, datetime.now, 'text')
        else: post = PhotoPost(self, content, datetime.now, 'image')
        self.posts.append(post)
        print('post reated')
        
    def share_post(self, post):
        self.shared.append(post)
        
    def comment_post(self, post, content):
        com = Comment(self, content, datetime.now)
        post.comments.append(com)
        
    def follow_other_user(self, other):
        other.followers.append(self)
        print(f'You started following {other.name}')
        
        
class Post(ABC):
    def __init__(self, user, content, date_time) -> None:
        self.user = user
        self.content = content
        self.date_time = date_time
        self.comments = []
        
    @abstractmethod
    def get_type(self):
        pass
        
class TextPost(Post):
    def __init__(self, user, content, date_time, text) -> None:
        super().__init__(user, content, date_time)
        self.text = text
        
    def get_type(self):
        return 'Text'

class PhotoPost(Post):
    def __init__(self, user, content, date_time, photo) -> None:
        super().__init__(user, content, date_time)
        self.photo = photo
        
    def get_type(self):
        return 'Photo'
        
class Comment:
    def __init__(self, user, content, date_time) -> None:
        self.user = user
        self.content= content
        self.date_time = date_time
        
user1 = User('mane', 'usih')
user2 = User('maneee', 'hubci')
user1.follow_other_user(user2)
user1.create_post('barev', 'text')