# -*- coding:utf-8 -*-

import time

from DFRobot_RaspberryPi_DC_Motor import DFRobot_DC_Motor_IIC as Board

board = Board(1, 0x10)    # Select bus 1, set address to 0x10

def board_detect():
  l = board.detecte()
  print("Board list conform:")
  print(l)

''' print last operate status, users can use this variable to determine the result of a function call. '''
def print_board_status():
  if board.last_operate_status == board.STA_OK:
    print("board status: everything ok")
  elif board.last_operate_status == board.STA_ERR:
    print("board status: unexpected error")
  elif board.last_operate_status == board.STA_ERR_DEVICE_NOT_DETECTED:
    print("board status: device not detected")
  elif board.last_operate_status == board.STA_ERR_PARAMETER:
    print("board status: parameter error, last operate no effective")
  elif board.last_operate_status == board.STA_ERR_SOFT_VERSION:
    print("board status: unsupport board framware version")

if __name__ == "__main__":

  board_detect()

  while board.begin() != board.STA_OK:
    print_board_status()
    print("board begin faild")
    time.sleep(2)
  print("board begin success")

  # board.set_encoder_enable(board.ALL)                 # Set selected DC motor encoder enable
  # board.set_encoder_disable(board.ALL)              # Set selected DC motor encoder disable
  # board.set_encoder_reduction_ratio(board.ALL, 43)    # Set selected DC motor encoder reduction ratio, test motor reduction ratio is 43.8

  board.set_moter_pwm_frequency(1000)   # Set DC motor pwm frequency to 1000HZ

  board.motor_movement([board.M1], board.CW, 5)
  board.motor_movement([board.M2], board.CW, 5)
  time.sleep(1)
  board.motor_stop(board.ALL)

'''
  while True:
    for duty in range(5, 95, 10):   # slow to fast
      board.motor_movement([board.M1], board.CW, duty)    # DC motor 1 movement, orientation clockwise
      board.motor_movement([board.M2], board.CCW, duty)   # DC motor 2 movement, orientation count-clockwise
      time.sleep(1)
      speed = board.get_encoder_speed(board.ALL)
      print("duty: %d, M1 encoder speed: %d rpm, M2 encoder speed %d rpm" %(duty, speed[0], speed[1]))

    for duty in range(95, 5, - 10):   # fast to low
      board.motor_movement([board.M1], board.CW, duty)    # DC motor 1 movement, orientation clockwise
      board.motor_movement([board.M2], board.CCW, duty)   # DC motor 2 movement, orientation count-clockwise
      time.sleep(1)
      speed = board.get_encoder_speed(board.ALL)      # Use boadrd.all to get all encoders speed
      print("duty: %d, M1 encoder speed: %d rpm, M2 encoder speed %d rpm" %(duty, speed[0], speed[1]))

    print("stop all motor")
    board.motor_stop(board.ALL)   # stop all DC motor
    print_board_status()
    time.sleep(4)
'''
