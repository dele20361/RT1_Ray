from gl import Raytracer, V3
from figures import *
from lights import *


width = 300
height = 300

# Materiales

white = Material(diffuse = (1, 1, 1))
orange = Material(diffuse = (1, 0.49, 0.31))
black = Material(diffuse = (0, 0, 0))
stone = Material(diffuse = (0.4, 0.4, 0.4))
grass = Material(diffuse = (0.3, 1, 0.3))

rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

#Cuerpo
rtx.scene.append( Sphere(V3(0,-3,-10), 2, white)  )
rtx.scene.append( Sphere(V3(0,0,-10), 1.5, white)  )
rtx.scene.append( Sphere(V3(0,2,-10), 1, white)  )

#Ojos
rtx.scene.append( Sphere(V3(0.35,2.1,-9.1), 0.1, white)  )
rtx.scene.append( Sphere(V3(0.35,2.15,-9), 0.06, black)  )
rtx.scene.append( Sphere(V3(-0.35,2.1,-9.1), 0.1, white)  )
rtx.scene.append( Sphere(V3(-0.35,2.15,-9), 0.06, black)  )

#Nariz
rtx.scene.append( Sphere(V3(0,1.9,-9.1), 0.2, orange)  )

#Boca
rtx.scene.append( Sphere(V3(-0.35,1.6,-9.2), 0.06, black)  )
rtx.scene.append( Sphere(V3(-0.10,1.5,-9.17), 0.06, black)  )
rtx.scene.append( Sphere(V3(0.1,1.5,-9.17), 0.06, black)  )
rtx.scene.append( Sphere(V3(0.35,1.6,-9.2), 0.06, black)  )

#Botones
rtx.scene.append( Sphere(V3(0,0.2,-8.5), 0.2, black)  )
rtx.scene.append( Sphere(V3(0,-1.2,-8.7), 0.3, black)  )
rtx.scene.append( Sphere(V3(0,-2.3,-8.2), 0.4, black)  )

rtx.glRender()

rtx.glFinish("output.bmp")