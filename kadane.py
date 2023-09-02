
def kadane_algo(arr):
   curr = 0
   res = 0
   for num in arr:
      curr+=num
      if curr<0:
         curr = 0
      res = max(res,curr)
   return res
   
   
def main():
   arr = list(map(int,input().split())
   return kadane_algo(arr)

if __name__=="__main__":
   print(main())


