import turtle as tu

class googlemapslogo:
    def __init__(self):
        self.red =[(220, 104) ,(235, 117) ,(259, 137) ,(284, 158) ,(312, 180) ,(289, 207) ,(267, 233) ,(238, 268) ,(216, 294) ,(194, 319) ,(187, 305) ,(181, 285) ,(179, 272) ,(175, 252) ,(174, 233) ,(175, 209) ,(178, 194) ,(181, 177) ,(186, 160) ,(194, 144) ,(203, 128) ,(210, 117) ,(220, 105)]
        self.yellow =[(194, 320) ,(210, 301) ,(226, 282) ,(244, 260) ,(262, 239) ,(282, 216) ,(304, 189) ,(300, 199) ,(296, 211) ,(294, 224) ,(294, 236) ,(298, 251) ,(304, 264) ,(311, 276) ,(320, 286) ,(332, 292) ,(342, 297) ,(357, 302) ,(374, 302) ,(385, 301) ,(397, 297) ,(409, 290) ,(419, 283) ,(396, 310) ,(381, 328) ,(362, 350) ,(343, 374) ,(320, 400) ,(305, 417) ,(295, 430) ,(281, 447) ,(268, 429) ,(252, 410) ,(236, 388) ,(224, 372) ,(216, 360) ,(210, 352) ,(206, 344) ,(200, 333) ,(196, 327) ,(194, 321)]
        self.green =[(281, 446) ,(287, 454) ,(293, 462) ,(300, 471) ,(306, 480) ,(312, 490) ,(318, 499) ,(324, 510) ,(330, 520) ,(336, 533) ,(340, 543) ,(344, 556) ,(349, 568) ,(352, 577) ,(355, 584) ,(359, 589) ,(365, 591) ,(371, 592) ,(377, 589) ,(381, 586) ,(384, 580) ,(387, 573) ,(391, 564) ,(393, 557) ,(396, 548) ,(398, 543) ,(401, 535) ,(406, 525) ,(410, 514) ,(416, 504) ,(421, 496) ,(427, 487) ,(435, 475) ,(443, 462) ,(453, 451) ,(464, 437) ,(475, 422) ,(483, 412) ,(492, 401) ,(501, 387) ,(507, 379) ,(516, 368) ,(524, 356) ,(535, 339) ,(541, 326) ,(548, 310) ,(551, 303) ,(554, 295) ,(556, 288) ,(558, 277) ,(560, 269) ,(562, 251) ,(563, 238) ,(563, 227) ,(563, 217) ,(562, 207) ,(561, 196) ,(559, 186) ,(557, 177) ,(554, 168) ,(552, 161) ,(547, 150) ,(541, 139) ,(533, 149) ,(521, 164) ,(508, 178) ,(491, 199) ,(478, 215) ,(468, 227) ,(458, 238) ,(448, 249) ,(439, 261) ,(426, 276) ,(411, 293) ,(404, 301) ,(394, 313) ,(383, 326) ,(370, 340) ,(358, 355) ,(345, 371) ,(336, 381) ,(322, 397) ,(311, 411) ,(303, 421) ,(293, 433) ,(281, 446)]
        self.blue =[(221, 102) ,(229, 111) ,(237, 118) ,(248, 128) ,(262, 140) ,(277, 152) ,(288, 161) ,(299, 170) ,(311, 179) ,(319, 171) ,(327, 161) ,(335, 151) ,(342, 142) ,(350, 132) ,(358, 123) ,(368, 111) ,(378, 99) ,(385, 92) ,(392, 84) ,(401, 73) ,(400, 73) ,(407, 66) ,(414, 57) ,(418, 49) ,(423, 41) ,(402, 37) ,(386, 34) ,(376, 34) ,(366, 34) ,(352, 35) ,(337, 35) ,(325, 38) ,(314, 41) ,(301, 44) ,(289, 49) ,(273, 57) ,(257, 68) ,(244, 78) ,(236, 86) ,(221, 102)]
        self.lightblue =[(311, 180) ,(322, 168) ,(334, 153) ,(348, 137) ,(361, 121) ,(376, 103) ,(393, 84) ,(410, 62) ,(420, 51) ,(426, 41) ,(435, 45) ,(442, 48) ,(451, 52) ,(460, 56) ,(474, 64) ,(486, 73) ,(494, 79) ,(503, 88) ,(515, 100) ,(523, 110) ,(531, 121) ,(538, 131) ,(542, 137) ,(535, 145) ,(528, 154) ,(522, 162) ,(513, 173) ,(504, 182) ,(495, 193) ,(487, 202) ,(479, 211) ,(469, 225) ,(457, 239) ,(448, 249) ,(441, 259) ,(431, 269) ,(435, 262) ,(439, 251) ,(441, 243) ,(443, 232) ,(443, 224) ,(443, 216) ,(441, 210) ,(439, 203) ,(436, 195) ,(432, 188) ,(424, 178) ,(417, 171) ,(408, 165) ,(401, 161) ,(394, 158) ,(384, 154) ,(375, 152) ,(366, 152) ,(356, 154) ,(346, 157) ,(339, 160) ,(331, 164) ,(321, 170) ,(316, 174)]
        self.improve =[(312, 179) ,(324, 164) ,(337, 148) ,(350, 134) ,(362, 121) ,(375, 103) ,(390, 86) ,(403, 70) ,(416, 55) ,(427, 42)]
        self.pen = tu.Turtle()
        self.pen.speed(0)
        self.x_offset = 320
        self.y_offset = 320


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
        self.draw_fn(self.red,co = (234, 68, 54),mode = 0)
        self.draw_fn(self.yellow,co = (251, 189, 4),mode = 0)
        self.draw_fn(self.green,co = (51, 168, 84),mode = 0)
        self.draw_fn(self.blue,co = (27, 115, 232),mode = 0)
        self.draw_fn(self.lightblue,co = (66, 133, 244),mode = 0)
        self.draw_fn(self.lightblue,co = (66, 133, 244),mode = 0)
        self.draw_fn(self.improve,co = (66, 133, 244),mode = 1,thickness=4)
        if retain:
            tu.done()

pen=googlemapslogo()
pen.draw()
