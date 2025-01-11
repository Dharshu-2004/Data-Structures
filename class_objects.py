class cookie:
    def __init__(self, color):
        self.color=color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color=color
cookie1=cookie('green')
cookie2=cookie('blue')

print("the color of cookie 1 is ",cookie1.get_color())
print("the color of cookie 2 is ",cookie2.get_color())
cookie1.set_color('yellow')
print("the color of cookie 1 is now ",cookie1.get_color())
print("the color of cookie 2 is still",cookie2.get_color())