from PIL import Image


im = Image.open('house1.jpg', 'r')
width = im.size[1]
lenght = im.size[0]
maxsize=int(width*lenght)

pixel_values = list(im.getdata())

pixel_new = []
pixel_final = []

b=int(len(pixel_values))
print(b)
print(width)
print(im.size)

y = range(0,b,int(2*lenght))
for m in y:

    x = range(0,lenght,2)
    for n in x:
        n1 = m+n

        a = pixel_values[n1]
        pixel_new.append(a)


print(len(pixel_new))

newlenght = round((lenght+0.6)/2)
newwidth = round((width+0.6)/2)

im.size = (newlenght,newwidth )
print(im.size)


image_out = Image.new(im.mode,im.size)
image_out.putdata(pixel_new)
image_out.save('house1.jpg')

