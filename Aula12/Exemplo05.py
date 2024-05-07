def soma(*args):
   total = 0
   print(args)
   for i in args:
       total += i
   return total

print(soma(1,2,3,4))