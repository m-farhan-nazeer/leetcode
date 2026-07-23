class Solution:
    def reverseQueue(self, q):
        # Base case: check if the deque is empty
        if len(q) == 0:
            return q
            
        # Step 1: Remove the front element
        front = q.popleft()
        
        # Step 2: Recursively reverse the remaining queue
        self.reverseQueue(q)
        
        # Step 3: Append the front element to the back
        q.append(front)
        
        # Return the modified queue object
        return q
