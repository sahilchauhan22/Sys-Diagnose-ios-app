import tarfile
import os

def extract_sysdiagnose(file_path, extract_to='extracted_logs'):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with tarfile.open(file_path, 'r:gz') as tar:
        tar.extractall(path=extract_to)

    return extract_to

import zipfile

def extract_zip_sysdiagnose(zip_path, extract_to='extracted_logs_zip'):
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    return extract_to

