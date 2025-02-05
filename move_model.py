import shutil
import os

# Define the source and destination paths
source_dir = 'artifacts/training/model.h5'  # The source file path
destination_dir = 'models'  # The target folder where the file should go

# Check if the source file exists
if os.path.exists(source_dir):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Full destination path (where the file will be copied)
    destination_path = os.path.join(destination_dir, 'model.h5')

    # Copy the file
    shutil.copy(source_dir, destination_path)

    print(f"File 'model.h5' has been copied to {destination_path}")
else:
    print(f"File '{source_dir}' not found!")
