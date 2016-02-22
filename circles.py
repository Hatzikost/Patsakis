import turtle
import random
import math

class MyTurtle(turtle.Turtle):
    radius = 0

    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")

    def kuklos(self, x, y, radius=(random.randrange(10, 500, 1))):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.circle(radius)
        self.radius = radius


    def sxediaseKuklous(self):
        positions = [(random.randrange(0,500,1), (random.randrange(0,500,1)) )]
        for position in positions:
            self.kuklos(position[0], position[1])
        return positions[0]

    def temnomenoiKukloi(self, list):
        count = 0
        for i in range(0, len(list)):
            for x in range(0, len(list)):
                if i != x:
                    d = math.sqrt(abs((pow((list[i][0]-list[x][0]), 2) + (pow((list[i][1]-list[x][1]), 2)))))
                    if d <= 2*self.radius:

                        count += 1
                        break
        return count





if __name__ == "__main__":
    t = MyTurtle()
    yolo = []
    for i in  range(1, 21):
        center = t.sxediaseKuklous()

        yolo.append(center)
    turtle.getscreen()._root.mainloop()
    counter = t.temnomenoiKukloi(yolo)
    print "Temnontai %s kukloi." % (counter,)