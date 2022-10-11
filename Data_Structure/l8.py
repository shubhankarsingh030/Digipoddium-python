from turtle import color


colors = ['red','white','green','purple','blue','black',
            'grey','orange','violet']

color_with_a = []
color_ending_with_n = []
for color in colors:
    if 'a' in color:
        color_with_a.append(color)
    if  color.endswith('n'):
        color_ending_with_n.append(color)

print(color_with_a)
print(color_ending_with_n)
