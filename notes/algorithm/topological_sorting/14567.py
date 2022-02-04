n, m = map(int, input().split())
req = {} # requirements
req_needed = []

# Input requirements
# Key: Requirements
# Value: (next)
for _ in range(m):
    a, b = map(int, input().split())
    req_needed += [b]
    if a not in req:
        req[a] = [b]
    else:
        req[a] += [b]

# Load queue
queue = []
for i in range(1, n+1):
    if i not in req_needed:
        queue += [i]

# Processing
result = []
while queue:
    val = queue.pop(0) # Pop front
    if val not in result: # Block duplicate
        result += [val] # Put val to result
    # Put requirements if val in req.keys()
    if val in req:
        queue += req[val] # req[val] is list.

print(result)