
###########################
# Created by Eric Davidson
# 6/30/19
###########################

line_count = 25
line_width = 800
line_sep = 30

circle_count = 100
circle_size = 10
circle_chance = .7

line_weight = 1

w = line_width+(line_width/4)
h = (line_count-1)*line_sep + (line_width/4)

ran_mov = 2

# Color Palettes
colors = [(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)]

def setup():
    # Set up the image
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    # Take advantage of retina display
    pixelDensity(2)
    
    # Color in the background (May add the background to palette)
    background(208, 200, 176)
    stroke(0)
    
    # Start the drawing based on line width 
    x_start = line_width/8
    y_start = line_width/8

    # Thicker
    strokeWeight(line_weight)
    
    for i in range(line_count):
        
        # We don't want to fill in the curves
        noFill()
        
        # Start the curve vertex
        beginShape()
        
        for j in range(0, line_width, line_width/circle_count):
            # Coordinates are calculated at circle centers essentially
            x_coord = x_start+j
            y_coord = y_start + (i*line_sep) + random(-ran_mov, ran_mov)
            
            curveVertex(x_coord, y_coord)
            
            # Circle Time
            prob = random(1)
            if (prob < circle_chance):
                c = colors[int(random(len(colors)))]
                fill(c[0], c[1], c[2], 255)
                circle(x_coord, y_coord, circle_size)
            noFill()
            
        # Draw the curvy line
        endShape()
        
    # Generate a 'seed' just to distinguish image files
    seed = int(random(600))
    
    # Save the image with line count and 'seed'
    save("Examples/Oblong-" + str(line_count) + "-" + str(seed) + ".png")
    
    # Only need to draw once
    noLoop()
    
def draw():
    image(img, 0, 0)
