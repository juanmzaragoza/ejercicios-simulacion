from scipy import stats

(a,p) = stats.chisquare([0,0,24,2,25,3,32,15,2,2])

if(1-p<0.01):
	print("Los valores corresponden a una distribu uniforme con p=",p,",alfa=0,01")
else:
	print("Los valores NO corresponden a una distribu uniforme p =",p,",alfa=0,01")

(a,p) = stats.chisquare([24,2,25,3,32,15,2,2])

if(1-p<0.01):
	print("Los valores corresponden a una distribu uniforme con p=",p,",alfa=0,01")
else:
	print("Los valores NO corresponden a una distribu uniforme p =",p,",alfa=0,01")