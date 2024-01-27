from matplotlib.patches import Ellipse

def create_ellipse(station):
    # ----------------------------------------
    if station == "Cadell": 
        # 1-meter buffer
        ellipse1_1m = Ellipse((790, 425), 70, 40, 0) 
        ellipse2_1m = Ellipse((930, 310), 70, 20, 0) 
        ellipse3_1m = Ellipse((1240, 550), 80, 40, 4) 
        ellipse4_1m = Ellipse((760, 260), 65, 20, 0) 
        ellipse5_1m = Ellipse((935, 275), 60, 20, 0) 
        ellipse6_1m = Ellipse((1610, 515), 90, 35, 4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((790, 425), 200, 90, 0) # 790, 425
        ellipse2_3m = Ellipse((930, 310), 140, 40, 0) # 930, 310
        ellipse3_3m = Ellipse((1240, 550), 270, 140, 4) # 1240, 550
        ellipse4_3m = Ellipse((760, 260), 110, 40, 0) # 760, 260
        ellipse5_3m = Ellipse((935, 275), 120, 40, 0) # 935, 275
        ellipse6_3m = Ellipse((1610, 515), 250, 90, 6) # 1610, 515

        # 6-meter buffer
        ellipse1_6m = Ellipse((790, 445), 400, 180, 0) # 790, 445
        ellipse2_6m = Ellipse((930, 315), 280, 80, 0) # 930, 315
        ellipse3_6m = Ellipse((1240, 600), 500, 280, 4) # 1240, 600
        ellipse4_6m = Ellipse((760, 260), 220, 80, 0) # 760, 260
        ellipse5_6m = Ellipse((935, 280), 260, 80, 0) # 935, 280
        ellipse6_6m = Ellipse((1610, 535), 500, 200, 6) # 1610, 535

        # 9-meter buffer
        ellipse1_9m = Ellipse((790, 455), 660, 280, 0) # 790, 455
        ellipse2_9m = Ellipse((930, 310), 420, 115, 0) # 930, 310
        ellipse3_9m = Ellipse((1240, 635), 880, 400, 4) # 1240, 635
        ellipse4_9m = Ellipse((760, 260), 330, 105, 0) # 760, 260
        ellipse5_9m = Ellipse((935, 280), 380, 100, 0) # 935, 280
        ellipse6_9m = Ellipse((1610, 565), 750, 380, 6) # 1610, 565  

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse4_1m, ellipse5_1m, ellipse6_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse4_3m, ellipse5_3m, ellipse6_3m,
            ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse4_6m, ellipse5_6m, ellipse6_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m, ellipse4_9m, ellipse5_9m, ellipse6_9m]

    
    elif station == "TechwayD": 
        # 1-meter buffer
        ellipse1_1m = Ellipse((365, 490), 65, 30, 0) # 370, 650 (05/24) #335, 680 # 365, 490 (06/07)
        ellipse2_1m = Ellipse((600, 330), 35, 20, 1)  # 605, 495 # 570, 530 # 600, 330 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((365, 490), 210, 53, 1.0) # 365, 490
        ellipse2_3m = Ellipse((600, 330), 150, 40, 1) # 600, 330
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((375, 490), 480, 125, 1.0) # 375, 490
        ellipse2_6m = Ellipse((615, 330), 280, 70, 1) # 615, 330
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((410, 490), 620, 180, 1) # 410, 490
        ellipse2_9m = Ellipse((625, 330), 400, 105, 1) # 625, 330

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayC": ### Not 6/7
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
        ellipse1_1m = Ellipse((1355, 465), 80, 20, 2) 
        ellipse2_1m = Ellipse((1090, 400), 40, 15, 0)  
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((1355, 460), 260, 30, 2) 
        ellipse2_3m = Ellipse((1090, 400), 175, 25, 0) 
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((1345, 460), 520, 70, 2) 
        ellipse2_6m = Ellipse((1090, 405), 300, 30, 0) 
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((1335, 480), 850, 130, 2)
        ellipse2_9m = Ellipse((1090, 405), 500, 45, 2) 

        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    elif station == "TechwayA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((745, 425), 180, 50, 2) 
        ellipse2_1m = Ellipse((405, 390), 65, 20, 0) 
        ellipse3_1m = Ellipse((300, 390), 50, 15, 0)  

        # 3-meter buffer
        ellipse1_3m = Ellipse((745, 435), 380, 100, -2) 
        ellipse2_3m = Ellipse((405, 390), 240, 40, -2) 
        ellipse3_3m = Ellipse((300, 390), 170, 20, -2)  
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((765, 465), 760, 210, -1) 
        ellipse2_6m = Ellipse((400, 400), 460, 60, -2) 
        ellipse3_6m = Ellipse((295, 390), 360, 28, -2)   
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((765, 505), 1180, 330, -2) 
        ellipse2_9m = Ellipse((410, 410), 650, 80, -2) 
        ellipse3_9m = Ellipse((300, 390), 450, 30, -2)  

        ells = [ellipse1_1m, ellipse2_1m, ellipse3_1m, ellipse1_3m, ellipse2_3m, ellipse3_3m, ellipse1_6m, ellipse2_6m, ellipse3_6m, ellipse1_9m, ellipse2_9m, ellipse3_9m]

    return(ells)
