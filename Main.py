#from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, time
import math
from math import sin,cos,sqrt,pi
import Reservoir
import Draw

print(sys.version)
print("Testing of Main.py")

class Camera:
	def __init__(self):
		super(Camera, self).__init__()
		self.target = (0, 0, 0)
		self.pos = (0, 2, 2)
		self.up = (0, 1, 0)

class Application(object):

	def define_reservoir1():
		res1 = Reservoir.Reservoir(width=10, height=10, depth=10, cell_dim=0.4)

		region = Reservoir.ResRegion()
		region.iStart = 1
		region.iEnd = 8
		region.jStart = 1
		region.jEnd = 8
		region.kStart = 1
		region.kEnd = 8

		res1.SetCellsValue(region, "wtrPct", 100.0)
		res1.SetCellsValue(region, "oilPct", 0.0)

		return res1

	def define_reservoir2():
		return Reservoir.Reservoir(width=4, height=4, depth=4, cell_dim=0.6)

	def define_reservoir3():
		res = Reservoir.Reservoir(width=10, height=10, depth=1, cell_dim=0.4)

		region = Reservoir.ResRegion()
		region.iStart = 1
		region.iEnd = 8
		region.jStart = 1
		region.jEnd = 8
		region.kStart = 0
		region.kEnd = 0

		res.SetCellsValue(region, "wtrPct", 100.0)
		res.SetCellsValue(region, "oilPct", 0.0)
		return res

	def __init__(self):
		super(Application, self).__init__()
		self.lastFrameTime = time.time()
		self.runTime = 0
		self.angle = 0
		self.camera = Camera()

		#Culling type. GL_BACK is the default.
		#glCullFace(GL_BACK)
		#glCullFace(GL_FRONT_AND_BACK)
		glEnable(GL_CULL_FACE)
		glEnable(GL_DEPTH_TEST)
		# glDisable(GL_CULL_FACE)
		glMatrixMode(GL_MODELVIEW)

		resSpecs1 = Application.define_reservoir3()

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
		glPolygonMode(GL_FRONT, GL_FILL) #(GL_FRONT_AND_BACK, GL_LINE)
		Draw.draw_res(resSpecs1)
		glEndList()

		self.lastFrameTime = time.time()

	def main_loop(self):
		delta_t = time.time() - self.lastFrameTime
		self.lastFrameTime = time.time()
		self.runTime = self.runTime + delta_t

		self.angle += 20.0 * delta_t % 360

		self.draw()
		#self.draw_cube_test()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1.0, 1.0, 1.0)
		glLoadIdentity()
		#Triangle()
		cam = self.camera
		gluLookAt(cam.pos[0], cam.pos[1], cam.pos[2],
		           cam.target[0], cam.target[1], cam.target[2],
				   cam.up[0], cam.up[1], cam.up[2])
		#glScalef(1.0, 2.0, 1.0)
		glPushMatrix()

		glRotatef(self.angle , 0.0, 1.0, 0.0)
		glCallList(self.res1)

		glFlush()
		glPopMatrix()
		glutSwapBuffers()

	def draw_cube_test(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glColor3f(1.0, 1.0, 1.0)

		glLoadIdentity()
		cam = self.camera
		gluLookAt(cam.pos[0], cam.pos[1], cam.pos[2],
		           cam.target[0], cam.target[1], cam.target[2],
				   cam.up[0], cam.up[1], cam.up[2])
		glPushMatrix()
		glRotatef(self.angle, 1.0, 1.0, 0.0)
		glCallList(self.cube1)
		glFlush()
		glPopMatrix()

		glutSwapBuffers()

	def reshape(self, w, h):
		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
		glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"OpenGL Testing")
app = Application()
glutDisplayFunc(app.main_loop)
glutReshapeFunc(app.reshape)
glutIdleFunc(app.main_loop)
glutMainLoop()
