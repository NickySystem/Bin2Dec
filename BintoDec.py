import pygame, os, sys, time

#pd
#pdpath = "c:\users\haln\desktop\coding\pd\bin\"

#arrays
array1 = [0,0,0,0,0,0,0,0]
array1Add = [0,0,0,0,0,0,0,0]

array2 = [0,0,0,0,0,0,0,0]
array2Add = [0,0,0,0,0,0,0,0]

binArray = [128,64,32,16,8,4,2,1]

# Initialize pygame
pygame.init()

def mouseProcess():
    #check the mouse position when clicked for collisions with images and text
    
    # array 1 buttons
    if (event.pos[0] > 20 and event.pos[0] < 45) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[0] = (array1[0]+1)%2
                
    if (event.pos[0] > 45 and event.pos[0] < 70) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[1] = (array1[1]+1)%2
    
    if (event.pos[0] > 70 and event.pos[0] < 95) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[2] = (array1[2]+1)%2
                
    if (event.pos[0] > 95 and event.pos[0] < 120) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[3] = (array1[3]+1)%2
                
    if (event.pos[0] > 120 and event.pos[0] < 145) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[4] = (array1[4]+1)%2
                
    if (event.pos[0] > 145 and event.pos[0] < 170) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[5] = (array1[5]+1)%2
                
    if (event.pos[0] > 170 and event.pos[0] < 195) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[6] = (array1[6]+1)%2
                
    if (event.pos[0] > 195 and event.pos[0] < 215) and (event.pos[1] > 100 and event.pos[1]<136):
                array1[7] = (array1[7]+1)%2
                
                
    # array 1 buttons
    if (event.pos[0] > 20 and event.pos[0] < 45) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[0] = (array2[0]+1)%2
                
    if (event.pos[0] > 45 and event.pos[0] < 70) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[1] = (array2[1]+1)%2
    
    if (event.pos[0] > 70 and event.pos[0] < 95) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[2] = (array2[2]+1)%2
                
    if (event.pos[0] > 95 and event.pos[0] < 120) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[3] = (array2[3]+1)%2
                
    if (event.pos[0] > 120 and event.pos[0] < 145) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[4] = (array2[4]+1)%2
                
    if (event.pos[0] > 145 and event.pos[0] < 170) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[5] = (array2[5]+1)%2
                
    if (event.pos[0] > 170 and event.pos[0] < 195) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[6] = (array2[6]+1)%2
                
    if (event.pos[0] > 195 and event.pos[0] < 215) and (event.pos[1] > 200 and event.pos[1]<236):
                array2[7] = (array2[7]+1)%2
    
                
def array1Graphics():
    if array1[0] == 0:
        screen.blit(zeroImg,(20,100))
        screen.blit(offImg,(20,150))
    else:
        screen.blit(oneImg,(20,100))
        screen.blit(onImg,(20,150))
        
    if array1[1] == 0:
        screen.blit(zeroImg,(45,100))
        screen.blit(offImg,(45,150))
    else:
        screen.blit(oneImg,(45,100))
        screen.blit(onImg,(45,150))
        
    if array1[2] == 0:
        screen.blit(zeroImg,(70,100))
        screen.blit(offImg,(70,150))
    else:
        screen.blit(oneImg,(70,100))
        screen.blit(onImg,(70,150))
        
    if array1[3] == 0:
        screen.blit(zeroImg,(95,100))
        screen.blit(offImg,(95,150))
    else:
        screen.blit(oneImg,(95,100))
        screen.blit(onImg,(95,150))

    if array1[4] == 0:
        screen.blit(zeroImg,(120,100))
        screen.blit(offImg,(120,150))
    else:
        screen.blit(oneImg,(120,100))
        screen.blit(onImg,(120,150))
        
    if array1[5] == 0:
        screen.blit(zeroImg,(145,100))
        screen.blit(offImg,(145,150))
    else:
        screen.blit(oneImg,(145,100))
        screen.blit(onImg,(145,150))
        
    if array1[6] == 0:
        screen.blit(zeroImg,(170,100))
        screen.blit(offImg,(170,150))
    else:
        screen.blit(oneImg,(170,100))
        screen.blit(onImg,(170,150))
        
    if array1[7] == 0:
        screen.blit(zeroImg,(195,100))
        screen.blit(offImg,(195,150))
    else:
        screen.blit(oneImg,(195,100))
        screen.blit(onImg,(195,150))
        
def array2Graphics():
    if array2[0] == 0:
        screen.blit(zeroImg,(20,200))
        screen.blit(offImg,(20,250))
    else:
        screen.blit(oneImg,(20,200))
        screen.blit(onImg,(20,250))
        
    if array2[1] == 0:
        screen.blit(zeroImg,(45,200))
        screen.blit(offImg,(45,250))
    else:
        screen.blit(oneImg,(45,200))
        screen.blit(onImg,(45,250))
        
    if array2[2] == 0:
        screen.blit(zeroImg,(70,200))
        screen.blit(offImg,(70,250))
    else:
        screen.blit(oneImg,(70,200))
        screen.blit(onImg,(70,250))
        
    if array2[3] == 0:
        screen.blit(zeroImg,(95,200))
        screen.blit(offImg,(95,250))
    else:
        screen.blit(oneImg,(95,200))
        screen.blit(onImg,(95,250))

    if array2[4] == 0:
        screen.blit(zeroImg,(120,200))
        screen.blit(offImg,(120,250))
    else:
        screen.blit(oneImg,(120,200))
        screen.blit(onImg,(120,250))
        
    if array2[5] == 0:
        screen.blit(zeroImg,(145,200))
        screen.blit(offImg,(145,250))
    else:
        screen.blit(oneImg,(145,200))
        screen.blit(onImg,(145,250))
        
    if array2[6] == 0:
        screen.blit(zeroImg,(170,200))
        screen.blit(offImg,(170,250))
    else:
        screen.blit(oneImg,(170,200))
        screen.blit(onImg,(170,250))
        
    if array2[7] == 0:
        screen.blit(zeroImg,(195,200))
        screen.blit(offImg,(195,250))
    else:
        screen.blit(oneImg,(195,200))
        screen.blit(onImg,(195,250))


def array1Addition():
    global array1
    global array1Add
    global array2
    global array2Add
    
    for x in range(8):
        if array1[x] == 1:
            array1Add[x] = binArray[x]
        else: array1Add[x] = 0
    
    for x in range(8):
        if array2[x] == 1:
            array2Add[x] = binArray[x]
        else: array2Add[x] = 0
    
    array1Text = font2.render(str(sum(array1Add)), True, (255,163,214))
    screen.blit(array1Text,(250,88))
    array2Text = font2.render(str(sum(array2Add)), True, (255,163,214))
    screen.blit(array2Text,(250,188))
    
# Set the height and width of the screen
size = [600, 300]
screen = pygame.display.set_mode(size)


#window caption & icon & font
pygame.display.set_caption("Garden - Dec2Bin")
pygame_icon = pygame.image.load('images/ico.png')
pygame.display.set_icon(pygame_icon)
font1 = pygame.font.Font('fonts/rainyhearts.ttf', 32)
font2 = pygame.font.Font('fonts/rainyhearts.ttf', 64)

#load images
zeroImg = pygame.image.load('images/0.png').convert_alpha()
oneImg = pygame.image.load('images/1.png').convert_alpha()
onImg = pygame.image.load('images/on.png').convert_alpha()
offImg = pygame.image.load('images/off.png').convert_alpha()
vine = pygame.image.load('images/vinetest.png').convert_alpha()
    
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseProcess()
            
        if event.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())
           
    
    # Clear the screen and set the screen background
    screen.fill((103,69,119))
    
    title = font1.render('Garden - Dec2Bin', True, (255,163,214))
    screen.blit(title,(20,20))  
    pygame.draw.line(screen, (100,185,202), [18, 55], [238,55], 2)
    
    screen.blit(vine,(300,0))
    
    #pygame.draw.line(screen, (100,185,202), [18, 300], [582,300], 2)
    
    array1Graphics()
    array2Graphics()
    
    array1Addition()
    
    mpos = pygame.mouse.get_pos() # Get mouse position
    
    pygame.display.flip()
    
    
# Be IDLE friendly
pygame.quit()