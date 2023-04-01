'''Write a program that simulates a music streaming platform. 
The program should have classes for songs, artists, and users. 
Songs should have attributes such as title, artist, and duration. 
Artists should have attributes such as name and contact information. 
Users should have attributes such as name and contact information, 
and a list of favorite songs/artists. The program should allow users to search for 
and listen to songs, create and share playlists, and discover new artists.
Use inheritance to implement classes for different types of songs 
(e.g., rock, pop) and abstract classes for music streaming operations.'''
from abc import ABC, abstractmethod
class Song:
    def __init__(self, title, artist, duration, type) -> None:
        self.title = title
        self.artist = artist
        self.duration = duration
        self.type = type
    @abstractmethod
    def get_type(self):
        pass
class Rock(Song):
    def __init__(self, title, artist, duration) -> None:
        super().__init__(title, artist, duration, 'Rock')
    def get_type(self):
        return self.type    
class Pop(Song):
    def __init__(self, title, artist, duration) -> None:
        super().__init__(title, artist, duration, 'Pop')
    def get_type(self):
        return self.type
        
class Artist: 
    def __init__(self, name, contact) -> None:
        self.name = name
        self.contact = contact
class User:
    def __init__(self,  name, contact) -> None:
        self.name = name
        self.contact = contact
        self.fav_songs = []
        self.fav_artists = []
        self.listened = []
        self.shared = []
    
    def listen_song(self, song):
        self.listen_song.append(song)
        print(f'Playing the song {song.title}')
        
    def search_song(self, title):
        for i in self.listened:
            if i.title == title:
                print(f'found the song {i}')
                return i
        else:
            print('Didnt find the song')
            
    def create_playlist(self,playlist_name, *songs ):
        self.playlist = []
        for i in songs:
            self.playlist.append((playlist_name, i.title, i.artist))
            print('Playlist is created')
            
    def share_playlist(self, playlist):
        for i in self.playlist:
            if i[0] == playlist:
                self.shared.append(playlist)
        print('Playlist is shared')
        
    def discover_an_artist(self, artist):
        self.fav_artists.append(artist)
        print('Added to the artists list')
        
user = User('mane', 'cbkjn')
song= Pop('Die for you', 'Weeknd', 3)
user.create_playlist('myplaylist', song)

user.share_playlist('myplaylist')
user.discover_an_artist('Weeknd')