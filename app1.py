from flask import Flask, render_template, request, jsonify, abort, make_response
# import sqlite3

seats = [
    {
        'id': "1",
        'location': u'First Floor',
        'status': u'Occupied'
    },
    {
        'id': "2",
        'location': u'Second Floor',
        'status': u'Empty'
    },
    {
        'id': "3",
        'location': u'Third Floor',
        'status': u'Occupied'
    }
]

app = Flask(__name__)
todos = {
    "todo1": "Remember the milk",
    "todo2": "Remember the milk"
}

def verify_seat():
    if not request.json or not 'id' in request.json or not 'location' in request.json or not 'status' in request.json:
        print(1)
        abort(400)
    if 'id' in request.json and type(request.json['id']) != str:
        print(2)
        abort(400)
    if 'location' in request.json and type(request.json['location']) is not str:
        print(3)
        abort(400)
    if 'status' in request.json and type(request.json['status']) is not str:
        print(4)
        abort(400)

@app.route('/seat', methods=['PUT'])
def update_seat():
    verify_seat()

    global seats
    seat = list(filter(lambda t: t['id'] == request.json['id'], seats))
    if len(seat) == 0:
        abort(404)
    
    seats = [seat for seat in seats if seat['id'] != request.json['id']]
    seats.append(seat[0])

    print(seats)
    return jsonify({'task': seat[0]}), 201

@app.route('/seats/<string:seat_id>', methods=['DELETE'])
def delete_task(seat_id):
    print(seats)
    task = list(filter(lambda t: t['id'] == seat_id, seats))
    print(task)

    if len(task) == 0:
        abort(404)
    
    seats.remove(task[0])
    return jsonify({'result': True})

@app.route('/seat', methods=['POST'])
def create_seat():
    verify_seat()

    seat = list(filter(lambda t: t['id'] == request.json['id'], seats))
    if len(seat) != 0:
        return jsonify({'error': 'Duplicate ID'}), 404
    
    seat = {
        'id': request.json['id'],
        'location': request.json['location'],
        'status': request.json['status']
    }
    seats.append(seat)

    return jsonify({'task': seats}), 201

@app.route('/seats', methods=['POST'])
def create_seats():
    if not request.json or not 'seats' in request.json:
        abort(400)
    if 'seats' in request.json and type(request.json['seats']) != list:
        abort(400)

    error_id = []
    for new_seat in request.json['seats']:
        print(new_seat)
        # verify_seat()

        seat = list(filter(lambda t: t['id'] == new_seat['id'], seats))
        if len(seat) != 0:
            error_id.append(new_seat['id'])
        else:
            seat = {
                'id': new_seat['id'],
                'location': new_seat['location'],
                'status': new_seat['status']
            }
            seats.append(seat)

    if len(error_id) == 0:
        return jsonify({'seats': seats}), 201
    else:
        return jsonify({
            'error': 'Duplicate ID',
            'error_id': error_id
        }), 201

@app.route('/seats', methods=['GET'])
def get_seats():
    return jsonify({'seats': seats})

@app.route('/seats/id/<string:seat_id>', methods=['GET'])
def get_task(seat_id):
    seat = list(filter(lambda t: t['id'] == seat_id, seats))

    if len(seat) == 0:
        abort(404)
    return jsonify(seat[0])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_understand(error):
    return make_response(jsonify({'error': 'Not Understand'}), 400)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    # table_name = 'TEST_TABLE'
    # conn = sqlite3.connect('example.db')

    # c = conn.cursor()
    # c.execute('SELECT * FROM %s' % (table_name))
    # c.close()

    # conn.commit()
    # conn.close()

    app.run(debug=True, host='0.0.0.0')
