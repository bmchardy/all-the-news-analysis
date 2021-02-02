
##
## =======================================================
##   (C) Bobby McHardy
##   01-05-21
##   All The News 2020 Dataset
## =======================================================
##

import time
import random

# get post-processed file
time_start = time.time()
# HEADER: i0,i1,date,year,month,day,author,title,article,url,section,publication
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-gtr2015.csv", "r", encoding='utf-8')
lines = data.readlines()

# done with this data
data.close()

n = len(lines)

# shuffle
print('Shuffling...')
random.shuffle(lines)
print('Shuffle complete.')

# start
print("NOTE: " + str(n) + " lines remaining.")

sources = {}

# for each article
recent_mult_of_ten = -1
for i in range(n-1, -1, -1):
	# update ui
	if recent_mult_of_ten != (100 * i // n):
		print(str(i) + " lines remaining (" + str(100 * i // n) + "%; " + str(time.time() - time_start) + "s elapsed).")
		recent_mult_of_ten = (100 * i // n)
	# select top 9053 of each source
	s = lines[i].split(',')[11].replace('\r\n', '').replace('\r', '').replace('\n', '') + lines[i].split(',')[3]
	if s in sources and sources[s] < 1575:
		# keep this line!
		sources[s] += 1
	elif s not in sources:
		# keep this line!
		sources[s] = 1
	else:
		# we can discard!
		del lines[i]

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-sampling1575yr.csv", "w", encoding='utf-8')
# write lines to the new file
new_file.writelines(lines)
# close the new corpus
new_file.close()
lines = None