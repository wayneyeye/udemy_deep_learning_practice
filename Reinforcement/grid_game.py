import numpy as np
import random
class grid_game():
    def __init__(self):
        #initialize the 5x5 grid
        self.reward_grid=np.zeros((5,5))
        self.reward_grid[3,2]=-5
        self.reward_grid[2,4]=5
        self.up_grid=np.zeros((5,5))
        self.down_grid=np.zeros((5,5))
        self.left_grid=np.zeros((5,5))
        self.right_grid=np.zeros((5,5))
        # blocks
        self.block_grid=np.zeros((5,5))
        self.block_grid[1,1]=1
        self.block_grid[1,3]=1
        self.block_grid[1,4]=1
        self.block_grid[3,1]=1
        #init state
        self.state=(0,0)
        self.reward_per_step=-1
        self.gameover=False
        self.state_record=[]
        self.reward_record=[]
        self.action_record=[]
    
    def next_step(self,action):
        self.action_record.append(action)
        self.state_record.append(self.state)
        if action=="U" and self.state[0]-1>=0 and self.block_grid[self.state[0]-1,self.state[1]]!=1:
            self.state=(self.state[0]-1,self.state[1])
        if action=="D" and self.state[0]+1<5 and self.block_grid[self.state[0]+1,self.state[1]]!=1:
            self.state=(self.state[0]+1,self.state[1])
        if action=="L" and self.state[1]-1>=0 and self.block_grid[self.state[0],self.state[1]-1]!=1:
            self.state=(self.state[0],self.state[1]-1)
        if action=="R" and self.state[1]+1<5 and self.block_grid[self.state[0],self.state[1]+1]!=1:
            self.state=(self.state[0],self.state[1]+1)
        self.reward_record.append(self.reward_per_step+self.reward_grid[self.state[0],self.state[1]])
        if self.state in [(3,2),(2,4)]:
            self.gameover=True
    
    def reset_game(self):
        #init state
        self.state=(4,0)
        self.gameover=False
        self.state_record=[]
        self.reward_record=[]
        self.action_record=[]
        
    def next_step_random(self):
        available_actions=["U","D","L","R"]
        chosen_action=random.choice(available_actions)
        self.next_step(chosen_action)
Game=grid_game()