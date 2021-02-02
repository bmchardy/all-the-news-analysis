
##
## =======================================================
##   (C) Bobby McHardy
##   12-22-20
##   A CORD-19 Dataset Aggregation.
##	 Dataset: AI2, CZI, MSR, Georgetown, NIH, & The White House
## =======================================================
##

import time

# get post-processed file
time_start = time.time()
# HEADER: i0,i1,date,year,month,day,author,title,article,url,section,publication
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-comma-removal.csv", "r", encoding='utf-8')
lines = data.readlines()
n = len(lines)

# start
print("NOTE: : " + str(n) + " lines remaining.")

# done with this data
data.close()

# for each file
commas = 0
for i in range(n-1, -1, -1):
	# remove all those lines that do not comply with the 12-column format (about 1500 lines; less than .5%)
	if len(lines[i].split(',')) != 12:
		del lines[i]

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-line-removal.csv", "w", encoding='utf-8')
# write lines to the new file
new_file.writelines(lines)
# close the new corpus
new_file.close()
lines = None