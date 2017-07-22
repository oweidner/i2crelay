#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Creation:    06.06.2017
# Last Update: 23.07.2017
#
# Copyright (c) 2017 Codewerft UG (haftungsbeschränkt) <https://codewerft.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# How to run this
# ===============
#
# 1. Install Python Flask:
# pip install Flask
#
# 2. Run the server
# python relay_server.py
#
# 3. Call the API
#
# - Toggle a relay:
#   curl -H "Content-Type: application/json" -X PUT -d '{"state":"toggle"}' localhost:5000/api/relay/1

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

