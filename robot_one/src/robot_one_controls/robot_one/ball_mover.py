# import sys
# sys.path.append('/home/rohit/yolov4-custom-functions/core/utils.py')
# import utils.py

import signal, sys

from numpy import angle
from rsa import sign
import rclpy
from rclpy.node import Node
from math import asin
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
from simple_pid import PID
import time

'''

theta = (sin^-1((d*g)/u^2))/2

u^2 = 

'''
# g = 9.8
# global pub, file

lastErr, kp, ki, kd, lastTime, angleLastTime, angleLasterr = 0, 1, 0, 0, 0, 0, 0

def sigint_handler(signal, frame):
    print("KeyboardInterrupt error caught")
    enode = Node('error_handling_node')
    epub = enode.create_publisher(Twist,'/cmd_vel',10)
    eangle_pub = enode.create_publisher(Int32, '/twisto', 10)
    error_msg = Twist()
    error_msg.angular.z = 0.0
    error_angle = Int32()
    error_angle.data = 300000

    epub.publish(error_msg)
    eangle_pub.publish(error_angle)

    rclpy.spin_once(enode, timeout_sec=2)
    print(error_msg, "\t", error_angle)
    sys.exit(0)



def timed_callback(pub, angle_pub):
    xfile = open('/home/rohit/ball.txt', 'r')
    data = xfile.read()
    yfile = open('/home/rohit/bally.txt', 'r')
    ydata = yfile.read()
    if (data==''):
        xmean = 320.0
    else:
        xmean = float(data)
    msg = Twist()
    
    # output = PID(xmean)
    output = 0
    
    msg.angular.z = 0.0
    if(xmean < 320):
        msg.angular.z = 1.2
    elif(xmean > 320):
        msg.angular.z = -1.2
    elif(xmean>300 and xmean<320):
        msg.angular.z = 0.0
    else:
        msg.angular.z = 0.0  

    if (ydata==''):
        ymean = 240
    else:
        ymean = float(ydata)
        ymean = int(ymean)
    angle = Int32()

    # angle_output = angle_PID(ymean)
    if(ymean< 240):
        angle.data = 200000
        # angle_pub.publish(100000)
    elif(ymean> 240):
        angle.data = 100000
        # angle_pub.publish(200000)
    else:
        angle.data = 300000
        # angle_pub.publish(300000)

    print(xmean, "  ", ymean)

    signal.signal(signal.SIGINT, sigint_handler)
    # print(msg.angular.z)
    # try:
    #     var=input() 
    #     print(xmean, "  ", ymean)
    # except KeyboardInterrupt:
    #     angle_pub.publish(300000)
    #     print("Keyboard Interrupt was there.\npublished 300000")
    #pub.publish(msg)
    angle_pub.publish(angle)
    yfile.close()
    xfile.close()

def PID(input, setpoint = 320):
    global lastTime, lastErr, kp, ki, kd
    now = time.time()*1000.0
    timeChange = now - lastTime
    error = setpoint - input
    errSum = error*timeChange
    dErr = (error-lastErr)/ timeChange

    output = (kp*error) + (ki*errSum) + (kd*dErr)
    print(output)

    lastErr = error
    lastTime = now

    return output

def angle_PID(input, setpoint = 240):
    global lastTime, lastErr, kp, ki, kd
    now = time.time()*1000.0
    timeChange = now - lastTime
    error = setpoint - input
    errSum = error*timeChange
    dErr = (error-lastErr)/ timeChange

    output = (kp*error) + (ki*errSum) + (kd*dErr)
    print(output)

    angleLastErr = error
    angleLastTime = now

    return output

def main(args=None):
    # global lastErr, kp, ki, kd, lastTime
    
    rclpy.init(args=args)
        
    node = Node('node')
    pub = node.create_publisher(Twist,'/cmd_vel',10)
    angle_pub = node.create_publisher(Int32, '/twisto', 10)

    # node.create_timer(1, timed_callback(pub=pub, file=file))
    # i = 0

    # start_time = time.time()
    # seconds = 0.2
    while (True):
        # current_time = time.time()
        # elapsed_time = current_time - start_time

        # if elapsed_time > seconds:
        timed_callback(pub=pub, angle_pub=angle_pub)
            # start_time=time.time()

    #    i+=1
    
    # node.create_timer(0.2, timed_callback(pub=pub, angle_pub=angle_pub))
    
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== '__main__':
    main()
