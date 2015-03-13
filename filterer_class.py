class image_filterer (object):
	import os,sys
	import Image
	rgb_im = Image.new("RGB",[0,0])
	image_location = ""
	
	def __init__(self,image_location):
		self.image_location = image_location
		self.rgb_im = self.Image.open(image_location)
		self.rgb_im = self.rgb_im.convert('RGB')

	#
	# Method(s) to Make image Black and white 
	##
	def make_gray(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.rgb_im.size[0]):
		   for j in range(0,self.rgb_im.size[1]):
		      a= int((self.rgb_im.getpixel((i, j))[1]+self.rgb_im.getpixel((i, j))[0]+self.rgb_im.getpixel((i, j))[2])/3)
		      self.rgb_im.putpixel((i,j), (a,a,a))
	
		return self
	##
	# Method(s) to set Normal Blur to image
	##
	def make_normal_blur(self):
		
		mat=[]
		for i in range(0,self.rgb_im.size[0]):
		   mat.append([])
		   for j in range(0,self.rgb_im.size[1]):
		      mat[i].append(self.rgb_im.getpixel((i, j)))

		# RGB matrix Obtained! For Example if you want i,j'th pixles red channel it's enough for you: mat[i][j][0] // 0 for red! 1 for green 2 for blue
		for i in range(0,self.rgb_im.size[0]-1):
		   for j in range(0,self.rgb_im.size[1]-1):
		      r=(mat[i-1][j-1][0]+mat[i][j-1][0]+mat[i+1][j-1][0]+mat[i+1][j][0]+mat[i+1][j+1][0]+mat[i][j+1][0]+mat[i-1][j+1][0]+mat[i-1][j][0])/8
		      g=(mat[i-1][j-1][1]+mat[i][j-1][1]+mat[i+1][j-1][1]+mat[i+1][j][1]+mat[i+1][j+1][1]+mat[i][j+1][1]+mat[i-1][j+1][1]+mat[i-1][j][1])/8
		      b=(mat[i-1][j-1][2]+mat[i][j-1][2]+mat[i+1][j-1][2]+mat[i+1][j][2]+mat[i+1][j+1][2]+mat[i][j+1][2]+mat[i-1][j+1][2]+mat[i-1][j][2])/8
		      self.rgb_im.putpixel((i,j),(r,g,b))
	##
	# Method(s) to make image Negative
	##
	def make_negative(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.rgb_im.size[0]):
		   for j in range(0,self.rgb_im.size[1]):
		      self.rgb_im.putpixel((i,j), (255-self.rgb_im.getpixel((i, j))[0],255-self.rgb_im.getpixel((i, j))[1],255-self.rgb_im.getpixel((i, j))[2]))
		self.rgb_im.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
		
		#rgb_im.save(out, "JPEG", quality=80, optimize=True, progressive=True)
	##
	#Method(s) to show current image in X-Window system.
	##
	def show(self):
		self.rgb_im.show()
	##
	#Method(s) to save Current image in a file
	##
	def save(self,output_path):
		self.rgb_im.save(output_path, "JPEG", quality=80, optimize=True, progressive=True)
		


if (__name__=="__main__"):
	out = raw_input("obtain address to save the output!")
	GIMP = image_filterer('a.jpg')
	GIMP.make_gray()
	GIMP.make_normal_blur()
	GIMP.show()
	GIMP.save(out)
