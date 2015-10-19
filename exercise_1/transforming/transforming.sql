-- EffectiveCare with Measures and MeasureScores
-- Remove points that are erroneously entered as a number greater than 100%
DROP TABLE EffectiveCare;
CREATE TABLE EffectiveCare AS 
	SELECT HospitalID, HospitalName, State, MeasureID, MeasureName, Score
	FROM EffectiveCareBase
	WHERE LENGTH(Score)<5 AND Cast(Score as float) < 101;


-- ReadmissionsAndDeaths with Measures and Scores
DROP TABLE ReadmissionsAndDeaths;
CREATE TABLE ReadmissionsAndDeaths AS 
	SELECT HospitalID, HospitalName, State, MeasureID, MeasureName, Score
	FROM ReadmissionsAndDeathsBase
	WHERE LENGTH(Score) < 5;

-- EffectiveCare with Measures and MeasureScores
DROP TABLE Hospitals;
CREATE TABLE Hospitals AS 
	SELECT HospitalID, HospitalName, State
	FROM HospitalsBase;

-- EffectiveCare with Measures and MeasureScores
DROP TABLE Measures;
CREATE TABLE Measures As
	SELECT MeasureName, MeasureID
	FROM MeasuresBase;

-- EffectiveCare with Measures and MeasureScores
DROP TABLE Surveys;
CREATE TABLE Surveys AS
	SELECT HospitalID, HospitalName, State, REGEXP_REPLACE(AchievePoints, '(.*) out of 10', '$1') AS AchievePointsClean,
 	REGEXP_REPLACE(ImprovePts, '^(.*) out of .*$', '$1') AS ImprovePointsClean,
 	REGEXP_REPLACE(DimScore, '^(.*) out of .*$', '$1') AS DimScoreClean
 	FROM SurveysBase
 	WHERE NOT REGEXP(AchievePoints,'[nN]ot') AND NOT REGEXP(ImprovePts,'[nN]ot') AND NOT REGEXP(DimScore,'[nN]ot');

