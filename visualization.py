import open3d as o3d
import numpy as np
import os
import json
import pyntcloud
import matplotlib.pyplot as plt

def visualization():
    # folder = './reconstruction/Demo_Scan/ply'
    folder = './data'

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        # 读取文件内容
        ply = o3d.io.read_point_cloud(file_path)
        
        # visualization1
        # 切片
        # selected_points = ply.points[::20]
        # ply_np = np.asarray(selected_points)
        # x, y, z = ply_np[:, 0], ply_np[:, 1], ply_np[:, 2]
        # fig = plt.figure()
        # ax = fig.add_subplot(111, projection='3d')
        # ax.scatter(x, y, z, c=z, cmap='Oranges_r')
        # plt.show()
        
        # visualization2
        num_points = len(ply.points)
        o3d.visualization.draw_geometries([ply], f'Point Cloud ({num_points} points){file}')


if __name__ == '__main__':
    visualization()

