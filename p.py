from PIL import Image
import os

def resize_and_compress_images(input_folder, output_folder, max_width=600, max_height=400, quality=50):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):  # Process image files only
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                with Image.open(input_path) as img:
                    # Get original dimensions
                    original_width, original_height = img.size

                    # Calculate the aspect ratio
                    aspect_ratio = original_width / original_height

                    # Determine new dimensions while keeping aspect ratio
                    if original_width > original_height:
                        # Landscape images
                        new_width = min(max_width, original_width)
                        new_height = int(new_width / aspect_ratio)
                    else:
                        # Portrait images
                        new_height = min(max_height, original_height)
                        new_width = int(new_height * aspect_ratio)

                    # Resize while preserving aspect ratio
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    # Convert to RGB (to handle non-RGB formats)
                    img = img.convert("RGB")
                    # Save with reduced quality
                    img.save(output_path, optimize=True, quality=quality)
                    print(f"Processed: {filename} -> {output_path} ({new_width}x{new_height})")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Input and output folder paths

input_folder = r"./images"  # Replace with the relative path to your original images
output_folder = r"./im2" 
# Run the function
# Run the function
resize_and_compress_images(input_folder, output_folder, max_width=600, max_height=400, quality=100)


# Run the function


# Run the function
