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

#Globals.
lastFrameTime = time.time()
runTime = 0

def draw():
	global lastFrameTime
	global runTime

	delta_t = time.time() - lastFrameTime
	lastFrameTime = time.time()
	runTime = runTime + delta_t
	angle = 20.0 * runTime % 360

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	glLoadIdentity()
	#Triangle()
	#gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	#glScalef(1.0, 2.0, 1.0)
	glPushMatrix()
	glRotatef(angle , 1.0, 1.0, 0.0)
	#glutWireCube(1.0)
	glCallList(res1)
	glFlush()
	glPopMatrix()
	#glRotatef(angle, 1.0, 1.0, 1.0)

	#glCallList(triangle1)
	#glCallList(cube1)
	#glCallList(res1)
	#glPopMatrix()
	glutSwapBuffers()

def draw_cube_test():
	global lastFrameTime
	global runTime

	delta_t = time.time() - lastFrameTime
	lastFrameTime = time.time()
	runTime = runTime + delta_t
	angle = 20.0 * runTime % 360

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)

	glLoadIdentity()
	glPushMatrix()
	glRotatef(angle, 1.0, 1.0, 0.0)
	glCallList(cube1)
	glFlush()
	glPopMatrix()

	glutSwapBuffers()

def init():
	global triangle1
	global cube1
	global res1
	global resSpecs1

	#glCullFace(GL_BACK)
	glEnable(GL_CULL_FACE)

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

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Testing")
init()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
