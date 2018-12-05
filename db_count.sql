-- -- DROP TABLE "COUNT";

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


-- SELECT 
--     avg("NUM") 
-- FROM 
--     (
--         SELECT
--             "NUM_OF_PEOPLE" as "NUM"
--         FROM
--             "COUNT"
--         WHERE
--             "TIME" >= 1543881600 AND "TIME" < 1543885200
--     )
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

-- SELECT 
--     "SEAT".LOCATION, "SENSOR".STATUS, "SENSOR".TEMP, "SENSOR".BATTERY 
-- FROM 
--     "SEAT" 
-- INNER JOIN 
--     "SENSOR" 
-- ON 
--     "SENSOR".ID = "SEAT".SENSOR_ID

CREATE TABLE IF NOT EXISTS 
    "COUNT" (
        "TIME" INTEGER NOT NULL, 
        "NUM_OF_PEOPLE" INTEGER NOT NULL
    );

CREATE TABLE IF NOT EXISTS 
    "SENSOR" (
        "ID" TEXT PRIMARY KEY NOT NULL UNIQUE, 
        "STATUS" TEXT NOT NULL, 
        "TEMP" TEXT NOT NULL, 
        "BATTERY" TEXT NOT NULL
    );
CREATE TABLE IF NOT EXISTS 
    "SEAT" (
        "ID" TEXT PRIMARY KEY NOT NULL UNIQUE, 
        "SENSOR_ID" TEXT NOT NULL, 
        "LOCATION" TEXT NOT NULL
    );

-- DELETE FROM
--     "SEAT"
-- WHERE
--     "ID" = "44";
-- INSERT INTO
--     "SEAT" (
--         "ID",
--         "SENSOR_ID",
--         "LOCATION"
--     )
-- VALUES
--     (
--         "42",
--         "D5:29:3F:A0",
--         "3rd floor"
--     );

-- SELECT * FROM "SEAT"

UPDATE
    "SEAT"
SET
    "ID" = "71"
WHERE
    "ID" = "104"
