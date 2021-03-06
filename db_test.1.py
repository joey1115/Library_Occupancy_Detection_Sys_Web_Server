import sqlite3
import time
import random

if __name__ == '__main__':
    table_sensor = "SENSOR"
    table_seat = "SEAT"
    table_count = "COUNT"

    conn = sqlite3.connect('/home/pi/webapp/DUDERSTADT_CENTER.db')
    c = conn.cursor()
    # c.execute('CREATE TABLE IF NOT EXISTS %s (ID TEXT PRIMARY KEY NOT NULL UNIQUE, STATUS TEXT NOT NULL, TEMP TEXT NOT NULL, BATTERY TEXT NOT NULL)' % (table_sensor))
    # c.execute('CREATE TABLE IF NOT EXISTS %s (ID TEXT PRIMARY KEY NOT NULL UNIQUE, SENSOR_ID TEXT NOT_NULL, LOCATION TEXT NOT NULL)' % (table_seat))
    # c.execute('INSERT INTO %s (ID, STATUS, TEMP, BATTERY) VALUES (?, ?, ?, ?)' % (table_sensor,), ("1", "2", "3", "4"))
    # c.execute('INSERT INTO %s (ID, STATUS, TEMP, BATTERY) VALUES (?, ?, ?, ?)' % (table_sensor,), ("2", "2", "3", "4"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("3", "FE:89:35:98", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("4", "DE:71:45:AF", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("5", "C0:F1:A7:54", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("6", "FB:F3:02:A3", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("7", "DF:01:4B:63", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("8", "DE:71:45:AF", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("9", "C6:7F:B0:C2", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("10", "CC:31:E8:3D", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("11", "FE:89:35:9A", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("12", "E2:3A:A8:32", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("13", "FE:89:35:9A", "3rd Floor"))
    # c.execute('INSERT INTO %s (ID, SENSOR_ID, LOCATION) VALUES (?, ?, ?)' % (table_seat,), ("8", "D1:E1:6C:5C", "3rd Floor"))
    # c.execute('DELETE FROM %s WHERE ID =?' % (table_seat,), ("8",))
    # c.execute(
    #     """
    #     SELECT 
    #         "SENSOR".ID, "SEAT".LOCATION, "SENSOR".STATUS, "SENSOR".TEMP, "SENSOR".BATTERY, "SEAT".ID
    #     FROM 
    #         "SEAT" 
    #     INNER JOIN 
    #         "SENSOR" 
    #     ON 
    #         "SENSOR".ID = "SEAT".SENSOR_ID
    #     """
    # )
    # SENSOR.ID, SEAT.LOCATION, SENSOR.STATUS, SENSOR.TEMP, SENSOR.BATTERY, SEAT.IDSENSOR.ID, SEAT.LOCATION, SENSOR.STATUS, SENSOR.TEMP, SENSOR.BATTERY, SEAT.ID
    # c.execute('SELECT :seat.LOCATION, :sensor.STATUS, :sensor.TEMP, :sensor.BATTERY FROM :seat INNER JOIN :sensor ON :sensor.ID = :seat.SENSOR_ID', {"seat": table_seat, "sensor": table_sensor})
    # count = c.fetchall()
    # print(count)
    # c.execute(
    #     """
    #     UPDATE
    #         "SEAT"
    #     SET
    #         "ID" = "71"
    #     WHERE
    #         "ID" = "104"
    #     """
    # )
    # c.execute(
    #     """
    #     INSERT INTO
    #         "SEAT" ("ID", "SENSOR_ID", "LOCATION")
    #     VALUES
    #         ("16", "DF:01:4B:63", "Testing")
    #     """
    # )
    c.execute(
        """
        SELECT
            *
        FROM
            "SEAT"
        """
    )
    count = c.fetchall()
    # print(count)
    c.close()
    conn.commit()
    conn.close()
