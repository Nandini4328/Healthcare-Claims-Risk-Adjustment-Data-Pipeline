SELECT
    member_id,
    COUNT(*) AS total_claims,
    SUM(amount) AS total_cost
FROM staging_claims
GROUP BY member_id
