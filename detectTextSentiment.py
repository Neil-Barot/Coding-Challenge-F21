import textcaret
from textcaret import TextSentiment

def averageSentiment(text):
    sentence = TextSentiment(text)
    avgSent = sentence.sentiment()['sentiment'].polarity
    return avgSent

def lineSentiment(text):
    sentence = TextSentiment(text)
    sent = sentence.sentiment()['sentiment'].polarity
    if sent < 0:
        return -1
    elif sent > 0:
        return 1
    else:
        return 0

def nextPunctuation(text, start):
    punctuation = [".", "!", "?"]
    spot = 0
    closestPunctuation = 999999999
    for character in punctuation:
        spot = text.find(character, start)
        if spot < closestPunctuation:
            closestPunctuation = spot
    
    return closestPunctuation

def solve(fileName):
    f = open(fileName, "r")
    doc = f.read()
    startSearch = 0
    spotString = ""
    spotPunctuation = 0
    spot = 0
    negative = 0
    positive = 0
    neutral = 0

    while(spotPunctuation != -1):
        spotPunctuation = nextPunctuation(doc, startSearch)
        spotString = doc[startSearch : spotPunctuation + 1]
        startSearch = spotPunctuation + 1
        spot = lineSentiment(spotString)
        if spot == 1:
            positive += 1
        elif spot == -1:
            negative += 1
        else:
            neutral += 1
    positivePercent = (positive/(positive + negative + neutral)) * 100
    negativePercent = (negative/(positive + negative + neutral)) * 100
    neutralPercent = (neutral/(positive + negative + neutral)) * 100
    print("\nThe sentiment of the sentences making up this text is:\n" + str(positivePercent) + "% positive\n" + str(negativePercent) + "% negative\n" + str(neutralPercent) + "% neutral\n")

    print("The average sentiment of this text is:")
    spot = averageSentiment(doc)
    if spot > 0:
        print(str(spot*100) + "% positive\n")
    elif spot < 0:
        print(str(spot*-100) + "% negative\n")
    else:
        print(str(spot*100) + "% neutral\n")
        

solve("input.txt")