-- Creates an archive table and moves records older than 1 year

CREATE TABLE IF NOT EXISTS payments_archive AS
SELECT *
FROM payments
WHERE 1 = 0;

INSERT INTO payments_archive
SELECT *
FROM payments
WHERE transaction_date < NOW() - INTERVAL '1 year';

DELETE FROM payments
WHERE transaction_date < NOW() - INTERVAL '1 year';