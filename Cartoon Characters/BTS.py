from turtle import *

speed(0)
hideturtle()


def myposition(x, y):
    penup()
    goto(x - 300, (y * -1) + 300)
    pendown()
    

def positions():
    positions.face_cut = [(195, 230), (193, 253), (193, 300), (199, 330), (214, 361), (214, 367), (219, 373), (228, 386), (238, 395), (248, 400), (258, 403), (284, 407), (297, 405), (361, 371), (373, 359), (395, 335), (396, 329), (406, 317), (411, 309), (406, 294), (402, 287), (398, 276), (390, 266), (384, 259), (375, 247), (369, 241), (379, 254), (370, 246), (365, 243), (358, 237), (353, 234), (347, 231), (357, 241), (345, 230), (335, 217), (331, 207), (331, 195), (331, 189), (325, 202), (322, 208), (319, 216), (318, 227), (319, 242), (321, 252), (314, 234), (312, 222), (311, 211), (316, 197), (310, 203), (305, 208), (301, 228), (299, 211), (296, 231), (295, 209), (293, 208), (290, 228), (292, 203), (288, 203), (283, 231), (290, 201), (298, 179), (275, 193), (262, 198), (243, 203), (231, 211), (229, 213), (235, 224), (223, 214), (221, 205), (208, 214), (197, 225), (194, 230), (191, 255), (191, 263),]
    
    positions.hair_out = [(191, 262), (189, 252), (187, 237), (186, 225), (186, 204), (182, 239), (181, 206), (175, 233), (177, 205), (167, 196), (168, 172), (158, 182), (165, 170), (169, 161), (170, 154), (159, 156), (151, 146), (158, 156), (168, 150), (174, 141), (171, 144), (167, 136), (168, 124), (172, 120), (174, 138), (174, 126), (174, 115), (175, 101), (181, 93), (194, 81), (209, 71), (219, 60), (230, 48), (238, 38), (245, 32), (259, 23), (269, 19), (279, 17), (295, 12), (304, 12), (317, 13), (320, 12), (329, 8), (345, 5), (354, 6), (365, 9), (375, 10), (377, 8), (389, 19), (391, 22), (397, 22), (406, 19), (416, 22), (424, 25), (432, 29), (443, 33), (451, 39), (458, 44), (463, 51), (485, 87), (499, 99), (507, 116), (509, 139), (511, 143), (515, 157), (517, 171), (516, 185), (517, 197), (518, 209), (513, 220), (493, 249), (491, 262), (495, 279), (488, 272), (488, 263), (486, 264), (483, 271), (481, 278), (488, 286), (493, 290), (484, 286), (479, 283), (478, 277), (478, 267), (479, 257), (476, 263), (470, 269), (471, 278), (469, 286), (477, 308), (474, 283), (474, 279), (466, 286), (463, 293), (449, 295), (453, 279), (448, 295), (451, 280), (444, 294), (449, 282), (438, 298), (447, 283), (429, 304), (450, 280), (418, 308), (446, 277), (417, 303), (449, 271), (422, 295), (410, 321), (412, 306), (426, 275), (407, 303), (417, 266), (406, 298), (409, 268), (409, 293), (406, 261), (404, 291), (396, 265), (398, 286), (389, 265), (381, 253), (382, 260), (367, 242), (355, 224), (375, 249), (365, 243), (356, 235), (347, 201), (349, 215), (359, 236), (347, 227), (341, 216), (340, 202), (347, 228), (339, 223), (334, 211), (331, 198), (330, 190), (321, 201), (317, 214), (316, 231), (320, 247), (314, 230), (311, 215), (311, 200), (313, 194), (305, 206), (300, 222), (301, 231), (301, 210), (296, 232), (296, 207), (291, 208), (290, 221), (290, 204), (282, 229), (286, 207), (282, 208), (276, 224), (280, 207), (258, 200), (282, 201), (293, 198), (301, 175), (290, 181), (286, 191), (257, 198), (246, 203), (233, 208), (229, 222), (221, 199), (223, 226), (220, 204), (213, 210), (204, 216), (195, 221), (193, 232), (219, 208), (222, 219), (223, 225), (204, 243), (204, 224), (199, 231), (200, 228), (221, 210), (219, 219), (204, 227), (204, 225), (204, 240), (205, 230), (226, 217), (223, 223), (202, 244), (199, 259),]
    
    positions.dress = [(198, 326), (195, 334), (192, 343), (184, 352), (177, 356), (183, 467), (187, 483), (172, 468), (178, 355), (183, 343), (190, 336), (196, 334), (177, 338), (138, 370), (31, 411), (134, 374), (78, 464), (64, 469), (75, 465), (120, 487), (163, 466), (171, 468), (185, 483), (180, 507), (172, 532), (159, 472), (117, 490), (159, 476), (122, 493), (159, 492), (172, 534), (210, 580), (207, 596), (218, 574), (187, 485), (219, 572), (243, 551), (265, 541), (293, 538), (309, 534), (320, 529), (327, 517), (335, 515), (357, 539), (361, 550), (369, 555), (379, 570), (407, 580), (397, 557), (392, 534), (383, 505), (381, 481), (382, 464), (374, 458), (372, 441), (408, 479), (418, 491), (427, 503), (448, 513), (471, 537), (487, 555), (466, 532), (440, 515), (423, 495), (409, 473), (392, 461), (373, 447), (367, 413), (356, 390), (359, 373), (347, 409), (341, 432), (342, 437), (303, 509), (295, 524), (289, 530), (271, 538), (260, 544), (231, 561), (217, 573), (210, 595), (255, 586), (264, 572), (282, 554), (297, 547), (310, 541), (321, 533), (325, 517),]
    
    positions.dress_shade = [(206, 350), (236, 419), (244, 426), (272, 432), (289, 431), (291, 454), (264, 474), (262, 486), (244, 498), (249, 514), (302, 510), (341, 440), (351, 392), (355, 411), (328, 512), (319, 527), (296, 539), (269, 541), (235, 553), (218, 571), (205, 599), (187, 584), (171, 539), (177, 539), (176, 547), (179, 543), (175, 555), (179, 547), (179, 558), (183, 546), (179, 565), (185, 550), (182, 567), (188, 550), (184, 578), (192, 555), (184, 588), (193, 554), (189, 586), (197, 557), (191, 588), (198, 561), (195, 586), (200, 566), (196, 591), (205, 569), (199, 596), (203, 571), (201, 599), (208, 576), (204, 599), (212, 584), (175, 543), (160, 473), (166, 474), (161, 476), (168, 475), (161, 473), (172, 472), (158, 477), (170, 482), (161, 484), (170, 480), (161, 479), (168, 485), (161, 487), (171, 490), (161, 490), (169, 488), (162, 487), (169, 491), (164, 494), (172, 494), (165, 494), (175, 498), (167, 498), (173, 501), (165, 501), (173, 504), (167, 506), (177, 510), (170, 511), (176, 513), (168, 513), (178, 518), (171, 518), (176, 519), (166, 519), (174, 523), (169, 523), (174, 527), (170, 527), (171, 537), (158, 470), (152, 472), (144, 552), (130, 554), (130, 485), (159, 475), (116, 491), (116, 497), (159, 479), (161, 483), (119, 500), (118, 506), (162, 489), (162, 496), (122, 510), (124, 514), (163, 499), (164, 506), (128, 519), (127, 528), (164, 511), (165, 520), (134, 537), (130, 543), (169, 525), (170, 532), (137, 546), (134, 557), (170, 538), (171, 545), (139, 561), (160, 565), (176, 554), (184, 582), (157, 543), (171, 537), (214, 578), (248, 549), (276, 536), (317, 528), (326, 520), (327, 521), (323, 522), (326, 526), (320, 526), (325, 527), (318, 527), (322, 533), (313, 533), (320, 537), (305, 537), (285, 541), (312, 534), (282, 545), (314, 537), (283, 545), (313, 539), (278, 549), (310, 542), (274, 554), (309, 544), (267, 560), (310, 544), (265, 566), (303, 550), (267, 567), (285, 563), (254, 572), (277, 568), (252, 578), (275, 573), (249, 588), (279, 574), (316, 539), (333, 514), (342, 517), (327, 524), (322, 530), (344, 522), (350, 531), (319, 536), (309, 551), (355, 536), (358, 542), (291, 559), (288, 567), (365, 550), (369, 558), (357, 563), (313, 565), (283, 573), (247, 584),]
    
    positions.nose = [(282, 309), (279, 309), (269, 299), (275, 306), (269, 305), (262, 301), (260, 294), (262, 288), (266, 282), (275, 282), (281, 289), (288, 295), (283, 297), (278, 295), (273, 300), (278, 308), (282, 310), (289, 310), (295, 307), (299, 310), (299, 311), (295, 310), (288, 310), (281, 310), (295, 314), (298, 316), (305, 314), (311, 309), (312, 305), (311, 295), (310, 279), (313, 290), (305, 292), (295, 287), (293, 293), (286, 296), (280, 294), (272, 299), (274, 304), (269, 306), (263, 300), (260, 291), (265, 284), (269, 279), (278, 276), (287, 260), (296, 243), (290, 239),]
    
    positions.l_eye = [(277, 239), (275, 230), (270, 224), (262, 219), (257, 217), (237, 212), (240, 213), (242, 219), (245, 225), (250, 231), (257, 233), (263, 235), (269, 235), (273, 235), (276, 240), (275, 232), (269, 224), (269, 229), (265, 231), (259, 230), (255, 226), (253, 222), (257, 219), (259, 217), (250, 215), (253, 223),]
    
    positions.l_eye_ball = [(257, 227), (258, 225), (261, 226), (264, 225), (261, 224), (261, 222), (257, 222), (257, 223), (258, 224), (261, 225), (261, 222), (265, 221), (261, 219), (254, 220),]
    
    positions.r_eye = [(335, 257), (343, 251), (357, 250), (366, 253), (378, 259), (381, 269), (370, 271), (360, 271), (349, 265), (341, 257), (335, 255), (335, 257), (344, 251), (351, 251), (349, 260), (359, 265), (365, 263), (366, 259), (366, 254),]
    
    positions.r_eye_ball = [(351, 254), (354, 253), (355, 251), (360, 251), (364, 253), (364, 258), (363, 259), (358, 259), (356, 262), (358, 259), (355, 257), (354, 254), (355, 252), (357, 254), (358, 257), (360, 257), (363, 258), (363, 256), (363, 254), (361, 253), (360, 253), (357, 255), (357, 251), (344, 251), (335, 257), (345, 267), (344, 266), (347, 263), (359, 271), (370, 271), (376, 268), (379, 267), (380, 273), (374, 275), (364, 275), (360, 274), (364, 275), (361, 270),]
    
    positions.mouth = [(238, 333), (243, 332), (249, 337), (253, 335), (258, 339), (276, 346), (285, 346), (280, 351), (267, 351), (258, 339), (276, 346), (283, 346), (299, 354), (303, 354), (302, 352), (305, 355), (303, 354), (299, 354), (290, 359), (280, 359), (272, 357), (268, 354), (261, 343), (254, 340), (242, 339), (252, 350), (265, 355), (269, 355), (266, 350), (255, 337), (249, 335), (242, 331), (241, 329), (248, 328), (261, 327), (265, 330), (270, 335), (280, 334), (288, 336), (302, 351), (298, 349), (283, 340), (274, 340), (271, 336), (268, 339), (261, 335), (244, 328),]
    
    positions.l_ear = [(395, 333), (408, 312), (408, 326), (420, 308), (431, 301), (439, 305), (447, 296), (446, 301), (452, 297), (458, 294), (459, 282), (466, 283), (464, 288), (461, 295), (441, 320), (423, 335), (415, 338), (407, 339), (401, 339), (394, 332), (404, 340), (404, 338), (405, 343), (409, 341), (409, 334), (409, 339), (421, 335), (418, 329), (421, 334), (418, 344), (411, 345), (410, 338), (412, 345), (414, 350), (419, 350), (419, 345), (414, 345), (414, 351), (411, 352), (411, 360), (413, 362), (418, 362), (421, 360), (421, 353), (418, 351), (420, 354), (421, 360), (417, 363), (418, 366), (415, 366), (414, 362), (417, 362), (417, 371), (415, 371), (414, 366), (408, 366), (407, 368), (424, 368), (424, 366), (416, 366), (414, 416),]
    
    positions.r_ear = [(191, 263), (185, 262), (171, 244), (169, 207), (171, 203), (169, 205), (170, 242), (175, 253), (176, 249), (180, 249), (175, 250), (174, 257), (180, 256), (181, 258), (186, 255), (181, 258), (180, 264), (180, 267), (186, 267), (188, 261), (191, 262),]
  
    positions.eye_brow = [(295, 249), (301, 237), (299, 225), (291, 208), (280, 201), (271, 200), (254, 201), (277, 208), (284, 212), (282, 231), (286, 214), (289, 207), (289, 234), (292, 209), (295, 231), (299, 213), (299, 229), (312, 200), (310, 217), (315, 235), (320, 250), (317, 230), (320, 208), (332, 190), (332, 205), (340, 226), (339, 225), (331, 225), (326, 233), (337, 230), (344, 230), (351, 232), (359, 237), (369, 244), (377, 254), (367, 249), (349, 245), (337, 248), (320, 257), (337, 246), (331, 245), (322, 251), (333, 245), (339, 246), (348, 246), (383, 267), (383, 272), (375, 276), (365, 275), (373, 282), (379, 287), (391, 289), (398, 291), (400, 307), (378, 335), (365, 357), (354, 370), (343, 381), (335, 386),]
   
    positions.hair = [(192, 250), (182, 218), (192, 205), (190, 188), (193, 173), (200, 163), (244, 118), (259, 94), (274, 80), (298, 68), (310, 65), (324, 55), (354, 41), (370, 38), (382, 39), (382, 39), (353, 101), (376, 42), (362, 90), (385, 44), (361, 85), (389, 43), (389, 71), (391, 99), (387, 64), (387, 38), (396, 44), (408, 90), (398, 47), (412, 63), (425, 94), (399, 45), (431, 87), (394, 44), (414, 52), (400, 49), (423, 69), (390, 43), (402, 32), (418, 38), (436, 53), (459, 80), (406, 34), (391, 38), (389, 30), (383, 29), (378, 31), (381, 38), (389, 42), (385, 33), (393, 26), (404, 20), (414, 22), (395, 31), (420, 24), (390, 35), (389, 20), (384, 9), (376, 9), (365, 8), (374, 15), (384, 25), (384, 29), (375, 30), (354, 19), (342, 14), (327, 17), (341, 16), (377, 32), (364, 30), (344, 30), (299, 52), (360, 27), (337, 19), (325, 18), (301, 27), (277, 42), (266, 48), (256, 59), (234, 89), (214, 105), (199, 113), (177, 132), (171, 152), (171, 170), (185, 199), (186, 175), (187, 149), (199, 125), (190, 157), (191, 182), (194, 145), (208, 131), (206, 129), (192, 158), (192, 170), (186, 191), (184, 147), (192, 118), (178, 132), (186, 100), (199, 85), (220, 67), (230, 52), (199, 89), (189, 106), (213, 90), (225, 72), (248, 50), (269, 48), (306, 33), (342, 32), (377, 32), (374, 54), (369, 66), (346, 118), (331, 136), (305, 158), (298, 157), (296, 145), (303, 132), (323, 104), (314, 105), (292, 122), (275, 143), (261, 163), (249, 183), (238, 196), (238, 206), (237, 222), (236, 197), (238, 185), (232, 209), (232, 219), (232, 205), (236, 187), (246, 174), (233, 185), (230, 198), (230, 212), (230, 219), (227, 214), (227, 205), (232, 193), (239, 185), (247, 177), (232, 193), (229, 201), (229, 212), (227, 219), (224, 208), (222, 200), (222, 189), (227, 180), (228, 179), (224, 189), (220, 199), (220, 190), (220, 179), (225, 170), (235, 160), (219, 174), (218, 182), (218, 195), (223, 201), (224, 209), (231, 202), (237, 188), (246, 182), (257, 172), (264, 168), (236, 188), (248, 183), (272, 179), (283, 178), (295, 170), (309, 158), (309, 158), (320, 145), (328, 138), (339, 122), (344, 117), (338, 134), (331, 143), (304, 177), (331, 151), (302, 183), (323, 160), (299, 191), (309, 180), (302, 203), (312, 183), (328, 164), (363, 131), (313, 193), (342, 158), (320, 193), (356, 148), (350, 178), (338, 196), (343, 222), (343, 202), (354, 182), (368, 161), (381, 143), (366, 174), (354, 187), (350, 199), (350, 210), (353, 223), (362, 239), (369, 247), (364, 237), (360, 229), (359, 212), (360, 198), (368, 188), (374, 177), (377, 167), (380, 151), (383, 129), (381, 160), (372, 174), (364, 189), (361, 205), (366, 220), (371, 233), (374, 242), (370, 225), (370, 212), (374, 198), (379, 187), (371, 209), (375, 228), (379, 244), (379, 227), (386, 207), (397, 188), (408, 169), (408, 156), (408, 136), (407, 123), (412, 144), (406, 159), (396, 179), (389, 194), (382, 208), (382, 227), (385, 242), (392, 250), (408, 264), (415, 282), (413, 266), (410, 257), (403, 249), (403, 228), (396, 238), (398, 251), (397, 265), (395, 281), (401, 258), (403, 237), (413, 214), (421, 195), (429, 176), (432, 159), (436, 139), (435, 114), (433, 111), (441, 129), (435, 145), (424, 164), (419, 176), (412, 195), (410, 210), (412, 225), (417, 238), (420, 247), (418, 264), (422, 277), (418, 290), (428, 273), (428, 258), (430, 240), (424, 219), (423, 206), (430, 189), (429, 206), (431, 220), (433, 247), (433, 262), (431, 278), (427, 287), (420, 303), (413, 314), (409, 322), (418, 311), (424, 302), (430, 292), (435, 285), (442, 279), (449, 268), (452, 261), (453, 272), (460, 279), (470, 283), (464, 280), (459, 272), (459, 262), (461, 253), (467, 242), (471, 234), (471, 220), (471, 208), (466, 202), (460, 197), (458, 190), (455, 183), (455, 171), (455, 157), (457, 147), (455, 137), (447, 127), (455, 140), (455, 148), (455, 168), (456, 185), (462, 168), (462, 155), (462, 141), (462, 132), (461, 119), (454, 109), (461, 137), (461, 156), (461, 169), (459, 190), (473, 153), (475, 139), (475, 125), (474, 184), (480, 201), (486, 219), (487, 232), (487, 241), (485, 250), (479, 259), (474, 263), (491, 251), (494, 240), (498, 226), (501, 213), (501, 196), (503, 184), (496, 158), (498, 178), (498, 190), (496, 208), (493, 216), (492, 221), (490, 244), (483, 254), (482, 266), (483, 276), (487,  265),]


def color_fill(coordinates, co = (0, 0, 0)):
    color(co)
    p_x, p_y = coordinates[0]
    myposition(p_x, p_y)
    fillcolor(co)
    begin_fill()
    t = 0
    for i in coordinates[1:]:
        x, y = i
        if t:
            myposition(x, y)
            t = 0
            begin_fill()
            continue
        if x == -1 and y == -1:
            t = 1
            end_fill()
            continue
        else:
            goto(x - 300, (y * -1) + 300)
    end_fill()


def draw(coordinates, mode = 1, co = (0, 0, 0), thickness = 1):
    co = (co[0] / 255, co[1] / 255, co[2] / 255)
    color(co)
    
    if mode:
        width(thickness)
        p_x, p_y = coordinates[0]
        myposition(p_x, p_y)
        t = 0
        for i in coordinates[1:]:
            x, y = i
            if t:
                myposition(x, y)
                t = 0
                continue
            if x == -1 and y == -1:
                t = 1
                continue
            else:
                goto(x - 300, (y * -1) + 300)
    else:
        color_fill(coordinates, co)


def files():
    positions()
    draw(positions.face_cut)
    draw(positions.hair_out)
    draw(positions.dress)
    draw(positions.dress_shade)
    draw(positions.nose)
    draw(positions.l_eye)
    draw(positions.l_eye_ball)
    draw(positions.r_eye)
    draw(positions.r_eye_ball)
    draw(positions.mouth)
    draw(positions.l_ear)
    draw(positions.r_ear)
    draw(positions.eye_brow)
    draw(positions.hair)
    

files()
done()
