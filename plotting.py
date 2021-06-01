import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [30,31,31,31,31,31,31,31,31,31,30,29] # average high
z = [23,24,24,24,25,24,24,24,24,24,24,23] # average low
plt.plot(x,y, 'm-.', x, z, 'c:')
plt.xlabel('Months', color='#1e8bc3')
plt.ylabel('Temperature (°C)', color='#e74c3c')
plt.title('Temperature in Singapore', color='#34495e')
high_legend = mpatches.Patch(color='magenta', label='High')
low_legend = mpatches.Patch(color='cyan', label='Low')
plt.legend(handles=[high_legend,low_legend])
plt.show()