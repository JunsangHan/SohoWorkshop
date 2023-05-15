from PIL import Image


def merge_images(image_paths, output_path):
    images = [Image.open(x) for x in image_paths]

    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    max_height = max(heights)

    new_img = Image.new('RGB', (max_width * 2, max_height * 2))

    for i in range(2):
        for j in range(2):
            new_img.paste(images[i * 2 + j], (i * max_width, j * max_height))

    new_img.save(output_path)


image_paths = ["image1.jpeg", "image2.jpeg", "image3.jpeg", "image4.jpeg"]
output_path = "merged.jpg"

merge_images(image_paths, output_path)
