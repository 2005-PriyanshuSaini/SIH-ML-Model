import os
from PIL import Image

def clean_dataset(dataset_path):
    """
    Check all images in dataset and remove corrupted ones.
    """
    removed_files = []
    for root, _, files in os.walk(dataset_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with Image.open(file_path) as img:
                    img.verify()  # Verify if valid image
            except Exception as e:
                removed_files.append(file_path)
                os.remove(file_path)
                print(f"❌ Removed corrupted image: {file_path}")
    print(f"✅ Cleaning complete. Removed {len(removed_files)} bad files.")

if __name__ == "__main__":
    dataset_dir = "dataset"  # change if needed
    clean_dataset(dataset_dir)
