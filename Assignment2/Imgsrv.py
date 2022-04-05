'''
Open image-service.txt:
1. if(read image-service.txt == type(number)), copy number to local variable
2. Use Mod operator to mod number with number of images 
3. Write path (ex : /users/cs361-images/{number}.jpg) to image-service.txt
Close file image-service.txt
'''


from time import sleep


while True:
    sleep(1)
    
    with open('image-service.txt', 'r+') as f:
        txt_content = f.read()
        if(txt_content.isnumeric()):
            random_num = int(txt_content) % 4 + 1 
            f.truncate(0)
            f.seek(0)
            #f.write("./cs361/{}.jpg".format(random_num))
            f.write(f'./cs361/{random_num}.jpg')
