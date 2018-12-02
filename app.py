from flask import Flask, render_template, request, jsonify, abort, make_response
import sqlite3
from threading import Timer

table_name = 'DUDERSTADT_CENTER.db'
table_sensor = "SENSOR"
table_seat = "SEAT"

conn = sqlite3.connect(table_name)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS %s (ID TEXT PRIMARY KEY NOT NULL UNIQUE, STATUS TEXT NOT NULL, TEMP TEXT NOT NULL, BATTERY TEXT NOT NULL)' % (table_sensor))
c.execute('CREATE TABLE IF NOT EXISTS %s (ID TEXT PRIMARY KEY NOT NULL UNIQUE, SENSOR_ID TEXT NOT NULL, LOCATION TEXT NOT NULL)' % (table_seat))
c.close()
conn.commit()
conn.close()

app = Flask(__name__)


def verify_seat(seat):
    if not seat or not 'id' in seat or not 'status' in seat or not 'temp' in seat or not 'battery' in seat:
        abort(400)
    if 'id' in seat and type(seat['id']) is not str:
        abort(400)
    if 'status' in seat and type(seat['status']) is not str:
        abort(400)
    if 'status' in seat and type(seat['temp']) is not str:
        abort(400)
    if 'status' in seat and type(seat['battery']) is not str:
        abort(400)


def verify_seats(seats):
    seat_id = []
    if not seats or not 'seats' in seats:
        abort(400)
    if 'seats' in seats and type(seats['seats']) is not list:
        abort(400)
    if len(seats['seats']) == 0:
        abort(400)
    for seat in seats['seats']:
        print(seat)
        verify_seat(seat)
        if seat['id'] in seat_id:
            abort(400)
        else:
            seat_id.append(seat['id'])


@app.route('/seat', methods=['PUT'])
def update_seat():
    verify_seat(request.json)

    new_seat = (request.json['status'], request.json['temp'], request.json['battery'], request.json['id'])
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()

    m_cur.execute('SELECT COUNT(*) FROM %s WHERE ID = ?' % (table_sensor,), (request.json['id'],))
    count = m_cur.fetchone()
    if count[0] == 0:
        abort(404)

    m_cur.execute('UPDATE %s SET STATUS=? TEMP=?, BATTERY=? WHERE ID=?' % (table_sensor,), new_seat)
    m_cur.close()
    m_conn.commit()
    m_conn.close()
    return jsonify({'message': 'Success'}), 200


@app.route('/seats', methods=['PUT'])
def update_seats():
    verify_seats(request.json)

    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()

    seats_id = tuple([seat['id'] for seat in request.json['seats']])

    m_cur.execute('SELECT ID FROM %s WHERE ID IN (?%s)' % (table_sensor, ',?' * (len(seats_id)-1)), seats_id)
    ids = m_cur.fetchall()

    existing_id = [id[0] for id in ids]

    new_seats = [(seat['status'], seat['temp'], seat['battery'], seat['id']) for seat in request.json['seats']]

    m_cur.executemany('UPDATE %s SET STATUS=?, TEMP=?, BATTERY=? WHERE ID=?' % (table_sensor,), new_seats)
    m_cur.close()
    m_conn.commit()
    m_conn.close()
    if len(existing_id) == len(request.json['seats']):
        return jsonify({'message': 'Success', 'error_id':[]}), 200
    else:
        return jsonify({'message': 'Partial Success', 'error_id': [seat['id'] for seat in request.json['seats'] if seat['id'] not in existing_id]}), 200


@app.route('/seat/<string:seat_id>', methods=['DELETE'])
def delete_task(seat_id):
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()

    m_cur.execute('SELECT COUNT(*) FROM %s WHERE ID = ?' % (table_sensor,), (seat_id,))
    count = m_cur.fetchone()
    if count[0] == 0:
        abort(404)

    m_cur.execute('DELETE FROM %s WHERE ID = ?' % (table_sensor,), (seat_id,))
    m_cur.close()
    m_conn.commit()
    m_conn.close()
    return jsonify({'message': 'Success'}), 200


@app.route('/seat', methods=['POST'])
def create_seat():
    verify_seat(request.json)

    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()

    m_cur.execute('SELECT COUNT(*) FROM %s WHERE ID = ?' % (table_sensor,), (request.json['id'],))
    count = m_cur.fetchone()

    if count[0] > 0:
        abort(404)
    
    try:
        m_cur.execute('INSERT INTO %s (ID, STATUS, TEMP, BATTERY) VALUES (?, ?, ?, ?)' % (table_sensor,), (request.json['id'], request.json['status'], request.json['temp'], request.json['battery']))
    except sqlite3.IntegrityError:
        m_cur.close()
        m_conn.close()
        abort(405)
    else:
        m_cur.close()
        m_conn.commit()
        m_conn.close()
        return jsonify({'message': 'Success'}), 201


@app.route('/seats', methods=['POST'])
def create_seats():
    verify_seats(request.json)

    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()

    seats_id = tuple([seat['id'] for seat in request.json['seats']])

    m_cur.execute('SELECT ID FROM %s WHERE ID IN (?%s)' % (table_sensor, ',?' * (len(seats_id)-1)), seats_id)
    ids = m_cur.fetchall()

    existing_id = [id[0] for id in ids]

    new_seats = [(seat['id'], seat['status'], seat['temp'], seat['battery']) for seat in request.json['seats'] if seat['id'] not in existing_id]

    try:
        m_cur.executemany('INSERT INTO %s (ID, STATUS, TEMP, BATTERY) VALUES (?,?,?,?)' % (table_sensor,), new_seats)
    except sqlite3.IntegrityError:
        m_cur.close()
        m_conn.close()
        abort(405)
    else:
        m_cur.close()
        m_conn.commit()
        m_conn.close()
        if len(existing_id) == 0:
            return jsonify({'message': 'Success', 'error_id':[]}), 201
        else:
            return jsonify({'message': 'Partial Success', "error_id": existing_id}), 201


@app.route('/seats', methods=['GET'])
def get_seats():
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()
    m_cur.execute('SELECT ID, STATUS, TEMP, BATTERY FROM %s' % (table_sensor,))
    seats = m_cur.fetchall()
    m_cur.close()
    m_conn.commit()
    m_conn.close()
    seats = [{
        'id': seat[0],
        'status': seat[1],
        'temp': seat[2],
        'battery': seat[3]
    } for seat in seats]
    return jsonify({'seats': seats}), 200


@app.route('/seat/id/<string:seat_id>', methods=['GET'])
def get_seat(seat_id):
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()
    try:
        m_cur.execute('SELECT ID, STATUS, TEMP, BATTERY FROM %s WHERE ID = ?' % (table_sensor,), (seat_id,))
    except sqlite3.IntegrityError:
        m_cur.close()
        m_conn.close()
        abort(404)
    else:
        seat = m_cur.fetchone()
        m_cur.close()
        m_conn.commit()
        m_conn.close()
        if seat is None:
            abort(404)
        else:
            seat = {
                'id': seat[0],
                'status': seat[1],
                'temp': seat[2],
                'battery': seat[3]
            }
            return jsonify(seat), 200

@app.route('/seats_info', methods=['GET'])
def get_seats_info():
    m_conn = sqlite3.connect(table_name)
    m_cur = m_conn.cursor()
    m_cur.execute('SELECT %s.ID, %s.LOCATION, %s.STATUS, %s.TEMP, %s.BATTERY, %s.ID FROM %s INNER JOIN %s ON %s.ID = %s.SENSOR_ID' % (
        table_sensor,
        table_seat,
        table_sensor,
        table_sensor,
        table_sensor,
        table_seat,
        table_seat,
        table_sensor,
        table_sensor,
        table_seat
    ))
    seats = m_cur.fetchall()
    m_cur.close()
    m_conn.commit()
    m_conn.close()
    seats = [{
        'id': seat[0],
        'location': seat[1],
        'status': seat[2],
        'temp': seat[3],
        'battery': seat[4],
        'seat_id': seat[5]
    } for seat in seats]
    return jsonify({'seats': seats}), 200, {
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': 0
        }


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def not_understand(error):
    return make_response(jsonify({'error': 'Not Understand'}), 400)


@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify({'error': "Not allowed"}), 405)


@app.route('/')
def index():
    return render_template('index.html'), 200, {
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': 0
        }


@app.route('/table')
# @headers({'Access-Control-Allow-Origin': '*'})
def table():
    return render_template('table.html'), 200, {
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': 0
        }


@app.route('/test')
def test():
    return render_template('test.html'), 200, {
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': 0
        }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
