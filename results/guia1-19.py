from scipy import stats

(a,p) = stats.chisquare([25,8,17,20,13,13])

if(1-p<0.05):
	print("Los valores corresponden a una distribu uniforme con p=",p,",alfa=0,05")
else:
	print("Los valores NO corresponden a una distribu uniforme p =",p,",alfa=0,05")