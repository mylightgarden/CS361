'''
Pseudorandom number generators (PRNGs):
Open and read Open file: prng-service.txt
If line in file is “run”:
1. Generate random number 
2. Erase “run” from prng-service.txt
3. Write random number in to prng-service.txt
Close file
'''

import random
from time import sleep


while True:
    sleep(1) 
    
    with open('prng-service.txt', 'r+') as f:
        txt_command = f.read()
        
        if txt_command == 'run':
            random_num = random.randint(1,100)
            
            # Clear the file content and move to the beinning of the file             
            f.truncate(0)
            f.seek(0)
            s = str(random_num)
            f.write(s)
    