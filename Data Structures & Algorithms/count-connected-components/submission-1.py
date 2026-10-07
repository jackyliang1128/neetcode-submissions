class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ## disjoint set method
        ## with smart union and path compression

        parent = []
        numOfSet = n
        ## initialize parent array where ith index is ith's parent
        for i in range(n):
            parent.append(i)

        ## initialize size of each set
        rank = [1] * n

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            
            return parent[n]

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            ## smaller size join bigger size
            if rank[p1] < rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        
        for n1, n2 in edges:
            if union(n1, n2):
                numOfSet -= 1
        
        return numOfSet
        
