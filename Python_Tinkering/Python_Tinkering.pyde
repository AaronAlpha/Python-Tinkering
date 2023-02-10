xCenter = 0
yCenter = 0


def setup():
    size(500, 500)
    global xCenter = width/2
    global yCenter = height/2 
    

def draw():
    
    rect(xCenter - xCenter*1/2, yCenter - yCenter*1/2, xCenter/2, yCenter/2)
    
