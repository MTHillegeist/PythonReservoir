from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin,cos,sqrt,pi,floor
from operator import add
import Draw

class ResRegion(object):
	"""docstring for ResRegion."""

	def __init__(self):
		super(ResRegion, self).__init__()
		self.iStart = 0
		self.iEnd = 0
		self.jStart = 0
		self.jEnd = 0
		self.kStart = 0
		self.kEnd = 0


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
		#Creates grid with a new defualt Cell for every element.
		self.grid = [[[Cell() for _ in range(width)] for _ in range(height)] for _ in range(depth)]

		region = ResRegion()
		region.iStart = floor(width / 4)
		region.iEnd = floor(width / 4 * 3)
		region.jStart = floor(height / 4)
		region.jEnd = floor(height / 4 * 3)
		region.kStart = floor(depth / 4)
		region.kEnd = floor(depth / 4 * 3)

		self.SetCellsValue(region, "wtrPct", 100.0)
		self.SetCellsValue(region, "oilPct", 0.0)

		# for i in range(self.width-1):
		# 	for j in range(self.height-1):
		# 		for k in range(self.depth-1):
		# 			#Set properties of the current cell.
		# 			if i % 2 == 1:
		# 				self.grid[i][j][k].oilPct = 0.0
		# 				self.grid[i][j][k].wtrPct = 100.0

	def SetCellsValue(self, region, source, value):
		for i in range(region.iStart,region.iEnd):
			for j in range(region.jStart,region.jEnd):
				for k in range(region.kStart,region.kEnd):
					#Set properties of the current cell.
					cell = self.grid[i][j][k]
					cell.oilPct = 0.0
					cell.wtrPct = 100.0
					# cell_prop = getattr(cell, source)
					# cell_prop = value

def DrawGrid(res):
	red = (0.8, 0.1, 0.0, 1.0)
	blue = (0.0, 0.0, 0.8, 1.0)
	cell_dim = res.cell_dim
	glPushMatrix()
	glScalef(cell_dim, cell_dim, cell_dim)

	#print("cell_dim: % f" % cell_dim)
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
				#print(cell_color)
				#print("(% f, % f, % f)" % ( x, y, z))
				glColor3f(cell_color[0], cell_color[1], cell_color[2])

				#Draw.DrawCube()
				glutSolidCube(cell_dim)
				#glutWireCube(cell_dim)
				glPopMatrix()
		#input()

	glPopMatrix()
