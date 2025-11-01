n = int(input())
alice = list(map(int, input().split()))
m = int(input())
bob = list(map(int, input().split()))

i=j=0
result = []

while i<n and j<m:
    if alice[i]<=bob[j]:
        