
def canBeDivdedBy(number, divisor):
    if number % divisor == 0:
        return True
    return False
output = []
n = int(input("Enter a number: "))
for value in range(1, n+1):
    if canBeDivdedBy(n, value):
        output.append(value)
print(output)