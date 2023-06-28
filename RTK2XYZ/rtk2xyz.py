from pyproj import CRS
from pyproj import Transformer
import pandas as pd
import numpy as np

def rtk2xyz(header, input_csv, output_csv, epsg = 32650, flag = False, base = []):
    """[RTK].csv to [XYZ].csv

    Args:
        header (string list): header of the csv file (can only includes the columns you need)
        input_csv (string): path of RTK csv file
        output_csv (string): path of XYZ csv file
        epsg (int): epsg code of the utm zone or other projected coordinate (default: 32650 which is the code of UTM50N)
        flag (bool): whether to use numpy to improve the accuracy using float64 (default: False)
        base (number list): [longitude, latitude] of the base point (default: [])
    """
    
    rtk_crs = CRS.from_epsg(4326) # WGS84 -- GPS所用坐标系统
    utm_crs = CRS.from_epsg(epsg) # UTM50N -- UTM投影坐标系统（正东方向为x轴正方向，正北方向为y轴正方向）
    transformer = Transformer.from_crs(rtk_crs, utm_crs)

    # 从csv读取
    if(flag):
        data = pd.read_csv(input_csv,usecols=header,dtype={'longitude':np.float64,'latitude':np.float64})
    else:
        data = pd.read_csv(input_csv,usecols=header,dtype={'longitude':float,'latitude':float})

    # 基准点
    if(base==[]):
        base_longitude = data['longitude'][0]
        base_latitude = data['latitude'][0]
        base_x , base_y = transformer.transform(base_latitude,base_longitude)
    else:
        base_x , base_y = transformer.transform(base[1],base[0])

    # 整体运算
    data['longitude'],data['latitude'] = transformer.transform(data['latitude'],data['longitude'])
    data['longitude'] = data['longitude'] - base_x
    data['latitude'] = data['latitude'] - base_y

    data.rename(columns={'longitude':'x','latitude':'y','altitude':'z'},inplace=True)

    # 输出到csv
    data.to_csv(output_csv,index=False)