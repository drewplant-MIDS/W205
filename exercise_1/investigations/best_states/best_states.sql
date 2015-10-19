-- Create a table of average Measure Scores for each hospital -- ALREADY RUN as part of best_hospitals.sql!
DROP TABLE HospBestMeasures;
CREATE TABLE HospBestMeasures AS
SELECT HospitalID, HospitalName, State, Avg(Cast(Score as float)) AS AvgScore
FROM EffectiveCare
GROUP BY HospitalID, HospitalName, State 
ORDER BY AvgScore DESC;

-- Roll-up of Measure Scores by state
DROP TABLE StateBestMeasures;
CREATE TABLE StateBestMeasures AS
SELECT State, Avg(AvgScore) AS StateAvgScoreMeasures
FROM HospBestMeasures
GROUP BY State 
ORDER BY StateAvgScoreMeasures DESC;


-- Create a table of average ReadsUndDeaths -- ALREADY RUN as part of best_hospitals.sql!
DROP TABLE ReadsAndDeathsAvgScore;
CREATE TABLE ReadsAndDeathsAvgScore AS
SELECT HospitalID, HospitalName, State, Avg(Cast(Score as float)) AS AvgScore
FROM ReadmissionsAndDeaths
GROUP BY HospitalID, HospitalName, State
ORDER BY AvgScore ASC;

-- Roll-up of Readmits and Deaths by state
DROP TABLE ReadsAndDeathsByState;
CREATE TABLE ReadsAndDeathsByState AS
SELECT State, Avg(AvgScore) AS StateAvgScoreReadsDeaths
FROM ReadsAndDeathsAvgScore
GROUP BY State
ORDER BY StateAvgScoreReadsDeaths ASC;

-- Create a table of average Survey scores for each hospital -- ALREADY RUN as part of best_hospitals.sql!
DROP TABLE SurveyAverages;
CREATE TABLE SurveyAverages AS
SELECT HospitalID, HospitalName, State, ((Cast(AchievePointsClean as float)+Cast(ImprovePointsClean as float)+Cast(DimScoreClean as float))/3) AS AvgOverall
FROM Surveys
ORDER BY AvgOverall DESC;

-- Roll-up of Survey Scores by state
DROP TABLE StateSurveyAvgs;
CREATE TABLE StateSurveyAvgs AS
SELECT State, Avg(AvgOverall) AS StateAvgSurvey
FROM SurveyAverages GROUP BY State;

-- Join above three tables
DROP TABLE CombState;
CREATE TABLE CombState AS
SELECT sbm.State, sbm.StateAvgScoreMeasures, radst.StateAvgScoreReadsDeaths, ssa.StateAvgSurvey 
	FROM StateBestMeasures AS sbm
	INNER JOIN ReadsAndDeathsByState AS radst
	ON sbm.State = radst.State
	INNER JOIN StateSurveyAvgs AS ssa
	ON sbm.State = ssa.State;

-- From the following query we can see that Readmissions/Deaths min = 13.54 % and max = 15.03%.  Since these values are somewhat
-- indistinguishable, we can ignore Readmissions and Deaths when finding the best states for health care
SELECT MIN(StateAvgScoreReadsDeaths), MAX(StateAvgScoreReadsDeaths)   FROM CombState;


-- Query to find the 10 best hospitals per Average Measure scores for each hospital
DROP TABLE CombStateBest;
CREATE TABLE CombStateBest AS
	SELECT State, StateAvgScoreMeasures, StateAvgScoreReadsDeaths, StateAvgSurvey FROM CombState
	ORDER BY StateAvgScoreMeasures DESC
	LIMIT 20;
