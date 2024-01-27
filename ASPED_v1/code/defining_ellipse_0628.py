from matplotlib.patches import Ellipse

def create_ellipse(station):
    # ----------------------------------------
    if station == "Cadell": 
        # 1-meter buffer
        ellipse1_1m = Ellipse((770, 335), 70, 40, 0) # 770, 335
        ellipse2_1m = Ellipse((905, 220), 70, 20, 0) # 910, 220
        ellipse3_1m = Ellipse((1230, 455), 80, 40, 4) # 1230, 455
        ellipse4_1m = Ellipse((710, 190), 65, 20, 0) # 710, 190
        ellipse5_1m = Ellipse((915, 185), 60, 20, 0) # 915, 185
        ellipse6_1m = Ellipse((1590, 430), 90, 35, 4) # 1590, 430

        # 3-meter buffer
        ellipse1_3m = Ellipse((770, 335), 200, 90, 0) # 770, 335
        ellipse2_3m = Ellipse((905, 220), 140, 40, 0) # 910, 220
        ellipse3_3m = Ellipse((1230, 455), 270, 140, 4) # 1230, 455
        ellipse4_3m = Ellipse((710, 190), 110, 40, 0) # 710, 190
        ellipse5_3m = Ellipse((915, 185), 120, 40, 0) # 915, 185
        ellipse6_3m = Ellipse((1590, 430), 250, 90, 6) # 1590, 430

        # 6-meter buffer
        ellipse1_6m = Ellipse((770, 355), 400, 180, 0) # 770, 355
        ellipse2_6m = Ellipse((905, 225), 280, 80, 0) # 910, 225
        ellipse3_6m = Ellipse((1230, 505), 500, 280, 4) # 1230, 505
        ellipse4_6m = Ellipse((710, 190), 220, 80, 0) # 710, 190
        ellipse5_6m = Ellipse((915, 195), 260, 80, 0) # 915, 195
        ellipse6_6m = Ellipse((1590, 450), 500, 200, 6) # 1590, 450

        # 9-meter buffer
        ellipse1_9m = Ellipse((770, 365), 660, 280, 0) # 770, 365
        ellipse2_9m = Ellipse((905, 225), 420, 115, 0) # 910, 225
        ellipse3_9m = Ellipse((1230, 535), 880, 400, 4) # 1230, 535
        ellipse4_9m = Ellipse((710, 190), 330, 105, 0) # 710, 190
        ellipse5_9m = Ellipse((915, 195), 380, 100, 0) # 915, 195
        ellipse6_9m = Ellipse((1590, 480), 750, 380, 6) # 1590, 480

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse4_1m, ellipse5_1m, ellipse6_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse4_3m, ellipse5_3m, ellipse6_3m,
            ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse4_6m, ellipse5_6m, ellipse6_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m, ellipse4_9m, ellipse5_9m, ellipse6_9m]

    
    elif station == "TechwayD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((680, 850), 65, 30, 0) # 370, 650 (05/24) #335, 680 # 365, 490 (06/07)
        ellipse2_1m = Ellipse((930, 730), 35, 20, 1)  # 605, 495 # 570, 530 # 600, 330 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((680, 850), 210, 53, 1.0)
        ellipse2_3m = Ellipse((930, 730), 150, 40, 1) 
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((690, 850), 480, 125, 1.0)
        ellipse2_6m = Ellipse((945, 730), 280, 70, 1) 
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((725, 850), 620, 180, 1)
        ellipse2_9m = Ellipse((955, 730), 400, 105, 1)

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1640, 640), 180, 40, 3.8) # 1200, 500 (05/24) # 1295, 470 
        ellipse2_1m = Ellipse((1345, 550), 80, 25, 2)  # 910, 450 # 1000, 405
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1640, 650), 500, 110, 3.5)
        ellipse2_3m = Ellipse((1340, 560), 280, 30, 1.5)
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1640, 670), 900, 155, 3)
        ellipse2_6m = Ellipse((1340, 555), 400, 40, 1)
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1640, 680), 1200, 230, 2)
        ellipse2_9m = Ellipse((1340, 550), 580, 45, 1)

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1315, 470), 80, 20, 2) # 1250, 530 (0524) # (1280, 490) # 1355, 465 (06/07)
        ellipse2_1m = Ellipse((1055, 425), 40, 15, 0)  # 990, 490  # 1020, 460 # 1090, 400
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1315, 470), 260, 30, 2)
        ellipse2_3m = Ellipse((1055, 425), 175, 25, 0)
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1315, 470), 520, 70, 2)
        ellipse2_6m = Ellipse((1055, 430), 350, 30, 0)
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1315, 490), 760, 130, 2)
        ellipse2_9m = Ellipse((1055, 430), 500, 45, 2)

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((805, 480), 180, 50, 2) # 980, 540 # 745, 425 (06/07) # 1060, 420 (6/21)
        ellipse2_1m = Ellipse((470, 435), 65, 20, 0)  # 660, 490  # 405, 390 # 735, 360 
        ellipse3_1m = Ellipse((370, 430), 50, 15, 0)  # 555, 480 # 300, 390 # 635, 360
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((805, 490), 380, 100, -2) # 980, 550
        ellipse2_3m = Ellipse((470, 435), 240, 40, -2) # 660, 490
        ellipse3_3m = Ellipse((370, 430), 170, 20, -2)  # 555, 480
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((825, 520), 760, 210, -1) # 1000, 580
        ellipse2_6m = Ellipse((465, 445), 460, 60, -2) # 660, 500
        ellipse3_6m = Ellipse((365, 430), 360, 28, -2)   # 555, 480
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((825, 560), 1180, 330, -2) # 1000, 620
        ellipse2_9m = Ellipse((470, 455), 650, 80, -2) # 660, 510
        ellipse3_9m = Ellipse((370, 430), 450, 30, -2)  # 555, 480

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m]

    return(ells)
