from matplotlib.patches import Ellipse
print("BUFFER FOR ASPED_version2")

def create_ellipse(station):
    # ----------------------------------------
    if station == "CamA":
        # 1-meter buffer
        ellipse1_1m = Ellipse((840, 450), 80, 20, 0) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((840, 450), 240, 50, 0)

        # 6-meter buffer
        ellipse1_6m = Ellipse((840, 460), 440, 80, 0)

        # 9-meter buffer
        ellipse1_9m = Ellipse((840, 460), 600, 130, 1)  
    
    elif station == "CamB":
        # 1-meter buffer
        ellipse1_1m = Ellipse((640, 425), 120, 50, 0)
        ellipse2_1m = Ellipse((1385, 475), 150, 50, 0) 
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((640, 425), 300, 60, 0)
        ellipse2_3m = Ellipse((1400, 480), 400, 100, 3) 
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((640, 430), 600, 110, 0)
        ellipse2_6m = Ellipse((1450, 500), 800, 170, 3) 
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((635, 430), 800, 120, 0)
        ellipse2_9m = Ellipse((1500, 520), 1100, 280, 3)

    elif station == "CamC":
        # 1-meter buffer
        ellipse1_1m = Ellipse((820, 595), 120, 30, -4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((820, 605), 360, 90, -8)

        # 6-meter buffer
        ellipse1_6m = Ellipse((820, 625), 740, 200, -8)

        # 9-meter buffer
        ellipse1_9m = Ellipse((790, 640), 1000, 320, -8)  

    elif station == "CamD":
        # 1-meter buffer
        ellipse1_1m = Ellipse((1130, 590), 120, 30, 4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((1130, 600), 360, 90, 4)

        # 6-meter buffer
        ellipse1_6m = Ellipse((1110, 620), 740, 200, 4)

        # 9-meter buffer
        ellipse1_9m = Ellipse((1050, 640), 900, 320, 4)  

    elif station == "CamE":
        # 1-meter buffer
        ellipse1_1m = Ellipse((615, 510), 120, 30, 4) 

        # 3-meter buffer
        ellipse1_3m = Ellipse((625, 520), 370, 90, 4)

        # 6-meter buffer
        ellipse1_6m = Ellipse((625, 540), 740, 200, 4)

        # 9-meter buffer
        ellipse1_9m = Ellipse((655, 585), 1000, 320, 4)  

    elif station == "CamF":
        # 1-meter buffer
        ellipse1_1m = Ellipse((485, 460), 100, 30, 2) # Cam F1
        ellipse2_1m = Ellipse((1050, 495), 120, 35, 4) # Cam F2
        
        # 3-meter buffer
        ellipse1_3m = Ellipse((485, 460), 200, 40, 2)
        ellipse2_3m = Ellipse((1050, 500), 220, 90, 4)
        
        # 6-meter buffer
        ellipse1_6m = Ellipse((485, 470), 400, 120, 2)
        ellipse2_6m = Ellipse((1050, 535), 480, 150, 4)
        
        # 9-meter buffer
        ellipse1_9m = Ellipse((485, 480), 650, 120, 2)
        ellipse2_9m = Ellipse((1150, 555), 850, 220, 4)    
    
    
    if station in ["CamA", "CamC", "CamD", "CamE"]:
        ells = [ellipse1_1m, ellipse1_3m, ellipse1_6m, ellipse1_9m]
    else:
        ells = [ellipse1_1m, ellipse2_1m, ellipse1_3m, ellipse2_3m, ellipse1_6m, ellipse2_6m, ellipse1_9m, ellipse2_9m]

    return(ells)
