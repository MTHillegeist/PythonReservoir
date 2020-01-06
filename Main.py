from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, time
from math import sin,cos,sqrt,pi
import Reservoir
from Draw import *

print(sys.version)
print("Testing of Main.py")





lastFrameTime = time.time()

def draw():
	delta_t = time.time() - lastFrameTime
	#lastFrameTime = time.time()

	angle = 10 * delta_t
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	glLoadIdentity()
	#Triangle()
	#gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	#glScalef(1.0, 2.0, 1.0)
	glPushMatrix()
	glRotatef(45.0 , 1.0, 1.0, 0.0)
	#glutWireCube(1.0)
	glFlush()
	glPopMatrix()
	#glRotatef(angle, 1.0, 1.0, 1.0)

	#glCallList(triangle1)
	#glCallList(cube1)
	#glCallList(res1)
	#glPopMatrix()
	glutSwapBuffers()

def draw_cube_test():
	delta_t = time.time() - lastFrameTime
	#lastFrameTime = time.time()

	angle = 10 * delta_t
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)

	glLoadIdentity()
	#gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	#glScalef(1.0, 2.0, 1.0)
	glPushMatrix()
	#glRotatef(45.0 , 1.0, 1.0, 0.0)
	glScalef(0.5, 0.5, 0.5)
	#glutSolidCube(1.0)
	glCallList(cube1)
	#glCallList(triangle1)
	glFlush()
	glPopMatrix()

	glutSwapBuffers()


def main():
	print("Main")

def init():
	global triangle1
	global cube1
	global res1
	global resSpecs1
	resSpecs1 = Reservoir.Reservoir(10,10,10,0.3)
	#print("Init()")
	red = (0.8, 0.1, 0.0, 1.0)
	blue = (0.0, 0.0, 1.0, 1.0)

	triangle1 = glGenLists(1)
	glNewList(triangle1, GL_COMPILE)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
	TriangleEquil()
	glEndList()


	cube1 = glGenLists(1)
	glNewList(cube1, GL_COMPILE)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
	glColor3f(red[0], red[1], red[2])
	glPolygonMode(GL_FRONT, GL_FILL)
	DrawCube()
	glEndList()

	res1 = glGenLists(1)
	glNewList(res1, GL_COMPILE)
	glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
	#glColor3f(red[0], red[1], red[2])
	glPolygonMode(GL_FRONT, GL_FILL) #(GL_FRONT_AND_BACK, GL_LINE)
	Reservoir.DrawGrid(resSpecs1)
	glEndList()

	lastFrameTime = time.time()
	#print(lastFrameTime)
	angle = 0.0
	#print("End Init()")

main()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Testing")
init()
glutDisplayFunc(draw_cube_test)
glutIdleFunc(draw_cube_test)
glutMainLoop()
