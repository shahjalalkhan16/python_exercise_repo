# Even Numbers: Use a loop to display all even numbers between 1 and 20.

even_num = []
for i in range(1, 21):
    if i%2 == 0:
        even_num.append(i)
   
print(even_num)
