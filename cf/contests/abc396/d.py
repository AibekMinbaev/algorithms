n, m = map(int, input().split()) 

adj = {v+1:[] for v in range(n)}

for _ in range(m): 
    v, u, w = map(int, input().split()) 
    adj[v].append((u,w)) 
    adj[u].append((v,w))


res = []
seen = set() 

def dfs(node, xor=0): 

    if node == n:
        res.append(xor) 
        return 
    
    seen.add(node) 
    for nei, w in adj[node]: 
        if nei not in seen:
            dfs(nei, xor ^ w) 
    seen.remove(node) 

dfs(1) 
print(min(res)) 