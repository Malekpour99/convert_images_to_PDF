import os
from pathlib import Path

from PIL import Image


def images_to_pdf(folder_path, output_pdf="output.pdf"):
    """
    Convert all images in a folder to a single PDF file.

    Args:
        folder_path: Path to the folder containing images
        output_pdf: Name of the output PDF file (default: "output.pdf")
    """
    # Supported image formats
    supported_formats = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

    # Get all image files from the folder
    image_files = []
    for file in sorted(os.listdir(folder_path)):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = Path(file).suffix.lower()
            if ext in supported_formats:
                image_files.append(file_path)

    if not image_files:
        print(f"No images found in {folder_path}")
        return

    print(f"Found {len(image_files)} images")

    # Open and convert images
    images = []
    for img_path in image_files:
        try:
            img = Image.open(img_path)
            # Convert to RGB if necessary (PDF requires RGB mode)
            if img.mode != "RGB":
                img = img.convert("RGB")
            images.append(img)
            print(f"Added: {os.path.basename(img_path)}")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

    if not images:
        print("No valid images to convert")
        return

    # Save as PDF
    try:
        # First image is the base, rest are appended
        images[0].save(
            output_pdf,
            save_all=True,
            append_images=images[1:],
            resolution=100.0,
            quality=95,
            optimize=True,
        )
        print(f"\nSuccessfully created {output_pdf}")
        print(f"Total pages: {len(images)}")
    except Exception as e:
        print(f"Error creating PDF: {e}")


if __name__ == "__main__":
    # Example usage
    folder_path = input("Enter the folder path containing images: ").strip()
    output_name = input(
        "Enter output PDF name (press Enter for 'output.pdf'): "
    ).strip()

    if not output_name:
        output_name = "output.pdf"
    elif not output_name.endswith(".pdf"):
        output_name += ".pdf"

    if os.path.exists(folder_path):
        images_to_pdf(folder_path, output_name)
    else:
        print(f"Error: Folder '{folder_path}' does not exist")
