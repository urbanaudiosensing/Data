from matplotlib.patches import Ellipse

def create_ellipse(station):
    # ----------------------------------------
    if station == "Cadell":
        # 1-meter buffer
        ellipse1_1m = Ellipse((775, 305), 70, 40, 0) # 775, 305
        ellipse2_1m = Ellipse((910, 185), 70, 20, 0) # 910, 185
        ellipse3_1m = Ellipse((1235, 415), 80, 40, 4) # 1235, 415
        ellipse4_1m = Ellipse((705, 165), 65, 20, 0) # 705, 165
        ellipse5_1m = Ellipse((920, 155), 60, 20, 0) # 920, 155
        ellipse6_1m = Ellipse((1600, 390), 90, 35, 4) # 1600, 390

        # 3-meter buffer
        ellipse1_3m = Ellipse((775, 305), 200, 90, 0) # 775, 305
        ellipse2_3m = Ellipse((910, 185), 140, 40, 0) # 910, 185
        ellipse3_3m = Ellipse((1235, 415), 270, 140, 4) # 1235, 415
        ellipse4_3m = Ellipse((705, 165), 110, 40, 0) # 705, 165
        ellipse5_3m = Ellipse((920, 155), 120, 40, 0) # 920, 155
        ellipse6_3m = Ellipse((1600, 390), 250, 90, 6) # 1600, 390

        # 6-meter buffer
        ellipse1_6m = Ellipse((775, 325), 400, 180, 0) # 775, 325
        ellipse2_6m = Ellipse((910, 190), 280, 80, 0) # 910, 190
        ellipse3_6m = Ellipse((1235, 465), 500, 280, 4) # 1235, 465
        ellipse4_6m = Ellipse((705, 165), 220, 80, 0) # 705, 165
        ellipse5_6m = Ellipse((920, 160), 260, 80, 0) # 920, 160
        ellipse6_6m = Ellipse((1600, 410), 500, 200, 6) # 1600, 410

        # 9-meter buffer
        ellipse1_9m = Ellipse((775, 335), 660, 280, 0) # 775, 335
        ellipse2_9m = Ellipse((910, 190), 420, 115, 0) # 910, 190
        ellipse3_9m = Ellipse((1235, 500), 880, 400, 4) # 1235, 500
        ellipse4_9m = Ellipse((705, 165), 330, 105, 0) # 705, 165
        ellipse5_9m = Ellipse((920, 160), 380, 100, 0) # 920, 160
        ellipse6_9m = Ellipse((1600, 440), 750, 380, 6) # 1600, 440

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse4_1m, ellipse5_1m, ellipse6_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse4_3m, ellipse5_3m, ellipse6_3m,
            ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse4_6m, ellipse5_6m, ellipse6_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m, ellipse4_9m, ellipse5_9m, ellipse6_9m]
        
    
    elif station == "TechwayD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((350, 660), 65, 30, 0) # 350, 660
        ellipse2_1m = Ellipse((585, 510), 35, 20, 1)  # 585, 510
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((350, 660), 210, 53, 1.0) # 350, 660
        ellipse2_3m = Ellipse((585, 510), 150, 40, 1)  # 585, 510
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((360, 660), 480, 125, 1.0) # 360, 660
        ellipse2_6m = Ellipse((600, 510), 280, 70, 1)  # 600, 510
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((395, 660), 620, 180, 1) # 395, 660
        ellipse2_9m = Ellipse((605, 510), 400, 105, 1) # 605, 510

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1645, 645), 160, 35, 3.8) # 1645, 645
        ellipse2_1m = Ellipse((1345, 560), 60, 25, 2)  # 1345, 560
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1645, 655), 450, 80, 3.5) # 1645, 655
        ellipse2_3m = Ellipse((1340, 570), 220, 30, 1.5) # 1340, 570
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1645, 675), 900, 110, 3) # 1645, 675
        ellipse2_6m = Ellipse((1340, 565), 350, 40, 1) # 1340, 565
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1645, 685), 1200, 230, 3) # 1645, 685
        ellipse2_9m = Ellipse((1345, 560), 600, 55, 1) # 1345, 560

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1270, 500), 80, 20, 2) # 1270, 500
        ellipse2_1m = Ellipse((1015, 445), 40, 15, 0)  # 1015, 445
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1270, 500), 260, 30, 2) # 1270, 500
        ellipse2_3m = Ellipse((1015, 445), 175, 25, 0) # 1015, 445
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1270, 500), 550, 70, 2) # 1270, 500
        ellipse2_6m = Ellipse((1015, 450), 330, 30, 0) # 1015, 450
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1270, 520), 900, 130, 2) # 1270, 520
        ellipse2_9m = Ellipse((1015, 450), 500, 45, 2) # 1015, 450

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1060, 430), 180, 50, 2) # 1060, 420 
        ellipse2_1m = Ellipse((735, 370), 65, 20, 0)  # 735, 360 
        ellipse3_1m = Ellipse((635, 360), 50, 15, 0)  # 635, 360
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1060, 435), 380, 100, -2) # 1060, 430
        ellipse2_3m = Ellipse((735, 370), 240, 40, -2) # 735, 360
        ellipse3_3m = Ellipse((635, 360), 170, 20, -2)  # 635, 360
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1080, 460), 760, 210, -1) # 1080, 460
        ellipse2_6m = Ellipse((730, 370), 460, 60, -2) # 730, 370
        ellipse3_6m = Ellipse((630, 360), 360, 28, -2)   # 630, 360
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1080, 500), 1180, 330, -1) # 1080, 500
        ellipse2_9m = Ellipse((735, 380), 650, 80, -2) # 735, 380
        ellipse3_9m = Ellipse((635, 360), 450, 30, -2)  # 635, 360

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m]

    return(ells)
