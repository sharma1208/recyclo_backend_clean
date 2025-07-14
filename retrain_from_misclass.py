import os
import json
import shutil
import subprocess
from datetime import datetime



SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # folder where your script lives
LOG_DIR = os.path.join(SCRIPT_DIR, "logs")  # absolute path to logs folder inside script folder
DATASET_DIR = 'datarecyclo/trashnet/data/dataset-resized'
# Define absolute path for train_classifier.py
TRAIN_SCRIPT = os.path.join(SCRIPT_DIR, "train_classifier.py")

def collect_misclassified_samples():
    samples = []
    for fname in os.listdir(LOG_DIR):
        if fname.startswith('misclassification_') and fname.endswith('.json'):
            fpath = os.path.join(LOG_DIR, fname)
            with open(fpath, 'r') as f:
                data = json.load(f)
                original = data.get('original', {})
                corrected_label = data.get('corrected_material')

                image_path = original.get('image_path')
                if image_path and corrected_label:
                    samples.append({
                        'image_path': image_path,
                        'label': corrected_label.lower()
                    })
    return samples

def copy_images(samples):
    copied_count = 0
    for sample in samples:
        label_dir = os.path.join(DATASET_DIR, sample['label'])
        if not os.path.exists(label_dir):
            print(f"Label folder does not exist, creating: {label_dir}")
            os.makedirs(label_dir)
        src = sample['image_path']
        dst = os.path.join(label_dir, os.path.basename(src))

        if not os.path.exists(src):
            print(f"Image file not found: {src}")
            continue

        if os.path.exists(dst):
            print(f"Image already exists in dataset: {dst}")
            continue

        shutil.copy2(src, dst)
        copied_count += 1
        print(f"Copied {src} -> {dst}")
    print(f"Total new images copied: {copied_count}")

def run_training():
    print(f"Starting training at {datetime.now().isoformat()}")
    result = subprocess.run(['python', TRAIN_SCRIPT], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Training error:\n{result.stderr}")
    else:
        print("Training completed successfully!")

if __name__ == '__main__':
    samples = collect_misclassified_samples()
    print(f"Found {len(samples)} misclassified samples.")
    copy_images(samples)
    run_training()
