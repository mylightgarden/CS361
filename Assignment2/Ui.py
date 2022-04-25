'''
Request for input.
If input == 1:
    1.Open prng-service.txt, write “run” in prng-service.txt , Sleep for 5 seconds 
    2. Read pseudo random number from prng-service.txt
    3. Open image-service.txt, erase data in image-service.txt, write pseudo random number, sleep for 5 seconds 
    4. Read and output image-service.txt
    5. Close image-service.txt and close prng-service.txt
else if input ==2
    return
else 
    print (“unknown option”)
'''
import logging
import os
import sys
from time import sleep

def open_image():
    with open('image-service.txt', 'r') as f:
        txt_content = f.read()
        if txt_content.isnumeric() == False:    
            folder_dir = os.path.dirname(__file__)
            #print('this is folder dir', folder_dir)
            abs_file_path = os.path.join(folder_dir, txt_content)
            os.startfile(abs_file_path)

def get_number_run():
    ask = int(input("Enter 1 to generate a random image, or enter 2 to exit >> ")) 
    if ask == 1 :
        txt_content = ''
        with open("prng-service.txt", "r+") as f:
            f.truncate(0)
            f.seek(0)
            f.write('run')
            
            # logger = setup_custom_logger('run')
            # logger.info('Just wrote run to prng-service.txt')
            
        sleep(5)
            
       
        with open("prng-service.txt", "r") as f:
            txt_content = f.read()
            print(txt_content)
        
        with open("image-service.txt", "r+") as f:
            f.truncate(0)
            f.seek(0)
            if (txt_content.isnumeric()):
                f.write(txt_content)
        sleep(2)
        open_image()

    elif ask == 2:
        return
    
    else:
        print("unknown option")
        
#def write_num_to_image_service():
    
    
def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger   
    
      
if __name__ == "__main__":
    while True:
        get_number_run()
    #open_image()


