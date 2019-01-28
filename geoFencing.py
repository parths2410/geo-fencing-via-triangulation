
points = [(19.164755, 72.851630),(19.164865, 72.851796),(19.164643, 72.851802),(19.164668,72.851705)]
point_in = (19.164746, 72.851730)
my_point = (19.164738, 72.851682)
my_point_out = (19.164837, 72.851889)


##SANJAY GANDHI NATIONAL PARK
#points = [(19.164468, 72.851736),(19.164462, 72.852083),(19.164193, 72.851955),(19.164295, 72.852107),(19.164253, 72.851778)]
#point_in = (19.164359, 72.851950)
#my_point = (19.164335, 72.851903)




# Gives output whether a location point (my_location) is inside a defined convex polygon (Based on polygon_coordinates).
def fencing(polygon_coordinates,inside_point,my_location):
	polygon_coordinates.append(polygon_coordinates[0]) #completing the polygon figure (start point=end point)
	length = len(polygon_coordinates)

	#Creating a list of three points to make triangular sub-fence
	tri_list = []
	i=0
	while i < length:
		#Appending co-ordinates of sub-fence
		tri_list.append(polygon_coordinates[i])   #first points
		tri_list.append(polygon_coordinates[i+1]) #next consecutive points
		tri_list.append(inside_point) #inside_point as third point

		tri_chk = 0 #Triangle checker

		#Rotating the 3 point's coordinates to remove OBTUSE ANGLE ANAMOLY
		'''
		*OBTUSE ANGLE ANAMOLY=because conditions fail for an obtuse angled side of triangle (only one obtuse angle in a triangle is possible),
		hence we rotate the points of triangle (pt_1,pt_2,pt_3) to check thrice and pass it only when true atleast 2 times.
		'''
		p1 = 0
		while p1 < 3:
			p2 = p1 + 1
			p3 = p2 + 1
			if p1 == 2:
				p2 = 0
				p3 = 1
			if p2 == 2:
				p3 = 0

			#Assigning of points
			pt_1=tri_list[p1]
			pt_2=tri_list[p2]
			pt_3=tri_list[p3]

			#Linear Distance Equation
			line_13_wrt_my_location = (my_location[0] - pt_1[0]) - ( ( (pt_3[0] - pt_1[0]) * (my_location[1] - pt_1[1]) ) / (pt_3[1] - pt_1[1]) )

			line_23_wrt_my_location = (my_location[0] - pt_2[0]) - ( ( (pt_3[0] - pt_2[0]) * (my_location[1] - pt_2[1]) ) / (pt_3[1] - pt_2[1]) )

			line_12_wrt_my_location = (my_location[0] - pt_1[0]) - ( ( (pt_2[0] - pt_1[0]) * (my_location[1] - pt_1[1]) ) / (pt_2[1] - pt_1[1]) )

			line_12_wrt_3           = (pt_3[0] - pt_1[0]) - ( ( (pt_2[0] - pt_1[0]) * (pt_3[1] - pt_1[1]) ) / (pt_2[1] - pt_1[1]) )


			#To check if the point is in the triangular sub-fence
				#first check condition
			if (line_13_wrt_my_location <= 0 and line_23_wrt_my_location >= 0) or (line_13_wrt_my_location >= 0 and line_23_wrt_my_location <= 0):
				chk_1 = 1
			else:
				chk_1 = 0

				#second check condition
			if (line_12_wrt_my_location <= 0 and line_12_wrt_3 <= 0) or (line_12_wrt_my_location >= 0 and line_12_wrt_3 >= 0):
				chk_2 = 1
			else:
				chk_2 = 0

				#if both conditions check,increase the triangle-checker(tri_chk) by 1
			if (chk_1 == 1 and chk_2 == 1):
				tri_chk += 1

			p1 += 1 #increment p1 by 1

		counter = 0
		#Check if the point is shown in atleast 2 times (tri_chk>=2) .
		if tri_chk >= 2:
			counter = 1
			break

		tri_list = []  #Re-initiate tri-list to empty for allowing the next triangular sub-fence

		i += 1  #increase i for loop

	#final output
	if counter == 1:
		print('in')
	else:
		print('out')


def main():                      # Define the main function
	fencing(points,point_in,my_point)


if __name__ == "__main__":
    main()

print('-----')
