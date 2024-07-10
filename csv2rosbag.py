import csv
import rospy
import rosbag
# range_based : 包名
# uwb_range   : msg中的对应的消息类型
from range_based.msg import uwb_range

# 替换为你的CSV文件路径
csv_file_path = './V1_01_easy_range.csv'

# 创建一个新的ROS bag文件
bag = rosbag.Bag('output.bag', 'w')

try:
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # 假设我们创建一个简单的String消息来存储每一行的数据
            # 实际上，你可能需要根据你的数据创建更具体的ROS消息类型
            msg = uwb_range()
            msg.anchorid = int(row['anchor_id'])
            msg.sensorid = int(row['sensor_id'])
            msg.distance = float(row['uwb_distance'])
            msg.anchor_location.x = float(row['anchor_coord.x'])
            msg.anchor_location.y = float(row['anchor_coord.y'])
            msg.anchor_location.z = float(row['anchor_coord.z'])
            msg.sensor_offset.x = float(row['sensor_coord.x'])
            msg.sensor_offset.y = float(row['sensor_coord.y'])
            msg.sensor_offset.z = float(row['sensor_coord.z'])
            # 使用CSV文件中的时间戳作为消息的时间戳
            # 注意：这里假设时间戳字段名为'field.timestamp'，并且是纳秒
            # 你可能需要根据你的CSV格式进行调整
            msg.timestamp = rospy.Time(nsecs=int(float(row['uwb_timestamp'])))
            # 将消息添加到bag文件中，topic名可以根据需要更改
            bag.write('/uwb_range', msg, msg.timestamp)
finally:
    bag.close()