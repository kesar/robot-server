from flask import Flask
from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board

board = Board(1, 0x10)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! :)"

@app.route("/motor/<string:speed>/<string:speed2>/")
def setSpeedMotor(speed, speed2):
    board.motor_movement([board.M1], board.CW, speed)
    board.motor_movement([board.M2], board.CW, speed2)
    return "OK!"

@app.route("/stop")
def stop(speed, speed2):
    board.motor_stop(board.ALL)
    return "OK!"

if __name__ == "__main__":
    while board.begin() != board.STA_OK:
        print_board_status()
        print("board begin faild")
        time.sleep(2)
        print("board begin success")

    board.set_moter_pwm_frequency(1000)
    board.motor_movement([board.M1], board.CW, 0)
    board.motor_movement([board.M2], board.CW, 0)
    app.run(host='0.0.0.0', port=8000)
