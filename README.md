# convert_images_to_PDF

This simple program reads images from a folder and converts all of those images to a single PDF file

## Features

- Supports multiple image formats: JPG, JPEG, PNG, BMP, GIF, TIFF, and WebP
- Automatically sorts images by filename
- Converts all images to RGB mode (required for PDF)
- Creates a single multi-page PDF with all images
- Provides progress feedback during conversion

## How to Use

1. Install requirements

   ```sh
   # Create a new virtual environment
   python3 -m venv venv

   # Activate environment
   source venv/bin/activate

   # Install requirements
   pip install -r requirements.txt
   ```

2. Run the script

   ```sh
   python main.py
   ```

3. Enter the folder path containing your images
4. Enter the desired PDF output name (or press Enter for "`output.pdf`")

- The program handles errors gracefully and will skip any corrupted or unsupported files while still processing the valid images.
