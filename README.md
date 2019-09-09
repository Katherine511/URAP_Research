## UC Berkeley Haas NueroEconomics Research 

In this repo you will find the following files: 

- addUnderscore.py: replace target words with the correct format, e.g. "San Francisco Giants" --> "San_Francisco_Giants" and use multitasking thread to improve runtime efficiency;

- webScraping.py: scrapped company names from wikipedia. 

- train.py: training script of a GloVe model on the pre-processed corpora. 

The training of a multi-token GloVe model can be separated into three parts: 1) Data acquisition of pre-trained corpora. 2) Data pre-processing and engineering, which involves tokenizing the corpora and adding underscore between multigram words, forcing the machine to treat them as a single vector. 3) Model training, which is basically running the python script on the pre-processed corpora. I used Wikipedia 2010 dump for the model training.

Running a few word similarity task on the HPC cluster will yield the following results. The numbers in the parentheses are the Euclidean distance between two word vectors, which provides an effective method for measuring the linguistic or semantic similarity of the corresponding words. 

Another thing that I looked at is the word analogies task: a to b is as c to d. The capital-country relation can be used to perform this task. For instance, Athens to Greece is as Beijing to China. It turned out that the Euclidean distance between Athens and Greece is 0.68 while the distance between Beijing and China is 0.63; Another example of word analogies task is using adjective and comparative adjective, such as “safe to safer is as young to younger”. In our model, the Euclidean distance from safe to safer is 0.61, and the distance from young to younger is 0.66. From what I observed in these tasks, the model performed well. 






