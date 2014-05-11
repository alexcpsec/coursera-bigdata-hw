import Orange


data = Orange.data.Table("genestrain")
classifier = Orange.classification.bayes.NaiveLearner(data)

data2 = Orange.data.Table("genesblind")

for i in range(0, len(data)):
	print "%s : originally %s" % (classifier(data[i]), data[i].getclass())

for i in range(0, len(data2)):
	print "%s : originally %s" % (classifier(data2[i]), data2[i].getclass())

"## -- End pasted text --"
"CEU :0: originally ?"
"CEU :0: originally ?"
"CEU :0: originally ?"
"CEU :0: originally ?"
"ASW :3: originally ?"
"YRI :4: originally ?"
"YRI :4: originally ?"
"CEU :0: originally ?"
"JPT :2: originally ?"
"GIH :1: originally ?"
"ASW :3: originally ?