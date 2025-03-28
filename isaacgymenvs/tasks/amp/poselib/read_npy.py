import numpy as np

# 加载 .npy 文件
data = np.load('/home/gdp/github/IsaacGymEnvs/isaacgymenvs/tasks/amp/poselib/data/atlas_v4_with_multisense.npy', allow_pickle=True)

# 打印数组的形状和数据类型
print("数组形状:", data.shape)
print("数据类型:", data.dtype)

# 如果数组较小，可以打印整个数组
if data.size < 1000:  # 这里假设如果元素数量少于1000个，则打印整个数组
    print("数组内容:\n", data)
    # 为了使用 savetxt，我们需要确保数据是二维的。如果 data 是一维的，我们可以添加一个新的轴。
    # 但是，如果 data 已经是多维的，并且你不想展平它，你需要先处理它。
    # 这里我们假设 data 是一维的，或者我们可以接受将其展平。
    if data.ndim == 1:
        data = data.reshape(-1, 1)  # 将一维数组转换为二维数组，其中每一行只有一个元素
    
else:
    print("数组内容太大，无法完整打印。")