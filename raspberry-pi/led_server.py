from flask import Flask, request
import serial

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/change_led', methods=['POST'])
def change_led():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']
    led_num = request.form['led_num']

    format_red = "%03d" % int(red)
    format_green = "%03d" % int(green)
    format_blue = "%03d" % int(blue)
    format_led_num = "%02d" % int(led_num)

    message_to_send = '{0}{1}{2}{3}\n'.format(format_green,
                                                    format_red,
                                                    format_blue,
                                                    format_led_num)

    arduinoSerialData.write(bytes(message_to_send, 'UTF-8'))

    return 'Done'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')