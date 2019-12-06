from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin,cos,sqrt,pi
from operator import add

class Cell(object):
	def __init__(self):
		self.porosity = 0.25
		self.oilPct = 100.0
		self.wtrPct = 0.0

class Reservoir(object):
	"""docstring for Reservoir."""

	def __init__(self, width, height, depth, cell_dim):
		super(Reservoir, self).__init__()
		self.width = width
		self.height = height
		self.depth = depth
		self.cell_dim = cell_dim
		self.grid = [[[0 for _ in range(width)] for _ in range(height)] for _ in range(depth)]

		for i in range(self.width-1):
			for j in range(self.height-1):
				for k in range(self.depth-1):
					self.grid[i][j][k] = Cell()
					if i % 2 == 1:
						self.grid[i][j][k].oilPct = 0.0
						self.grid[i][j][k].wtrPct = 100.0

def DrawGrid(res):
	red = (0.8, 0.1, 0.0, 1.0)
	blue = (0.0, 0.0, 0.8, 1.0)
	cell_dim = res.cell_dim
	glPushMatrix()
	glScalef(cell_dim, cell_dim, cell_dim)

	print("cell_dim: % f" % cell_dim)
	#print("Width: %d Height: %d Depth: %d" %(res.width, res.height, res.depth))
	for i in range(res.width-1):
		for j in range(res.height-1):
			for k in range(res.depth-1):
				glPushMatrix()
				x = -res.width / 2 *cell_dim + i * cell_dim
				y = -res.height / 2 *cell_dim + j * cell_dim
				z = - k * cell_dim
				glTranslatef(x, y, z)
				oilWeight = res.grid[i][j][k].oilPct / 100.0
				wtrWeight = res.grid[i][j][k].wtrPct / 100.0
				#print("Oil: %.1f Water; %.1f" % (oilWeight, wtrWeight))
				oilColor = [oilWeight * x for x in red]
				wtrColor = [wtrWeight * x for x in blue]
				cell_color = list(map(add, oilColor, wtrColor))
				print(cell_color)
				#print("(% f, % f, % f)" % ( x, y, z))
				glColor3f(cell_color[0], cell_color[1], cell_color[2])

				DrawCube()
				glPopMatrix()
		#input()

	glPopMatrix()

#draw a cube, dimensions of 1 all directions, centered at 0,0,0
def DrawCube():

	vertices = (
		(-0.5, 0.5, 0.5), #0
		(-0.5, -0.5, 0.5), #1
		(0.5, -0.5, 0.5), #2
		(0.5, 0.5, 0.5), #3
		(0.5, 0.5, -0.5), #4
		(-0.5, 0.5, -0.5), #5
		(-0.5, -0.5, -0.5), #6
		(0.5, -0.5, -0.5) #7
		)

	tris = (
	(0, 1, 2), (0, 2, 3), #Front
	(0, 3, 5), (5, 3, 4), #Top
	(1, 6, 2), (2, 6, 7), #Bottom
	(5, 1, 0), (5, 6, 1), #Left
	(3, 2, 7), (3, 7, 4), #right
	(5, 7, 4), (5, 6, 7)) #back

	glBegin(GL_TRIANGLES)
	for tri in tris:
		for index in tri:
			glColor3f(vertices[index][0], vertices[index][1], vertices[index][2])
			glVertex3fv(vertices[index])
	glEnd()
