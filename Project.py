
#JOY OF PROGRAMMING USING PYTHON
#PROJECT ON IMAGE PROCESSING
print("\n\t\tWELCOME TO IMAGEEDITS\n")
print("CHOICES :- \n")
print("\t 1 :- Image Rotation & Grayscale")
print("\t 2 :- Image Cropping & Blurring Effect")
print("\t 3 :- Image Flipping & Merging The RGB Bands")
print("\t 4 :- Merging Images")
print("\t 5 :- Image Resizing ")
print("\t 6 :- Watermark On Image")
print("\t 7 :- Image Formation")
for n in range(1,9):    
    n=int(input("Enter Your Choice :- "))
    print("\nYour Choice Is :-",n)
    
    
    if n==1:
        
        #Import required image library
        from PIL import Image
    
        #Open image
        im = Image.open("C:/Dhaval/Photos/lykan.jpg")
    
        #Display original image
        im.show()
        im = Image.open("C:/Dhaval/Photos/lykan.jpg").convert('L')
    
        #Image rotation & in grayscale
        im.rotate(45).show()
        
        #Save the image
        im.save('C:/Dhaval/Photos/rotation&grayscale.jpg')
    
    
    elif n==2:
        
        #Import required image library
        from PIL import Image, ImageFilter
     
        #Open image
        OriImage = Image.open('C:/Dhaval/Photos/lykan.jpg')
        
        #Display original image
        OriImage.show()
        
        #Applying boxblur filter
        boxImage = OriImage.filter(ImageFilter.BoxBlur(20))
    
        #Save boxblur image
        boxImage.save('C:/Dhaval/Photos/boxblur.jpg')
    
        #left, upper, right, lower
        #Crop
        cropped = boxImage.crop((700,20,1500,900))
    
        #Display the cropped & blurred image
        cropped.show()
    
        #Save the cropped image
        cropped.save('C:/Dhaval/Photos/cropped.jpg')
        
        
    elif n==3:
        
        #Using the merge() function, we can merge the RGB bands of an image  
        #Import required image library
        from PIL import Image
        
        #Open image
        image = Image.open("C:/Dhaval/Photos/lykan.jpg")
        r, g, b = image.split()
        
        #Display original image
        image.show()
        image = Image.merge("RGB", (b, g, r))
        
        #Do a flip of left and right
        hori_flippedImage = image.transpose(Image.FLIP_LEFT_RIGHT)
        
        #Display the horizontal flipped image
        hori_flippedImage.show()
        
        #Save the image
        hori_flippedImage.save('C:/Dhaval/Photos/merge&flip.jpg')
        
        
    elif n==4:
        
        #Import required image library
        from PIL import Image
        
        #Open the two images
        image1 = Image.open('C:/Dhaval/Photos/lykan.jpg')
        image1.show()
        image2 = Image.open('C:/Dhaval/Photos/hypersport.jpg')
        image2.show()
        
        #resize, first image
        image1 = image1.resize((426, 240))
        
        #resize, second image
        image2 = image2.resize((426, 240))
        
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(image1_size[0],0))
        
        #Save the image
        new_image.save("C:/Dhaval/Photos/merged_image.jpg","JPEG")
        
        #Display merged images
        new_image.show()
        
        
    elif n==5:
        
        #Import required image library
        from PIL import Image
        
        #Open image
        im = Image.open("C:/Dhaval/Photos/lykan.jpg")
        
        #Display original image
        im.show()
        
        #Make the new image half the width and half the height of the original image
        resized_im = im.resize((round(im.size[0]*0.09), round(im.size[1]*0.09)))
        
        #Display the resized imaged
        resized_im.show()
        
        #Save the resized image
        resized_im.save('C:/Dhaval/Photos/resized.jpg')
        
        
    elif n==6:
        
            
        #Import required image library
        from PIL import Image, ImageDraw, ImageFont
        
        #Open image
        im = Image.open('C:/Dhaval/Photos/lykan.jpg')
        width, height = im.size
        
        draw = ImageDraw.Draw(im)
        text = "lykan Hypersport"
        
        font = ImageFont.truetype('arial.ttf', 250)
        textwidth, textheight = draw.textsize(text, font)
        
        #calculate the x,y coordinates of the text
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        
        #draw watermark on the image
        draw.text((x, y), text, font=font)
        
        #Display image
        im.show()
        
        #Save watermarked image
        im.save('C:/Dhaval/Photos/watermark.jpg')
        
        
    elif n==7:
        #Import required image library
        from PIL import Image
        import numpy as np
        
        arr = np.zeros([150,300], dtype=np.uint8)
        
        #Set grey value to black or white depending on x position
        for x in range(300):
            for y in range(150):
                 if (x % 16) // 8 == (y % 16)//8:
                    arr[y, x] = 0
                 else:
                    arr[y, x] = 255
        img = Image.fromarray(arr)
        
        #Display image
        img.show()
        
        #Save the image
        img.save('C:/Dhaval/Photos/greyscale.jpg')
        
        continue
        
    
    else:
        
        print("\nThe entered choice is NOT VALID! Please Enter it again")
        
#***************************** END OF THE CODE ****************************** 
