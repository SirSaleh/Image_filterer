class image_filterer (object):
	import os,sys
	from PIL import Image
	rgb_im = Image.new("RGB",[0,0])
	image_location = ""
	
	def __init__(self,image_location):
		self.image_location = image_location
		self.rgb_im = self.Image.open(image_location)
		self.rgb_im = self.rgb_im.convert('RGB')

	##
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

	def make_normal_blur(self,level=1):
		mat=[]
		for i in range(0,self.rgb_im.size[0]):
		   mat.append([])
		   for j in range(0,self.rgb_im.size[1]):
		      mat[i].append(self.rgb_im.getpixel((i, j)))
	
		# RGB matrix Obtained! For Example if you want i,j'th pixles red channel it's enough for you: mat[i][j][0] // 0 for red! 1 for green 2 for blue TODO: Continue here
		for i in range(0,self.rgb_im.size[0]-1):
			for j in range(0,self.rgb_im.size[1]-1):
                                r=0
                                g=0
                                b=0
				for k in range(-1*level,level+1):
					for h in range (-1*level,level+1):
                                                if (i+k < self.rgb_im.size[0]-1 and j+h < self.rgb_im.size[1]-1 and i+k>=0 and j+h>=0):
							#print i,j,"---",i+k,j+h,"--",h+level,k+level
                                                        r=r+(mat[i+k][j+h][0])*(1/float((2*level+1)*(2*level+1)))
                                                        g=g+(mat[i+k][j+h][1])*(1/float((2*level+1)*(2*level+1)))
                                                        b=b+(mat[i+k][j+h][2])*(1/float((2*level+1)*(2*level+1)))
							#print level,(1/float((2*level+1)*(2*level+1)))
                                                else:
                                                        break;
                                self.rgb_im.putpixel((i,j),(r.__int__(),g.__int__(),b.__int__()))


	##
	# Method(s) to set Smooth (normal, Gausian) Blur to image
	##
	def make_gaussian_blur(self,level=1):
		# Must Use another method via KERNEL FUNCTIONS.
		weight=self.gaussian_weight_matrix(radius=level, sigma = 1.5)
		mat=[]
		for i in range(0,self.rgb_im.size[0]):
		   mat.append([])
		   for j in range(0,self.rgb_im.size[1]):
		      mat[i].append(self.rgb_im.getpixel((i, j)))
	
		# RGB matrix Obtained! For Example if you want i,j'th pixles red channel it's enough for you: mat[i][j][0] // 0 for red! 1 for green 2 for blue TODO: Continue here
		for i in range(0,self.rgb_im.size[0]-1):
			for j in range(0,self.rgb_im.size[1]-1):
                                r=0
                                g=0
                                b=0
				for k in range(-1*level,level+1):
					for h in range (-1*level,level+1):
                                                if (i+k < self.rgb_im.size[0]-1 and j+h < self.rgb_im.size[1]-1 and i+k>=0 and j+h>=0):
							#print i,j,"---",i+k,j+h,"--",h+level,k+level
                                                        r=r+(mat[i+k][j+h][0]*weight[k+level][h+level])
                                                        g=g+(mat[i+k][j+h][1]*weight[k+level][h+level])
                                                        b=b+(mat[i+k][j+h][2]*weight[k+level][h+level])
							
                                                else:
							
                                                        continue;
                                self.rgb_im.putpixel((i,j),(r.__int__(),g.__int__(),b.__int__()))
		

	##
	# Method(s) to make image Negative
	##
	
	def make_negative(self):
		r, g, b = self.rgb_im.getpixel((1, 1))
		for i in range(0,self.rgb_im.size[0]):
		   for j in range(0,self.rgb_im.size[1]):
		      self.rgb_im.putpixel((i,j), (255-self.rgb_im.getpixel((i, j))[0],255-self.rgb_im.getpixel((i, j))[1],255-self.rgb_im.getpixel((i, j))[2]))
		

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
	
	##########
	##########----Additional Methods (Private) But Can use public :)
	##########		
		##
	# Method(s) to calculate Gaussian Weight Matrix 
	# Here I set default Standard deviation to 1.5. Change it in argumant if you want. guassian _matrix(1 , 5) for SD=5 ie.
	##
	def gaussian_weight_matrix(self,radius=1, sigma = 1.5):
		import numpy as n
		g_mat = n.zeros([2*radius+1,2*radius+1]) # g_mat (Stands for Gausian Matrix) to store Gaustian weight matrix 
		g_mat = g_mat.tolist();
		#radius MUST be integer	
		for i in range(-1*radius,radius+1):
			for j in range(-1*radius,radius+1):
				g_mat[i+radius][j+radius]=self.guassian_function(i,j,sigma)

		g_sum_mat= (sum(a) for a in g_mat)
		g_sum= sum(g_sum_mat)
		for i in range(-1*radius,radius+1):
			for j in range(-1*radius,radius+1):
				g_mat[i+radius][j+radius]=g_mat[i+radius][j+radius]/g_sum
		return g_mat
		
	##
	# To caclulate Density of 2 independence Normal Random variable.
	##
	def guassian_function(self,x , y,sigma):
		import numpy as n
		return n.exp(-(x*x+y*y)/(2*sigma*sigma))/(2*sigma*sigma*n.pi)


if (__name__=="__main__"):
	print "Use the class easily"

