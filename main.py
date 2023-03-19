import pygame
import random
import os
import math
from pygame.event import *
from pygame.locals import *
from pygame import font
# Global Variables
clicked=False
start=True
action_start=False
action_exit=False
action_quit=False
action_play=False
highscorerun=False
running = False
rule=False
# Initializing Pygame
pygame.init()

# Creating display
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders Deluxe")  # Setting Caption

#Giving Icon to window
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Giving Background
background=pygame.image.load('images\space.jpg')
background=pygame.transform.scale(background,(800,600))

# Making Buttons
font1 = font.Font('freesansbold.ttf' or None, 20)
fontmenu = font.Font('freesansbold.ttf', 40)
button_col = (255, 0, 0)
hover_col = (75, 225, 255)
click_col = (50, 150, 255)
text_col = (0,0,0)
width = 120
height = 40
widthmenu=180
heightmenu=80
# Play again button
def playagain():
    x=210
    y=320
    global clicked,action_play
    action_play = False
    button_rect = Rect(x,y, width, height)
    if button_rect.collidepoint(pos):
	    if pygame.mouse.get_pressed()[0] == 1:
		    clicked = True
		    pygame.draw.rect(screen, click_col, button_rect)
	    elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
		    clicked = False
		    action_play = True
	    else:
		    pygame.draw.rect(screen, hover_col, button_rect)
    else:
	    pygame.draw.rect(screen, button_col, button_rect)

    pygame.draw.line(screen, (255,255,255), (x, y), (x + width, y), 2)
    pygame.draw.line(screen, (255,255,255), (x,y), (x, y + height), 2)
    pygame.draw.line(screen, (0,0,0), (x, y + height), (x + width, y + height), 2)
    pygame.draw.line(screen, (0,0,0), (x + width, y), (x + width,y + height), 2)
    text_img = font1.render(" Play Again ", True, text_col)
    text_len = text_img.get_width()
    screen.blit(text_img, (x + int(width / 2) - int(text_len / 2), y + 15))
    return action_play
# Exit button
def exit():
    x=450
    y=320
    global clicked
    global action_exit
    global running
    action_exit = False
    button_rect = Rect(x,y, width, height)
    if button_rect.collidepoint(pos):
	    if pygame.mouse.get_pressed()[0] == 1:
		    clicked = True
		    pygame.draw.rect(screen, click_col, button_rect)
	    elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
		    clicked = False
		    action_exit = True
	    else:
		    pygame.draw.rect(screen, hover_col, button_rect)
    else:
	    pygame.draw.rect(screen, button_col, button_rect)

    pygame.draw.line(screen, (255,255,255), (x, y), (x + width, y), 2)
    pygame.draw.line(screen, (255,255,255), (x,y), (x, y + height), 2)
    pygame.draw.line(screen, (0,0,0), (x, y + height), (x + width, y + height), 2)
    pygame.draw.line(screen, (0,0,0), (x + width, y), (x + width,y + height), 2)
    text_img = font1.render(" Exit ", True, text_col)
    text_len = text_img.get_width()
    screen.blit(text_img, (x + int(width / 2) - int(text_len / 2), y + 15))
    if action_exit:
        running=False
    return action_exit


    
# Background Sound
sound_background=pygame.mixer.Sound("background.wav")
sound_background.set_volume(0.09)
sound_background.play(-1)
# Score
score_value=0
font123 = font.Font("freesansbold.ttf",32)
text_x=10
text_y=10
def score(s_x,s_y):
    score=font123.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(s_x,s_y))
# High score
font_highscore=font.Font("freesansbold.ttf",32)
high_x=10
high_y=50
# Game Over
gameover = font.Font("freesansbold.ttf",80)
over_x=180
over_y=230
def game_over_text():
    game1=gameover.render("Game Over",True,(255,255,255))
    game=gameover.render("Game Over",True,(255,0,0))
    screen.blit(game1,(over_x,over_y))
    screen.blit(game,(over_x-5,over_y))

# Making Levels
level=1
def levels():
    global score_value,level
    levelis=font123.render('Level : '+str(level),True,(255,255,255))
    screen.blit(levelis,(360,10))
    if score_value==0:
        level=1
    elif score_value>50 and score_value<100:
        level=2
    elif score_value>120:
        level=3
# Creating Player
playerimg=pygame.image.load("arcade-game.png")
playerx=370
playery=480
changex=0
changey=0
def player(x,y):
    screen.blit(playerimg,(x,y))

# Creating Bullet
bullet=pygame.image.load('bullet.png')
bulletx=0
bullety=0
bulletxchange=0
bulletychange=0.9
bulletstate="ready"
def fire(i,j):
    global bulletstate
    # bulletstate='fire'
    screen.blit(bullet,(i,j))
# Creating Enemies
enemy1=[]
enemyx=[]
enemyy=[]
changeex=[]
changeey=[]
number_of_enemies=8
for i in range(number_of_enemies):
    enemy1.append(pygame.image.load("alien2.png"))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    changeex.append(0.4)
    changeey.append(30)
def enemy(enemyimage,x1,y1):
    screen.blit(enemyimage,(x1,y1))
#Enemy 2
enemy2=[]
enemyx2=[]
enemyy2=[]
changeex2=[]
changeey2=[]
number_of_enemies2=5
for i in range(number_of_enemies2):
    enemy2.append(pygame.image.load("alien.png"))
    enemyx2.append(random.randint(0,735))
    enemyy2.append(random.randint(50,150))
    changeex2.append(0.5)
    changeey2.append(30)
#Enemy 3
enemy3=[]
enemyx3=[]
enemyy3=[]
changeex3=[]
changeey3=[]
number_of_enemies3=4
for i in range(number_of_enemies3):
    enemy3.append(pygame.image.load("alien3.png"))
    enemyx3.append(random.randint(0,735))
    enemyy3.append(random.randint(50,150))
    changeex3.append(0.6)
    changeey3.append(30)

# Rules 
fontrule = font.Font('freesansbold.ttf', 17)
rule1=fontrule.render("(i) You can move your spaceship in the game using the arrow keys",True,(255,255,255))
rule2=fontrule.render("(ii) If you want to fire the enemy you can do it through pressing space button",True,(255,255,255))
rule3=fontrule.render("(iii) There are 3 levels present in the game with each level enemy are going to increase",True,(255,255,255))
rule4=fontrule.render("(iv) If you shoot enemy at level 1 you will get +1 in scores",True,(255,255,255))
rule5=fontrule.render("(v) If you shoot enemy at level 2 you will get +2 in scores",True,(255,255,255))
rule6=fontrule.render("(vi) If you shoot enemy at level 3 you will get +3 in scores",True,(255,255,255))
rule7=fontrule.render("(vii) If the enemy hits you or they crossed a particular line then the game will be over",True,(255,255,255))
presskeytocontinue=fontrule.render("PRESS ANY KEY TO CONTINUE",True,(0,0,0),(0,250,205))


# Bullet Sound
laser =pygame.mixer.Sound('laser.wav')
laser.set_volume(0.1)

# Collision of bullet and enemy
def iscollisionbullet(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx,2))+(math.pow(enemyy-bullety,2)))
    if distance < 18:
        return True
    else:
        return False
    
# Collision of player and enemy
def iscollisionplayer(enemyx,enemyy,playerx,playery):
    distance=math.sqrt((math.pow(enemyx-playerx,2))+(math.pow(enemyy-playery,2)))
    if distance < 27:
        return True
    else:
        return False
# Start Button
def startbutton():
    x=300
    y=170
    global clicked,action_start
    global running
    button_rect = Rect(x,y, widthmenu, heightmenu)
    if button_rect.collidepoint(pos):
	    if pygame.mouse.get_pressed()[0] == 1:
		    clicked = True
		    pygame.draw.rect(screen, click_col, button_rect)
	    elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
		    clicked = False
		    action_start=True
	    else:
		    pygame.draw.rect(screen, hover_col, button_rect)
    else:
	    pygame.draw.rect(screen, button_col, button_rect)

    pygame.draw.line(screen, (255,255,255), (x, y), (x + widthmenu, y), 2)
    pygame.draw.line(screen, (255,255,255), (x,y), (x, y + heightmenu), 2)
    pygame.draw.line(screen, (0,0,0), (x, y + heightmenu), (x + widthmenu, y + heightmenu), 2)
    pygame.draw.line(screen, (0,0,0), (x + widthmenu, y), (x + widthmenu,y + heightmenu), 2)
    text_img = fontmenu.render(" Start ", True, text_col)
    text_len = text_img.get_width()
    screen.blit(text_img, (x + int(widthmenu / 2) - int(text_len / 2), y  + 30))
    return action_start

# Quit Button
def Quit():
    x=300
    y=300
    global clicked,action_quit
    global running
    button_rect = Rect(x,y, widthmenu, heightmenu)
    if button_rect.collidepoint(pos):
	    if pygame.mouse.get_pressed()[0] == 1:
		    clicked = True
		    pygame.draw.rect(screen, click_col, button_rect)
	    elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
		    clicked = False
		    action_quit=True
	    else:
		    pygame.draw.rect(screen, hover_col, button_rect)
    else:
	    pygame.draw.rect(screen, button_col, button_rect)

    pygame.draw.line(screen, (255,255,255), (x, y), (x + widthmenu, y), 2)
    pygame.draw.line(screen, (255,255,255), (x,y), (x, y + heightmenu), 2)
    pygame.draw.line(screen, (0,0,0), (x, y + heightmenu), (x + widthmenu, y + heightmenu), 2)
    pygame.draw.line(screen, (0,0,0), (x + widthmenu, y), (x + widthmenu,y + heightmenu), 2)
    text_img = fontmenu.render(" Quit ", True, text_col)
    text_len = text_img.get_width()
    screen.blit(text_img, (x + int(widthmenu / 2) - int(text_len / 2), y  + 30))
    return action_quit

# Opening Menu
def menu():
    global running,level,start,action_quit,rule
    level=1
    if action_start:
        rule=True
        start=False
    elif action_quit:
        start=False
        action_quit=False
# Reset
def reset():
    global level,playerimg,playerx,playery,changex,changey,enemy1,enemyx,enemyy,changeex,changeey,action_play,score_value,sound_background,enemy2,enemyx2,enemyy2
    global changeex2,changeey2,enemy3,enemyx3,enemyy3,changeex3,changeey3
    playerimg=pygame.image.load("arcade-game.png")
    playerx=370
    playery=480
    changex=0
    changey=0
    enemy1=[]
    enemyx=[]
    enemyy=[]
    changeex=[]
    changeey=[]
    score_value=0
    number_of_enemies=8
    for i in range(number_of_enemies):
        enemy1.append(pygame.image.load("alien2.png"))
        enemyx.append(random.randint(0,735))
        enemyy.append(random.randint(50,150))
        changeex.append(0.4)
        changeey.append(30)
    enemy2=[]
    enemyx2=[]
    enemyy2=[]
    changeex2=[]
    changeey2=[]
    number_of_enemies2=5
    for i in range(number_of_enemies2):
        enemy2.append(pygame.image.load("alien.png"))
        enemyx2.append(random.randint(0,735))
        enemyy2.append(random.randint(50,150))
        changeex2.append(0.5)
        changeey2.append(30)
    enemy3=[]
    enemyx3=[]
    enemyy3=[]
    changeex3=[]
    changeey3=[]
    number_of_enemies3=4
    for i in range(number_of_enemies3):
        enemy3.append(pygame.image.load("alien3.png"))
        enemyx3.append(random.randint(0,735))
        enemyy3.append(random.randint(50,150))
        changeex3.append(0.6)
        changeey3.append(30)
    sound_background.play()
    action_play=False
    levels()

# Score.txt file
def storehighscore(sco):
    with open('highscore.txt') as f:
        highscore=int(f.read())
    if int(highscore) < sco:
        with open("highscore.txt",'w') as f:
            f.write(str(sco))
splash=pygame.image.load("splash.jpg")
splash=pygame.transform.scale(splash,(800,600))
#get score
def getscore():
    with open('highscore.txt') as f:
        highscore=int(f.read())
    return highscore
#Show Highscore
def show():
    global myscore
    myscore=getscore()
    score=font123.render("Highscore:"+str(myscore),True,(255,255,255))
    screen.blit(score,(high_x,high_y))    
# Starting Code
while start:
    screen.blit(splash,(0,0))
    spaceinvaders=gameover.render("Space Invaders",True,(128,0,128))
    spaceinvader=gameover.render("Space Invaders",True,(0,255,0))
    screen.blit(spaceinvaders,(120,50))
    screen.blit(spaceinvader,(125,50))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Close button 
        if event.type==pygame.QUIT:
            start=False 
    menu()
    startbutton()
    Quit()
    pygame.display.update()
keypoints=gameover.render("Key Points",True,(0,255,0))
keypointborder=gameover.render("Key Points",True,(0,0,0))
line=font123.render("--------",True,(255,0,0))
while rule:
    screen.blit(splash,(0,0))
    screen.blit(keypointborder,(210,20))
    screen.blit(keypoints,(205,20))
    screen.blit(rule1,(50,150))
    screen.blit(rule2,(50,200))
    screen.blit(rule3,(50,250))
    screen.blit(rule4,(50,300))
    screen.blit(rule5,(50,350))
    screen.blit(rule6,(50,400))
    screen.blit(rule7,(50,450))
    screen.blit(presskeytocontinue,(280,500))
    for event in pygame.event.get():
        
    # Close button 
        if event.type==pygame.QUIT:
            rule=False 

    # Player's movement    
        if event.type==pygame.KEYDOWN:
               running=True
               rule=False
    pygame.display.update()


# Running
while running:
    # screen.fill((0,0,0))
    # screen.blit(splash,(0,0))
    screen.blit(background,(0,0))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        
        # Close button 
        if event.type==pygame.QUIT:
            running=False 

        # Player's movement    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changex=-0.7
            if event.key==pygame.K_RIGHT:
                changex=0.7
            if event.key==pygame.K_UP:
                changey=-0.7
            if event.key==pygame.K_DOWN:
                changey=0.7
        
            # Bullet fire code logic
            if event.key==pygame.K_SPACE:
                if bulletstate=='ready':
                    k=playery
                    j=playerx
                    bulletstate='fire'
                    laser.play()
        # Defining to stop player when key is up
        if event.type==pygame.KEYUP:
            changey=0
            changex=0
    
    # Bullet Movement
    if bulletstate=="fire":
        fire(j+16,k+10)
        k-=bulletychange
        bullety=k
        bulletx=j

    # Initializing Bullet to ready 
    if bullety<=-20:
        bullety=playery
        bulletstate='ready'

    # Player's Movement
    playerx+=changex
    playery+=changey

    # Writing code to keep player within limits 
    if playerx<0:
        playerx=0
    elif playerx>735:
        playerx=735
    if playery<0:
        playery=0
    elif playery>535:
        playery=535

    player(playerx,playery)

    # Enemy's Movement
    if level==1:
        for i in range(number_of_enemies):
            #Game Over
            if iscollisionplayer(enemyx[i],enemyy[i],playerx,playery) or enemyy[i]>480:
                for q in range(number_of_enemies):
                    enemyy[q]=2000
                for q in range(number_of_enemies2):
                    enemyy2[q]=2000
                for q in range(number_of_enemies3):
                    enemyy3[q]=2000
                game_over_text()
                storehighscore(score_value)
                changey=0
                changex=0
                bulletstate="ready"
                laser.stop()
                sound_background.stop()
                playagain()
                exit()
                if action_play:
                    reset()
                else:
                    break
            enemyx[i]+=changeex[i]
            if enemyx[i]<0:
                changeex[i]=0.4
                enemyy[i]+=changeey[i]
            elif enemyx[i]>735:
                changeex[i]=-0.4
                enemyy[i]+=changeey[i] 
            
            
        
        # Collision with bullet
            collision = iscollisionbullet(enemyx[i],enemyy[i],bulletx,bullety)
            if collision:
                bullety=playery
                bulletstate='ready'
                score_value+=1
                explosion=pygame.mixer.Sound("explosion.wav")
                explosion.set_volume(0.1)
                explosion.play()
                enemyx[i]=random.randint(0,735)
                enemyy[i]=random.randint(50,150)
            enemy(enemy1[i],enemyx[i],enemyy[i])    
    if level==2:
        for i in range(number_of_enemies):
            #Game Over
            if iscollisionplayer(enemyx[i],enemyy[i],playerx,playery) or enemyy[i]>480:
                for q in range(number_of_enemies):
                    enemyy[q]=2000
                for q in range(number_of_enemies2):
                    enemyy2[q]=2000
                for q in range(number_of_enemies3):
                    enemyy3[q]=2000
                game_over_text()
                storehighscore(score_value)
                changey=0
                changex=0
                bulletstate="ready"
                laser.stop()
                sound_background.stop()
                playagain()
                exit()
                if action_play:
                    reset()
                else:
                    break
            enemyx[i]+=changeex[i]
            if enemyx[i]<0:
                changeex[i]=0.4
                enemyy[i]+=changeey[i]
            elif enemyx[i]>735:
                changeex[i]=-0.4
                enemyy[i]+=changeey[i] 
            
            
        
        # Collision with bullet
            collision = iscollisionbullet(enemyx[i],enemyy[i],bulletx,bullety)
            if collision:
                bullety=playery
                bulletstate='ready'
                score_value+=1
                explosion=pygame.mixer.Sound("explosion.wav")
                explosion.set_volume(0.1)
                explosion.play()
                enemyx[i]=random.randint(0,735)
                enemyy[i]=random.randint(50,150)
            enemy(enemy1[i],enemyx[i],enemyy[i])
        for i in range(number_of_enemies2):
                #Game Over
                if iscollisionplayer(enemyx2[i],enemyy2[i],playerx,playery) or enemyy2[i]>480:
                    for q in range(number_of_enemies2):
                        enemyy2[q]=2000
                    for q in range(number_of_enemies):
                        enemyy[q]=2000
                    # for q in range(number_of_enemies3):
                        # enemyy3[q]=2000
                    game_over_text()
                    storehighscore(score_value)
                    changey=0
                    changex=0
                    bulletstate="ready"
                    laser.stop()
                    sound_background.stop()
                    playagain()
                    exit()
                    if action_play:
                        reset()
                    else:
                        break
                enemyx2[i]+=changeex2[i]
                if enemyx2[i]<0:
                    changeex2[i]=0.5
                    enemyy2[i]+=changeey2[i]
                elif enemyx2[i]>735:
                    changeex2[i]=-0.5
                    enemyy2[i]+=changeey2[i] 
                
                
            
            # Collision with bullet
                collision = iscollisionbullet(enemyx2[i],enemyy2[i],bulletx,bullety)
                if collision:
                    bullety=playery
                    bulletstate='ready'
                    score_value+=2
                    explosion=pygame.mixer.Sound("explosion.wav")
                    explosion.set_volume(0.1)
                    explosion.play()
                    enemyx2[i]=random.randint(0,735)
                    enemyy2[i]=random.randint(50,150)
                enemy(enemy2[i],enemyx2[i],enemyy2[i])
        
    if level==3:
        for i in range(number_of_enemies):
            #Game Over
            if iscollisionplayer(enemyx[i],enemyy[i],playerx,playery) or enemyy[i]>480:
                for q in range(number_of_enemies):
                    enemyy[q]=2000
                for q in range(number_of_enemies2):
                    enemyy2[q]=2000
                for q in range(number_of_enemies3):
                    enemyy3[q]=2000
                game_over_text()
                storehighscore(score_value)
                changey=0
                changex=0
                bulletstate="ready"
                laser.stop()
                sound_background.stop()
                playagain()
                exit()
                if action_play:
                    reset()
                else:
                    break
            enemyx[i]+=changeex[i]
            if enemyx[i]<0:
                changeex[i]=0.4
                enemyy[i]+=changeey[i]
            elif enemyx[i]>735:
                changeex[i]=-0.4
                enemyy[i]+=changeey[i] 
            
            
        
        # Collision with bullet
            collision = iscollisionbullet(enemyx[i],enemyy[i],bulletx,bullety)
            if collision:
                bullety=playery
                bulletstate='ready'
                score_value+=1
                explosion=pygame.mixer.Sound("explosion.wav")
                explosion.set_volume(0.1)
                explosion.play()
                enemyx[i]=random.randint(0,735)
                enemyy[i]=random.randint(50,150)
            enemy(enemy1[i],enemyx[i],enemyy[i])
        for i in range(number_of_enemies2):
                #Game Over
                if iscollisionplayer(enemyx2[i],enemyy2[i],playerx,playery) or enemyy2[i]>480:
                    for q in range(number_of_enemies2):
                        enemyy2[q]=2000
                    for q in range(number_of_enemies):
                        enemyy[q]=2000
                    # for q in range(number_of_enemies3):
                        # enemyy3[q]=2000
                    game_over_text()
                    storehighscore(score_value)
                    changey=0
                    changex=0
                    bulletstate="ready"
                    laser.stop()
                    sound_background.stop()
                    playagain()
                    exit()
                    if action_play:
                        reset()
                    else:
                        break
                enemyx2[i]+=changeex2[i]
                if enemyx2[i]<0:
                    changeex2[i]=0.5
                    enemyy2[i]+=changeey2[i]
                elif enemyx2[i]>735:
                    changeex2[i]=-0.5
                    enemyy2[i]+=changeey2[i] 
                
                
            
            # Collision with bullet
                collision = iscollisionbullet(enemyx2[i],enemyy2[i],bulletx,bullety)
                if collision:
                    bullety=playery
                    bulletstate='ready'
                    score_value+=2
                    explosion=pygame.mixer.Sound("explosion.wav")
                    explosion.set_volume(0.1)
                    explosion.play()
                    enemyx2[i]=random.randint(0,735)
                    enemyy2[i]=random.randint(50,150)
                # enemy(enemy2[i],enemyx2[i],enemyy2[i])
        for i in range(number_of_enemies3):
                #Game Over
            if iscollisionplayer(enemyx3[i],enemyy3[i],playerx,playery) or enemyy3[i]>480:
                for q in range(number_of_enemies3):
                    enemyy3[q]=2000
                for q in range(number_of_enemies2):
                    enemyy2[q]=2000
                for q in range(number_of_enemies):
                    enemyy[q]=2000
                game_over_text()
                storehighscore(score_value)
                changey=0
                changex=0
                bulletstate="ready"
                laser.stop()
                sound_background.stop()
                playagain()
                exit()
                if action_play:
                    reset()
                else:
                    break
            enemyx3[i]+=changeex3[i]
            if enemyx3[i]<0:
                changeex3[i]=0.6
                enemyy3[i]+=changeey3[i]
            elif enemyx3[i]>735:
                changeex3[i]=-0.6
                enemyy3[i]+=changeey3[i] 
                
                
            
           # Collision with bullet
            collision = iscollisionbullet(enemyx3[i],enemyy3[i],bulletx,bullety)
            if collision:
                bullety=playery
                bulletstate='ready'
                score_value+=4
                explosion=pygame.mixer.Sound("explosion.wav")
                explosion.set_volume(0.1)
                explosion.play()
                enemyx3[i]=random.randint(0,735)
                enemyy3[i]=random.randint(50,150)
            enemy(enemy2[i],enemyx2[i],enemyy2[i])
            enemy(enemy3[i],enemyx3[i],enemyy3[i])
    # Show Score
    score(text_x,text_y)
    show()
    levels()
    screen.blit(line,(0,480))
    # Updating Game's Window
    pygame.display.update()