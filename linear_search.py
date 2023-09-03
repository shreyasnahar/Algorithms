
def linear_search(arr,item):
   ''' Inbuilt function to find the index'''
   ''' Checks the index of item in arr'''
   return arr.index(item)!=-1
   
def main():
   arr = list(map(int,input().split()))
   item = int(input())
   
   print(linear_search(arr,item))
   return
   
if __name__=="__main__":
   print(main())
