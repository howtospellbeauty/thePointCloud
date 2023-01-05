import os
import numpy as np
import open3d as o3d

def main():
    folder = './data'

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        ply = o3d.io.read_point_cloud(file_path)

        ply_np = np.asarray(ply.points)
        x, y, z = ply_np[:, 0], ply_np[:, 1], ply_np[:, 2]




if __name__ == '__main__':
    main()