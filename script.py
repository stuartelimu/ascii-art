from PIL import Image

# read image
im = Image.open('img.png')

print('Successfully loaded image!')
print(f'Image size: {im.size[0]} x {im.size[1]}')