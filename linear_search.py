
def linear_search(arr,item):
   ''' Inbuilt function to find the index'''
   return arr.index(item)!=-1
   
def main():
   arr = list(map(int,input().split()))
   item = int(input())
   
   print(linear_search(arr,item))
   return
   
if __name__=="__main__":
   print(main())
