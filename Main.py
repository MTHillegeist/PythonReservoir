#from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, time
from math import sin,cos,sqrt,pi
import Reservoir
import Draw

print(sys.version)
print("Testing of Main.py")

class Application(object):
	def __init__(self):
		super(Application, self).__init__()
		self.lastFrameTime = time.time()
		self.runTime = 0

		#glCullFace(GL_BACK)
		#glCullFace(GL_FRONT_AND_BACK)
		glEnable(GL_CULL_FACE)

		resSpecs1 = Reservoir.Reservoir(10,10,10,0.3)
		#print("Init()")
		red = (0.8, 0.1, 0.0, 1.0)
		blue = (0.0, 0.0, 1.0, 1.0)

		self.triangle1 = glGenLists(1)
		glNewList(self.triangle1, GL_COMPILE)
		glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
		Draw.TriangleEquil()
		glEndList()


		self.cube1 = glGenLists(1)
		glNewList(self.cube1, GL_COMPILE)
		glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
		glColor3f(red[0], red[1], red[2])
		glPolygonMode(GL_FRONT, GL_FILL)
		Draw.DrawCube()
		glEndList()

		self.res1 = glGenLists(1)
		glNewList(self.res1, GL_COMPILE)
		glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, red)
		#glColor3f(red[0], red[1], red[2])
		glPolygonMode(GL_FRONT, GL_FILL) #(GL_FRONT_AND_BACK, GL_LINE)
		Reservoir.DrawGrid(resSpecs1)
		glEndList()

		self.lastFrameTime = time.time()
		#print(lastFrameTime)
		#print("End Init()")

	def draw(self):

		delta_t = time.time() - self.lastFrameTime
		self.lastFrameTime = time.time()
		self.runTime = self.runTime + delta_t
		angle = 20.0 * self.runTime % 360

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1.0, 1.0, 1.0)
		glLoadIdentity()
		#Triangle()
		#gluLookAt (0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
		#glScalef(1.0, 2.0, 1.0)
		glPushMatrix()
		glRotatef(angle , 1.0, 1.0, 0.0)
		#glutWireCube(1.0)
		glCallList(self.res1)
		glFlush()
		glPopMatrix()
		#glRotatef(angle, 1.0, 1.0, 1.0)

		#glCallList(triangle1)
		#glCallList(cube1)
		#glCallList(res1)
		#glPopMatrix()
		glutSwapBuffers()

	def draw_cube_test(self):
		delta_t = time.time() - self.lastFrameTime
		self.lastFrameTime = time.time()
		self.runTime = self.runTime + delta_t
		angle = 20.0 * self.runTime % 360

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1.0, 1.0, 1.0)

		glLoadIdentity()
		glPushMatrix()
		glRotatef(angle, 1.0, 1.0, 0.0)
		glCallList(cube1)
		glFlush()
		glPopMatrix()

		glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Testing")
app = Application()
glutDisplayFunc(app.draw)
glutIdleFunc(app.draw)
glutMainLoop()
