from glob import iglob
from random import randint
from PIL import Image
from numpy import array

# Create an empty stack

stack = []

# Open all the images in the 'images/original' folder and convert it numpy array
# and store it in the stack

for f in iglob("images/original/*"):
    stack.append(array(Image.open(f)))

lenImages = len(stack)

newImage = stack[0]

# The newly created collage will have 25 part of images within it

collage = [(200, 200), (200, 150), (200, 100), (200, 50), (200, 0),
           (150, 200), (150, 150), (150, 100), (150, 50), (150, 0),
           (100, 200), (100, 150), (100, 100), (100, 50), (100, 0),
           (50, 200), (50, 150), (50, 100), (50, 50), (50, 0),
           (0, 200), (0, 150), (0, 100), (0, 50), (0, 0)]

for _ in range(len(collage)):

    a, b = collage.pop()
    rand = randint(0, lenImages-1)
    for j in range(50):
        for i in range(50):
            # Randomly add a part of the image from the input images

            newImage[a+i][b+j] = stack[rand][a+i][b+j]

# Store the newly created image in a stack

newStack = []
newStack.append(newImage)

# Convert the created array to a new image

newImage = Image.fromarray(newImage)

# Save the created image

newImage.save('./images/modified/newImage.png', format='PNG')

newImage = Image.open('./images/modified/newImage.png')

# Display the newly created image

newImage.show()
