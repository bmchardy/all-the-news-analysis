
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
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-proc.csv", "r", encoding='utf-8')
lines = data.readlines()
linesnew = []
n = len(lines)

# start
print("NOTE: : " + str(n) + " lines remaining.")

# done with this data
data.close()

# for each file
recent_mult_of_ten = -1
for i in range(n-1, -1, -1):
	# update ui
	if recent_mult_of_ten != (100 * i // n):
		print(str(i) + " lines remaining (" + str(100 * i // n) + "%; " + str(time.time() - time_start) + "s elapsed).")
		recent_mult_of_ten = (100 * i // n)
	# is this a valid line?
	if len(lines[i].split(',https://www.')) > 1 and ("cnn.com" in lines[i].split(',https://www.')[1] or "nytimes.com" in lines[i].split(',https://www.')[1] or "thehill.com" in lines[i].split(',https://www.')[1] or "foxnews.com" in lines[i].split(',https://www.')[1]):
		linesnew.append(str(lines[i]))
	del lines[i]

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-select.csv", "w", encoding='utf-8')
# write lines to the new file
new_file.writelines(linesnew)
# close the new corpus
new_file.close()
lines = None