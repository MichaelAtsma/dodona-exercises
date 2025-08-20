import math

center = (230, 110)
radius = 40
startAngle = 180
endAngle = 150

if startAngle < endAngle:
    startAngle, endAngle = endAngle, startAngle

x1 = round(center[0] + radius * math.cos(math.radians(startAngle)))
y1 = round(center[1] - radius * math.sin(math.radians(startAngle)))
x2 = round(center[0] + radius * math.cos(math.radians(endAngle)))
y2 = round(center[1] - radius * math.sin(math.radians(endAngle)))

if center[0] > x1:
    orientation = '0 0 1'
else:
    orientation = '0 0 0'

result = f'd="M {x1} {y1} A {radius} {radius} {orientation} {x2} {y2}"'
print(result)