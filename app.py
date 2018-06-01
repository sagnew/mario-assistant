import json

from flask import Flask, request, jsonify
from pprint import pprint


power_to_ram = {
    'small': '01',
    'super': '02',
    'fire': '03',
    'raccoon': '04',
    'frog': '05',
    'tanooki': '06',
    'hammer': '07',
}

synonyms_dict = {
    'UC4d37cfbf9b3a6f5f692a026228c6a057': 'raccoon',
    'UC854e50b50a98fba47de467ea3130ffaf': 'frog',
    'UCd54693473ae587a5b9adbc2cb0deee20': 'fire',
    'UC4236bd8920aa43137b572a59648d0c58': 'small',
    'UC5c38ed73161f1c44abda2caced77dc82': 'super',
    'UC24fbfad2e841ced17f10d6e2df304166': 'hammer',
    'UC09863aeeb594845672f07860e852ca01': 'tanooki',
}

app = Flask(__name__)


@app.route('/transform', methods=['POST'])
def transform():
    request_body = json.loads(request.data)
    print(request_body)

    power = None

    try:
        power_value = request_body['current_intents'][0]['fields']['power_type']['value'][0]
    except KeyError:
        return jsonify({ 'say': 'Couldn\'t find that powerup.' })

    if power_value in synonyms_dict.keys():
        power = synonyms_dict[power_value]
    elif power_value.lower() in power_to_ram.keys():
        power = power_value.lower()
    else:
        for power_str in power_to_ram.keys():
            if power_str in power_value.lower():
                power = power_str

    if power == None:
        return jsonify({ 'say': 'Couldn\'t find that powerup.' })

    ram_value = power_to_ram[power]

    with open('address.txt', 'w') as f:
        f.write('0578')
    with open('value.txt', 'w') as f:
        f.write(ram_value)

    return jsonify({ 'say': 'Turning you into {} Mario now.'.format(power) })

if __name__ == '__main__':
    app.run(debug=True)
