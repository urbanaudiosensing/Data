from matplotlib.patches import Ellipse

def create_ellipse(station):
    # ----------------------------------------
    if station == "Cadell":
        # 1-meter buffer
        ellipse1_1m = Ellipse((770, 645), 70, 40, 0) # 760, 645 (05/24) # 760, 470 (06/01) # 790, 425
        ellipse2_1m = Ellipse((905, 520), 70, 20, 0) # 895, 520 (05/24) # 900, 350 #930, 310
        ellipse3_1m = Ellipse((1230, 740), 80, 40, 4) # 1220, 740 (05/24) #1215, 580 # 1240, 550
        ellipse4_1m = Ellipse((710, 500), 65, 20, 0) # 700, 500 (05/24) # 730, 300 # 760, 260
        ellipse5_1m = Ellipse((905, 490), 60, 20, 0) # 895, 490 (05/24) #905, 315  #935, 275
        ellipse6_1m = Ellipse((1590, 680), 90, 35, 4) # 1580, 680 (05/24) #1570, 540 #1610, 515

        # 3-meter buffer
        ellipse1_3m = Ellipse((770, 645), 200, 90, 0) # 760, 645
        ellipse2_3m = Ellipse((905, 520), 140, 40, 0) # 895, 520
        ellipse3_3m = Ellipse((1230, 740), 270, 140, 4) # 1220, 740
        ellipse4_3m = Ellipse((710, 500), 110, 40, 0) # 700, 500
        ellipse5_3m = Ellipse((905, 490), 120, 40, 0) # 895, 490
        ellipse6_3m = Ellipse((1590, 680), 250, 90, 6) # 1580, 680

        # 6-meter buffer
        ellipse1_6m = Ellipse((770, 670), 400, 180, 0) # 760, 670
        ellipse2_6m = Ellipse((905, 525), 280, 80, 0) # 895, 525
        ellipse3_6m = Ellipse((1230, 790), 500, 280, 4) # 1220, 790
        ellipse4_6m = Ellipse((710, 500), 220, 80, 0) # 700, 500 
        ellipse5_6m = Ellipse((905, 495), 260, 80, 0) # 895, 495
        ellipse6_6m = Ellipse((1590, 700), 500, 200, 6) # 1580, 700

        # 9-meter buffer
        ellipse1_9m = Ellipse((770, 680), 660, 280, 0) # 760, 680
        ellipse2_9m = Ellipse((905, 525), 420, 115, 0) # 895, 525
        ellipse3_9m = Ellipse((1230, 815), 880, 400, 4) # 1220, 815
        ellipse4_9m = Ellipse((710, 500), 330, 105, 0) # 700, 500
        ellipse5_9m = Ellipse((905, 495), 380, 100, 0) # 895, 495
        ellipse6_9m = Ellipse((1590, 730), 750, 380, 6)    # 1580, 730

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse4_1m, ellipse5_1m, ellipse6_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse4_3m, ellipse5_3m, ellipse6_3m,
            ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse4_6m, ellipse5_6m, ellipse6_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m, ellipse4_9m, ellipse5_9m, ellipse6_9m]
        
    
    elif station == "TechwayD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((370, 650), 65, 30, 0) # 370, 650 (05/24) #335, 680 # 365, 490 (06/07)
        ellipse2_1m = Ellipse((605, 495), 35, 20, 1)  # 605, 495 # 570, 530 # 600, 330 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((370, 650), 210, 53, 1.0) # 370, 650
        ellipse2_3m = Ellipse((605, 495), 150, 40, 1) # 605, 495
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((380, 650), 480, 125, 1.0) # 380, 650
        ellipse2_6m = Ellipse((620, 495), 280, 70, 1) # 620, 495
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((415, 650), 620, 180, 1) # 415, 650
        ellipse2_9m = Ellipse((630, 495), 400, 105, 1) # 630, 495

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1200, 505), 180, 40, 3.8) # 1200, 500 (05/24) # 1295, 470 
        ellipse2_1m = Ellipse((910, 445), 80, 25, 2)  # 910, 450 # 1000, 405
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1200, 510), 400, 110, 3.5) # 1200, 510
        ellipse2_3m = Ellipse((905, 450), 200, 30, 1.5) # 905, 460
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1200, 530), 650, 155, 3) # 1200, 530
        ellipse2_6m = Ellipse((905, 450), 300, 50, 1) # 905, 455
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1200, 540), 900, 220, 2) # 1200, 540
        ellipse2_9m = Ellipse((910, 450), 500, 60, 1) # 905, 450

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1250, 530), 80, 20, 2) # 1250, 530 (0524) # (1280, 490) # 1355, 465 (06/07)
        ellipse2_1m = Ellipse((990, 490), 40, 15, 0)  # 990, 490  # 1020, 460 # 1090, 400
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1250, 530), 260, 30, 2) # 1250, 530
        ellipse2_3m = Ellipse((990, 490), 175, 25, 0) # 990, 490 
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1250, 530), 520, 70, 2) # 1250, 530
        ellipse2_6m = Ellipse((990, 495), 350, 30, 0) # 990, 495 
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1250, 570), 760, 150, 2) # 1250, 550
        ellipse2_9m = Ellipse((990, 495), 500, 45, 2) # 990, 495 

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((980, 540), 180, 50, 2) # 980, 540 # 745, 425 (06/07) # 1060, 420 (6/21)
        ellipse2_1m = Ellipse((660, 490), 65, 20, 0)  # 660, 490  # 405, 390 # 735, 360 
        ellipse3_1m = Ellipse((555, 480), 50, 15, 0)  # 555, 480 # 300, 390 # 635, 360
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((980, 550), 380, 100, -2) # 980, 550
        ellipse2_3m = Ellipse((660, 495), 240, 40, -2) # 660, 495
        ellipse3_3m = Ellipse((555, 480), 170, 20, -2)  # 555, 480
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1000, 580), 760, 210, -1) # 1000, 580
        ellipse2_6m = Ellipse((660, 500), 460, 60, -2) # 660, 500
        ellipse3_6m = Ellipse((555, 480), 360, 28, -2)   # 555, 480
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1000, 620), 1180, 330, -2) # 1000, 620
        ellipse2_9m = Ellipse((660, 520), 650, 80, -2) # 660, 520
        ellipse3_9m = Ellipse((560, 485), 450, 30, -2)  # 560, 485

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m]
    
    elif station == "fifthF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1050, 555), 80, 20, 2) # 1250, 530 (0524) # (1280, 490) # 1355, 465 (06/07)
        ellipse2_1m = Ellipse((480, 525), 40, 15, 0)  # 990, 490  # 1020, 460 # 1090, 400
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1050, 555), 260, 30, 2)
        ellipse2_3m = Ellipse((480, 525), 175, 25, 0)
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1050, 55), 520, 70, 2)
        ellipse2_6m = Ellipse((480, 525), 350, 30, 0)
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1050, 555), 760, 130, 2)
        ellipse2_9m = Ellipse((480, 525), 500, 45, 2)

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]    

    return(ells)
