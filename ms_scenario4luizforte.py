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
	Model = random.randint(13,16)

#variables
	ThetaCOI = random.uniform(0.1,20.0)
	ThetaCHP2 = random.uniform(0.1,20.0)
	DivTime = random.uniform(6.45, 57.33)
	ExpTime4 = random.uniform(0.0, DivTime)
	ExpTime5 = random.uniform(0.0, DivTime)
	GrowthRatio = random.uniform(0.01,0.9)
	GrowthRate12 = -(1/ExpTime4) * math.log(GrowthRatio)
	GrowthRate13 = -(1/ExpTime5) * math.log(GrowthRatio)
	GrowthRate14 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate15 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate16 = -(1/0.053) * math.log(GrowthRatio)
	GrowthRate17 = -(1/0.053) * math.log(GrowthRatio)
	N9 = random.uniform(5.0, 10.0)
	N10 = random.uniform(5.0, 10.0)
	N11 = random.uniform(5.0, 10.0)
	N12 = random.uniform(5.0, 10.0)
	
		

#ms's commands
	if Model == 13:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 | perl msSS.pl >> ./scenario4_COI.txt" % (ThetaCOI, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 | perl msSS.pl >> ./scenario4_CHP2.txt" % (ThetaCHP2, DivTime))
		Counter += 1
	elif Model == 14:
		os.system("./ms 65 1 -t %f -I 2 23 42 -g 1 %f -g 2 %f -eg %f 1 0.0 -eg %f 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario4_COI.txt" % (ThetaCOI, GrowthRate12, GrowthRate13, ExpTime4, ExpTime5, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -g 1 %f -g 2 %f -eg %f 1 0.0 -eg %f 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario4_CHP2.txt" % (ThetaCHP2, GrowthRate12, GrowthRate13, ExpTime4, ExpTime5, DivTime))
		Counter += 1
	elif Model == 15:
		os.system("./ms 65 1 -t %f -I 2 23 42 -en 0.053 1 %f -en 0.053 2 %f -eg 0.053 1 %f -eg 0.053 2 %f -eg 0.299 1 0.0 -eg 0.299 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario4_COI.txt" % (ThetaCOI, N9, N10, GrowthRate14, GrowthRate15, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -en 0.053 1 %f -en 0.053 2 %f -eg 0.053 1 %f -eg 0.053 2 %f -eg 0.299 1 0.0 -eg 0.299 2 0.0 -ej %f 2 1 | perl msSS.pl >> ./scenario4_CHP2.txt" % (ThetaCHP2, N9, N10, GrowthRate14, GrowthRate15, DivTime))
		Counter += 1
	elif Model == 16:
		os.system("./ms 65 1 -t %f -I 2 23 42 -g 1 %f -g 2 %f -eg 0.053 1 0.0 -eg 0.053 2 0.0 -en 0.299 1 %f -en 0.299 2 %f -ej %f 2 1 | perl msSS.pl >> ./scenario4_COI.txt" % (ThetaCOI, GrowthRate16, GrowthRate17, N11, N12, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -g 1 %f -g 2 %f -eg 0.053 1 0.0 -eg 0.053 2 0.0 -en 0.299 1 %f -en 0.299 2 %f -ej %f 2 1 | perl msSS.pl >> ./scenario4_CHP2.txt" % (ThetaCHP2, GrowthRate16, GrowthRate17, N11, N12, DivTime))
		Counter += 1
	
		
#print prior values
	print '_%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f' % (Model, ThetaCOI, ThetaCHP2, GrowthRate12, GrowthRate13, ExpTime4, ExpTime5, N9, N10, GrowthRate14, GrowthRate15, N11, N12, GrowthRate16, GrowthRate17, DivTime)
