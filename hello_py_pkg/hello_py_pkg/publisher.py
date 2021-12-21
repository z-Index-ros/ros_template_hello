import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisher(Node):

    def __init__(self):
        super().__init__('hello_publisher')
        self.publisher = self.create_publisher(String, 'hello_topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World! #%d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publishing "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    helloPublisher = HelloPublisher()

    rclpy.spin(helloPublisher)

    helloPublisher.destroy_node()
    rclpy.shutdown()

if __name__ == 'main':
    main()
    