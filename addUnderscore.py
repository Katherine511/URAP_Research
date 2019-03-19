import re
from pathos import multiprocessing
from flashtext.keyword import KeywordProcessor 

title = open("nGramsCompNames.txt", "r")
sentences = open("sentences_short.txt", "r")
output = open("clean_sentences.txt", "w")

keyword_processor = KeywordProcessor(case_sensitive = True)
sentence = sentences.readlines() # create an iterable object of sentenes

for line in title.readlines():
	string = line.split()
	keyword_processor.add_keyword(string[0].replace("_", " "), string[0]) 

def addUnderscore(sentence):
	target = keyword_processor.extract_keywords(sentence)
	new_line = keyword_processor.replace_keywords(sentence)
	return new_line

pool = multiprocessing.Pool(processes = 4) 		# number of threads
for result in pool.imap_unordered(addUnderscore, sentence):
	output.write(result)

output.close()


