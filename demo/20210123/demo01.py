import numpy as np
from utils.file_utils import fileutils
from path import temporary_data_path

# data = {'name':"ly",'age':'23'}
#
# np.save('../../data/temporary_data.npy', data)
# demo1 = np.load('../../data/temporary_data.npy', allow_pickle=True)
# print(demo1.item())
#
# np.save('../../data/temporary_data.npy', {})
# demo2 = np.load('../../data/temporary_data.npy', allow_pickle=True)
# print(demo2.item())

temporary = np.load(fileutils.local_file(temporary_data_path),allow_pickle=True).item()
print(temporary)

