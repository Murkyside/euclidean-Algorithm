# Timothy Gorst 3/12/2021
# This one shows off how long it takes to find the GCF of two numbers

# drawing stuff
from guizero import App, Drawing
import math

w = 500
h = 500
pan = 150
scale = 1
app = App(width=w, height=h)
drawing = Drawing(app, width=w, height=h)

def transform(coord):
    return coord * scale + pan
# end of drawing stuff

def euclideanAlgorithm(x,y,i):
  if x > y:
    x = x - y
    while x > y:
      x = x - y
    if y != 0:
      return(euclideanAlgorithm(y,x,i+1))
    else:
      return(x,i)
  else:
    y = y-x
    while y > x:
      y = y - x
    if y != 0:
      return(euclideanAlgorithm(x,y,i+1))
    else:
      return(y,i) 

def main():
  value = 0
  for x in range(-150,150):
    for y in range(-150,150):
      if x == 0 or y == 0:
        continue
      value = 10*euclideanAlgorithm(math.fabs(x),math.fabs(y),0)[1] 
      drawing.rectangle(transform(x),transform(y),transform(x)+5,transform(y)+5,color = (value*2,value*2,value*2))
main()
