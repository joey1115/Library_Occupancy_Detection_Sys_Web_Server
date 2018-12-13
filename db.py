import threading, sqlite3, time

table_name = '/home/ubuntu/webapp/DUDERSTADT_CENTER.db'
table_count = "COUNT"

def seat_count():
    timer = threading.Timer(60, seat_count)
    timer.setDaemon(True)
    timer.start()
    db_count()

def db_init():
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()
    m_cur.execute('CREATE TABLE IF NOT EXISTS %s (TIME INTEGER NOT NULL, NUM_OF_PEOPLE INTEGER NOT NULL)' % (table_count))
    m_cur.close()
    m_conn.close()

def db_count():
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()
    m_cur.execute(
        """
        INSERT INTO
            "COUNT" (
                "TIME",
                "NUM_OF_PEOPLE"
            )
        VALUES
            (
                ?,
                (
                    SELECT
                        COUNT(*)
                    FROM
                        (
                            SELECT
                                "SENSOR".ID, "SEAT".LOCATION, "SENSOR".STATUS, "SENSOR".TEMP, "SENSOR".BATTERY, "SEAT".ID 
                            FROM 
                                "SEAT" 
                            INNER JOIN 
                                "SENSOR"
                            ON 
                                "SENSOR".ID = "SEAT".SENSOR_ID
                            WHERE
                                "SENSOR".STATUS = "occupied"
                        )
                )
            )
        """ , 
        (int(time.time()),)
    )
    # m_cur.execute(
    #         """
    #         DELETE FROM "COUNT" WHERE "TIME"<?
    #         """,
    #         (int(time.time() - 72*60*60),)
    # )
    m_cur.close()
    m_conn.commit()
    m_conn.close()

if __name__ == "__main__":
    db_init()
    seat_count()
    while True:
        pass