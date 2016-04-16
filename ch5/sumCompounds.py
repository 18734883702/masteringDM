# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:26:48 2016

@author: megan
"""

from nltk.sentiment.vader import SentimentIntensityAnalyzer

with open('data/ubuntu2016-04-04/ubuntu.txt', encoding='utf-8') as ubuntu:
    ubuntuLines = [line.strip() for line in ubuntu.readlines()]
ubuntu.close()

with open('data/ubuntu2016-04-04/ubuntu-devel.txt', encoding='utf-8') as ubuntuDevel:
    ubuntuDevelLines = [line.strip() for line in ubuntuDevel.readlines()]
ubuntuDevel.close()

listOfChannels = [ubuntuLines,ubuntuDevelLines]
sid = SentimentIntensityAnalyzer()
for channel in listOfChannels:
    finalScore = 0
    for line in channel:
        ss = sid.polarity_scores(line)    
        score = ss['compound']
        finalScore = finalScore + score
    
    roundedFinalScore = round(finalScore/len(channel),4)
    print("Score", roundedFinalScore)
