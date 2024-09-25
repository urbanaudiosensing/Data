from matplotlib.patches import Ellipse
print("BUFFER FOR ASPED_version2")

def create_ellipse(station):
    # ----------------------------------------
    if station == "CamA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((905, 525), 80, 20, 4) #905, 525

        # 3-meter buffer
        ellipse1_3m = Ellipse((905, 525), 240, 50, 4) #905, 525

        # 6-meter buffer
        ellipse1_6m = Ellipse((905, 535), 440, 80, 4) #905, 535

        # 9-meter buffer
        ellipse1_9m = Ellipse((905, 535), 600, 130, 4)   #905, 535
    
    elif station == "CamB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((595, 420), 120, 50, 0)   # 595, 420
        ellipse2_1m = Ellipse((1325, 470), 150, 50, 3) # 1325, 470
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((595, 420), 300, 60, 0) # 595, 420
        ellipse2_3m = Ellipse((1340, 475), 400, 100, 3) # 1340, 475
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((595, 425), 600, 110, 0) # 595, 425
        ellipse2_6m = Ellipse((1390, 515), 800, 200, 5) # 1390, 515
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((590, 425), 800, 120, 0) # 590, 425
        ellipse2_9m = Ellipse((1440, 535), 1100, 300, 6) # 1440, 535

    elif station == "CamC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((845, 635), 120, 50, 2) # 845, 635

        # 3-meter buffer
        ellipse1_3m = Ellipse((845, 645), 360, 100, 2) # 845, 645

        # 6-meter buffer
        ellipse1_6m = Ellipse((845, 665), 740, 200, 2) # 845, 665

        # 9-meter buffer
        ellipse1_9m = Ellipse((815, 680), 1000, 320, 2)  # 815, 680

    elif station == "CamD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1145, 605), 120, 30, 4) # 1145, 605

        # 3-meter buffer
        ellipse1_3m = Ellipse((1145, 615), 360, 90, 4) # 1145, 615

        # 6-meter buffer
        ellipse1_6m = Ellipse((1125, 635), 740, 200, 4) # 1125, 635

        # 9-meter buffer
        ellipse1_9m = Ellipse((1065, 655), 900, 320, 4)  # 1065, 655

    elif station == "CamE":
        # 1-meter buffer
        ellipse1_1m = Ellipse((670, 520), 120, 30, 4) # 670, 520

        # 3-meter buffer
        ellipse1_3m = Ellipse((680, 530), 370, 90, 4) # 680, 530

        # 6-meter buffer
        ellipse1_6m = Ellipse((680, 560), 740, 200, 4) # 680, 560

        # 9-meter buffer
        ellipse1_9m = Ellipse((705, 605), 1000, 320, 4) # 710, 605

    elif station == "CamF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((700, 440), 100, 30, 2) # Cam F1 700, 435
        ellipse2_1m = Ellipse((1265, 495), 120, 35, 4) # Cam F2 1265, 495
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((700, 440), 200, 40, 2) # 700, 435
        ellipse2_3m = Ellipse((1265, 500), 220, 90, 4) # 1265, 500
         
        # 6-meter buffer
        ellipse1_6m = Ellipse((700, 450), 400, 120, 2) # 700, 445
        ellipse2_6m = Ellipse((1265, 530), 480, 150, 4) # 1265, 530
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((700, 450), 650, 120, 2) # 700, 445
        ellipse2_9m = Ellipse((1365, 550), 850, 220, 4) # 1365, 550
    
    
    if station in ["CamA", "CamC", "CamD", "CamE"]:
        ells = [ellipse1_1m, ellipse1_3m, ellipse1_6m, ellipse1_9m]
    else:
        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    return(ells)
