from collections import Counter

N_list = ['q', 'q', 'w', 'w', 'd', 'we']
count_list = Counter(N_list)
print(count_list)

N_str = 'шла саша по шоссе и сосала сушку'
count_str = Counter(N_str)
print(count_str)