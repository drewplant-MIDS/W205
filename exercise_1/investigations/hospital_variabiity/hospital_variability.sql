-- Create a table of Variance for different measures across hospitals; note that MeaureName has been removed in case it's not always
-- ...always distinct within a MeasureID...
DROP TABLE MeasureVariance;
CREATE TABLE MeasureVariance AS
	SELECT MeasureID, Variance(Score) AS VarMeasureScore
	FROM EffectiveCare
	GROUP BY MeasureID ;

-- Query the table
DROP TABLE TopVarianceFirst;
CREATE TABLE TopVarianceFirst AS
	SELECT *
	FROM MeasureVariance
	ORDER BY VarMeasureScore DESC
	LIMIT 20;

-- Add back the Measure Name
DROP TABLE TopVariance;
CREATE TABLE TopVariance AS
	SELECT tvf.MeasureID, mb.MeasureName, tvf.VarMeasureScore
	FROM TopVarianceFirst AS tvf 
	INNER JOIN MeasuresBase as mb
	ON tvf.MeasureID = mb.MeasureID
	ORDER BY VarMeasureScore DESC
	LIMIT 20;

SELECT MeasureID, MeasureName, VarMeasureScore FROM TopVariance ORDER BY VarMeasureScore DESC;



