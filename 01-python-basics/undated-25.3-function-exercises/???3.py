import random
def count_draws_until_sum_exceeds(limit: int = 42) -> int:
     limit = 42
     list_ = []
     count = 0
     while True:
         if sum(list_) < limit:
             list_.append(random.randint(1, 10))
             count += 1
         else:

            return count, list_

print(count_draws_until_sum_exceeds())