import rosbag

# 要合并的rosbag文件列表
bag_files = ['path 1', 'path 2']

# 输出的rosbag文件
output_bag_file = 'path to output file'

with rosbag.Bag(output_bag_file, 'w') as outbag:
    for bag_file in bag_files:
        with rosbag.Bag(bag_file, 'r') as inbag:
            for topic, msg, t in inbag.read_messages():
                outbag.write(topic, msg, t)