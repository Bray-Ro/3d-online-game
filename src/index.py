import pygame
import Tkinter
from pygame.locals import *
import pymongo
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import sys
global player2x
global player2y
global player2z
#SETUP DATABASE
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mineTime3d"]
gameone = db["game_one"]
game_one_generation = db["game_one_generation"]
print("==============================================")
print("Welcome to mineTime3D!")
print("==============================================")
def game_one():
    global rotated
    global player2x
    global player2y
    global player2z

    rotated = 0
    player2x = 1
    player2y = 1
    player2z = 1
    global player3x
    global player3y
    global player3z
    player3x = 1
    player3y = 1
    player3z = 1
    players = gameone.count()
    if players == 3:
        print("Sorry, there are already 3 players in this game come back later!")
    else:

        usrname = "player" + str(players + 1)
        print("hello, your username is " + usrname)
        # generate the player's starting coordinates
        playercoor = random.randint(1, 10)
        playerx = playercoor
        playerz = playercoor
    
        gameone.insert({"username": usrname, "x": playerx, "z": playerz})
        pygame.init()

        player2_verticies = (
                (5, -5, -5),
                (5, 5, -5),
                (-5, 5, -5),
                (-5, -5, -5),
                (5, -5, 5),
                (5, 5, 5),
                (-5, -5, 5),
                (-5, 5, 5)
            )
        
        blue_lad_verticies = (
                (1, -1, -1),
                (1, 1, -1),
                (-1, 1, -1),
                (-1, -1, -1),
                (1, -1, 1),
                (1, 1, 1),
                (-1, -1, 1),
                (-1, 1, 1)
        )
        
        bluelad_corner1_coordinates = (10, -10, 10)
        player3_verticies = (
                (5, -5, -5),
                (5, 5, -5),
                (-5, 5, -5),
                (-5, -5, -5),
                (5, -5, 5),
                (5, 5, 5),
                (-5, -5, 5),
                (-5, 5, 5)
            )       

        edges = (
            (0,1),
            (0,3),
            (0,4),
            (2,1),
            (2,3),
            (2,7),
            (6,3),
            (6,4),
            (6,7),
            (5,1),
            (5,4),
            (5,7)
        )
        surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
        )
        ground_surfaces = (0,1,2,3)
        ground_vertices = (
        (-10,-0.1,50),
        (10,-0.1,50),
        (-10,-0.1,-300),
        (10,-0.1,-300),

        )

        colors = (
            (1,0,0),
            (0,1,0),
            (0,0,1),
            (0,1,0),
            (1,1,1),
            (0,1,1),
            (1,0,0),
            (0,1,0),
            (0,0,1),
            (1,0,0),
            (1,1,1),
            (0,1,1),
            )
        def loadTexture():
            textureSurface = pygame.image.load('Screen Shot 2020-04-07 at 10.16.51.png')
            textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
            width = textureSurface.get_width()
            height = textureSurface.get_height()

            glEnable(GL_TEXTURE_2D)
            texid = glGenTextures(1)

            glBindTexture(GL_TEXTURE_2D, texid)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                        0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

            return texid





        def Cube(lines=False):
            global player2x
            global player2y
            global player2z
            if lines:
                glBegin(GL_QUADS)
                
                for surface in surfaces:
                    x = 0
                
                
                for vertex in surface:
                    

        
            
                        glVertex3fv(player2_verticies[vertex])  
       
    
                        
                glEnd()

                glBegin(GL_LINES)
                for edge in edges:
                    for vertex in edge:


                        glVertex3fv(player2_verticies[vertex])              
          
                glEnd()
            else:         
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glEnd() 
        def draw_bluelad(lines=False):
            global player2x
            global player2y
            global player2z
            textureSurface = pygame.image.load('Profile_-_Genie.jpg')
            textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
            width = textureSurface.get_width()
            height = textureSurface.get_height()

            glEnable(GL_TEXTURE_2D)
            texid = glGenTextures(1)

            glBindTexture(GL_TEXTURE_2D, texid)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                        0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            if lines:
                glBegin(GL_QUADS)
                
                for surface in surfaces:
                    x = 0
                
                
                for vertex in surface:
                    

        
            

                        glVertex3fv(blue_lad_verticies[vertex])                  
    
                        
                glEnd()

                glBegin(GL_LINES)
                for edge in edges:
                    for vertex in edge:


           
                        glVertex3fv(blue_lad_verticies[vertex])                 
                glEnd()
            else:         
                glBegin(GL_QUADS)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(1.0,  1.0, -1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(1.0, -1.0,  1.0)
                glTexCoord2f(0.0, 0.0)
                glVertex3f(-1.0, -1.0, -1.0)
                glTexCoord2f(1.0, 0.0)
                glVertex3f(-1.0, -1.0,  1.0)
                glTexCoord2f(1.0, 1.0)
                glVertex3f(-1.0,  1.0,  1.0)
                glTexCoord2f(0.0, 1.0)
                glVertex3f(-1.0,  1.0, -1.0)
                glEnd() 
        global player2x
        global player2y
        global player2z
        pygame.init()
        display = (800,600)
        DISPLAY = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, (display[0]/display[1]), 0.1, 1000.0)

        glTranslatef(0,0, -10)

        glRotatef(25, 0, 25, 0)

        
        loadTexture()
        while True:
            print(playerx, player2y)
            players = gameone.count()
            player2xbefore = player2x
            player2zbefore = player2z
            player3xbefore = player3x
            player3zbefore = player3z
            #get coorrdinates of other players
            if players == 2:         
                if usrname == "player1":
                    player2stats = gameone.find({"username": "player2"})
                else:
                    player2stats = gameone.find({"username": "player1"})
                for x in player2stats:
                    player2x = int(x["x"])
                    player2z = int(x["z"])
            if players == 3:
                if usrname == "player1":
                    player2stats = gameone.find({"username": "player2"})
                    player3stats = gameone.find({"username": "player3"})                        
                elif usrname == "player2":
                    player2stats = gameone.find({"username": "player1"})
                    player3stats = gameone.find({"username": "player3"})
                else:
                    player2stats = gameone.find({"username": "player1"})
                    player3stats = gameone.find({"username": "player2"})                        
                for x in player2stats:

                    player2x = int(x["x"])
                    player2z = int(x["z"])
                for y in player3stats:
                    player2x = int(y["x"])
                    player2z = int(y["z"])
            if player2xbefore < player2x:
         
                glTranslatef(player2x - player2xbefore, 0, 0)
            if player2xbefore > player2x:
         
                glTranslatef(-player2x - player2xbefore, 0, 0)
            if player2zbefore < player2z:
         
                glTranslatef(0, 0, player2z - player2zbefore)
            if player2zbefore > player2z:
         
                glTranslatef(0, 0, -player2z - player2zbefore)
            print(player2_verticies)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameone.delete_one({"username": usrname})
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:

                    playerx += 0.5
                    glTranslatef(0.5, 0,0)
            
                if keys[pygame.K_RIGHT]:

                    playerx -= 0.5
                    glTranslatef(-0.5,0,0)
                    
                if keys[pygame.K_UP]:

                    playerz += 0.5
                    glTranslatef(0,0,0.5)
                    
                if keys[pygame.K_DOWN]:

                    playerz -= 0.5
                    glTranslatef(0,0,-0.5)
                if keys[pygame.K_w]:
                
                    glRotatef(3, -2.0, 0, 0)
                if keys[pygame.K_a]:
                
                    glRotatef(3, 0, -2.0, 0)
                if keys[pygame.K_s]:
                
                    glRotatef(3, 2.0, 0, 0)
                if keys[pygame.K_d]:
                
                    glRotatef(3, 0, 2.0, 0)
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if event.button == 4:
                #         glTranslatef(0,0,1.0)

                #     if event.button == 5:
                #         glTranslatef(0,0,-1.0)

            #glRotatef(1, 3, 1, 1)
            #gets coordinates of player

            gameone.update_one({"username": usrname}, {"$set": {"x": playerx}})
 
            gameone.update_one({"username": usrname}, {"$set": {"z": playerz}})            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            loadTexture()
            Cube()
            pygame.display.flip()
            pygame.time.wait(10)
            loadTexture()
            Cube(lines=True)

            draw_bluelad(lines=True)
        loadTexture()
        Cube(lines=False)
        draw_bluelad(lines=False)

        Ground()
game_one()
