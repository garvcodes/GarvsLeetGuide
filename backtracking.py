# Terminology:
# States - Essentially, a backtracking problem asks you to find a valid state, aka the desired orientation of whatever object you are dealing with.








# Examples: 
# The N-Queen Problem: This involves placing n queens on an n x n chess board such that no queens can attack each other. 
	
# To do this, we build up from previous states. Let’s look at a 4 x 4 board for an example. We can arbitrarily put our first queen wherever we want. Our second queen however, is limited. Next, we see where we can fit our third queen. 
# Finally, we do the same for our last queen. Then, we’ve found a valid solution.

#This is the general template:

def is_valid_state(state):
  #Check if it is a valid solution
  #Implement logic to verify that it is a valid state
  return True

def get_candidates(state):
  return []

def search(state, solutions):
  if is_valid_state(state):
    solutions.append(state.copy())
    #return

for candidate in get_candidates(state):
  state.add(candidate)
  search(state, solutions)
  state.remove(candidate)

def solve():
  solutions = []
  state = set()
  search(state, solutions)
  return solutions


#With that in mind, let's finally solve the N-Queen's problem, which you can find on leetcode at this Link: https://leetcode.com/problems/n-queens/

