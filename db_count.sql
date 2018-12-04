-- -- DROP TABLE "COUNT";
-- -- CREATE TABLE IF NOT EXISTS 
-- --     "COUNT" (
-- --         "TIME" INTEGER NOT NULL, 
-- --         "NUM_OF_PEOPLE" INTEGER NOT NULL
-- --     );
-- INSERT INTO
--     "COUNT" (
--         "TIME",
--         "NUM_OF_PEOPLE"
--     )
-- VALUES
--     (
--         1543881482,
--         (
--             SELECT
--                 COUNT(*)
--             FROM
--                 (
--                     SELECT
--                         "SENSOR".ID, "SEAT".LOCATION, "SENSOR".STATUS, "SENSOR".TEMP, "SENSOR".BATTERY, "SEAT".ID 
--                     FROM 
--                         "SEAT" 
--                     INNER JOIN 
--                         "SENSOR"
--                     ON 
--                         "SENSOR".ID = "SEAT".SENSOR_ID
--                     WHERE
--                         "SENSOR".STATUS = "occupied"
--                 )
--         )
--     )
-- DELETE FROM "COUNT" WHERE "TIME" < 10


SELECT 
    avg("NUM") 
FROM 
    (
        SELECT
            "NUM_OF_PEOPLE" as "NUM"
        FROM
            "COUNT"
        WHERE
            "TIME" >= 1543881600 AND "TIME" < 1543885200
    )
-- INSERT INTO
--             "COUNT" (
--                 "TIME",
--                 "NUM_OF_PEOPLE"
--             )
--         VALUES
--             (
--                 2,
--                 (
--                     SELECT
--                         COUNT(*)
--                     FROM
--                         (
--                             SELECT
--                                 "SENSOR".ID, "SEAT".LOCATION, "SENSOR".STATUS, "SENSOR".TEMP, "SENSOR".BATTERY, "SEAT".ID 
--                             FROM 
--                                 "SEAT" 
--                             INNER JOIN 
--                                 "SENSOR"
--                             ON 
--                                 "SENSOR".ID = "SEAT".SENSOR_ID
--                             WHERE
--                                 "SENSOR".STATUS = "occupied"
--                         )
--                 )
--             )

