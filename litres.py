#! /usr/bin/python
import numpy
import measure

class litres:
	wheight=0
	daimeter=0
	area=0
	def __init__(self,h,d):
		self.height=h
		self.diameter=d
		self.area=numpy.pi*pow(d,2)/4
	def calculate(self,top_height):
		self.waterHeight=self.height-top_height
		return self.area*self.waterHeight*.001
if __name__=="__main__":
	t=measure.tank()
	t.select_max()
	l=litres(t.height,t.diameter)
	volume=l.calculate(0)					#change it later to suit the intel galileo board
	print volume

