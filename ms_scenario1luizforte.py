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
	Model = random.randint(1,4)

#variables
	ThetaCOI = random.uniform(0.1,20.0)
	ThetaCHP2 = random.uniform(0.1,20.0)
	ExpTime = random.uniform(0.0,6.45)
	GrowthRatio = random.uniform(0.01,0.9)
	GrowthRate = -(1/ExpTime) * math.log(GrowthRatio)
	GrowthRate1 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate2 = -(1/0.053) * math.log(GrowthRatio)
	N1 = random.uniform(5.0, 10.0)
	N2 = random.uniform(5.0, 10.0)
		

#ms's commands
	if Model == 1:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej 0.0001 2 1 | perl msSS.pl >> ./scenario1_COI.txt" % (ThetaCOI))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej 0.0001 2 1 | perl msSS.pl >> ./scenario1_CHP2.txt" % (ThetaCHP2))
		Counter += 1
	elif Model == 2:
		os.system("./ms 65 1 -t %f -I 2 23 42 -G %f -ej 0.0001 2 1 -eG %f 0.0 | perl msSS.pl >> ./scenario1_COI.txt" % (ThetaCOI, GrowthRate, ExpTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -G %f -ej 0.0001 2 1 -eG %f 0.0 | perl msSS.pl >> ./scenario1_CHP2.txt" % (ThetaCHP2, GrowthRate, ExpTime))
		Counter += 1
	elif Model == 3:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej 0.0001 2 1 -eN 0.053 %f -eG 0.053 %f -eG 0.299 0.0 | perl msSS.pl >> ./scenario1_COI.txt" % (ThetaCOI, N1, GrowthRate1))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej 0.0001 2 1 -eN 0.053 %f -eG 0.053 %f -eG 0.299 0.0 | perl msSS.pl >> ./scenario1_CHP2.txt" % (ThetaCHP2, N1, GrowthRate1))
		Counter += 1
	elif Model == 4:
		os.system("./ms 65 1 -t %f -I 2 23 42 -G %f -ej 0.0001 2 1 -eG 0.053 0.0 -eN 0.299 %f | perl msSS.pl >> ./scenario1_COI.txt" % (ThetaCOI, GrowthRate2, N2))
		os.system("./ms 130 1 -t %f -I 2 46 84 -G %f -ej 0.0001 2 1 -eG 0.053 0.0 -eN 0.299 %f | perl msSS.pl >> ./scenario1_CHP2.txt" % (ThetaCHP2, GrowthRate2, N2))
		Counter += 1
	
		
#print prior values
	print '_%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f' % (Model, ThetaCOI, ThetaCHP2, GrowthRate, GrowthRate1, GrowthRate2, ExpTime, N1, N2)
