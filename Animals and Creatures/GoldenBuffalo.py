from turtle import *
import time


BG_COLOR = '#B30016'
COW_COLOR = 'yellow'


def draw_circle(radius, color):
    penup()
    setheading(towards(0, 0))
    right(90)
    pencolor(color)
    pendown()
    begin_fill()
    circle(radius)
    fillcolor(color)
    end_fill()


def draw_circle_and_set_start(radius, color):
    penup()
    sety(-radius)
    setx(0)
    setheading(towards(0, 0))
    right(90)
    pencolor(color)
    pendown()
    begin_fill()
    circle(radius)
    fillcolor(color)
    end_fill()


def draw_arc(radius, arc, color):
    penup()
    sety(-radius)
    pencolor(color)
    pendown()
    begin_fill()
    circle(radius, extent=arc)
    fillcolor(color)
    end_fill()


def draw_outer_ring():
    penup()
    sety(-241)
    setx(0)
    setheading(towards(0, 0))
    right(90)
    circle(240, extent=6)
    pencolor(COW_COLOR)
    pendown()
    begin_fill()
    for i in range(26):
        circle(240, extent=(360-19.5)/26)
        setheading(towards(0, 0))
        forward(24)
        left(90)
        circle(-216, extent=(360-156)/26/2)
        setheading(towards(0, 0))
        forward(7)
        right(90)
        circle(209, extent=(360-136.5)/26)
        setheading(towards(0, 0))
        backward(7)
        left(90)
        circle(-216, extent=(360-156)/26/2)
        setheading(towards(0, 0))
        backward(24)
        right(90)
    fillcolor(COW_COLOR)
    end_fill()


def draw_inner_ring():
    penup()
    sety(-232)
    setx(0)
    setheading(towards(0, 0))
    right(90)
    circle(240, extent=5.5)
    pencolor(BG_COLOR)
    circle(232, extent=2)
    pendown()
    begin_fill()
    for i in range(26):
        circle(232, extent=(360-123.5)/26)
        setheading(towards(0, 0))
        forward(8)
        left(90)
        circle(-224, extent=(360-156)/26/2)
        setheading(towards(0, 0))
        forward(23)
        right(90)
        circle(201, extent=(360-32.5)/26)
        setheading(towards(0, 0))
        backward(23)
        left(90)
        circle(-224, extent=(360-156)/26/2)
        setheading(towards(0, 0))
        backward(8)
        right(90)
    fillcolor(BG_COLOR)
    end_fill()


def draw_blossom(long):
    color('yellow')
    begin_fill()
    for i in range(40):
        forward(long)
        left(175)
        forward(long)
        right(165)
    fillcolor(COW_COLOR)
    end_fill()


def draw_flower(a, color):
    pencolor('red')
    begin_fill()
    for j in range(5):
        for i in range(40):
            if 0 <= i < 20:
                a = a - 0.08
            else:
                a = a + 0.08
            forward(a)
            left(6)
        right(168)
    fillcolor(color)
    end_fill()


def draw_outline_out():
    penup()
    sety(-185)
    setx(0)
    setheading(towards(0, 0))
    right(90)
    pendown()
    pencolor(BG_COLOR)
    begin_fill()
    circle(185, extent=130)
    right(60)
    for i in range(5):
        forward(2.5)
        left(8)
    forward(35)
    left(30)
    a = 5
    for i in range(4):
        forward(a)
        left(38)
        a += 3
    setheading(towards(0, 0))
    right(90)
    circle(185, extent=72)
    right(90)
    circle(-60, extent=65)
    left(30)
    for i in range(4):
        forward(3)
        left(30)
    circle(80, extent=90)
    setheading(towards(0, 0))
    right(90)
    circle(185, extent=6)
    right(45)
    a = 15
    for i in range(9):
        if 0 <= i < 5:
            a = a - 2.5
        else:
            a = a + 2.5
        forward(a)
        left(15)
    setheading(towards(0, 0))
    right(90)
    circle(185, extent=100)
    fillcolor(BG_COLOR)
    end_fill()


def draw_outline_inner():
    penup()
    sety(-175)
    setx(0)
    setheading(towards(0, 0))
    right(90)
    circle(175, extent=285)
    pendown()
    pencolor(COW_COLOR)
    begin_fill()
    circle(175, extent=155)
    draw_tail()
    draw_body()
    draw_face()
    draw_right_ear()
    draw_right_horn()
    draw_head_up()
    draw_left_horn()
    right(145)
    draw_left_ear()
    fillcolor(COW_COLOR)
    end_fill()


def draw_face():
    right(160)
    for i in range(3):
        forward(11)
        left(7)
    left(12)
    forward(43)
    left(30)
    for i in range(3):
        forward(4)
        left(12)
    left(90)
    forward(2)
    left(28)
    for i in range(5):
        forward(9)
        right(4)
    for i in range(3):
        forward(3)
        right(30)
    right(90)
    for i in range(6):
        forward(9.3)
        left(4)
    left(55)
    for i in range(5):
        forward(4.5)
        left(3)
    left(45)
    a = 3.5
    for i in range(5):
        forward(a)
        left(30)
        a += 1
    right(90)
    forward(3)
    right(45)
    a, b = 12, 20
    for i in range(6):
        forward(a)
        left(b)
        a -= 1.5
        b += 10
    right(45)
    forward(3)
    right(45)
    for i in range(5):
        forward(2)
        right(35)
    a = 8
    for i in range(5):
        forward(a)
        right(30)
        a -= 0.9
    left(120)
    a = 6
    for i in range(5):
        forward(a)
        if i < 3:
            left(5)
            a += 2
        else:
            right(5)
            a -= 2
    right(170)
    a = 9
    for i in range(5):
        forward(a)
        if i < 2:
            left(5)
            a += 2
        else:
            right(10)
            a -= 3
    left(70)
    for i in range(3):
        forward(3)
        right(5)
    for i in range(4):
        forward(5)
        left(8)
    for i in range(6):
        forward(3)
        right(8)
    left(145)
    for i in range(4):
        forward(8)
        left(5)
    for i in range(4):
        forward(3)
        right(10)
    forward(20)
    right(160)
    for i in range(4):
        forward(5)
        right(5)


def draw_body():
    right(90)
    a = 24
    for i in range(5):
        forward(a)
        left(7.5)
        a -= 1
    left(60)
    a = 12
    for i in range(5):
        forward(a)
        right(15)
        a -= 1.5
    for i in range(5):
        forward(10)
        right(3)
    right(25)
    for i in range(3):
        forward(12)
        right(7)


def draw_tail():
    left(8)
    a = 23
    for i in range(10):
        forward(a)
        left(5.8)
        a -= 1.8
    right(90)
    for i in range(4):
        forward(6)
        left(14)
    forward(20)
    for i in range(5):
        forward(1.5)
        right(10)
    left(90)
    forward(2)
    left(45)
    for i in range(2):
        forward(2)
        left(23)
    a, b = 13.5, 0
    for i in range(6):
        forward(a)
        left(b)
        a -= 1.3
        b += 10
    right(70)
    left(8)
    a = 5
    for i in range(10):
        forward(a)
        right(7.8)
        a += 2.3


def draw_head_up():
    forward(20)
    right(30)
    for i in range(6):
        forward(5)
        left(10)
    for i in range(3):
        forward(1)
        right(15)
    a = 5
    for i in range(6):
        forward(a)
        left(10)
        a += 1
    for i in range(7):
        forward(2)
        right(8)


def draw_right_horn():
    right(100)
    a = 5
    for i in range(10):
        forward(12.5)
        left(a)
        a += 2
    for i in range(3):
        forward(1.5)
        left(43)
    for i in range(4):
        forward(3.2)
        right(4)
    left(100)
    draw_tooth_right(3, 150)
    left(30)
    for i in range(4):
        forward(3.5)
        right(4)
    left(110)
    draw_tooth_right(4, 150)
    left(25)
    for i in range(4):
        forward(3)
        right(4)
    left(110)
    draw_tooth_right(5, 150)
    left(40)
    for i in range(4):
        forward(3.2)
        right(4)
    left(100)
    draw_tooth_right(5, 150)
    left(40)


def draw_left_horn():
    left(70)
    draw_tooth_left(5.5, 155)
    left(110)
    for i in range(4):
        forward(5.5)
        right(4)
    left(65)
    draw_tooth_left(5, 160)
    left(110)
    for i in range(4):
        forward(4)
        right(4)
    left(70)
    draw_tooth_left(4.5, 160)
    left(118)
    for i in range(4):
        forward(3.5)
        right(4)
    left(60)
    draw_tooth_left(4, 165)
    left(125)
    for i in range(6):
        forward(7.5)
        right(5)
    for i in range(4):
        forward(0.5)
        left(38)
    a, b = 8, 8
    for i in range(13):
        forward(a)
        left(b)
        a += 1
        b += 0.3


def draw_right_ear():
    left(70)
    a, b = 12, 15
    for i in range(3):
        forward(a)
        left(b)
        a -= 2
        b += 5
    a = 5
    for i in range(5):
        forward(a)
        left(5)
        a += 1
    for i in range(4):
        left(30)
        forward(2)
    for i in range(5):
        forward(5)
        right(5)
    for i in range(5):
        forward(5.5)
        left(5)
    right(80)
    forward(5)


def draw_left_ear():
    for i in range(7):
        forward(4.5)
        right(8.2)
    a = 10
    for i in range(8):
        forward(a)
        left(11)
        if i < 5:
            a -= 1
        else:
            a += 1.5
    for i in range(3):
        forward(2.5)
        left(20)
    a = 10
    for i in range(2):
        forward(a)
        left(12)
        a -= 0.5
    forward(15)
    for i in range(11):
        left(6.5)
        forward(5)
    right(95)
    forward(8)
    right(80)
    a = 8
    for i in range(6):
        forward(a)
        right(5)
        a -= 1
    left(50)
    for i in range(7):
        forward(9)
        left(5)


def draw_tooth_right(lenght, angle):
    for i in range(5):
        forward(lenght)
        right(10)
    right(angle)
    for i in range(5):
        forward(lenght)
        left(10)


def draw_tooth_left(lenght, angle):
    for i in range(5):
        forward(lenght)
        left(10)
    right(angle)
    for i in range(5):
        forward(lenght+0.5)
        right(15)


def draw_tail_inner():
    penup()
    goto(118, 105)
    pendown()
    pencolor(BG_COLOR)
    begin_fill()
    setheading(towards(0, 0))
    right(75)
    for i in range(5):
        forward(6)
        right(25)
    right(130)
    for i in range(5):
        forward(3.5)
        left(15)
    left(110)
    forward(12)
    right(150)
    for i in range(5):
        forward(2.5)
        right(5)
    for i in range(4):
        forward(2.5)
        left(5)
    fillcolor(BG_COLOR)
    end_fill()


def draw_right_first_flower():
    penup()
    goto(85, -88)
    pendown()
    pencolor(BG_COLOR)
    setheading(towards(0, 0))
    left(40)
    draw_flower(2.2, BG_COLOR)
    penup()
    goto(90, -88)
    pendown()
    draw_blossom(12)
    penup()
    goto(101, -94)
    pendown()
    draw_circle(6, BG_COLOR)


def draw_right_second_flower():
    penup()
    goto(20, -96)
    pendown()
    pencolor(BG_COLOR)
    setheading(towards(0, 0))
    right(20)
    draw_flower(1.8, BG_COLOR)
    penup()
    goto(20, -100)
    pendown()
    draw_blossom(7)
    penup()
    goto(20, -108)
    pendown()
    draw_circle(4.5, BG_COLOR)


def draw_left_second_flower():
    penup()
    goto(-30, -115)
    pendown()
    pencolor(BG_COLOR)
    setheading(towards(0, 0))
    right(30)
    draw_flower(2.2, BG_COLOR)
    penup()
    goto(-35, -120)
    pendown()
    draw_blossom(12)
    penup()
    goto(-42, -130)
    pendown()
    draw_circle(6, BG_COLOR)


def draw_left_first_flower():
    penup()
    goto(-95, -50)
    pendown()
    pencolor(BG_COLOR)
    setheading(towards(0, 0))
    left(8)
    draw_flower(2.3, BG_COLOR)
    penup()
    goto(-102, -55)
    pendown()
    draw_blossom(13)
    penup()
    goto(-113, -62)
    pendown()
    draw_circle(6.5, BG_COLOR)


def draw_seven_petals():
    pencolor(BG_COLOR)
    penup()
    goto(132, -72)
    pendown()
    setheading(towards(0, 0))
    right(155)
    draw_petal(3.5, 3.5, 1.8, 1.8)
    penup()
    goto(122, -60)
    pendown()
    setheading(towards(0, 0))
    right(120)
    draw_petal(4, 3.5, 1.9, 1.9)
    penup()
    goto(103, -52)
    pendown()
    setheading(towards(0, 0))
    right(100)
    draw_petal(3.6, 3.2, 1.8, 1.8)
    penup()
    goto(84, -53)
    pendown()
    setheading(towards(0, 0))
    right(70)
    draw_petal(3.3, 2.8, 1.5, 1.5)
    penup()
    goto(70, -58)
    pendown()
    setheading(towards(0, 0))
    right(30)
    draw_petal(2.9, 2.5, 1.2, 1.2)
    penup()
    goto(62, -72)
    pendown()
    setheading(towards(0, 0))
    right(10)
    draw_petal(2.8, 2.4, 1.2, 1.2)
    penup()
    goto(60, -85)
    pendown()
    setheading(towards(0, 0))
    left(30)
    draw_petal(2.4, 2.2, 1, 1)


def draw_petal(a, b,  c, d):
    begin_fill()
    for i in range(9):
        forward(a)
        if i < 5:
            left(18)
            a -= 0.3
        else:
            right(10)
            a += 0.05
    left(120)
    for i in range(9):
        forward(b)
        left(12)
        b -= 0.15
    left(135)
    for i in range(7):
        forward(c)
        right(8)
        c += 0.15
    right(135)
    for i in range(8):
        forward(d)
        if i < 4:
            left(8)
            a -= 0.2
        else:
            right(23)
            a += 0.15
    fillcolor(BG_COLOR)
    end_fill()


def draw_water_right():
    pencolor(BG_COLOR)
    penup()
    goto(30, -125)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    right(120)
    a = 7
    for i in range(7):
        forward(a)
        left(10)
        a -= 1
    a = 1
    for i in range(6):
        forward(a)
        right(35)
        a += 0.5
    for i in range(12):
        forward(2.5)
        right(6)
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(25, -145)
    pendown()
    draw_circle(4, BG_COLOR)


def draw_water_left():
    pencolor(BG_COLOR)
    penup()
    goto(-80, -88)
    pendown()
    draw_circle(4, BG_COLOR)
    penup()
    goto(-115, -30)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    left(120)
    a = 7.2
    for i in range(7):
        forward(a)
        left(10)
        a -= 1
    a = 1
    for i in range(6):
        forward(a)
        right(35)
        a += 0.5
    for i in range(12):
        forward(2.5)
        right(5)
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(-110, -28)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    left(55)
    a = 6.5
    for i in range(6):
        forward(a)
        right(10)
        a -= 1
    a = 1
    for i in range(6):
        forward(a)
        left(35)
        a += 0.4
    for i in range(12):
        forward(2.5)
        left(5)
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(-125, -3)
    pendown()
    draw_circle(4, BG_COLOR)


def draw_left_ear_inner():
    pencolor(BG_COLOR)
    penup()
    goto(-117, 51)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    right(150)
    a = 8
    for i in range(10):
        forward(a)
        a -= 0.5
        right(5)
    left(150)
    for i in range(12):
        forward(5.8)
        left(9)
    left(150)
    for i in range(5):
        forward(3)
        right(5)
    right(160)
    for i in range(5):
        forward(3.1)
        left(5)
    left(160)
    for i in range(5):
        forward(6)
        right(6)
    right(160)
    for i in range(5):
        forward(6)
        left(7.5)
    fillcolor(BG_COLOR)
    end_fill()


def draw_head_up_flower():
    pencolor(BG_COLOR)
    penup()
    goto(-28, 102)
    pendown()
    setheading(towards(0, 0))
    right(128)
    begin_fill()
    a = 1.7
    for j in range(3):
        for i in range(40):
            if 0 <= i < 20:
                a = a - 0.07
            else:
                a = a + 0.07
            forward(a)
            left(6)
        right(168)
    fillcolor(BG_COLOR)
    end_fill()
    pencolor(COW_COLOR)
    penup()
    goto(-37, 102)
    pendown()
    setheading(towards(0, 0))
    right(85)
    draw_little_moon()
    penup()
    goto(-29, 83)
    pendown()
    setheading(towards(0, 0))
    right(5)
    draw_little_moon()
    penup()
    goto(-10, 88)
    pendown()
    setheading(towards(0, 0))
    left(65)
    draw_little_moon()
    penup()
    goto(-23, 99)
    pendown()
    draw_blossom(6.5)


def draw_little_moon():
    begin_fill()
    for i in range(10):
        forward(1.1)
        left(15)
    right(170)
    for i in range(10):
        forward(1.2)
        right(20)
    fillcolor(COW_COLOR)
    end_fill()


def draw_right_ear_inner():
    pencolor(BG_COLOR)
    penup()
    goto(31, 37)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    left(106)
    a = 6
    for i in range(10):
        forward(a)
        a -= 0.5
        left(5)
    right(140)
    for i in range(10):
        forward(4)
        right(11)
    right(135)
    for i in range(3):
        forward(2)
        left(5)
    left(140)
    for i in range(3):
        forward(3)
        right(5)
    right(150)
    for i in range(5):
        forward(4)
        left(6)
    left(155)
    for i in range(5):
        forward(4.5)
        right(7)
    fillcolor(BG_COLOR)
    end_fill()


def draw_nose():
    pencolor(BG_COLOR)
    penup()
    goto(30, -29)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    left(170)
    forward(4)
    for i in range(3):
        forward(1)
        left(48)
    forward(3.5)
    for i in range(8):
        forward(1)
        left(20)
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(5, -28)
    begin_fill()
    pendown()
    setheading(towards(0, 0))
    left(95)
    for i in range(5):
        forward(2.5)
        left(2)
    a = 0.5
    for i in range(8):
        forward(a)
        right(35)
        a += 0.8
    fillcolor(BG_COLOR)
    end_fill()


def draw_water_up():
    pencolor(BG_COLOR)
    penup()
    goto(-92, 18)
    pendown()
    setheading(towards(0, 0))
    right(18)
    begin_fill()
    a = 7
    for i in range(6):
        forward(a)
        right(18)
        a -= 1
    a = 1
    for i in range(6):
        forward(a)
        left(35)
        a += 0.25
    for i in range(12):
        forward(2.5)
        left(9)
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(-95, 25)
    pendown()
    setheading(towards(0, 0))
    left(10)
    begin_fill()
    for i in range(10):
        forward(6)
        right(8)
    left(180)
    for i in range(10):
        forward(7)
        left(10.8)
    fillcolor(BG_COLOR)
    end_fill()


def draw_five_circle():
    pencolor(BG_COLOR)
    penup()
    goto(-42, -36)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(4.8, BG_COLOR)
    pencolor(BG_COLOR)
    penup()
    goto(-40, -22)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(3.8, BG_COLOR)
    penup()
    goto(-42, -10)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(3, BG_COLOR)
    penup()
    goto(-44, 0)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(2.5, BG_COLOR)
    penup()
    goto(-49, 7)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(2, BG_COLOR)


def draw_eye():
    pencolor(BG_COLOR)
    penup()
    goto(-75, 40)
    pendown()
    setheading(towards(0, 0))
    right(38)
    begin_fill()
    a = 3.5
    for i in range(7):
        forward(a)
        left(15)
        a += 0.5
    left(70)
    a = 7
    for i in range(7):
        forward(a)
        left(18)
        a -= 0.5
    left(150)
    a = 3
    for i in range(7):
        forward(a)
        right(14)
        a += 0.5
    right(80)
    a = 6.5
    for i in range(5):
        forward(a)
        right(16)
        a -= 0.5
    fillcolor(BG_COLOR)
    end_fill()
    penup()
    goto(-68, 44)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(7, BG_COLOR)
    penup()
    goto(-64, 42)
    pendown()
    setheading(towards(0, 0))
    right(90)
    draw_circle(4, COW_COLOR)


def draw_eyelash():
    pencolor(BG_COLOR)
    penup()
    goto(-40, 32)
    pendown()
    setheading(towards(0, 0))
    left(10)
    draw_petal(1.8, 1.6, 0.6, 0.6)
    penup()
    goto(-42, 39)
    pendown()
    setheading(towards(0, 0))
    left(30)
    draw_petal(2, 1.8, 0.8, 0.8)
    penup()
    goto(-46, 45)
    pendown()
    setheading(towards(0, 0))
    left(50)
    draw_petal(2.3, 2, 1, 1)
    penup()
    goto(-52, 52)
    pendown()
    setheading(towards(0, 0))
    left(80)
    draw_petal(2.4, 2.1, 1, 1)
    penup()
    goto(-62, 55)
    pendown()
    setheading(towards(0, 0))
    left(90)
    draw_petal(2.5, 2.2, 1.1, 1.1)
    penup()
    goto(-72, 55)
    pendown()
    setheading(towards(0, 0))
    left(115)
    draw_petal(2.4, 2.1, 1, 1)


if __name__ == '__main__':
    title('Drawing golden buffalo in Python')
    setup(800, 600, 150, 100)
    screensize(1040, 585, BG_COLOR)
    pencolor(COW_COLOR)
    speed(10)
    time.sleep(1)
    draw_circle_and_set_start(255, COW_COLOR)
    draw_circle_and_set_start(245, BG_COLOR)
    draw_outer_ring()
    draw_inner_ring()
    draw_circle_and_set_start(198, COW_COLOR)
    draw_circle_and_set_start(185, BG_COLOR)
    draw_outline_out()
    draw_outline_inner()
    draw_tail_inner()
    draw_right_first_flower()
    draw_seven_petals()
    draw_right_second_flower()
    draw_water_right()
    draw_left_second_flower()
    draw_left_first_flower()
    draw_water_left()
    draw_water_up()
    draw_left_ear_inner()
    draw_head_up_flower()
    draw_right_ear_inner()
    draw_nose()
    draw_five_circle()
    draw_eyelash()
    draw_eye()
    penup()
    goto(400, 0)
    done()
