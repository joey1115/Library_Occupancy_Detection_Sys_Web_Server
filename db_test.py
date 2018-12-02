import sqlite3
import time
import random

if __name__ == '__main__':
    conn = sqlite3.connect('example.db')
    data = [
        ('1', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int))),
        ('2', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int))),
        ('3', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int))),
        ('4', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int))),
        ('5', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int))),
        ('6', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int)))
    ]

    c = conn.cursor()
    # c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_name = 'TEST_TABLE'
    c.execute('CREATE TABLE IF NOT EXISTS %s (ID varchar(255) NOT NULL UNIQUE, LOCATION varchar(255) NOT NULL, STATUS varchar(255) NOT NULL);' % (table_name))
    c.close()

    c = conn.cursor()
    try:
        c.executemany('INSERT INTO %s VALUES (?,?,?)' % (table_name), data)
    except sqlite3.IntegrityError:
        print("Duplicate ID")
    c.close()

    # command = ('7', 'Dud', str(random.randrange(0, stop=2, step=1, _int=int)))
    seat_id = '7'
    new_seats = [
        ('11', '2', '10')
    ]
    cur = conn.cursor()
    try:
        # c.execute('INSERT INTO %s VALUES (?, ?, ?)' % (table_name), command)
        # cur.execute('DELETE FROM %s WHERE TIME = ?' % (table_name), seat_id)
        # cur.executemany('UPDATE %s SET LOCATION=?, STATUS=? WHERE ID=?' % (table_name), new_seats)
        cur.execute('SELECT * FROM %s WHERE ID = ?' % (table_name), seat_id)
    except sqlite3.IntegrityError as e:
        print(e)
    except sqlite3.OperationalError as e:
        print(e)
    else:
        print([row for row in cur])
    c.close()

    cur = conn.cursor()
    cur.execute('SELECT * FROM %s' % (table_name))
    seats = [{
        'id': seat[0],
        'location': seat[1],
        'status': seat[2]
    } for seat in cur]
    print(seats)
    cur.close()
    
    conn.commit()
    conn.close()
