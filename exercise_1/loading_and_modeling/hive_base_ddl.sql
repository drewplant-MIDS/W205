DROP TABLE EffectiveCareBase;
CREATE EXTERNAL TABLE EffectiveCareBase (HospitalID VARCHAR(8), 
HospitalName VARCHAR(52),
Address VARCHAR(46),
City VARCHAR(22),
State VARCHAR(4),
ZipCode VARCHAR(7),
County VARCHAR(22),
Phone VARCHAR(12),
Condition VARCHAR(37),
MeasureID VARCHAR(18),
MeasureName VARCHAR(137),
Score VARCHAR(44),
Sample VARCHAR(15),
Footnote VARCHAR(181),
MeasureStartDate VARCHAR(12),
MesureEndDate VARCHAR(12))
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/EffectiveCare';

-- Load the table from hadoop repo
LOAD DATA INPATH '/user/w205/hospital_compare/stripeffective_care.csv'
OVERWRITE INTO TABLE EffectiveCareBase;

DROP TABLE HospitalsBase;
CREATE EXTERNAL TABLE HospitalsBase (HospitalID VARCHAR(8), 
HospitalName VARCHAR(52),
Address VARCHAR(46),
City VARCHAR(22),
State VARCHAR(4),
ZipCode VARCHAR(7),
County VARCHAR(22),
Phone VARCHAR(12),
HospitalType VARCHAR(38),
HospitalOwner VARCHAR(45))
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/hospitals';

-- Load the table from hadoop repo
LOAD DATA INPATH '/user/w205/hospital_compare/striphospitals.csv'
OVERWRITE INTO TABLE HospitalsBase;

DROP TABLE MeasuresBase;
CREATE EXTERNAL TABLE MeasuresBase (MeasureName VARCHAR(89), 
MeasureID VARCHAR(20),
MeasStartQtr VARCHAR(8),
MeasStartDate VARCHAR(12),
MeasEndQtr VARCHAR(8),
MeasEndDate VARCHAR(12))
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/measures';

-- Load the table from hadoop repo
LOAD DATA INPATH '/user/w205/hospital_compare/stripmeasureDates.csv'
OVERWRITE INTO TABLE MeasuresBase;


DROP TABLE ReadmissionsAndDeathsBase;
CREATE EXTERNAL TABLE ReadmissionsAndDeathsBase (HospitalID VARCHAR(8), 
HospitalName VARCHAR(52),
Address VARCHAR(45),
City VARCHAR(22),
State VARCHAR(4),
ZipCode VARCHAR(7),
County VARCHAR(22),
Phone VARCHAR(12),
MeasureName VARCHAR(89),
MeasureID VARCHAR(20),
Comp2NatAvg VARCHAR(37),
Denominator VARCHAR(15),
Score VARCHAR(15),
LowerEstimate VARCHAR(15),
HigherEstimate VARCHAR(15),
Footnote VARCHAR(58),
MeasStartDate VARCHAR(12),
MeasEndDate VARCHAR(12))
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/ReadsAndDeaths';

-- Load the table from hadoop repo
LOAD DATA INPATH '/user/w205/hospital_compare/stripreadmissionsUndDeath.csv'
OVERWRITE INTO TABLE ReadmissionsAndDeathsBase ;


DROP TABLE SurveysBase;
CREATE EXTERNAL TABLE SurveysBase (HospitalID VARCHAR(8), 
HospitalName VARCHAR(52),
Address VARCHAR(46),
City VARCHAR(22),
State VARCHAR(4),
ZipCode VARCHAR(12),
County VARCHAR(22),
COMMNURSEAPTS VARCHAR(15), 
COMMNURSEIPTS VARCHAR(15), 
COMMNURSEDIMSCORE VARCHAR(15), 
COMMDOCSAPTS VARCHAR(15), 
COMMDOCSIPTS VARCHAR(15), 
COMMDOCSDIMSCORE VARCHAR(15), 
RESPSTAFFAPTS VARCHAR(15), 
RESPSTAFFIPTS VARCHAR(15), 
RESPSTAFFDIMSCORE VARCHAR(15), 
PAINMGTAPTS VARCHAR(15), 
PAINMGTIPTS VARCHAR(15), 
PAINMGTDIMSCORE VARCHAR(15), 
COMMMEDSAPTS VARCHAR(15), 
COMMMEDSIPTS VARCHAR(15), 
COMMMEDSDIMSCORE VARCHAR(15), 
CLEANQUIETAPTS VARCHAR(15), 
CLEANQUIETIPTS VARCHAR(15), 
CLEANQUIETDIMSCORE VARCHAR(15), 
DISCHARGEINFOAPTS VARCHAR(15), 
DISCHARGEINFOIPTS VARCHAR(15), 
DISCHARGEINFODIMSCORE VARCHAR(15), 
AchievePoints VARCHAR(15), 
ImprovePts VARCHAR(15), 
DimScore VARCHAR(15))
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde' 
STORED AS TEXTFILE
LOCATION '/user/w205/hospital_compare/Surveys';

-- Load the table from hadoop repo
LOAD DATA INPATH '/user/w205/hospital_compare/stripsurveys_responses.csv'
OVERWRITE INTO TABLE SurveysBase;
