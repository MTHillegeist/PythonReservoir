from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin,cos,sqrt,pi
from operator import add

vertices = (
	(-0.5, 0.5, 0.5),   #0
	(-0.5, -0.5, 0.5),  #1
	(0.5, -0.5, 0.5),   #2
	(0.5, 0.5, 0.5),    #3
	(0.5, 0.5, -0.5),   #4
	(-0.5, 0.5, -0.5),  #5
	(-0.5, -0.5, -0.5), #6
	(0.5, -0.5, -0.5))  #7


tris = (
(0, 1, 2), (0, 2, 3), #Front
(0, 3, 5), (5, 3, 4), #Top
(1, 6, 7), (1, 7, 2), #Bottom
(5, 1, 0), (5, 6, 1), #Left
(3, 2, 7), (3, 7, 4), #right
(5, 7, 4), (5, 6, 7)) #back

normals = (
(0.0, 0.0, 1.0),  #Front
(0.0, 1.0, 0.0),  #Top
(0.0, -1.0, 0.0), #Bottom
(-1.0, 0.0, 0.0), #Left
(1.0, 0.0, 0.0),  #Right
(0.0, 0.0, -1.0)) #Back



#draw a cube, dimensions of 1 all directions, centered at 0,0,0
def DrawCube():

	glBegin(GL_TRIANGLES)

	# for faceIndex in range(0, 1):
	# 	glNormal3f(normals[faceIndex * 2][0], normals[faceIndex * 2][1], normals[faceIndex * 2][2])
	# 	print("Begin drawing face %d" % faceIndex)
	# 	tri = vertices[faceIndex * 2]
	# 	glColor3f(tri[0], tri[1], tri[2])
	# 	glVertex3fv(tri)
	# 	print(tri)
	#
	# 	tri = vertices[faceIndex * 2 + 1]
	# 	glColor3f(tri[0], tri[1], tri[2])
	# 	glVertex3fv(tri)
	# 	print(tri)

		#print("End Drawing Face")

	#Drawing front face
	glNormal3f(normals[0][0], normals[0][1], normals[0][1])
	glColor3f(1.0, 0.0, 0.0)
	tri = tris[0]
	glVertex3fv(vertices[tri[0]])
	glVertex3fv(vertices[tri[1]])
	glVertex3fv(vertices[tri[2]])

	tri = tris[1]
	glVertex3fv(vertices[tri[0]])
	glVertex3fv(vertices[tri[1]])
	glVertex3fv(vertices[tri[2]])



	glEnd()


edges = (
	(0, 1),
	(1, 2),
	(2, 0))

def TriangleEquil(radius = 0.5):
	angleThird = 2.0 * pi / 3
	topAngle = pi / 2
	vertices = (
	(radius * cos(topAngle-angleThird), radius * sin(topAngle-angleThird), 0),
	(0.0, radius, 0),
	(radius * cos(topAngle + angleThird), radius * sin(topAngle + angleThird), 0))
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
