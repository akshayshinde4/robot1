import time

global lastErr, kp, ki, kd
def Compute(setpoint, input):
    now = time.time()*1000.0
    timeChange = now - timeChange
    error = setpoint - input
    errSum += error*timeChange
    dErr = (error-lastErr)/ timeChange

    output = (kp*error) + (ki*errSum) + (kd*dErr)

    lastErr = error
    lastTime = now