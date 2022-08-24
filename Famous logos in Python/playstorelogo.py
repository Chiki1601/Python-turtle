import turtle as tu


class playstorelogo:
    def __init__(self):
        self.first = [(219, 190),(229, 179),(242, 167),(253, 156),(263, 145),(270, 141),(288, 149),(305, 159),(322, 169),(332, 175),(339, 181),(342, 190),(340, 198),(334, 204),(320, 214),(305, 222),(287, 233),(270, 242),(262, 234),(254, 227),(243, 216),(233, 206),(224, 196)]
        self.second = [(68, 40),(79, 50),(89, 62),(103, 77),(118, 92),(135, 109),(154, 128),(177, 149),(197, 169),(218, 191),(209, 200),(199, 210),(187, 222),(175, 234),(160, 248),(144, 265),(130, 279),(114, 294),(99, 310),(86, 323),(76, 333),(67, 342),(63, 340),(61, 336),(61, 325),(61, 310),(61, 291),(61, 267),(61, 233),(61, 200),(61, 172),(61, 126),(61, 98),(61, 78),(61, 64),(62, 53),(62, 43)]
        self.third = [(67, 342),(73, 347),(82, 348),(97, 341),(112, 333),(124, 326),(140, 316),(155, 308),(171, 298),(194, 286),(223, 269),(256, 251),(270, 243),(255, 228),(240, 213),(228, 201),(218, 189),(208, 201),(196, 214),(178, 230),(162, 247),(140, 270),(98, 311),(78, 330)]
        self.fourth = [(69, 40),(74, 45),(80, 52),(89, 62),(99, 72),(110, 84),(122, 95),(137, 111),(161, 133),(181, 155),(196, 169),(217, 190),(232, 177),(252, 156),(266, 144),(268, 140),(244, 126),(224, 114),(194, 98),(159, 78),(114, 53),(105, 46),(88, 37),(78, 34),(66, 41)]
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = 250
        self.y_offset = 250


    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        self.pen.pendown()  


    def paint(self,coord,co=(0,0,0)):
        self.pen.color(co)
        t_x,t_y = coord[0]
        self.go(t_x,t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x,y = i
            if t:
                self.go(x,y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset) 
        self.pen.end_fill()


    def draw_fn(self,coord,mode = 1,co = (0,0,0),thickness = 1):
        co = (co[0]/255,co[1]/255,co[2]/255)

        self.pen.color(co)

        if mode:
            self.pen.width(thickness)
            t_x,t_y = coord[0]
            self.go(t_x,t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x,y = i
                if t:
                    self.go(x,y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x-self.x_offset,(y*-1)+self.y_offset)
        else:
            self.paint(coord=coord,co = co)

    
    def draw(self,retain=True):
        self.draw_fn(self.first,co = (255, 199, 0),mode = 0)
        self.draw_fn(self.third,co = (250, 53, 72),mode = 0)
        self.draw_fn(self.second,co = (0, 207, 255),mode = 0)
        self.draw_fn(self.fourth,co = (0, 241, 119),mode = 0)
        if retain:
            tu.done()

pen=playstorelogo()
pen.draw()
