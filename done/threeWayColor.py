import random
colors = ['blue', 'red', 'green', 'banana']

# WAY 1
secret_color = random.randrange(0, len(colors) - 1)
print("Colors is:", colors[secret_color])
# WAY 2
print("Color is: ", random.choice(colors))
# WAY 3
# shuffle is mix the value in the list 
shuffle_color = random.shuffle(colors)
print("colors is:", colors[0])