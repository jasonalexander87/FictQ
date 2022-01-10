# -*- coding: utf-8 -*-
"""minimaxQ.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQv7awtCJgv--d0dIKARor_v1LPe1T80
"""

from numpy.linalg.linalg import solve
import numpy as np
import random 
from scipy.optimize import linprog

#R = np.array([[1.0,-1.0],[-1.0,1.0]])
#C = np.array([[-1.0,1.0],[1.0,-1.0]])
R = np.array([[-2.0,3.0],[3.0,-4.0]])
C = np.array([[2.0,-3.0],[-3.0,4.0]])
moves = np.array([0,1])
#Init Values PLAYER1
valueQ_p1 = np.array([[1.0,1.0],[1.0,1.0]])
valueV_p1 = 1.0
valueP_p1 = np.array([0.9,0.1])
#Init Values PLAYER2
valueQ_p2 = np.array([[1.0,1.0],[1.0,1.0]])
valueV_p2 = 1.0
valueP_p2 = np.array([0.9,0.1])

#VALUE OF THE GAME
value_game_p1 = 1.0
value_game_p2 = 1.0

alpha = 1.0
explor = 0.1
notexplor = 0.9

def getRew_p1(action1,action2):
  return R[action1][action2]

def getRew_p2(action1,action2):
  return C[action1][action2]

def chooseMove(movs,wei):
  return random.choices(movs,weights=wei,k=1)[0]

def updateQ_p1(a,rew,mov,movO):
  return (1-a)*valueQ_p1[mov][movO] + a*rew

def updateQ_p2(a,rew,mov,movO):
  return (1-a)*valueQ_p2[mov][movO] + a*rew

def solveLP(Q):
  c = np.array([[0.0,0.0,1.0]])
  b_ub = np.array([0.0,0.0])
  b_eq = np.array([1.0])
  A_eq = np.array([[1.0,1.0,0.0]])
  x0_bounds = (0.0,1.0)
  x1_bounds = (0.0,1.0)
  x2_bounds = (-1.0, 1.0)  # +/- np.inf can be used instead of None
  bounds = [x0_bounds, x1_bounds, x2_bounds]

  test1 = []
  test1.append(Q[0][0])
  test1.append(Q[1][0])
  test1.append(1)

  test2 = []
  test2.append(Q[0][1])
  test2.append(Q[1][1])
  test2.append(1)

  A_ub = []
  A_ub.append(test1)
  A_ub.append(test2)

  result = linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds)

  return result.x[0],result.x[1]


def computeValue2_p1(policy,Q):
  res1 = policy[0]*Q[0][0] + policy[1]*Q[1][0]
  res2 = policy[0]*Q[0][1] + policy[1]*Q[1][1]
  return min(res1,res2)

def computeValue2_p2(policy,Q):
  res1 = policy[0]*Q[0][0] + policy[1]*Q[1][0]
  res2 = policy[0]*Q[0][1] + policy[1]*Q[1][1]
  return max(res1,res2)

def updateAlpha(alhpa):
  decay = 0.95
  return alpha*decay

iterations = 0
while iterations < 1000 :
#RANDOM PLAY OR POLICY PLAY 
 play_random1 = random.random()
 play_random2 = random.random()
 if(play_random1 > explor):
   weights1 = valueP_p1
 else:
   weights1 = np.array([0.5,0.5])
 if(play_random2 > explor):
   weights2 = valueP_p2
 else:
   weights2 = np.array([0.5,0.5])

#EPILOGH KINHSHS GIA KA8E PAIXTH
 move_p1 = chooseMove(moves,weights1)  
 move_p2 = chooseMove(moves,weights2)
 
 reward1 = getRew_p1(move_p1,move_p2)
 reward2 = getRew_p2(move_p2,move_p1)
#UPDATE Q VALUES
 valueQ_p1[move_p1][move_p2] = updateQ_p1(alpha,reward1,move_p1,move_p2)
 valueQ_p2[move_p2][move_p1] = updateQ_p2(alpha,reward2,move_p2,move_p1)

#YPOLOGISMOS TOU NEOU POLICY GIA KA8E PAIXTH
 valueP_p1[0], valueP_p1[1] = solveLP(valueQ_p1)
 valueP_p2[0], valueP_p2[1] = solveLP(valueQ_p2)
#UPDATE VALUE OF THE GAME FOR PLAYERS
 value_game_p1 = computeValue2_p1(valueP_p1,valueQ_p1)
 value_game_p2 = computeValue2_p2(valueP_p2,valueQ_p2)
#UPDATE ALPHA
 alpha = updateAlpha(alpha)

 iterations = iterations + 1
 

print(value_game_p1)
print(value_game_p2)

from numpy.linalg.linalg import solve
import numpy as np
import random 
from scipy.optimize import linprog

#FUNCTION TO CHOOSE MOVE BASED ON WEIGTHS
def chooseMove(movs,wei):
  return random.choices(movs,weights=wei,k=1)[0]

#FUNCTION TO RETURN REWARD BASED ON ACTIONS AND STATE FOR PLAYER 1
def getRew_p1(action1,action2,state):
  if state == 0:
    return R_0[action1][action2]
  elif state == 1:
    return R_1[action1][action2]
  else:
    return R_2[action1][action2]    
  
#FUNCTION TO RETURN REWARD BASED ON ACTIONS AND STATE FOR PLAYER 2
def getRew_p2(action1,action2,state):
  if state == 0:
    return C_0[action1][action2]
  elif state == 1:
    return C_1[action1][action2]
  else:
    return C_2[action1][action2] 

#FUNCTION TO UPDATE Q VALUE BASED ON PARAMETERS FOR PLAYER 1
def updateQ_p1(a,rew,mov,movO,state):
  if state == 0:
    return (1-a)*valueQ_state1_p1[mov][movO] + a*rew
  elif state == 1:
    return (1-a)*valueQ_state2_p1[mov][movO] + a*rew
  else:
    return (1-a)*valueQ_state3_p1[mov][movO] + a*rew  

#FUNCTION TO UPDATE Q VALUE BASED ON PARAMETERS FOR PLAYER 2
def updateQ_p2(a,rew,mov,movO,state):
  if state == 0:
    return (1-a)*valueQ_state1_p2[mov][movO] + a*rew
  elif state == 1:
    return (1-a)*valueQ_state2_p2[mov][movO] + a*rew
  else:
    return (1-a)*valueQ_state3_p2[mov][movO] + a*rew 

#SOLVE LINERAR PROGRAM TO FIND POLICY 
def solveLP(state,player):
  if state == 0 and player == 0:
    Q = valueQ_state1_p1
  elif state == 1 and player == 0:
    Q = valueQ_state2_p1
  elif state == 2 and player == 0:
    Q = valueQ_state3_p1
  elif state == 0 and player == 1:
    Q = valueQ_state1_p2
  elif state == 1 and player == 1:
    Q = valueQ_state2_p2
  else:
    Q = valueQ_state3_p2      

  c = np.array([[0.0,0.0,0.0,0.0,1.0]])
  b_ub = np.array([0.0,0.0,0.0,0.0])
  b_eq = np.array([1.0])
  A_eq = np.array([[1.0,1.0,1.0,1.0,0.0]])
  x0_bounds = (0.0,1.0)
  x1_bounds = (0.0,1.0)
  x2_bounds = (0.0,1.0)
  x3_bounds = (0.0,1.0)
  x4_bounds = (-1.0, 1.0)  # +/- np.inf can be used instead of None
  bounds = [x0_bounds, x1_bounds, x2_bounds, x3_bounds, x4_bounds]

  test1 = []
  test1.append(Q[0][0])
  test1.append(Q[1][0])
  test1.append(Q[2][0])
  test1.append(Q[3][0])
  test1.append(1)

  test2 = []
  test2.append(Q[0][1])
  test2.append(Q[1][1])
  test2.append(Q[2][1])
  test2.append(Q[3][1])
  test2.append(1)

  test3 = []
  test3.append(Q[0][2])
  test3.append(Q[1][2])
  test3.append(Q[2][2])
  test3.append(Q[3][2])
  test3.append(1)

  test4 = []
  test4.append(Q[0][3])
  test4.append(Q[1][3])
  test4.append(Q[2][3])
  test4.append(Q[3][3])
  test4.append(1)

  A_ub = []
  A_ub.append(test1)
  A_ub.append(test2)
  A_ub.append(test3)
  A_ub.append(test4)

  result = linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=bounds)

  return result.x[0],result.x[1],result.x[2],result.x[3]

#COMPUTE THE VALUE OF THE STATE
def computeValue_p1(state):
  if state == 0:
    Q = valueQ_state1_p1
    P = valueP_p1[0]
  elif state == 1:
    Q = valueQ_state2_p1
    P = valueP_p1[1]
  else:
    Q = valueQ_state3_p1
    P = valueP_p1[2]
  
  res1 = P[0]*Q[0][0] + P[1]*Q[1][0] + P[2]*Q[2][0] + P[3]*Q[3][0] 
  res2 = P[0]*Q[0][1] + P[1]*Q[1][1] + P[2]*Q[2][1] + P[3]*Q[3][1]  
  res3 = P[0]*Q[0][2] + P[1]*Q[1][2] + P[2]*Q[2][2] + P[3]*Q[3][2] 
  res4 = P[0]*Q[0][3] + P[1]*Q[1][3] + P[2]*Q[2][3] + P[3]*Q[3][3] 

  array = []
  array.append(res1)
  array.append(res2)
  array.append(res3)
  array.append(res4)
  result = max(array)

  return result

def computeValue_p2(state):
  if state == 0:
    Q = valueQ_state1_p2
    P = valueP_p2[0]
  elif state == 1:
    Q = valueQ_state2_p2
    P = valueP_p2[1]
  elif state == 2:
    Q = valueQ_state3_p2
    P = valueP_p2[2]
  
  res1 = P[0]*Q[0][0] + P[1]*Q[1][0] + P[2]*Q[2][0] + P[3]*Q[3][0] 
  res2 = P[0]*Q[0][1] + P[1]*Q[1][1] + P[2]*Q[2][1] + P[3]*Q[3][1]  
  res3 = P[0]*Q[0][2] + P[1]*Q[1][2] + P[2]*Q[2][2] + P[3]*Q[3][2] 
  res4 = P[0]*Q[0][3] + P[1]*Q[1][3] + P[2]*Q[2][3] + P[3]*Q[3][3] 

  array = []
  array.append(res1)
  array.append(res2)
  array.append(res3)
  array.append(res4)
  result = min(array)

  return result   

#UPDATE ALPHA BASED ON a = 1/k NOT DECAY THIS TIME !!!
def updateAlphaKappa(player,mov,mov0,state):
  if state == 0 and player == 0:
    alpha = alpha_s1_p1
    kappa = kappa_state_1_p1
  elif state == 1 and player == 0:
    alpha = alpha_s2_p1
    kappa = kappa_state_2_p1
  elif state == 2 and player == 0:
    alpha = alpha_s3_p1
    kappa = kappa_state_3_p1
  elif state == 0 and player == 1:
    alpha = alpha_s1_p2
    kappa = kappa_state_1_p2
  elif state == 1 and player == 1:
    alpha = alpha_s2_p2
    kappa = kappa_state_2_p2
  else:
    alpha = alpha_s3_p2
    kappa = kappa_state_3_p2

  kappa_new = kappa[mov][mov0] +1
  kappa[mov][mov0] = kappa_new
  alpha[mov][mov0] = 1/kappa[mov][mov0] 


#PAYOFF MATRIX S_0 STATE 0 
R_0 = np.array([[0.0,0.0,-0.5,-1.0],[0.0,0.0,-0.5,-1.0],[0.5,0.5,0.0,0.5],[1.0,1.0,-0.5,0.0]])
C_0 = R_0*(-1)
#PAYOFF MATRIX S_1 STATE 1
R_1 = np.array([[0.0,0.0,-0.5,1.0],[0.0,0.0,-0.5,-1.0],[0.5,0.5,0.0,0.0],[1.0,-1.0,0.0,0.0]])
C_1 = R_1*(-1)
#PAYOFF MATRIX S_2 STATE 2
R_2 = np.array([[0.0,0.0,-0.5,-1.0],[0.0,0.0,-0.5,1.0],[0.5,0.5,0.0,0.0],[-1.0,1.0,0.0,0.0]])
C_2 = R_2*(-1)
#MOVES 0=R 1=L 2=B 3=A POSSIBLE MOVES
moves = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
movs = np.array([0,1,2,3])


#STATES 0,1,2,3 STATE 3 IS TERMINAL 
states = np.array([0,1,2,3])
#TRANSITION FROM S_0
T_0 = np.array([[0,2,1,1],[1,0,2,3],[2,1,0,0],[3,1,0,3]])
#TRANSITION FROM S_1
T_1 = np.array([[1,0,2,3],[2,1,0,0],[0,2,1,1],[0,3,1,3]])
#TRANSITION FROM S_2
T_2 = np.array([[2,1,0,0],[0,2,1,1],[1,0,2,2],[1,1,2,3]])

#Init Values PLAYER1 Q VALUES FOR EACH STATE AND ACTION PROFILE
valueQ_state1_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
valueQ_state2_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
valueQ_state3_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
#VALUE OF EACH STATE PLAYER 1
valueV_p1 = np.array([1.0,1.0,1.0])
#POLICY VALUE ONE FOR EACH STATE
valueP_p1 = np.array([[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]])

#Init Values PLAYER2
valueQ_state1_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
valueQ_state2_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
valueQ_state3_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])

valueV_p2 = np.array([1.0,1.0,1.0])
valueP_p2 = np.array([[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]])

#ALPHA VALUE FOR EACH STATE AND ACTION PROFILE
alpha_s1_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
alpha_s2_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
alpha_s3_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
#K values for each state action profile
kappa_state_1_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
kappa_state_2_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
kappa_state_3_p1 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])

#ALPHA VALUE FOR EACH STATE AND ACTION PROFILE player 2
alpha_s1_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
alpha_s2_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
alpha_s3_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
#K values for each state action profile player 2
kappa_state_1_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
kappa_state_2_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])
kappa_state_3_p2 = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0]])

#STARTING STATE
current_state = 0
explor = 0.1

iterations = 1

while iterations < 1000 :
 if current_state == 3:
   current_state = 0 
#RANDOM PLAY OR POLICY PLAY 
 play_random1 = random.random()
 play_random2 = random.random()
 if(play_random1 > explor):
   weights1 = valueP_p1[current_state]
 else:
   weights1 = np.array([0.25,0.25,0.25,0.25])
 if(play_random2 > explor):
   weights2 = valueP_p2[current_state]
 else:
   weights2 = np.array([0.25,0.25,0.25,0.25])
#CHOOSE MOVES  
 move_p1 = chooseMove(movs,weights1)  
 move_p2 = chooseMove(movs,weights2) 
#GET REWARD
 reward1 = getRew_p1(move_p1,move_p2,current_state)
 reward2 = getRew_p2(move_p2,move_p1,current_state)
#UPDATE Q VALUES
 if current_state == 0:
   alpha_1 = alpha_s1_p1[move_p1][move_p2]
   alpha_2 = alpha_s1_p2[move_p2][move_p1]

   updateAlphaKappa(0,move_p1,move_p2,current_state)
   updateAlphaKappa(1,move_p2,move_p1,current_state)

   valueQ_state1_p1[move_p1][move_p2] = updateQ_p1(alpha_1,reward1,move_p1,move_p2,current_state)
   valueQ_state1_p2[move_p2][move_p1] = updateQ_p2(alpha_2,reward2,move_p2,move_p1,current_state)
 elif current_state == 1:
   alpha_1 = alpha_s2_p1[move_p1][move_p2]
   alpha_2 = alpha_s2_p2[move_p2][move_p1]

   updateAlphaKappa(0,move_p1,move_p2,current_state)
   updateAlphaKappa(1,move_p2,move_p1,current_state)

   valueQ_state2_p1[move_p1][move_p2] = updateQ_p1(alpha_1,reward1,move_p1,move_p2,current_state)
   valueQ_state2_p2[move_p2][move_p1] = updateQ_p2(alpha_2,reward2,move_p2,move_p1,current_state)
 else:
   alpha_1 = alpha_s3_p1[move_p1][move_p2]
   alpha_2 = alpha_s3_p2[move_p2][move_p1]

   updateAlphaKappa(0,move_p1,move_p2,current_state)
   updateAlphaKappa(1,move_p2,move_p1,current_state)

   valueQ_state3_p1[move_p1][move_p2] = updateQ_p1(alpha_1,reward1,move_p1,move_p2,current_state)
   valueQ_state3_p2[move_p2][move_p1] = updateQ_p2(alpha_2,reward2,move_p2,move_p1,current_state)  
#FIND POLICY

 valueP_p1[current_state][0],valueP_p1[current_state][1],valueP_p1[current_state][2],valueP_p1[current_state][3] = solveLP(current_state,0)
 valueP_p2[current_state][0],valueP_p2[current_state][1],valueP_p2[current_state][2],valueP_p2[current_state][3] = solveLP(current_state,1)

 valueV_p1[current_state] = computeValue_p1(current_state)
 valueV_p2[current_state] = computeValue_p2(current_state)

 if current_state == 0:
    current_state = T_0[move_p1][move_p2]
 elif current_state == 1:
    current_state = T_1[move_p1][move_p2]
 elif current_state == 2:
    current_state = T_2[move_p1][move_p2]
 else:
    current_state = 0   

 iterations = iterations +1


print(valueQ_state1_p1[0])
print(valueQ_state1_p1[1])
print(valueQ_state1_p1[2])
print(valueQ_state1_p2[0])
print(valueQ_state1_p2[1])
print(valueQ_state1_p2[2])