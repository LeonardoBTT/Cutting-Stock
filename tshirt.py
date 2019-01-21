#############################################################
##
## NOME
##   tshirt.py
##
## DESCRICAO
##   Procura as melhores combinacoes de cortes de camisetas.
##
## Escrito por:
## leonardo bittencourt da silva
##
## E-mail:
## leonardo.bits@gmail.com
##
#############################################################

import math
import numpy as np
import matplotlib.pyplot as plt

# xo => Start point on the x-axis.
# xf => End point on the x-axis.
# yo => Start point on the y-axis.
# yf => End point on the y-axis.

# Returns the cut vectors based on the point of origin and the angle of rotation.
def make(xo, yo, angle):
	tshirt=[]
	xf, yf = 0, 30

	# Rotates the vector based on the steering angle.
	# xfo => Rotation assist on x-axis.
	# yfo => Rotation assist on y-axis.
	def rotaciona(xf, yf):
		xfo,yfo= math.cos(angle)*xf - math.sin(angle)*yf, math.sin(angle)*xf + math.cos(angle)*yf
		xf,yf=xfo,yfo
		return xf,yf

	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, -5, -5
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, -3, 5
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, 8.5, 8
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, 5, 0
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, 3, -2
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, 0, -36
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	xo, yo, xf, yf = xo+xf, yo+yf, -8.5, 0
	xf,yf = rotaciona(xf,yf)
	tshirt+=[xo, yo, xf, yf],
	return tshirt

tshirt1 = make(10,10,0)
tshirt2 = make(50,30,-20)

tshirts=[]
tshirts+=tshirt1
tshirts+=tshirt2

soa = np.array(tshirts)

X, Y, U, V = zip(*soa)

plt.figure()

ax = plt.gca()	

ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)

ax.set_xlim([-1, 120])

ax.set_ylim([-1, 120])

plt.draw()

plt.show()
