import gdown
import zipfile

def download_file_from_google_drive(file_id, output_file):
    """
    Download a file from Google Drive.

    :param file_id: The Google Drive file ID.
    :param output_file: The name of the file to save.
    """
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_file, quiet=False)

# Example usage:
bone_fracture_detection_file_id = "1--fAnsBtykHxIvq6oqxDAaOJpaWZ5LbP"
bone_out = "bone_fracture_detection.zip"
download_file_from_google_drive(bone_fracture_detection_file_id, bone_out)

# Open the ZIP file for reading
with zipfile.ZipFile(bone_out, 'r') as zip_ref:
    # Extract all the contents to the specified directory
    zip_ref.extractall()

tumor_detection_file_id = "1-2_xDKaO3K1LUtEL-AdGZzZiQP9ulzdM"
tumor_out = "tumor_detection.zip"
download_file_from_google_drive(tumor_detection_file_id, tumor_out)


with zipfile.ZipFile(tumor_out, 'r') as zip_ref:
    # Extract all the contents to the specified directory
    zip_ref.extractall()