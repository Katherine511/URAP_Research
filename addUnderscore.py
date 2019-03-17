import re
from flashtext.keyword import KeywordProcessor 

title = open("nGramsCompNames.txt", "r")
sentence = open("sentences_short.txt", "r")
output = open("clean_sentences.txt", "w")

keyword_processor = KeywordProcessor()
for line in title.readlines():
	string = line.split()
	# add target words to the keyword processor
	keyword_processor.add_keyword(string[0].replace("_", " "), string[0]) 

for sentence in sentence: 
	target = keyword_processor.extract_keywords(sentence)
	# replace words in the sentence with target words from nGramsCompNames.txt
	new_line = keyword_processor.replace_keywords(sentence)
	output.write(new_line)

output.close()


