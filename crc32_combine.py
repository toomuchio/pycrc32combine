def gf2_matrix_square(square, mat):
	for n in range(0, 32):
		if (len(square) < (n + 1)):
			square.append(gf2_matrix_times(mat, mat[n]))
		else:
			square[n] = gf2_matrix_times(mat, mat[n])
	return square

def gf2_matrix_times(mat, vec):
	sum = 0
	i = 0
	while vec:
		if (vec & 1):
			sum = sum ^ mat[i]
		vec = (vec >> 1) & 0x7FFFFFFF
		i = i + 1
	return sum

def crc32_combine(crc1, crc2, len2):
	even = []
	odd = []
	if (len2 == 0):
		return crc1

	odd.append(0xEDB88320L)
	row = 1

	for n in range(1, 32):
		odd.append(row)
		row = row << 1

	even = gf2_matrix_square(even, odd)
	odd = gf2_matrix_square(odd, even)

	while (len2 != 0):
		even = gf2_matrix_square(even, odd)
		if (len2 & 1):
			crc1 = gf2_matrix_times(even, crc1)
		len2 = len2 >> 1
  
		if (len2 == 0):
			break
  
		odd = gf2_matrix_square(odd, even)
		if (len2 & 1):
			crc1 = gf2_matrix_times(odd, crc1)
		len2 = len2 >> 1
  
	crc1 = crc1 ^ crc2
	return crc1

