def countfreq(tmpList, dictl):
	tempStr = ','.join(tmpList)
	
	print tempStr

	if tempStr in dictl:
		dictl[tempStr] = dictl[tempStr] + 1
	else:
		dictl[tempStr] = 1


def checkmatch(frqs, parfrqs, nqs):

	for key in frqs:

		for parkey in parfrqs:

			fullist = key.split(',')
			parlist = parkey.split(',')
			count = 0
			for f,p in zip(fullist,parlist):
				if f == p and p != 'NA' and f != 'NA':
					count = count + 1
				elif f != p and (p == 'NA' or f == 'NA'):
					continue
				else:
					count = 0 
					break

			frac = float(count)/float(nqs)

			frqs[key] = frqs[key]+frac











def calcfreqs(infile, nqs, maxrat):

	#TODO update variable names

	#hash without NA and keys will be responses stored as strings (comma seperated) values are the frequencies as doubles
	frqs = {}

	#hash with NA same idea as frqs
	parfrqs = {}

	with open(infile,'rU') as f:
		for line in f:

			tmpList = []
			tmpList = line.split()

			if 'NA' in tmpList:
				countfreq(tmpList,parfrqs)
			else:
				countfreq(tmpList,frqs)

	checkmatch(frqs, parfrqs, nqs)

	# print "frqs hash"
	# for i in frqs:
	# 	print i,", ",frqs[i]
	# print "parfrqs hash"
	# for k in parfrqs:
	# 	print k,", ",parfrqs[k]

	return frqs




