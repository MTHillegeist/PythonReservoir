#from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin,cos,sqrt,pi,floor
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
		self.pressure = 1.0

class Reservoir(object):
	"""docstring for Reservoir."""

	def __init__(self, width, height, depth, cell_dim):
		super(Reservoir, self).__init__()
		self.width = width
		self.height = height
		self.depth = depth
		self.cell_dim = cell_dim
		#Creates grid with a new defualt Cell for every element.
		self.grid = [[[Cell() for _ in range(depth)] for _ in range(height)] for _ in range(width)]

		# for i in range(self.width):
		# 	for j in range(self.height):
		# 		for k in range(self.depth):
		# 			print("(% f, % f, % f)" % ( i, j, k))
		# 			print(self.grid[i][j][k])

	def SetCellsValue(self, region, source, value):
		for i in range(region.iStart,region.iEnd + 1):
			for j in range(region.jStart,region.jEnd + 1):
				for k in range(region.kStart,region.kEnd + 1):
					#Set properties of the current cell.
					#print(i,j,k)
					cell = self.grid[i][j][k]
					cell.oilPct = 0.0
					cell.wtrPct = 100.0
					# cell_prop = getattr(cell, source)
					# cell_prop = value
