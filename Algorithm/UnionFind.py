class Uf:
    def __init__(self,size):
        self.parent = list(range(size))

    def find(self,i):
        if self.parent[i] == i:
            return i
        return  self.find(self.parent[i])
    
    def union(self,i,j):
        repi = self.find(i)
        repj = self.find(j)

        self.parent[repi] = repj

class UnionFind:
    def __init__(self,size):
        self.parent =list(range(size))
        self.rank = [0]*size
        
    def Find(self,i):
        if self.parent[i] != i:
            self.parent[x] = self.Find(self.parent[i]) #path compression
        return self.parent[i]
    
    def Union(self,i,j):
        repi = self.Find(i)
        repj = self.Find(j)

        if repi!=repj:
            if self.rank[repi] < self.rank[repj]:
                self.parent[repi] = repj
            elif self.rank[repi] > self.rank[repj]:
                self.parent[repj] = repi
            else:
                self.parent[repj] = repi
                self.rank[repi] += 1

size = int(input("Enter the size of array:"))
uf = UnionFind(size)

print("Note: Valid indices are 0 to", size-1)
i,j = map(int,input("Enter the Union Elements I,J :").split())
# Check if indices are valid
if 0 <= i < size and 0 <= j < size:
    uf.Union(i,j)
else:
    print("Invalid indices! Must be between 0 and", size-1)
    exit(1)

x,y = map(int,input("Enter the connection of x,y:").split())
# Check if indices are valid
if 0 <= x < size and 0 <= y < size:
    inConnectedTo = (uf.Find(x) == uf.Find(y))
    print(f"Is {x}, {y} connected =", "yes" if inConnectedTo else "No")
else:
    print("Invalid indices! Must be between 0 and", size-1)