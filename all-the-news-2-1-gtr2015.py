
##
## =======================================================
##   (C) Bobby McHardy
##   01-05-21
##   All The News 2020 Dataset
## =======================================================
##

import time

# get post-processed file
time_start = time.time()
# HEADER: i0,i1,date,year,month,day,author,title,article,url,section,publication
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-line-removal.csv", "r", encoding='utf-8')
lines = data.readlines()
sources = {}
n = len(lines)

# start
print("NOTE: " + str(n) + " lines remaining.")

# done with this data
data.close()

# for each file
commas = 0
for i in range(n-1, -1, -1):
	# remove all < 2015 (only keep 2015 and greater)
	if int(lines[i].split(',')[3]) < 2015:
		del lines[i]

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-gtr2015.csv", "w", encoding='utf-8')
# write lines to the new file
new_file.writelines(lines)
# close the new corpus
new_file.close()
lines = None