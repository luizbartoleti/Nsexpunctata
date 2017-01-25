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
	Model = random.randint(5,8)

#variables
	ThetaCOI = random.uniform(0.1,20.0)
	ThetaCHP2 = random.uniform(0.1,20.0)
	DivTime = random.uniform(0.001, 0.053)
	ExpTime1 = random.uniform(0.0, 0.299)
	GrowthRatio = random.uniform(0.01,0.9)
	GrowthRate3 = -(1/ExpTime1) * math.log(GrowthRatio)
	GrowthRate4 = -(1/0.299) * math.log(GrowthRatio)
	GrowthRate5 = -(1/0.053) * math.log(GrowthRatio)
	N3 = random.uniform(5.0, 10.0)
	N4 = random.uniform(5.0, 10.0)
			

#ms's commands
	if Model == 5:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 | perl msSS.pl >> ./scenario2_COI.txt" % (ThetaCOI, DivTime))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 | perl msSS.pl >> ./scenario2_CHP2.txt" % (ThetaCHP2, DivTime))
		Counter += 1
	elif Model == 6:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 -eG %f %f -eG %f 0.0 | perl msSS.pl >> ./scenario2_COI.txt" % (ThetaCOI, DivTime, DivTime, GrowthRate3, ExpTime1))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 -eG %f %f -eG %f 0.0 | perl msSS.pl >> ./scenario2_CHP2.txt" % (ThetaCHP2, DivTime, DivTime, GrowthRate3, ExpTime1))
		Counter += 1
	elif Model == 7:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 -eN 0.053 %f -eG 0.053 %f -eG 0.299 0.0 | perl msSS.pl >> ./scenario2_COI.txt" % (ThetaCOI, DivTime, N3, GrowthRate4))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 -eN 0.053 %f -eG 0.053 %f -eG 0.299 0.0 | perl msSS.pl >> ./scenario2_CHP2.txt" % (ThetaCHP2, DivTime, N3, GrowthRate4))
		Counter += 1
	elif Model == 8:
		os.system("./ms 65 1 -t %f -I 2 23 42 -ej %f 2 1 -eG %f %f -eG 0.053 0.0 -eN 0.299 %f | perl msSS.pl >> ./scenario2_COI.txt" % (ThetaCOI, DivTime, DivTime, GrowthRate5, N4))
		os.system("./ms 130 1 -t %f -I 2 46 84 -ej %f 2 1 -eG %f %f -eG 0.053 0.0 -eN 0.299 %f | perl msSS.pl >> ./scenario2_CHP2.txt" % (ThetaCHP2, DivTime, DivTime, GrowthRate5, N4))
		Counter += 1
	
		
#print prior values
	print '_%d\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f\t%f' % (Model, ThetaCOI, ThetaCHP2, DivTime, ExpTime1, GrowthRate3, GrowthRate4, GrowthRate5, N3, N4)
