# Created by: Wendi Yu
# Created on: Dec 2018
# This program display calculation of value of cylinder

def volumeFormula(radius, height):
  # enter radius and height and return them
  
  PI =3.14
  Volume = PI * radius**2 * height
  return Volume

height = int(input("Height = "))
radius = int(input("Radius = "))

if height < 0 or radius < 0:
  print("Please input vaild number")
else:
  volume_print = volumeFormula(radius, height)
  print("The volume of cylinder is :" + str(volume_print) +"cm^3")

input()
