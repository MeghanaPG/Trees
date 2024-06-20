class LockingTree:
    # BFS 
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [None] * len(parent)
        self.child = {i:[] for i in range(len(parent))}
        for i in range(1, len(parent)):
            # for parent we are appending it's children
            self.child[parent[i]].append(i)


    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]: return False
        self.locked[num] = user 
        return True 

    def unlock(self, num: int, user: int) -> bool:
        # if it is not unlocked by the same user then we return False
        if self.locked[num] != user: return False 
        # below is the way we unlock the lock 
        self.locked[num] = None
        return True 

    def upgrade(self, num: int, user: int) -> bool:
        # first we will be checking if any of the ancestors is locked 
        i = num 
        # to check till the root 
        while i != -1:
            if self.locked[i]:
                return False
            # above if it's locked we will return false
            # otherwise we keep going up 
            i = self.parent[i]

        lockedCount, q = 0, deque([num])
        while q:
            n = q.popleft()
            # if it is locked we will unlock it and increment the count 
            if self.locked[n]:
                self.locked[n] = None 
                lockedCount += 1 
            # we are taking all the children and adding it to the 
            # q 
            q.extend(self.child[n])

        # for the below condition, we will lock by the user
        if lockedCount > 0:
            self.locked[num] = user 
        return lockedCount > 0 
                



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)