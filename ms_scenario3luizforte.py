#!/usr/bin/python

#import the required modules
import random
import os
import math

#draw from prior
SimNum = 400000
Counter = 0


#while loop
while Counter < SimNum:
	Model = random.randint(9,12)

#variables
	ThetaCOI = random.uniform(0.1,20.0)
	ThetaCHP2 = random.uniform(0.1,20.0)
	DivTime = random.uniform(0.299, 6.45)
	ExpTime2 = random.uniform(0.0, DivTime)
	ExpTime3 = random.uniform(0.0, DivTime)
	GrowthRatio = random.uniform(0.01,0.9)
	GrowthRate6 = -(1/ExpTime2) * math.log(GrowthRatio)
	GrowthRate7 = -(1/ExpTime3) * math.log(GrowthRatio)
	GrowthRate8 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate9 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate10 = -(1/0.053) * math.log(GrowthRatio)
	GrowthRate11 = -(1/0.053) * math.log(GrowthRatio)
	N5 = random.uniform(5.0, 10.0)
	N6 = random.uniform(5.0, 10.0)
	N7 = random.uniform(5.0, 10.0)
	N8 = random.uniform(5.0, 10.0)
	
		

#ms's commands
	if Model == 9:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 | perl msSS.pl >> ./scenario3_COI.txt" % (ThetaCOI, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 | perl msSS.pl >> ./scenario3_CHP2.txt" % (ThetaCHP2, DivTime))
		Counter += 1
	elif Model == 10:
		os.system("./ms 65 1 -t %f -I 2 23 42 -g 1 %f -g 2 %f -eg %f 1 0.0 -eg %f 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario3_COI.txt" % (ThetaCOI, GrowthRate6, GrowthRate7, ExpTime2, ExpTime3, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -g 1 %f -g 2 %f -eg %f 1 0.0 -eg %f 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario3_CHP2.txt" % (ThetaCHP2, GrowthRate6, GrowthRate7, ExpTime2, ExpTime3, DivTime))
		Counter += 1
	elif Model == 11:
		os.system("./ms 65 1 -t %f -I 2 23 42 -en 0.053 1 %f -eg 0.053 1 %f -en 0.053 2 %f -eg 0.053 2 %f -eg 0.299 1 0.0 -eg 0.299 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario3_COI.txt" % (ThetaCOI, N5, GrowthRate8, N6, GrowthRate9, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -en 0.053 1 %f -eg 0.053 1 %f -en 0.053 2 %f -eg 0.053 2 %f -eg 0.299 1 0.0 -eg 0.299 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario3_CHP2.txt" % (ThetaCHP2, N5, GrowthRate8, N6, GrowthRate9, DivTime))
		Counter += 1
	elif Model == 12:
		os.system("./ms 65 1 -t %f -I 2 23 42 -g 1 %f -g 2 %f -eg 0.053 1 0.0 -eg 0.053 2 0.0 -en 0.299 1 %f -en 0.299 2 %f -ej %f 2 1 | perl msSS.pl >> ./scenario3_COI.txt" % (ThetaCOI, GrowthRate10, GrowthRate11, N7, N8, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -g 1 %f -g 2 %f -eg 0.053 1 0.0 -eg 0.053 2 0.0 -en 0.299 1 %f -en 0.299 2 %f -ej %f 2 1 | perl msSS.pl >> ./scenario3_CHP2.txt" % (ThetaCHP2, GrowthRate10, GrowthRate11, N7, N8, DivTime))
		Counter += 1
	
		
#print prior values
	print '_%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f' % (Model, ThetaCOI, ThetaCHP2, GrowthRate6, GrowthRate7, ExpTime2, ExpTime3, N5, N6, GrowthRate8, GrowthRate9, GrowthRate10, GrowthRate11, N7, N8, DivTime)
