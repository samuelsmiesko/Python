from PIL import Image
import numpy as np



im = Image.open('unnamed.jpg', 'r')
width = im.size[1]
lenght = im.size[0]

pixel_values = list(im.getdata())

pixel_new = []
pixel_final = []
pixel_end = []

print(len(pixel_values))
x = range(1,20736)
last = pixel_values[0]
pixel_new.append(last)
for n in x:
        j = n - 1
        b = pixel_values[j]
        c = pixel_values[n]
        a = (tuple(map(lambda n, j: (int(j/2)) + (int(n/2)), b, c)))

        pixel_new.append(a)

def picture():

    x = range(20736)

    for n in x:
        d = pixel_values[n]
        e = pixel_new[n]
        pixel_final.append(d)
        pixel_final.append(e)


    pixel_new.clear()

    x = range(288,41471)
    last = pixel_final[41471]
    for n in x:
            j = n - 288
            b = pixel_final[j]
            c = pixel_final[n]
            a = (tuple(map(lambda n, j: int((j/2)) + int((n/2)), b, c)))

            pixel_new.append(a)


    x = range(41183,41471)
    last = pixel_final[41471]
    for n in x:

        pixel_new.append(pixel_final[n])

    pixel_new.append(last)


    im.size = (288, 288)

    #a = pixel_new[0:288]
    #b = pixel_final[0:288]
    #pixel_end.append(a)
    #pixel_end.append(b)

    for md in range(0,144):
       for pico in range(0,288):

          pozicia = 288*md+pico
          e = pixel_new[pozicia]

          pixel_end.append(e)

       for pico in range(0,288):
          pozicia = 288*md+pico

          d = pixel_final[pozicia]

          pixel_end.append(d)

picture()
def save():

    #image_out = Image.new(im.mode,im.size)
    #image_out.putdata(pixel_final)
    #image_out.save('test_out.jpg')


    #image_out = Image.new(im.mode,im.size)
    #image_out.putdata(pixel_new)
    #image_out.save('test_out1.jpg')

    image_out = Image.new(im.mode,im.size)
    image_out.putdata(pixel_end)
    image_out.save('test_out2.jpg')
save()
