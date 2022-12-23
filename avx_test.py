import math
import time
import nexstar
import numpy as np


def circle_distance(a, b):
    return (a - b + 180) % 360 - 180


port = '/dev/ttyUSB0'
controller = nexstar.NexstarHandController(port)
speed = 7

position = controller.getPosition()
print(f'Position {position[0]:.2f}, {position[1]:.2f}')
target = [0, 0]
controller.gotoPosition(target[0], target[1], highPrecisionFlag=False)
while True:
    time.sleep(0.1)
    position = controller.getPosition()
    error = math.sqrt(circle_distance(target[0], position[0])**2 + circle_distance(target[1], position[1])**2)
    print(f'Target {target[0]:.2f}, {target[1]:.2f}. Position {position[0]:.2f}, {position[1]:.2f}. Error {error:.2f}')
    if error <= 0.1:
        controller.cancelGoto()
        break

controller.slew_fixed(nexstar.NexstarDeviceId.AZM_RA_MOTOR, 7)
controller.slew_fixed(nexstar.NexstarDeviceId.ALT_DEC_MOTOR, 9)
while True:
    position = controller.getPosition()
    print(f'Position {position[0]:.2f}, {position[1]:.2f}.')

# direction = +1;
# target = 180;
# for i in np.arange(0.0, 45.0, 0.25):
#     # controller.slew_fixed(nexstar.NexstarDeviceId.AZM_RA_MOTOR, speed)
#     controller.slew_fixed(nexstar.NexstarDeviceId.ALT_DEC_MOTOR, direction * speed)
#     while True:
#         time.sleep(0.1)
#         position = controller.getPosition()
#         print(f'Target {i:.2f}, {target:.2f}. Position {position[0]:.2f}, {position[1]:.2f}.')
#         if circle_distance(target, position[1]) <= 0.0:
#             direction = -1*direction
#             target = direction * target


# for i in np.arange(0.0, 45.0, 0.25):
#     while True:
#         time.sleep(0.5)
#         position = controller.getPosition()
#         print(f'Target {i:.2f}, ---. Position {position[0]:.2f}, {position[1]:.2f}.')
#         if circle_distance(i, position[0]) > 0.0:
#             controller.slew_fixed(nexstar.NexstarDeviceId.AZM_RA_MOTOR, speed)
#         else:
#             controller.slew_fixed(nexstar.NexstarDeviceId.AZM_RA_MOTOR, 0)
#             break
#
#     for j in np.arange(0.0, 360.0, 0.25):
#         while True:
#             time.sleep(0.5)
#             position = controller.getPosition()
#             print(f'Target {i:.2f}, {j:.2f}. Position {position[0]:.2f}, {position[1]:.2f}.')
#             if circle_distance(j, position[1]) > 0.0:
#                 controller.slew_fixed(nexstar.NexstarDeviceId.ALT_DEC_MOTOR, speed)
#             else:
#                 controller.slew_fixed(nexstar.NexstarDeviceId.ALT_DEC_MOTOR, 0)
#                 break


# controller.slew_fixed(nexstar.NexstarDeviceId.AZM_RA_MOTOR, -6)
# controller.slew_fixed(nexstar.NexstarDeviceId.ALT_DEC_MOTOR, -6)
#
# while True:
#     time.sleep(0.1)
#     p_new = controller.getPosition()
#     print(f'Position {p_new[0]:.2f}, {p_new[1]:.2f}')

# controller.gotoPosition(0, 0, highPrecisionFlag=False)
#
# while True:
#     time.sleep(0.1)
#     p_new = controller.getPosition()
#     print(p_new)
#     if p == p_new:
#         break
#     p = p_new
