rows=int(input("Enter rows:"))
columns=int(input("Enter columns:"))

for row in range(rows):
    for col in range(columns):
        if row==col:
            print("#",end=" ")
        elif row>=col:
            print("@",end=" ")
        else:
            print(' ',end=" ")
    print()
