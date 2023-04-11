import os

print('#' * 60)


print('#' * 60)
print('-' * 60)      

ip_to_check = input('Please put your IP to ping: ')

print('-' * 60)
os.system('ping -n 4 {}'.format(ip_to_check))
print('-' * 60)

input('Press Enter to exit.')
