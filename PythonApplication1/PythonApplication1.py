import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


#def cube():
#    glBegin(GL_QUADS)

#    for surface in surfaces:
#        x = 0
#        for vertex in surface:
#            x += 1
#            glColor3fv(colors[x])
#            glVertex3fv(vertices[vertex])

#    glEnd()

#    glBegin(GL_LINES)
#    for edge in edges:
#        for vertex in edge:
#            glVertex3fv(vertices[vertex])

#    glEnd()

x = 1.01
y=-1.0
z=1.0

a = 10.0
b = 28.0
c = 8.0/3.0

l=0

def lorenz():
    global x
    global y
    global z

    global a
    global b
    global c

    #global l
    dt = 0.1

    dx = (a * (y-x)) * dt
    dy = (x * (b-z) - y) *dt
    dz = (x * y - c * z) *dt

    x = x + dx
    y = y + dy
    z = z + dz

    points = (x,y,z)
    print(points)
    
    glPointSize(2)

    glBegin(GL_POINTS)    
    
    glVertex3fv(points)
    
    glEnd()
    

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 300.0)

    glTranslatef(0, 0, -120 )

    glRotatef(0, 0, 0, 0)

        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        lorenz()
        
        pygame.display.flip()
        pygame.time.wait(1)



#def main():
#    pygame.init()
#    display = (800, 600)
#    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

#    glTranslatef(1, 1, -5)

#    glRotatef(0, 0, 0, 0)

#    while True:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()

#        #glRotatef(1, 3, 1, 1)
#        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#        cube()
#        pygame.display.flip()
#        pygame.time.wait(10)


main()
