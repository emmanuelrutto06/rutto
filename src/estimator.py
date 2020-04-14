import json

my_data= {
"region": {
"name": "Africa",
"avgAge": 19.7,
"avgDailyIncomeInUSD": 5,
"avgDailyIncomePopulation": 0.71
},
"periodType": "days",
"timeToElapse": 58,
"reportedCases": 674,
"population": 66622705,
"totalHospitalBeds": 1380614
}


def currentlyInfectedimpact(my_data):
	wjdata = json.dumps(my_data["reportedCases"])
	return int(json.dumps(my_data["reportedCases"]))*10

def currentlyInfectedsevereImpact(my_data):
	return int(json.dumps(my_data["reportedCases"]))*50

def infectionsByRequestedTimeForImpact(my_data):
	return int(json.dumps(my_data["reportedCases"]))*(pow(2,9))*10

def infectionsByRequestedTimeForSevereImpact(my_data):
	return int(json.dumps(my_data["reportedCases"]))*(pow(2,9))*50



DAYS_IN_YEAR = 365
DAYS_IN_WEEK=7
DAYS_IN_MONTH=30 


# #duration_type =days,weeks,months,years
# #duration = a number representing a duration_type 
  
def find( duration_type,duration ):

	number_of_days=0
# 	# Assume that years is 
#      # of 365 days/ 
	if(duration_type=='weeks'):
		number_of_days=int(duration) * 7
	if(duration_type=='months'):
		number_of_days=int(duration) * 30
	if(duration_type=='years'):
		number_of_days =int(duration) * 365
	if(duration_type=='days'):
		number_of_days=int(duration)


	return int(number_of_days)

print(find('days',20 ))
print(find('months',4))
print(find('weeks',3 ))
print(find('years',2 ))

def severeCasesByRequestedTimeForImpact(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*(1.5%100))

def severeCasesByRequestedTimeForImpact(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*(75%100))

def NumberOfUsedBeds(my_data):
	return int(json.dumps(my_data["totalHospitalBeds"]))*(0.68)

def NumberofAvailableBedsForCovid(my_data):
	return int(json.dumps(my_data["totalHospitalBeds"]))- int(json.dumps(my_data["totalHospitalBeds"]))*int((0.68))

def hospitalBedsByRequestedTime(my_data):
	return int(json.dumps(my_data["totalHospitalBeds"]))- int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*(75))

def ImpactcasesFoICUByRequestedTime(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*0.5)

def SevereImpactcasesFoICUByRequestedTime(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*2.5)

def ImpactcasesForrVentilatorsByrequestedTime(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*0.2)

def SeverImpactcasesForVentilatorsByRequestedTime(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))*1)

def impactdollarsInFlight(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9)) *(0.325))


def SevereimpactdollarsInFlight(my_data):
	return int(json.dumps(my_data["reportedCases"]))*int((pow(2,9))* (1.625))




print(currentlyInfectedimpact(my_data))
print(currentlyInfectedsevereImpact(my_data))
print(infectionsByRequestedTimeForImpact(my_data))
print(infectionsByRequestedTimeForSevereImpact(my_data))
print(severeCasesByRequestedTimeForImpact(my_data))
print(NumberOfUsedBeds(my_data))
print(NumberofAvailableBedsForCovid(my_data))
print(hospitalBedsByRequestedTime(my_data))
print(ImpactcasesFoICUByRequestedTime(my_data))
print(SevereImpactcasesFoICUByRequestedTime(my_data))
print(ImpactcasesForrVentilatorsByrequestedTime(my_data))
print(SeverImpactcasesForVentilatorsByRequestedTime(my_data))
print(impactdollarsInFlight(my_data))
print(SevereimpactdollarsInFlight(my_data))


