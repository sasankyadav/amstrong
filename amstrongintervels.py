x = int(raw_input())
y = int(raw_input())
 
for num in range(x,y + 1):
   sum = 0
 
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
