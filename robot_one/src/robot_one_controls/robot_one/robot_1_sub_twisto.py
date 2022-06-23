from numpy import int32
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
# from my_msgs.msg import Bull
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist


class MinimalSubscriber(Node):
	def __init__(self):
		super().__init__('minimal_subscriber')
		# self.bot = Bull()
		self.bot = Int32()
		
		self.msg = Joy()
		self.subscription = self.create_subscription(Joy, '/joy', self.listener_callback, 10)
		self.subscription  # prevent unused variable warning

		## experiment
		self.publisher_ = self.create_publisher(Int32, '/twisto', 10)
		timer_period = 0.1  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0
				
	def listener_callback(self, msg):
		# if (msg.axes[6]==1):
		# 	self.bot.data = self.bot.data*10 + 1
		# elif (msg.axes[7] == 1):
		# 	self.bot.data = self.bot.data*10 + 2
		# elif (msg.axes[6] == -1):
		# 	self.bot.data = self.bot.data*10 + 3
		# else:
		# 	self.bot.data = self.bot.data*10 + 4
		# # bot.num = msg.axes[6]
		# # global bot
		# self.bot.data = self.bot.data*10 + msg.buttons[3]
		# self.bot.data = self.bot.data*10 + msg.buttons[0]
		# self.bot.data = self.bot.data*10 + msg.buttons[2]
		# self.bot.data = self.bot.data*10 + msg.buttons[1]	

		# self.bot.linear.x = msg.buttons[0] * 1.0
		# self.bot.linear.y = msg.buttons[3] * 1.0
		# self.bot.linear.z = msg.buttons[1] * 1.0
		# if (self.bot.linear.y == 0):
		# 	self.bot.linear.y = msg.buttons[2] * -1.0
		# self.bot.angular.x = msg.axes[5]
		self.bot.data = 0
		if (msg.axes[7]==1):
			self.bot.data = self.bot.data*10 + 1
		elif (msg.axes[7] == -1):
			self.bot.data = self.bot.data*10 + 2
		else:
			self.bot.data = self.bot.data*10 + 3
		
		self.bot.data = self.bot.data*10 + msg.buttons[3]
		self.bot.data = self.bot.data*10 + msg.buttons[2]
		self.bot.data = self.bot.data*10 + msg.buttons[0]
		self.bot.data = self.bot.data*10 + msg.buttons[1]
		self.bot.data = self.bot.data*10 + msg.buttons[10]
		
	def timer_callback(self):
		#data = Bull()
		#data = bot
		#global bot
		self.publisher_.publish(self.bot)
		#self.get_logger().info('Publishing: "%s"' % msg.data)
		self.i += 1	
	
def main(args=None):
	rclpy.init(args=args)
	
	minimal_subscriber = MinimalSubscriber()
	# minimal_publisher = MinimalPublisher()

	rclpy.spin(minimal_subscriber)
	# rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
	minimal_subscriber.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
