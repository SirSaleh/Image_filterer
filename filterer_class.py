GIMP.make_gray()GIMP.make_gray()class image_filterer (object):
	import os,sys
	import Image
	rgb_im = Image.new("RGB",[0,0])
	image_location = ""
	output = "out.jpg"
	
	def __init__(self,image_location,output):
		self.image_location = image_location
		self.output = output
		self.rgb_im = self.Image.open(image_location)
		self.rgb_im = self.rgb_im.convert('RGB')
	
	def make_gray(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.rgb_im.size[0]):
		   for j in range(0,self.rgb_im.size[1]):
		      a= int((self.rgb_im.getpixel((i, j))[1]+self.rgb_im.getpixel((i, j))[0]+self.rgb_im.getpixel((i, j))[2])/3)
		      self.rgb_im.putpixel((i,j), (a,a,a))
		
		return self

		#self.rgb_im.save(output, "JPEG", quality=80, optimize=True, progressive=True)

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
		
		
		
		#rgb_im.save(out, "JPEG", quality=80, optimize=True, progressive=True)

	def show(self):
		self.rgb_im.show()

	def save(self):
		self.rgb_im.save(out, "JPEG", quality=80, optimize=True, progressive=True)
		



GIMP = image_filterer('a.jpg','o.jpg')
print GIMP.output
GIMP.make_gray()
GIMP.make_normal_blur()
GIMP.show()
GIMP.save()
dir (GIMP)
