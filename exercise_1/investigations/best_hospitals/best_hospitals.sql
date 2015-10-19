-- Create a table of average Measure Scores for each hospital
DROP TABLE HospBestMeasures;
CREATE TABLE HospBestMeasures AS
SELECT HospitalID, HospitalName, State, Avg(Cast(Score as float)) AS AvgScore
FROM EffectiveCare
GROUP BY HospitalID, HospitalName, State 
ORDER BY AvgScore DESC;

-- Create a table of average ReadsUndDeaths
DROP TABLE ReadsAndDeathsAvgScore;
CREATE TABLE ReadsAndDeathsAvgScore AS
SELECT HospitalID, HospitalName, State, Avg(Cast(Score as float)) AS AvgScore
FROM ReadmissionsAndDeaths
GROUP BY HospitalID, HospitalName, State
ORDER BY AvgScore ASC;

-- Create a table of average Survey Scores for each hospital
DROP TABLE SurveyAverages;
CREATE TABLE SurveyAverages AS
SELECT HospitalID, HospitalName, State, ((Cast(AchievePointsClean as float)+Cast(ImprovePointsClean as float)+Cast(DimScoreClean as float))/3) AS AvgOverall
FROM Surveys
ORDER BY AvgOverall DESC;

-- Join above three tables
DROP TABLE CombHospBestMeasures;
CREATE TABLE CombHospBestMeasures AS
SELECT hbm.HospitalID, hbm.HospitalName, hbm.State, hbm.AvgScore AS HospBestMeasAvgScore, rad.AvgScore AS ReadmAndDeathsAvgScore, sa.AvgOverall AS SurveyAvg
FROM HospBestMeasures AS hbm
INNER JOIN ReadsAndDeathsAvgScore AS rad
	ON hbm.HospitalID = rad.HospitalID
INNER JOIN SurveyAverages AS sa
	ON hbm.HospitalID = sa.HospitalID
ORDER BY HospBestMeasAvgScore DESC;

-- From this query we can see that Readmissions/Deaths min = 4.4% and max = 19.25%.  We can therefore convert the ReadmAndDeathsAvgScore score to a linear scale where 4.4% -> 100% and 19.25% -> 0%

DROP TABLE CombHospBMRSReads;
CREATE TABLE CombHospBMRSReads AS
SELECT HospitalID, HospitalName, State, HospBestMeasAvgScore, ReadmAndDeathsAvgScore, (19.25 - Cast(ReadmAndDeathsAvgScore as float)*100/(19.25-4.4)) AS RDMap, SurveyAvg
FROM CombHospBestMeasures;

-- Query to find the 10 best hospitals per Average Measure scores for each hospital
DROP TABLE CombHospBest;
CREATE TABLE CombHospBest AS
SELECT HospitalID, HospitalName, State, HospBestMeasAvgScore, ReadmAndDeathsAvgScore, (HospBestMeasAvgScore + RDMap/2) AS CombScores, SurveyAvg FROM CombHospBMRSReads
ORDER BY CombScores DESC
LIMIT 20;
