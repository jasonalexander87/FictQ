# -*- coding: utf-8 -*-
"""Ficticious.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ivQdI_4cJyWE30plgChJgo7bfygUAmEc
"""

import numpy as np

def find_payoff(Matrix,mx,mv1,mv2):
  res1 = mv1.dot(Matrix.dot(mx))
  res2 = mv2.dot(Matrix.dot(mx))
  if res1> res2:
    max = res1
    min = res2
  else:
    max = res1
    min = res2
  return max, min    


def selectAction(Matrix, mx, mv1, mv2):
  res1 = mv1.dot(Matrix.dot(mx))
  res2 = mv2.dot(Matrix.dot(mx))
  if res1 > res2:
    return mv1
  else:
    return mv2  

def upper_lower(Matrix,mx,mv1,mv2):
  res1 = mv1.dot(Matrix.dot(mx))
  res2 = mv2.dot(Matrix.dot(mx))
  return res1,res2

def updateBeliefs(beliefs,action,iteration):
  const1 = (iteration-1)/(iteration)
  const2 = 1/iteration
  res = np.multiply(const1,beliefs) + np.multiply(const2,action)
  return res

R = np.array([[ -2, 3], [ 3, -4]])
C = np.array([[ 2, -3], [ -3, 4]])

move1 = np.array([1,0])
move2 = np.array([0,1])

mixed_p1 = np.array([0.9,0.1])
mixed_p2 = np.array([0.1,0.9])

payoff_max = 0
payoff_min = 0
iteration = 1

while iteration < 100:

  action_p1 = selectAction(R,mixed_p2,move1,move2)
  action_p2 = selectAction(C,mixed_p1,move1,move2)

  mixed_p1 = updateBeliefs(mixed_p1,action_p2,iteration)
  mixed_p2 = updateBeliefs(mixed_p2,action_p1,iteration)
  
  max, min = find_payoff(R, mixed_p2,move1,move2)
  print(mixed_p2)
  #print(max,"==",min)
  iteration = iteration +1

import numpy as np

def selectAction(Matrix, mx, mv1, mv2,mv3,mv4):
  res1 = mv1.dot(Matrix.dot(mx))
  res2 = mv2.dot(Matrix.dot(mx))
  res3 = mv3.dot(Matrix.dot(mx))
  res4 = mv4.dot(Matrix.dot(mx))
  array = []
  array.append(res1)
  array.append(res2)
  array.append(res3)
  array.append(res4)
  result = max(array)
  if res1 == result:
    return mv1
  elif res2 == result:
    return mv2
  elif res3 == result:
    return mv3
  else:
    return mv4      

def getActionIndex(action,moves):
  res = np.array_equiv(action, moves[0])
  if res:
    return 0 
  res = np.array_equiv(action, moves[1])
  if res:
    return 1  
  res = np.array_equiv(action, moves[2])
  if res:
    return 2
  res = np.array_equiv(action, moves[3])
  if res:
    return 3    

def updateBeliefs(beliefs,action,iteration):
  const1 = (iteration-1)/(iteration)
  const2 = 1/iteration
  res = np.multiply(const1,beliefs) + np.multiply(const2,action)
  return res

#PAYOFF MATRIX S_0
R_0 = np.array([[0.0,0.0,-0.5,-1.0],[0.0,0.0,-0.5,-1.0],[0.5,0.5,0.0,0.5],[1.0,1.0,-0.5,0.0]])
C_0 = R_0*(-1)
#PAYOFF MATRIX S_1
R_1 = np.array([[0.0,0.0,-0.5,1.0],[0.0,0.0,-0.5,-1.0],[0.5,0.5,0.0,0.0],[1.0,-1.0,0.0,0.0]])
C_1 = R_1*(-1)
#PAYOFF MATRIX S_2
R_2 = np.array([[0.0,0.0,-0.5,-1.0],[0.0,0.0,-0.5,1.0],[0.5,0.5,0.0,0.0],[-1.0,1.0,0.0,0.0]])
C_2 = R_2*(-1)
#MOVES 0=R 1=L 2=B 3=A
moves = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

#STATES 0,1,2,3
states = np.array([0,1,2,3])
#TRANSITION FROM S_0
T_0 = np.array([[0,2,1,1],[1,0,2,3],[2,1,0,0],[3,1,0,3]])
#TRANSITION FROM S_1
T_1 = np.array([[1,0,2,3],[2,1,0,0],[0,2,1,1],[0,3,1,3]])
#TRANSITION FROM S_2
T_2 = np.array([[2,1,0,0],[0,2,1,1],[1,0,2,2],[1,1,2,3]])
#MIXED POLICIES PER STATE
mixed_p1 = np.array([[0.8,0.1,0.1,0.0],[0.7,0.1,0.2,0.0],[0.6,0.1,0.1,0.2]])
mixed_p2 = np.array([[0.8,0.1,0.1,0.0],[0.8,0.1,0.1,0.0],[0.8,0.1,0.1,0.0]])

mixed_total_p1 = np.array([0.8,0.1,0.1,0.0])
mixed_total_p2 = np.array([0.8,0.1,0.1,0.0])

iterations_special = 1
iterations = np.array([1,1,1])
iterations_total = 1
current_state = 0
current_iteration = 1

while iterations_total <10:
 if current_state == 0:
    transition = T_0
    R = R_0
    C = C_0
    mixed_1 = mixed_p1[0]
    mixed_2 = mixed_p2[0]
    current_iteration = iterations[0]
    iterations[0] = iterations[0] + 1
 elif current_state == 1:
    transition = T_1
    R = R_1
    C = C_1
    mixed_1 = mixed_p1[1]
    mixed_2 = mixed_p2[1]
    current_iteration = iterations[1]
    iterations[1] = iterations[1] + 1
 elif current_state == 2:
    transition = T_2
    R = R_2
    C = C_2
    mixed_1 = mixed_p1[2]
    mixed_2 = mixed_p2[2]
    current_iteration = iterations[2]
    iterations[2] = iterations[2] + 1
 else:
    current_state = 0
    transition = T_0
    R = R_0
    C = C_0
    mixed_1 = mixed_p1[0]
    mixed_2 = mixed_p2[0]
    current_iteration = iterations[0]
    iterations[0] = iterations[0] + 1
 
 action_p1 = selectAction(R,mixed_1,moves[0],moves[1],moves[2],moves[3])
 action_p2 = selectAction(C,mixed_2,moves[0],moves[1],moves[2],moves[3])

 action_index_1 = getActionIndex(action_p1,moves)
 action_index_2 = getActionIndex(action_p2,moves)

 mixed_p1[current_state] = updateBeliefs(mixed_p1[current_state],action_p1,current_iteration)
 mixed_p2[current_state] = updateBeliefs(mixed_p2[current_state],action_p2,current_iteration)

 mixed_total_p1 = updateBeliefs(mixed_total_p1,action_p1,iterations_special)
 mixed_total_p2 = updateBeliefs(mixed_total_p2,action_p2,iterations_special)
 
 current_state = T_0[action_index_1][action_index_2]
 iterations_total = iterations_total + 1
 iterations_special = iterations_special + 1
