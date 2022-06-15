from collections import Counter, deque

N_list = ['q', 'q', 'w', 'w', 'd', 'we']
count_list = Counter(N_list)
print(count_list)

N_str = 'шла саша по шоссе и сосала сушку'
count_str = Counter(N_str)
print(count_str)

N_str_2 = 'слишком много буков в тексте'
count_str_2 = Counter(N_str_2)

print(f'объеденить {count_str + count_str_2}')
print(f'вычесть {count_str - count_str_2}')
print(f'общее {count_str & count_str_2}')

d = deque('worldofwarcraft')
print(d.popleft())
print(d.pop())

car = N_str
rac = car[::-1] #revers words
print(rac)