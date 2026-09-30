import random
random.seed(42)
random_data=random.sample(range(1,1000),100)
sorted_data=list(range(100))
reverse_data=list(range(99,-1,-1))
nearly_sorted=list(range(100))
nearly_sorted[40],nearly_sorted[41]=nearly_sorted[41],nearly_sorted[40]
