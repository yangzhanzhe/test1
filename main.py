import os
import pickle
import matplotlib.pyplot as plt

file_name_all = os.listdir(r'C:\Users\Shanzhe.Yang\Desktop\data\振动信号')
file_name = []
for i in file_name_all:
    if i[-3:] == 'txt':
        file_name.append(i)
data = {}
for j in file_name:
    file = open(r'C:\Users\Shanzhe.Yang\Desktop\data\振动信号'+ '\\' +j, 'r')
    file_data = file.readlines()[17:-1]
    x, y, z = [], [], []
    for i in file_data:
        temp = i.split('\t')
        x.append(float(temp[0]))
        y.append(float(temp[1]))
        z.append(float(temp[2]))
    file.close()

    # plt.plot(z)
    # plt.show()
    # point1 = 12000
    # point2 = 62000
    # point3 = 63000
    # point4 = 113800
    # data[j[:-4]]['正'] = [x[point1:point2], y[point1:point2], z[point1:point2]]
    # data[j[:-4]]['反'] = [x[point3:point4], y[point3:point4], z[point3:point4]]

    # data[j[:-4]] = [x, y, z]

with open(r'C:\Users\Shanzhe.Yang\Desktop\data\振动信号\data_s.DB', 'wb') as f:
    pickle.dump(data, f)

with open(r'C:\Users\Shanzhe.Yang\Desktop\data\振动信号\data_s.DB', 'rb') as f:
    data_dict = pickle.load(f)


plt.plot(data_dict['norm_1000'][2])
plt.show()

plt.plot(z)
plt.show(block=True)
point1 = 11000
point2 = 60000
point3 = 66000
point4 = 112500
data[j[:-4]] = {}
data[j[:-4]]['正'] = [x[point1:point2], y[point1:point2], z[point1:point2]]
data[j[:-4]]['反'] = [x[point3:point4], y[point3:point4], z[point3:point4]]