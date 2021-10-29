# Example of a class

class fruit:
    def __init__(self, name, color, shape, texture, insideC, insideT):
        self.name = name
        self.color = color
        self.shape = shape
        self.texture = texture
        self.insideColor = insideC
        self.insideTexture = insideT
    def aboutMe(self):
        print(f'I am a {self.name}, I am shaped like a {self.shape}, and I am {self.color}! if you touch me, i feel {self.texture}')
    def peel(self):
        self.color = self.insideColor
        self.texture = self.insideTexture

myBanana = fruit('banana', 'yellow', 'crescent', 'smooth', 'white', 'sticky')
myApple = fruit('apple', 'red', 'sphere', 'smooth', 'white', 'porous')
myOrange = fruit('orange', 'orange', 'sphere', 'rough', 'yellow', 'porous')

myBanana.aboutMe()
myBanana.peel()
myBanana.aboutMe()

print(f'My apple is {myApple.color} on the outside and {myApple.insideColor} on the inside')
print(f'My orange feels {myOrange.texture}, and my apple feels {myApple.texture}.')

myOrange.color = 'blue'
print(f'I painted my orange, and the color is now blue')