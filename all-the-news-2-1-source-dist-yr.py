
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
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-gtr2015.csv", "r", encoding='utf-8')
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
	# remove all columns except publication
	s = lines[i].split(',')[11].replace('\r\n', '').replace('\r', '').replace('\n', '') + lines[i].split(',')[3]
	if s in sources:
		sources[s] += 1
	else:
		sources[s] = 1
	del s

# summarize stats
output = 'Fox News2016:' + str(sources['Fox News2016']) + ', Fox News2017:' + str(sources['Fox News2017']) + ', Fox News2018:' + str(sources['Fox News2018']) + ', The New York Times2016:' + str(sources['The New York Times2016']) + ', The New York Times2017:' + str(sources['The New York Times2017']) + ', The New York Times2018:' + str(sources['The New York Times2018']) + ', The New York Times2019:' + str(sources['The New York Times2019']) + ', The New York Times2020:' + str(sources['The New York Times2020']) + ', CNN2016:' + str(sources['CNN2016']) + ', CNN2017:' + str(sources['CNN2017']) + ', CNN2018:' + str(sources['CNN2018']) + ', CNN2019:' + str(sources['CNN2019']) + ', CNN2020:' + str(sources['CNN2020'])

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-source-dist-yr.txt", "w", encoding='utf-8')
# write lines to the new file
new_file.write(output)
# close the new corpus
new_file.close()
lines = None