# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
class Solution:
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    def detect(node, colors, adj, parent):
	        colors[node] = 1
	        nbrs = adj[node]
	        
	        for nbr in nbrs:
	            if nbr == parent:
	                continue
	            
	            if colors[nbr] == 1:
	                return True
	            
	            is_cycle = detect(nbr, colors, adj, node) if colors[nbr] == 0 else False
	            if is_cycle:
	                return True
	               
	        colors[node] = 2
	       
	        return False
	        
		colors = [0]*V
		
		for i in range(V):
		    if colors[i] == 0:
		        is_cycle = detect(i, colors, adj, -1)
		        if is_cycle:
		            return 1
		 
		return 0