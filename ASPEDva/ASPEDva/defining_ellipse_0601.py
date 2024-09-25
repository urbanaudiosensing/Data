from matplotlib.patches import Ellipse

def create_ellipse(station):
    # ----------------------------------------
    if station == "Cadell":
        # 1-meter buffer
        ellipse1_1m = Ellipse((760, 470), 70, 40, 0) 
        ellipse2_1m = Ellipse((900, 350), 70, 20, 0) 
        ellipse3_1m = Ellipse((1215, 580), 80, 40, 4) 
        ellipse4_1m = Ellipse((730, 300), 65, 20, 0) 
        ellipse5_1m = Ellipse((905, 315), 60, 20, 0) 
        ellipse6_1m = Ellipse((1570, 540), 90, 35, 4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((760, 470), 200, 90, 0)
        ellipse2_3m = Ellipse((900, 350), 140, 40, 0)
        ellipse3_3m = Ellipse((1215, 580), 270, 140, 4)
        ellipse4_3m = Ellipse((730, 300), 110, 40, 0)
        ellipse5_3m = Ellipse((905, 315), 120, 40, 0)
        ellipse6_3m = Ellipse((1570, 540), 250, 90, 6)

        # 6-meter buffer
        ellipse1_6m = Ellipse((760, 495), 400, 180, 0)
        ellipse2_6m = Ellipse((900, 355), 280, 80, 0)
        ellipse3_6m = Ellipse((1215, 630), 500, 280, 4)
        ellipse4_6m = Ellipse((730, 300), 220, 80, 0)
        ellipse5_6m = Ellipse((905, 320), 260, 80, 0)
        ellipse6_6m = Ellipse((1570, 560), 500, 200, 6)

        # 9-meter buffer
        ellipse1_9m = Ellipse((760, 505), 660, 280, 0)
        ellipse2_9m = Ellipse((900, 355), 420, 115, 0)
        ellipse3_9m = Ellipse((1215, 665), 880, 400, 4)
        ellipse4_9m = Ellipse((730, 300), 330, 105, 0)
        ellipse5_9m = Ellipse((905, 320), 380, 100, 0)
        ellipse6_9m = Ellipse((1570, 590), 750, 380, 6)   

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse4_1m, ellipse5_1m, ellipse6_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse4_3m, ellipse5_3m, ellipse6_3m,
            ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse4_6m, ellipse5_6m, ellipse6_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m, ellipse4_9m, ellipse5_9m, ellipse6_9m]

    
    elif station == "TechwayD":   
        # 1-meter buffer
        ellipse1_1m = Ellipse((335, 680), 65, 30, 0) 
        ellipse2_1m = Ellipse((570, 530), 35, 20, 1) 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((335, 680), 210, 53, 1.0) # 335, 680
        ellipse2_3m = Ellipse((570, 530), 150, 40, 1) # 570, 530
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((345, 680), 480, 125, 1.0) # 345, 680
        ellipse2_6m = Ellipse((585, 530), 280, 70, 1) # 585, 530
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((375, 680), 620, 180, 1) # 375, 680
        ellipse2_9m = Ellipse((595, 530), 400, 105, 1) # 595, 530

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1295, 470), 160, 35, 3.8) # 1295, 470 
        ellipse2_1m = Ellipse((1000, 405), 60, 25, 2)  # 1000, 405
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1295, 480), 450, 80, 3.5) # 1295, 480
        ellipse2_3m = Ellipse((995, 415), 220, 30, 1.5) # 995, 415
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1295, 500), 700, 110, 3) # 1295, 500
        ellipse2_6m = Ellipse((995, 410), 350, 40, 1) # 995, 410
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1295, 510), 900, 230, 3) # 1295, 510
        ellipse2_9m = Ellipse((1000, 405), 500, 55, 1) # 995, 405

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayB":  
        # 1-meter buffer
        ellipse1_1m = Ellipse((1280, 490), 80, 20, 2) 
        ellipse2_1m = Ellipse((1020, 460), 40, 15, 0) 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1280, 490), 260, 30, 2) 
        ellipse2_3m = Ellipse((1020, 460), 175, 25, 0)
         
        # 6-meter buffer
        ellipse1_6m = Ellipse((1280, 490), 500, 70, 2) 
        ellipse2_6m = Ellipse((1020, 465), 300, 30, 0) 
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1280, 510), 740, 130, 2) 
        ellipse2_9m = Ellipse((1020, 465), 500, 45, 2) 

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayA":  ### Not 6/1 
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
