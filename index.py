from PIL import Image  # Imaging Library
import shutil  # save img locally
import urllib.request as urllib  # request img from web

# ----------------------------------  Define Some Parameters ----------------------------------
# *** JUST CHANGE THIS SECTION ***
# Minimum & Maximum page numbers
minPageNumber = 1
maxPageNumber = 100
# Write URl that includes the section of incremental decimal
baseURL = "https://image.slidesharecdn.com/tdd-introduction-170610182910/75/an-introduction-to-test-driven-development-%s-2048.jpg?cb=1665590184"
# File name that includes the section of incremental decimal
baseFileName = "file%s.jpg"
# Name of first file
file1Name = "file1.jpg"
# Name of output pdf
file1Name = "total.pdf"
# ----------------------------------  Get Data From URL ----------------------------------
for i in range(minPageNumber, maxPageNumber + 1):
    name = baseURL % str(i)
    resource = urllib.urlopen(name)
    output = open(baseFileName % str(i), "wb")
    output.write(resource.read())
    output.close()
# ----------------------------------  Save Images in root of project ----------------------------------
image_1 = Image.open(file1Name)
im_1 = image_1.convert("RGB")
image_list = []
for i in range(minPageNumber + 1, maxPageNumber + 1):
    image = Image.open(baseFileName % str(i))
    image_RGB = image.convert("RGB")
    image_list.append(image_RGB)
im_1.save(file1Name, save_all=True, append_images=image_list)
