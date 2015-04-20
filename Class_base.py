x = 3
class Base:
    x = 1
class Child(Base):
    x = 2
c = Child()
c.y = x
print c.x + c.y