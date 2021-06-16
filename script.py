from PIL import Image

# read image
im = Image.open('ascii-pineapple.jpg')

print('Successfully loaded image!')
print(f'Image size: {im.size[0]} x {im.size[1]}')

# load pixel data of image
px = im.load()

width, height = im.size

# 2D array of pixels
pixel_list = [[x for x in list(im.getdata())]]

# loop through array and print all pixels of image
print('Iterating through pixel contents')
for x in range(len(pixel_list)):
    for y in range(len(pixel_list[x])):
        pixel = pixel_list[x][y]
        # print(pixel)

# construct brightness matrix
brightness_matrix = [[round((x[0]+x[1]+x[2])/3) for x in list(im.getdata())]]

# loop through brightness matrix
print('Iterating through pixel brightness')
for x in range(len(brightness_matrix)):
    for y in range(len(brightness_matrix[x])):
        pixel = brightness_matrix[x][y]
        # print(pixel)

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
print(len(list(chars)))

value_of_char = round(255/len(chars))

print(value_of_char)

chars_matrix = []
for x in range(len(brightness_matrix)):
    for y in range(len(brightness_matrix[x])):
        pixel = brightness_matrix[x][y]
        # print(pixel)
        char_index = round(pixel/value_of_char)
        char_list = [chars[char_index]]
        chars_matrix.append(char_list)
        # print(chars[char_index])

print('Iterating through pixel brightness')
for x in range(len(chars_matrix)):
    for y in range(len(chars_matrix[x])):
        pixel = chars_matrix[x][y]
        print(pixel*3, end='')
