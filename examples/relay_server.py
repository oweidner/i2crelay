#!/usr/bin/python


# Toggle a relay:
# curl -H "Content-Type: application/json" -X PUT -d '{"state":"toggle"}' localhost:5000/api/relay/1

from flask import Flask, jsonify, request, g
from i2crelay import I2CRelayBoard

I2C_BUS = 1
I2C_ADDR = 0x20

app = Flask(__name__)

def get_relay():
    relay = getattr(g, '_relay', None)
    if relay is None:
        relay = g._relay = I2CRelayBoard(I2C_BUS, I2C_ADDR)
    return relay

@app.route('/api/relay/<int:relay_id>', methods=['GET'])
def get_relay_state(relay_id):
    state = get_relay().is_on(relay_id)
    return jsonify({'relay': relay_id, 'state': state})

@app.route('/api/relay/<int:relay_id>', methods=['PUT'])
def switch_relay(relay_id):
    if 'state' not in request.json:
        abort(400)
    else:
        if request.json['state'].lower() == 'on':
            get_relay().switch_on(relay_id)
        elif request.json['state'].lower() == 'off':
            get_relay().switch_off(relay_id)
        elif request.json['state'].lower() == 'toggle':
            get_relay().toggle(relay_id)
        else:
            abort(400)
    state = get_relay().is_on(relay_id)
    return jsonify({'relay': relay_id, 'state': state})

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')

