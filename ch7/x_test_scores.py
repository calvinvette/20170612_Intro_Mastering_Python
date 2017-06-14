#!/usr/bin/env python

scores = {}
scores_total = 0

with open("../DATA/testscores.dat") as f:

    for line in f:
        (name,score) = line.split(":")
        score = int(score)
        scores[name] =  { 'score': score }

        #scores['Fleck, Bela'] = 88

        scores_total += score

for student, dictValue in sorted(scores.items()):
    grade = None
    score = dictValue['score']
    if score > 94:
        dictValue['grade'] = 'A'
    elif score > 88:
        dictValue['grade'] = 'B'
    elif score > 82:
        dictValue['grade'] = 'C'
    elif score > 74:
        dictValue['grade'] = 'D'
    else:
        dictValue['grade'] = 'F'
    print("{0:<20s}\t{1}\t{2}".format(student,scores[student]['score'],scores[student]['grade']))

average = float(scores_total)/len(scores)
print("\naverage score is  {0:.2f}\n".format(average))



#result = requests.get('http://foo.com/api/customers')
