class Dog:
    def __init__(self, name, breed, age, color) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.state = "standing"
    def bark(self):
        print("Haf-haf!")
    def set_name(self, new_name):
        self.name = new_name
    def set_state(self, new_state:'str'):
        self.state = new_state
        print(f'Now {self.name} is {self.state}.')
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_breed(self):
        print(self.breed)
    def get_color(self):
        print(self.color)
    def eat(self, food):
        if food in {'apple', 'pear', 'chicken', 'beef', 'turkey', 'strawberries', 'carrots', 'rice', 'dog food'}:
            print(f'{self.name} is eatting {food} now.')
        else:
            print(f"{self.name} doesn't eat {food}")

class Helicopter:
    def __init__(self) -> None:
        self.type = 'aircraft'
        self.engine_works= False
        self.position = [0, 0, 0] #[x,y,z]
        self.door_state = 'open'
    def close_the_door(self):
        self.door_state = 'closed'
        return('The door is closed, now you can start the flight.')
    def start_flying(self):
        if self.door_state == 'open':
            return('The door has to be closed!')
        else:
            self.engine_works = True
            if self.position[2] == 0:
                self.position[2] = 10
                return(f'Your coordinates are {self.position}. Have a nice flight.')
            return("You are already in the air.")
    def fly_to_right(self, how_much: 'float'):
        if self.engine_works:
            self.position[0] += how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'
    def fly_to_left(self, how_much: 'float'):
        if self.engine_works:
            self.position[0] -= how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'
    def fly_to_up(self, how_much: 'float'):
        if self.engine_works:
            self.position[1] += how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'   
    def fly_to_down(self, how_much: 'float'):
        if self.engine_works:
            if self.position[2] - how_much >= 0:
                self.position[2] -= how_much
                return(f'Youre coordinates are {self.position}.')
            return(f'Cant do this action!')
        else:
            return f'Engine is turned off. Start flying'


helicopter = Helicopter()
print(helicopter.close_the_door())
print(helicopter.start_flying())
print(helicopter.fly_to_down(5))
print(helicopter.fly_to_left(4))
print(helicopter.fly_to_up(10))