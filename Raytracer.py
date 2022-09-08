from gl import Raytracer, V3
from figures import *
from lights import *


width = 600
height = 600

# Materiales

white = Material(diffuse = (1, 1, 1))
black = Material(diffuse = (0, 0, 0))
stone = Material(diffuse = (0.4, 0.4, 0.4))
grass = Material(diffuse = (0.3, 1, 0.3))



rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))


rtx.scene.append( Sphere(V3(0,-3,-10), 2, white)  )
rtx.scene.append( Sphere(V3(0,0,-10), 1.5, white)  )
rtx.scene.append( Sphere(V3(0,2,-10), 1, white)  )
rtx.scene.append( Sphere(V3(0,5,-2), 0.25, white)  )
rtx.scene.append( Sphere(V3(0,5,-2), 0.25, white)  )


rtx.glRender()

rtx.glFinish("output.bmp")