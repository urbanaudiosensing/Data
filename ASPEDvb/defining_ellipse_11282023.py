from matplotlib.patches import Ellipse
print("BUFFER FOR ASPED_version2")

def create_ellipse(station):
    # ----------------------------------------
    if station == "CamA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((820, 500), 80, 20, 4) # 820, 490

        # 3-meter buffer
        ellipse1_3m = Ellipse((820, 500), 240, 50, 4) # 820, 490

        # 6-meter buffer
        ellipse1_6m = Ellipse((820, 510), 440, 80, 4) # 820, 500

        # 9-meter buffer
        ellipse1_9m = Ellipse((820, 510), 600, 130, 4)   # 820, 500
    
    elif station == "CamB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((535, 420), 120, 50, 0)   # 535, 420
        ellipse2_1m = Ellipse((1260, 490), 150, 50, 3) # 1260, 490
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((535, 420), 300, 60, 0) # 535, 420
        ellipse2_3m = Ellipse((1275, 495), 400, 100, 3) # 1275, 495
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((535, 425), 600, 110, 0) # 535, 425
        ellipse2_6m = Ellipse((1325, 535), 800, 200, 5) # 1325, 535
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((530, 425), 800, 120, 0) # 530, 425
        ellipse2_9m = Ellipse((1375, 555), 1100, 300, 6) # 1375, 555

    elif station == "CamC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((720, 670), 120, 50, 2) # 720, 670

        # 3-meter buffer
        ellipse1_3m = Ellipse((720, 680), 360, 100, 2) # 720, 680

        # 6-meter buffer
        ellipse1_6m = Ellipse((720, 700), 740, 200, 2) # 720, 700

        # 9-meter buffer
        ellipse1_9m = Ellipse((675, 695), 1000, 330, 2)  # 675, 695

    elif station == "CamD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1140, 430), 120, 30, 4) # 1140, 430

        # 3-meter buffer
        ellipse1_3m = Ellipse((1140, 440), 360, 90, 4) # 1140, 440

        # 6-meter buffer
        ellipse1_6m = Ellipse((1110, 460), 740, 180, 4) # 1110, 460

        # 9-meter buffer
        ellipse1_9m = Ellipse((1100, 480), 900, 320, 4)  # 1060, 480

    elif station == "CamE":
        # 1-meter buffer
        ellipse1_1m = Ellipse((575, 490), 120, 30, 6) # 575, 490

        # 3-meter buffer
        ellipse1_3m = Ellipse((585, 500), 370, 90, 6) # 585, 500

        # 6-meter buffer
        ellipse1_6m = Ellipse((585, 530), 820, 200, 8) # 585, 530

        # 9-meter buffer
        ellipse1_9m = Ellipse((615, 575), 1100, 320, 8) # 615, 575

    elif station == "CamF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((735, 470), 100, 30, 2) # Cam F1 735, 470
        ellipse2_1m = Ellipse((1295, 515), 120, 35, 4) # Cam F2 1295, 515
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((735, 470), 200, 40, 2) # 735, 470
        ellipse2_3m = Ellipse((1295, 520), 220, 90, 4) # 1295, 520
         
        # 6-meter buffer
        ellipse1_6m = Ellipse((735, 480), 350, 120, 2) # 735, 480
        ellipse2_6m = Ellipse((1295, 550), 480, 150, 4) # 1295, 550
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((735, 480), 600, 120, 2) # 735, 480
        ellipse2_9m = Ellipse((1400, 580), 800, 220, 4) # 1395, 570
    
    
    if station in ["CamA", "CamC", "CamD", "CamE"]:
        ells = [ellipse1_1m, ellipse1_3m, ellipse1_6m, ellipse1_9m]
    else:
        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    return(ells)
