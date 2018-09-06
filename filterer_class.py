class image_filterer (object):
	import os,sys
	import numpy
	from PIL import Image
	rgb_im = Image.new("RGB",[0,0])
	image_location = ""

	def __init__(self,image_location):
		self.image_location = image_location
		self.rgb_im = self.Image.open(image_location)
		self.rgb_im = self.rgb_im.convert('RGB')
	
	def make_gray(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.rgb_im.size[0]):
			for j in range(0,self.rgb_im.size[1]):
				a= int((self.rgb_im.getpixel((i, j))[1]+self.rgb_im.getpixel((i, j))[0]+self.rgb_im.getpixel((i, j))[2])/3)
				self.rgb_im.putpixel((i,j), (a,a,a))
		return self

	def make_normal_blur(self,level=1):
		mat=[]
		for i in range(0,self.rgb_im.size[0]):
			mat.append([])
			for j in range(0,self.rgb_im.size[1]):
				mat[i].append(self.rgb_im.getpixel((i, j)))
		for i in range(0,self.rgb_im.size[0]-1):
			for j in range(0,self.rgb_im.size[1]-1):
				r=0
				g=0
				b=0
				for k in range(-1*level,level+1):
					for h in range (-1*level,level+1):
						if (i+k < self.rgb_im.size[0]-1 and j+h < self.rgb_im.size[1]-1 and i+k>=0 and j+h>=0):
							r=r+(mat[i+k][j+h][0])*(1/float((2*level+1)*(2*level+1)))
							g=g+(mat[i+k][j+h][1])*(1/float((2*level+1)*(2*level+1)))
							b=b+(mat[i+k][j+h][2])*(1/float((2*level+1)*(2*level+1)))
						else:
							break;
				self.rgb_im.putpixel((i,j),(r.__int__(),g.__int__(),b.__int__()))
		return self

	def make_negative(self):
		ImageMatrix = self.numpy.asarray(self.rgb_im)
		NegativeImageNumber = 255 - ImageMatrix
		NegativeImageInstance = self.Image.fromarray(NegativeImageNumber,'RGB')
		self.rgb_im = NegativeImageInstance
		return self

	def show(self):
		self.rgb_im.show()

if __name__=='__main__':
	# EXAMPLE USAGE:
	image = image_filterer('./test/a.jpg')
	#image.make_gray().make_normal_blur().show()