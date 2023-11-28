import numpy as np
time_interval = np.array([10,20,30,40,50])
vertical_position = np.array([100,200,300,400,500])
print("Time Interval: ",time_interval)
print("Vertical Position: ",vertical_position)
delta_vertical_position = np.diff(vertical_position)
delta_time_interval = np.diff(time_interval)
print("Changing time interval: ",delta_time_interval)
print("Changing vertical position: ",delta_vertical_position)
avg_velocity =delta_vertical_position/ delta_time_interval
print("Average Velocity: ",avg_velocity)
