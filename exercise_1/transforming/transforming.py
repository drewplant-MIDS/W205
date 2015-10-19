from pyspark.sql import SQLContext
from pyspark.sql.types import *
sqlContext = SQLContext(sc)
# Load hdfs files
HospitalCareFile = sc.textFile('/user/w205/hospital_compare/stripeffective_care.csv')
HospitalsFile = sc.textFile('/user/w205/hospital_compare/striphospitals.csv')
MeasuresFile = sc.textFile('/user/w205/hospital_compare/stripmeasureDates.csv')
ReadsUndDeathsFile = sc.textFile('/user/w205/hospital_compare/stripreadmissionsUndDeath.csv')
SurveysFile = sc.textFile('/user/w205/hospital_compare/stripsurveys_responses.csv')

# Break each file into proper records by splitting along '","' delimiters.
# ...Simply splitting by "," won't work because some of the individual 
# ...fields include commas.
HospitalCareParts = HospitalCareFile.map( lambda boohoo: boohoo.split("\",\""))
HospitalsParts = HospitalsFile.map( lambda boohoo: boohoo.split("\",\""))
MeasuresParts = MeasuresFile.map( lambda boohoo: boohoo.split("\",\""))
ReadsUndDeathsParts = ReadsUndDeathsFile.map( lambda boohoo: boohoo.split("\",\""))
SurveysParts = SurveysFile.map( lambda boohoo: boohoo.split("\",\""))

# Create filtered tables
# 1.  Effective Care
HospitalCare = HospitalCareParts.map(lambda p: (p[0], p[1], p[4], p[9], p[10], p[11]))
# Filter out non-numeric scores
HospitalCare = HospitalCare.filter(lambda p: len(p[5]) < 5)
schemaString = 'HospitalID HospitalName State MeasureID MeasureName Score'
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split() ]
schema = StructType(fields)
schemaHospitalCare = sqlContext.createDataFrame(HospitalCare, schema)
schemaHospitalCare.registerTempTable('HospitalCare')

# 2. Readmissions and Deaths
ReadsUndDeaths = ReadsUndDeathsParts.map(lambda p: (p[0][1:], p[1], p[4], p[9], p[10], p[12]))
## ...Filter out non-numeric scores
ReadsUndDeaths = ReadsUndDeaths.filter(lambda p: len(p[5]) < 5 )
## ...Convert Score field to float type to enable proper ordering in SQL
ReadsUndDeaths = ReadsUndDeaths.map(lambda p: (p[0], p[1], p[2], p[3], p[4], float(p[5])))

schemaString = 'HospitalID HospitalName State MeasureID Comp2National Score'
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split() ]
## ...Convert last fields tuple to FloatType
fields[5] = StructField('Score',FloatType(), True)
schema = StructType(fields)
schemaReadsUndDeaths = sqlContext.createDataFrame(ReadsUndDeaths, schema)
schemaReadsUndDeaths.registerTempTable('ReadsUndDeaths')

# 3. Hospitals
Hospitals = HospitalsParts.map(lambda p: (p[0], p[1], p[4]))
schemaString = 'HospitalID HospitalName State'
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split() ]
schema = StructType(fields)
schemaHospitals = sqlContext.createDataFrame(Hospitals, schema)
schemaHospitals.registerTempTable('Hospitals')

# 4. Measures
Measures = MeasuresParts.map(lambda p: (p[0], p[1]))
schemaString = 'MeasureName MeasureID'
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split() ]
schema = StructType(fields)
schemaMeasures = sqlContext.createDataFrame(Measures, schema)
schemaMeasures.registerTempTable('Measures')

# 5. Surveys
Surveys = SurveysParts.map(lambda p: (p[0], p[1],  p[4], p[29], p[30], p[31]))
schemaString = 'HospitalID HospitalName State AchievePoints ImprovePts DimScore'
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split() ]
schema = StructType(fields)
schemaSurveys = sqlContext.createDataFrame(Surveys, schema)
schemaSurveys.registerTempTable('Surveys')


# Let's answer some questions about this stuff...
# 1. Find MeasureHi, MeasureLow, Average over each hospital 
results = sqlContext.sql('SELECT C.HospitalID, C.HospitalName, AVG(Score) AS AvgScore, MIN(Score) AS MinScore, MAX(Score) AS MaxScore FROM HospitalCare AS C GROUP BY C.HospitalID, C.HospitalName ORDER BY C.HospitalName ASC')

results = sqlContext.sql('SELECT Avg(Score) FROM ReadsUndDeaths GROUP BY HospitalID')

results=sqlContext.sql('SELECT HospitalID, HospitalName, State, MeasureID, Comp2National, Score FROM ReadsUndDeaths')

results=sqlContext.sql('SELECT HospitalName, Avg(Score) FROM ReadsUndDeaths GROUP BY HospitalName')

results=sqlContext.sql('CREATE TABLE AvgReadsUnDeaths AS (SELECT HospitalName, HospitalID, State, Avg(Score) AS AvgScore FROM ReadsUndDeaths GROUP BY HospitalName, HospitalID, State ORDER BY AvgScore DESC)')

results=sqlContext.sql('SELECT HospitalName, HospitalID, State, MeasureID, Avg(Score) AS AvgScore FROM ReadsUndDeaths WHERE MeasureID="MORT*" GROUP BY HospitalName, HospitalID, State ORDER BY State')

# Create Table of AvgScore for MORTALITY_IN_30DAYS 
results=sqlContext.sql('SELECT HospitalName, HospitalID, State, MeasureID, Avg(Score) AS AvgScore FROM ReadsUndDeaths WHERE MeasureID LIKE \'MORT_30%\' GROUP BY HospitalName, HospitalID, State, MeasureID ORDER BY AvgScore ASC')

# This doesn't work:  Create Table of AvgScore for READMISSION_IN_30DAYS 
results=sqlContext.sql('CREATE TABLE AvgReads AS (SELECT HospitalName, HospitalID, State, MeasureID, Avg(Score) AS AvgScore FROM ReadsUndDeaths WHERE MeasureID LIKE \'READM_30%\' GROUP BY HospitalName, HospitalID, State, MeasureID ORDER BY AvgScore ASC)')
