
def deletenode(parent, val):
    parent[val] = -1
    def findAncestor(i):
        if parent[i] == -1:
            return -1
        if parent[i] != i:
            ancestor = findAncestor(parent[i])
            if ancestor == -1:
                parent[i] = -1
        return parent[i]
    for idx in range(len(parent)):
        findAncestor(idx)
    return parent

print(deletenode([0,0,0,0,3,3,2,4], 2))
