def Compute():
#    How long since we last calculated
#    now = millis()
    timeChange = (now - lastTime)
  
#    Compute all the working error variables
    error = Setpoint - Input
    errSum += (error * timeChange)
    dErr = (error - lastErr) / timeChange
  
#    Compute PID Output
    Output = kp * error + ki * errSum + kd * dErr
  
#    Remember some variables for next time
    lastErr = error
    lastTime = now