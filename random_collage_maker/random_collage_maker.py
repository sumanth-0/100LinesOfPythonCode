from PIL import Image
import os

def create_collage(image_paths, output_path='collage.jpg', collage_type='grid', max_width=1920):
    images = [Image.open(path) for path in image_paths]
    
    if collage_type == 'grid':

        num_images = len(images)
        cols = int(num_images ** 0.5)
        rows = (num_images + cols - 1) // cols
        

        avg_width = sum(img.width for img in images) // num_images
        avg_height = sum(img.height for img in images) // num_images
        

        cell_width = min(avg_width, max_width // cols)
        cell_height = int(cell_width * avg_height / avg_width)

        canvas_width = cell_width * cols
        canvas_height = cell_height * rows
        collage = Image.new('RGB', (canvas_width, canvas_height), 'white')
        

        for idx, img in enumerate(images):

            img_resized = img.resize((cell_width, cell_height), Image.LANCZOS)
            
            row = idx // cols
            col = idx % cols
            x = col * cell_width
            y = row * cell_height
            
            collage.paste(img_resized, (x, y))
    
    elif collage_type == 'horizontal':
        min_height = min(img.height for img in images)
        resized_images = []
        for img in images:
            aspect_ratio = img.width / img.height
            new_width = int(min_height * aspect_ratio)
            resized_images.append(img.resize((new_width, min_height), Image.LANCZOS))
        
        total_width = sum(img.width for img in resized_images)
        collage = Image.new('RGB', (total_width, min_height), 'white')

        x_offset = 0
        for img in resized_images:
            collage.paste(img, (x_offset, 0))
            x_offset += img.width
    
    elif collage_type == 'vertical':

        min_width = min(img.width for img in images)
        resized_images = []
        for img in images:
            aspect_ratio = img.height / img.width
            new_height = int(min_width * aspect_ratio)
            resized_images.append(img.resize((min_width, new_height), Image.LANCZOS))
        
        total_height = sum(img.height for img in resized_images)
        collage = Image.new('RGB', (min_width, total_height), 'white')
        
        y_offset = 0
        for img in resized_images:
            collage.paste(img, (0, y_offset))
            y_offset += img.height
    
    collage.save(output_path, quality=95)
    print(f"Collage saved to {output_path}")
    print(f"Dimensions: {collage.width}x{collage.height}")


if __name__ == "__main__":

    image_files = [
    r'C:\Users\HP\Downloads\image1.jpg',
    r'C:\Users\HP\Downloads\image2.jpg',
    r'C:\Users\HP\Downloads\image3.jpg',
    r'C:\Users\HP\Downloads\image4.jpg',
]


    
    existing_files = [f for f in image_files if os.path.exists(f)]
    
    if existing_files:
        create_collage(existing_files, output_path='my_collage.jpg', collage_type='grid')

    else:
        print("No image files found. Please update the image_files list with your actual image paths.")