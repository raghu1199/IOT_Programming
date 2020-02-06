import RPi.GPIO as gpio
from flask import Flask,request,jsonify
app=Flask(__name__)

pin=8
gpio.setmode(gpio.BOARD)
gpio.setup(pin,gpio.OUT)


@app.route("/",methods=['GET'])
def led():
    status=request.args.get('status')
    if status=="on":
        gpio.output(pin,gpio.HIGH)
        return jsonify({"message":"Led Turned On"})

    elif(status=="off"):
        gpio.output(pin,gpio.LOW)
        return jsonify({"message":"Led turned Off"})

    else:
        return jsonify({"message":"Not valid status"})


if __name__=='__main__':
    app.run()

