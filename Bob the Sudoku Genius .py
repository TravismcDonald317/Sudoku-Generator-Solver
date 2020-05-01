#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import random
from random import randint, shuffle
from time import sleep


# In[2]:


grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


# In[3]:


#using turtle to make the grid for the sudoku game. I will name him "bob".I want bob to be a cat but idk if thats possible.
bob= turtle.Turtle()
turtle.title("Bob's Sudoku")
bob.speed(10)
bob.color('black')
bob.shape("turtle")
topLeft_x=-150
topLeft_y=150


# In[4]:


def text(message,x,y,size):
    FONT = ('Times New Roman', size, 'normal')
    bob.penup()
    bob.goto(x,y)    		  
    bob.write(message,align="left",font=FONT)


# In[5]:


#now I need to draw the sudoku map using bob I want the outside to be a thicker border than the inside
def drawGrid(grid):
    intDim= 35
    for row in range(0,10):
        if (row%3)==0:
            bob.pensize(4)
        else:
            bob.pensize(1)
        bob.penup()
        bob.goto(topLeft_x,topLeft_y-row*intDim)
        bob.pendown()
        bob.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
    
    for col in range(0,10):
        if (col%3)==0:
            bob.pensize(4)
        else:
            bob.pensize(1)
        bob.penup()
        bob.goto(topLeft_x+col*intDim,topLeft_y)
        bob.pendown()
        bob.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

    for row in range (0,9):
      for col in range (0,9):
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)

        


# In[6]:


def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        if grid[row][col]==0:
          return False
    
  return True 


# In[7]:


def solveGrid(grid):
  global counter
  
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        
        if not(value in grid[row]):
          
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                counter+=1
                break
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col]=0  

numberList=[1,2,3,4,5,6,7,8,9]


# In[8]:


#Using a backtracking/recursive function to help generate a possible sudoku solution 
def fillGrid(grid):
  global counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      shuffle(numberList)      
      for value in numberList:
        
        if not(value in grid[row]):
         
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if checkGrid(grid):
                return True
              else:
                if fillGrid(grid):
                  return True
      break
  grid[row][col]=0             


# In[9]:


fillGrid(grid)
drawGrid(grid) 
bob.getscreen().update()
sleep(5)


# In[10]:


#Now we have a full sudoku solution that bob has drawn for us (thanks bob!) now we need to create a solvable sudoku map!
#I want this to be aple to be able to create different levels of difficulty so I will be using a random number generator on the number attempts
#the more the attempts = the more difficult the problem so here I have max difficulty set to 7

attempts = random.randint(2,6)
counter = 1
while attempts>0:
  row = randint(0,8)
  col = randint(0,8)
  while grid[row][col]==0:
    row = randint(0,8)
    col = randint(0,8)
    
  backup = grid[row][col]
  grid[row][col]=0
    
  copyGrid = []
  for r in range(0,9):
     copyGrid.append([])
     for c in range(0,9):
        copyGrid[r].append(grid[r][c])
  counter=0     
  solveGrid(copyGrid)   
    
  if counter!=1:
    grid[row][col]=backup
    attempts -= 1
    
  bob.clear()
  drawGrid(grid)
  bob.getscreen().update()

print("Bob's hand-made puzzle ... for you!")
text("Bob's hand-made puzzle ... for you!", -175,-250,20)
      


# In[11]:


#Well this takes an absolutely long time but it works!
#I will just have to come back to it later! Now I want to solve it but I want enough time to copy it down and work it out!
#I want to try a sleep function 
sleep(20)


# In[12]:


#Now I want to have bob solve his puzzle! I will be checking the rows and the columns to see if a values from [1,10] have been used.
#Then it will make sure that the value is not being used already in the local 3x3 square
#if there is an error then bob will backtrack and remove the values he added to the puzzle and input new ones (this isn't the most elegant solution but it works)

def solveGrid(grid):
  for i in range(0,81):
    row=i//9
    col=i%9
    if grid[row][col]==0:
      for value in range (1,10):
        if not(value in grid[row]):
          if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              bob.clear()
              drawGrid(grid) 
              bob.getscreen().update()            
              if checkGrid(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  print("Backtrack")
  grid[row][col]=0  
  
drawGrid(grid) 
bob.getscreen().update()


# In[13]:


complete = solveGrid(grid)
if complete:
  print("Bob is done!")
  text("Bob is done!",-50,-230,20)
else:  
  print("Bob is confused...")
  text("Bob is confused...",-90,-230,20)
    
bob.getscreen().update()	


# In[ ]:




