from matplotlib.patches import Ellipse
print("BUFFER FOR ASPED_version2")

def create_ellipse(station):
    # ----------------------------------------
    if station == "CamA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((770, 435), 80, 20, 4) # 770, 435

        # 3-meter buffer
        ellipse1_3m = Ellipse((770, 435), 240, 50, 4) # 770, 435

        # 6-meter buffer
        ellipse1_6m = Ellipse((770, 445), 440, 80, 4) # 770, 445

        # 9-meter buffer
        ellipse1_9m = Ellipse((770, 445), 600, 130, 4)   # 770, 445
    
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
        ellipse1_1m = Ellipse((635, 720), 120, 50, 2) # 635, 720

        # 3-meter buffer
        ellipse1_3m = Ellipse((635, 730), 360, 100, 2) # 635, 730

        # 6-meter buffer
        ellipse1_6m = Ellipse((635, 750), 740, 200, 2) # 635, 750

        # 9-meter buffer
        ellipse1_9m = Ellipse((590, 745), 1000, 330, 2)  # 605, 745

    elif station == "CamD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1030, 675), 120, 30, 4) # 1030, 675

        # 3-meter buffer
        ellipse1_3m = Ellipse((1030, 685), 360, 90, 4) # 1030, 685

        # 6-meter buffer
        ellipse1_6m = Ellipse((1000, 705), 740, 180, 4) # 1010, 705

        # 9-meter buffer
        ellipse1_9m = Ellipse((950, 725), 900, 320, 4)  # 950, 725

    elif station == "CamE":
        # 1-meter buffer
        ellipse1_1m = Ellipse((660, 530), 120, 30, 6) # 660, 530

        # 3-meter buffer
        ellipse1_3m = Ellipse((670, 540), 370, 90, 6) # 670, 540

        # 6-meter buffer
        ellipse1_6m = Ellipse((670, 570), 820, 200, 8) # 670, 570

        # 9-meter buffer
        ellipse1_9m = Ellipse((700, 615), 1100, 320, 8) # 695, 615

    elif station == "CamF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((730, 480), 100, 30, 2) # Cam F1 730, 480
        ellipse2_1m = Ellipse((1295, 515), 120, 35, 4) # Cam F2 1295, 515
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((730, 480), 200, 40, 2) # 730, 480
        ellipse2_3m = Ellipse((1295, 520), 220, 90, 4) # 1295, 520
         
        # 6-meter buffer
        ellipse1_6m = Ellipse((730, 490), 350, 120, 2) # 730, 490
        ellipse2_6m = Ellipse((1295, 550), 480, 150, 4) # 1295, 550
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((730, 490), 600, 120, 2) # 730, 490
        ellipse2_9m = Ellipse((1400, 580), 800, 220, 4) # 1395, 570
    
    
    if station in ["CamA", "CamC", "CamD", "CamE"]:
        ells = [ellipse1_1m, ellipse1_3m, ellipse1_6m, ellipse1_9m]
    else:
        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    return(ells)
