-- Use previous table to calculate the correlation coefficient
SELECT CORR(CombScores, SurveyAvg) FROM CombHospBest;

-- Use previous table CombState to calculate the correlation coefficient at the state level
SELECT CORR(StateAvgScoreMeasures, StateAvgSurvey) FROM CombState;

