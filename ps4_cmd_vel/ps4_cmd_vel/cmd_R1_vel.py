from numpy import int32
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
# from my_msgs.msg import Bull
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from lagori_robot_msgs.msg import RobotOneControls

class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__('minimal_subscriber')
		
		self.r1_cmd = Twist()
		
		self.msg = Joy()
		self.subscription = self.create_subscription(Joy, '/joy', self.listener_callback,10)
		self.subscription  # prevent unused variable warning

		## experiment
		self.publisher_ = self.create_publisher(Twist, '/robot_1/cmd_vel', 10)
		timer_period = 0.1  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
				
	def listener_callback(self, msg):
	  	
		self.r1_cmd.linear.x = 3.5*msg.axes[1]	
		self.r1_cmd.linear.y = 3.5*msg.axes[0]
		self.r1_cmd.linear.z = 0.0
		self.r1_cmd.angular.x = 0.0
		self.r1_cmd.angular.y = 0.0
		self.r1_cmd.angular.z = 0.78*msg.axes[3]
		
	def timer_callback(self):
		self.publisher_.publish(self.r1_cmd)
		self.i += 1	
	
def main(args=None):
	rclpy.init(args=args)
	
	minimal_subscriber = MinimalSubscriber()
	rclpy.spin(minimal_subscriber)
	minimal_subscriber.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
