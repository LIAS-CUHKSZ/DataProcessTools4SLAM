# Convert2Rosbag
Collection of some useful tools to generate rosbags from raw data, especially for NCLT dataset. 

1. <merge_rosbag.py> Merge multiple rosbags into one rosbag. You can select to merge all the topics of some of the topics.
2. <vel2pclrosbag.py> Convert .bin files to pointcloud2 in rosbag. The timestamps are the name of .bin files.
3. <convert_image2rosbag.py> Convert raw images to rosbag. The timestamps are the name of .bin files.
4. </.RTK2XYZ> Convert RTK csv/rosbag to XYZ csv with multiple options.

Other materials and references:
- http://zhaoxuhui.top/blog/2022/06/15/ros-bag-from-various-data-files.html#1%e5%b0%86%e5%bd%b1%e5%83%8f%e5%ba%8f%e5%88%97%e8%bd%ac%e6%8d%a2%e6%88%90bag%e6%96%87%e4%bb%b6
- FastLio:   https://github.com/hku-mars/FAST_LIO
- Faster lio: https://github.com/gaoxiang12/faster-lio  providing some NCLT rosbags(lidar+IMU): https://drive.google.com/drive/folders/1VBK5idI1oyW0GC_I_Hxh63aqam3nocNK
- NCLT dataset: provide scripts to convert raw messages to rosbag (not completed)
