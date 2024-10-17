from matplotlib.patches import Ellipse
print("BUFFER FOR ASPED_version2")

def create_ellipse(station):
    # ----------------------------------------
    if station == "CamA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((850, 540), 80, 20, 0) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((850, 540), 240, 50, 0)

        # 6-meter buffer
        ellipse1_6m = Ellipse((850, 550), 440, 80, 0)

        # 9-meter buffer
        ellipse1_9m = Ellipse((850, 550), 600, 130, 1)  
    
    elif station == "CamB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((620, 315), 120, 50, 0)   # 620, 315
        ellipse2_1m = Ellipse((1365, 375), 150, 50, 3) # 1365, 370
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((620, 315), 300, 60, 0) # 620, 315
        ellipse2_3m = Ellipse((1380, 380), 400, 100, 3) # 1380, 375
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((620, 320), 600, 110, 0) # 620, 320
        ellipse2_6m = Ellipse((1430, 420), 800, 200, 5) # 1430, 395
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((615, 320), 800, 120, 0) # 615, 320
        ellipse2_9m = Ellipse((1480, 440), 1100, 300, 6) # 1480, 415

    elif station == "CamC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((885, 640), 120, 50, 2) # 885, 640

        # 3-meter buffer
        ellipse1_3m = Ellipse((885, 650), 360, 100, 2) # 885, 650

        # 6-meter buffer
        ellipse1_6m = Ellipse((885, 670), 740, 200, 2) # 885, 670

        # 9-meter buffer
        ellipse1_9m = Ellipse((855, 685), 1000, 320, 2)  # 855, 685

    elif station == "CamD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((990, 635), 120, 30, 4) # 990, 635

        # 3-meter buffer
        ellipse1_3m = Ellipse((990, 645), 360, 90, 4) # 990, 645

        # 6-meter buffer
        ellipse1_6m = Ellipse((970, 665), 740, 200, 4) # 970, 665

        # 9-meter buffer
        ellipse1_9m = Ellipse((910, 685), 900, 320, 4)  # 910, 685

    elif station == "CamE":
        # 1-meter buffer
        ellipse1_1m = Ellipse((470, 530), 120, 30, 4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((480, 540), 370, 90, 4) 

        # 6-meter buffer
        ellipse1_6m = Ellipse((480, 570), 740, 200, 4) 

        # 9-meter buffer
        ellipse1_9m = Ellipse((510, 615), 1000, 320, 4) 

    elif station == "CamF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((480, 530), 100, 30, 2) # Cam F1 480, 520
        ellipse2_1m = Ellipse((1050, 555), 120, 35, 4) # Cam F2 1050, 555
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((480, 530), 200, 40, 2) # 480, 520
        ellipse2_3m = Ellipse((1050, 560), 220, 90, 4) # 1050, 560
         
        # 6-meter buffer
        ellipse1_6m = Ellipse((480, 540), 400, 120, 2) # 480, 530
        ellipse2_6m = Ellipse((1050, 590), 480, 150, 4) # 1050, 590
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((480, 540), 650, 120, 2) # 480, 530
        ellipse2_9m = Ellipse((1150, 610), 850, 220, 4) # 1150, 610
    
    
    if station in ["CamA", "CamC", "CamD", "CamE"]:
        ells = [ellipse1_1m, ellipse1_3m, ellipse1_6m, ellipse1_9m]
    else:
        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    return(ells)
