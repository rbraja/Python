m,n = map(int,input().split())
product= m * n

# Check if the root squared equals the product
if root * root == product:
    print("yes")
else:
    print("no")
