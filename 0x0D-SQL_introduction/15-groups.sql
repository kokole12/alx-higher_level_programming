-- Listing records with eqaul scores
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;

