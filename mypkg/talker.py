import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")                               #ノード作成
pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャ作成
n = 0 #カウント用変数

def cb():                  #定期的に呼ぶコールバック関数
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)  #タイマー設定（周期0.5[s]）
rclpy.spin(node)            #実行（無限ループ）
