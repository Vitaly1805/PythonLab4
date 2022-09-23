import re
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def get_string_to_list(list_distance_and_point, i):
    result = []

    for key, value in enumerate(list_distance_and_point):
        result.append(list_distance_and_point[key][i].split(","))

    return result


fileForRead = open('n_log1.txt', 'r')
listDistanceAndPoint = re.findall(r'A00000000003 <<<.+ON_LINE-.+distance_arr=\[(.+)],point_arr=\[(.+)],l', fileForRead.read())

listDistance = get_string_to_list(listDistanceAndPoint, 0)
listPoint = get_string_to_list(listDistanceAndPoint, 1)

fileForRead.seek(0)
listTime = re.findall(r'(\d{2}:\d{2}:\d{2},\d{3}).*A00000000003 <<<.+ON_LINE-', fileForRead.read())

start = int(listTime[0][3:5])
substring1 = 'B00000000001'
substring2 = 'B00000000002'
substring3 = 'B00000000003'
substring4 = 'B00000000004'
substring5 = 'B00000000005'
abscissa = []
ordinate = []
abscissa1 = []
ordinate1 = []
abscissa2 = []
ordinate2 = []
abscissa3 = []
ordinate3 = []
abscissa4 = []
ordinate4 = []
abscissa5 = []
ordinate5 = []

fl = True

for key1, value1 in enumerate(listTime):
    if int(value1[3:5]) - start == 10:
        fl = False

    if int(value1[3:5]) - start == 15:
        break

    if fl:
        for key2, value2 in enumerate(listPoint[key1]):
            if value2 == substring4:
                abscissa.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate.append(float(listDistance[key1][key2]))

    if not fl:
        for key2, value2 in enumerate(listPoint[key1]):
            if value2 == substring1:
                abscissa1.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate1.append(float(listDistance[key1][key2]))
            elif value2 == substring2:
                abscissa2.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate2.append(float(listDistance[key1][key2]))
            elif value2 == substring3:
                abscissa3.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate3.append(float(listDistance[key1][key2]))
            elif value2 == substring4:
                abscissa4.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate4.append(float(listDistance[key1][key2]))
            elif value2 == substring5:
                abscissa5.append(datetime.strptime(value1, "%H:%M:%S,%f"))
                ordinate5.append(float(listDistance[key1][key2]))

fig1, ax1 = plt.subplots()
ax1.plot(abscissa, ordinate, label='B00000000004')
ax1.legend(loc='best')
ax1.set_title('График №1', fontsize=20)
plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(abscissa1, ordinate1, color='red', linestyle='-', label='B00000000001')
ax2.plot(abscissa2, ordinate2, color='blue', linestyle='--', label='B00000000002')
ax2.plot(abscissa3, ordinate3, color='green', linestyle='-.', label='B00000000003')
ax2.plot(abscissa4, ordinate4, color='pink', linestyle=':', label='B00000000004')
ax2.plot(abscissa5, ordinate5, color='yellow', linestyle='dashed', label='B00000000005')
ax2.legend(loc='best')
ax2.set_title('График №2', fontsize=20)

plt.show()