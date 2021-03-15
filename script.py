# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:07:12 2021

@author: Martin Høigaard Rasmussen
"""

import numpy as np
from numpy.linalg import inv

A = np.array([[ 3, 1 ],[ 2, 6]])
B = np.array([[ -1, 4 ],[ 3, 8]])

print("Task 1")

print("a)")
print(A.T)

print("b)")
print(B.T)

print("c)")
print("@:")
print(A@B)
print("*:")
print(A*B)

print("d)")
ab_multiplied = A@B
print(ab_multiplied.T)

print("e)")
bTaT = B.T@A.T
print(bTaT)

print("f)")
A_T = A.T
print(A_T.T)

print("g)")
print(A@A.T)

print("")
print("Task 2")

A = np.array([[ 2, 1 ],[ 3, 2]])
B = np.array([[ 1, 2 ],[ 3, 4]])

print("a)")
print("A@B:")
print(A@B)
print("B@A:")
print(B@A)

print("")
print("Task 3")

print("a)")
print(inv(A))

print("b)")
print(inv(B))

print("c)")
A_inversed = inv(A)
print(A@A_inversed)

print("d)")
print(A_inversed@A)

print("e)")
B_inversed = inv(B)
print(B@B_inversed)

print("f)")
print(B_inversed@B)

print("")
print("Task 4")

A = np.array([[ 2, 4 ],[ 1, 2]])

print("a)")
#print(inv(A))
print("error - division by zero")

print("")
print("Task 5")
from matplotlib import pyplot as plt
import math 

xs = np.array([0,0,3,3,0,1.5,3]) # List of x coordinates
ys = np.array([1,0,0,1,1,2 ,1]) # List of y coordinates
fig = plt.figure()
fig, ax = plt.subplots()
xs_ys = np.array([xs,ys])
ax.axis('equal')
# Plot the points
ax.plot( *xs_ys, '-', color='b')
# Create a rotation matrix
rot = np.array([[math.cos(math.pi/4),-math.sin(math.pi/4)],[math.sin(math.pi/4),math.cos(math.pi/4)]]) # <-- CHANGE THIS
# turn the two lists (xs, ys) into a list of (x,y) tuples
points = np.array([[x,y] for x,y in zip(xs,ys)])
# Make the transformation:
points_rot = (points @ rot)
# Turn it into a row of xs and a row of ys:
xs_ys_rot = np.array([points_rot[:,0], points_rot[:,1]])
# Finally, plot it
ax.plot( *xs_ys_rot, '-', color='r')
fig




























