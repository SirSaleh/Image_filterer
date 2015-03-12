class image_filterer (object):
	import os,sys
	import Image
	im = Image.new("RGB",[100,100])
	rgb_im=im.convert('RGB')
	output = "out.jpg"
	
	def __init__(self,image_location,output):
		self.image = image_location
		self.output = output
		self.im = self.Image.open(self.image)
		rgb_im = self.im.convert('RGB')
	
	def make_gray(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.__init__.rgb_im.size[0]):
		   for j in range(0,self.__init__.rgb_im.size[1]):
		      a= int((self.__init__.rgb_im.getpixel((i, j))[1]+self.__init__.rgb_im.getpixel((i, j))[0]+self.__init__.rgb_im.getpixel((i, j))[2])/3)
		      rgb_im.putpixel((i,j), (a,a,a))

		#self.__init__.rgb_im.save(output, "JPEG", quality=80, optimize=True, progressive=True)

	def make_normal_blur(self):
		
		mat=[]
		for i in range(0,self.rgb_im.size[0]):
		   mat.append([])
		   for j in range(0,self.__init__.rgb_im.size[1]):
		      mat[i].append(self.__init__.rgb_im.getpixel((i, j)))

		# RGB matrix Obtained! For Example if you want i,j'th pixles red channel it's enough for you: mat[i][j][0] // 0 for red! 1 for green 2 for blue
		for i in range(0,self.__init__.rgb_im.size[0]-1):
		   for j in range(0,self.__init__.rgb_im.size[1]-1):
		      r=(mat[i-1][j-1][0]+mat[i][j-1][0]+mat[i+1][j-1][0]+mat[i+1][j][0]+mat[i+1][j+1][0]+mat[i][j+1][0]+mat[i-1][j+1][0]+mat[i-1][j][0])/8
		      g=(mat[i-1][j-1][1]+mat[i][j-1][1]+mat[i+1][j-1][1]+mat[i+1][j][1]+mat[i+1][j+1][1]+mat[i][j+1][1]+mat[i-1][j+1][1]+mat[i-1][j][1])/8
		      b=(mat[i-1][j-1][2]+mat[i][j-1][2]+mat[i+1][j-1][2]+mat[i+1][j][2]+mat[i+1][j+1][2]+mat[i][j+1][2]+mat[i-1][j+1][2]+mat[i-1][j][2])/8
		      self.__init__.rgb_im.putpixel((i,j),(r,g,b))
		
		
		
		#rgb_im.save(out, "JPEG", quality=80, optimize=True, progressive=True)

	def show(self):
		self.__init__.rgb_im.show()

	def save(self):
		self.__init__.rgb_im.save(out, "JPEG", quality=80, optimize=True, progressive=True)
		



GIMP = image_filterer('a.jpg','o.jpg')
print GIMP.output
GIMP.make_normal_blur()
GIMP.show()
GIMP.save()
dir (GIMP)
