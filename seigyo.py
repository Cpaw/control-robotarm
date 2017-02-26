import webiopi
import time

webiopi.setDebug()
GPIO = webiopi.GPIO

#モーターに使うピン
MOT_PIN1 = 2
MOT_PIN2 = 3
MOT_PIN3 = 4
MOT_PIN4 = 17
MOT_PIN5 = 27
MOT_PIN6 = 22
MOT_PIN7 = 10
MOT_PIN8 = 9
MOT_PIN9 = 11
MOT_PIN10 = 7
#LED(プログラムの試験用)に使うピン
LEDPIN_1 = 8

#LEDクラス
class LED():
        def __init__(self, pin1):
                GPIO.setFunction(pin1, GPIO.PWM)
                self.pin1 = pin1
                self.per = 50 #duty比(パーセンテージ)
                self.mode = "0"
                self.behavior = {"0":"OFF",
                                 "1":"ON"}
        def write(self):
                if self.mode == "1":
                        if 100 < self.per:
                                self.per = 100
                        if 0 > self.per:
                                self.per = 0
                        if 10 > self.per:
                                GPIO.pwmWrite(self.pin1, 0)
                        else:
                                GPIO.pwmWrite(self.pin1, self.per*0.01)
                elif self.mode == "0":
                        GPIO.pwmWrite(self.pin1, 0)
                
#モータークラス
class Motor():
        def __init__(self, pin1, pin2,  name, behavior):
                GPIO.setFunction(pin1, GPIO.PWM)
                GPIO.setFunction(pin2, GPIO.PWM)
                self.pin1 = pin1
                self.pin2 = pin2
                self.per = 50 #duty比(パーセンテージ)
                self.name = name
                self.behavior = {"0":"Stop",
                                 "1":behavior[0],
                                 "2":behavior[1]}
                self.mode = "0"
                
        def write(self):
                if self.mode == "1":
                        #ショート回避
                        GPIO.pwmWrite(self.pin2, 0)
                        time.sleep(0.2)
                        
                        if 100 < self.per:
                                self.per = 100
                        if 0 > self.per:
                                self.per = 0
                        if 10 > self.per:
                                GPIO.pwmWrite(self.pin1, 0)
                        else:
                                GPIO.pwmWrite(self.pin1, self.per*0.01)
                elif self.mode == "2":
                        #ショート回避
                        GPIO.pwmWrite(self.pin1, 0)
                        time.sleep(0.2)
                        
                        if 100 < self.per:
                                self.per = 100
                        if 0 > self.per:
                                self.per = 0
                        if 10 > self.per:
                                GPIO.pwmWrite(self.pin2, 0)
                        else:
                                GPIO.pwmWrite(self.pin2, self.per*0.01)
                elif self.mode == "0":
                        GPIO.pwmWrite(self.pin1, 0)
                        GPIO.pwmWrite(self.pin2, 0)
                        
                        
Motors = {"1": Motor(MOT_PIN1, MOT_PIN2, "Gripper", ["Catch","Release"]),
          "2": Motor(MOT_PIN3, MOT_PIN4, "Wrist", ["Turn Left","Turn Right"]),
          "3": Motor(MOT_PIN5, MOT_PIN6, "Elbow", ["Up","Down"]),
          "4": Motor(MOT_PIN7, MOT_PIN8, "Shoulder", ["Up","Down"]),
          "5": Motor(MOT_PIN9, MOT_PIN10, "Base", ["Turn Left","Turn Right"])}

LED_1 = LED(LEDPIN_1)


#モーターのモード変更
@webiopi.macro
def motorChangemode(mtype, mode):
        webiopi.debug("{} : {}".format(Motors[mtype].name, Motors[mtype].behavior[mode]))
        Motors[mtype].mode = mode
        Motors[mtype].write()

#モーターのduty比変更
@webiopi.macro
def motorChangeduty(mtype, level):
        webiopi.debug("ChangeDutycycle({}) : {}%".format(Motors[mtype].name, level))
        Motors[mtype].per = 10 * int(level)
        Motors[mtype].write()
        
#LEDのモード変更
@webiopi.macro
def ledChangemode(mode):
        webiopi.debug("LED : {}".format(LED_1.behavior[mode]))
        LED_1.mode = mode
        LED_1.write()

#LEDのduty比変更
@webiopi.macro
def ledChangeduty(level):
        webiopi.debug("ChangeDutyCycle(LED) : {}%".format(level))
        LED_1.per = 10 * int(level)
        LED_1.write()
        
#全モーター,LEDをOFF
@webiopi.macro
def allOff():
        webiopi.debug("ALL OFF")
        ledChangemode("0")
        for mtype in Motors:
                motorChangemode(mtype, "0")

#全モーター,LEDのduty比を変更
@webiopi.macro
def allChangeduty(level):
        webiopi.debug("ChangeAllDutyCycle : {}%".format(level))
        ledChangeduty(level)
        for mtype in Motors:
                motorChangeduty(mtype, level)
        
#サーバー停止時に実行。全モーター,LEDをOFF
def destroy():
        allOff()
