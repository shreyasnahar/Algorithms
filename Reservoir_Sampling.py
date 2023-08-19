import random

def get_sampling(k,n):
  sample = [-1 for _ in range(k)]
  
  for i in range(n):
     random_num = random.randint(1,i+1)
     if random_num<=k:
        sample[random_num-1] = i+1
  return sample
  
if __name__=="__main__":
   sampling = get_sampling(4,10)
   print(" ".join(map(str,sampling)))
