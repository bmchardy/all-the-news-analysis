
##
## =======================================================
##   (C) Bobby McHardy
##   01-05-21
##   All The News 2020 Dataset
## =======================================================
##

import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# prep sentiment analyis
si_analyzer = SentimentIntensityAnalyzer()

# get post-processed file
time_start = time.time()
# HEADER: i0,i1,date,year,month,day,author,title,article,url,section,publication
data = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-sampling1575yr.csv", "r", encoding='utf-8')
lines = data.readlines()
linesnew = ['year,month,day,title-neg-sent,title-neu-sent,title-pos-sent,article-neg-sent,article-neu-sent,article-pos-sent,publication,title,url\n']
n = len(lines)

# start
print("NOTE: " + str(n) + " lines remaining.")

# done with this data
data.close()

# for each article
recent_mult_of_ten = -1
for i in range(n-1, -1, -1):
	# update ui
	if recent_mult_of_ten != (100 * i // n):
		print(str(i) + " lines remaining (" + str(100 * i // n) + "%; " + str(time.time() - time_start) + "s elapsed).")
		recent_mult_of_ten = (100 * i // n)
	# HEADER: i0,i1,date,year,month,day,author,title,article,url,section,publication
	# we'll want HEADER: year, month, day, title-neg-sent, title-neu-sent, title-pos-sent, article-neg-sent, article-neu-sent, article-pos-sent, publication, url
	parts = lines[i].replace('\r\n', '').replace('\r', '').replace('\n', '').split(',')
	sent_title = si_analyzer.polarity_scores(parts[7])
	sent_article = si_analyzer.polarity_scores(parts[8])
	linesnew.append(str(parts[3] + ',' + parts[4] + ',' + parts[5] + ',' + str(sent_title['neg']) + ',' + str(sent_title['neu']) + ',' + str(sent_title['pos']) + ',' + str(sent_article['neg']) + ',' + str(sent_article['neu']) + ',' + str(sent_article['pos']) + ',' + parts[11] + ',' + parts[7] + ',' + parts[9] + '\n'))
	del parts
	del sent_title
	del sent_article
	del lines[i]

# flat file for dictionary
new_file = open(r"C:\Users\26hmk\Downloads\all-the-news-2-1-table.csv", "w", encoding='utf-8')
# write lines to the new file
new_file.writelines(linesnew)
# close the new corpus
new_file.close()
lines = None