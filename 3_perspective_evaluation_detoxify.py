import argparse
from detoxify import Detoxify
import pandas as pd

def evaluate_file(file_path):
    # Load lines from the file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Run Detoxify model
    model = Detoxify('original')
    results = model.predict(lines)

    # Combine results with original lines
    df = pd.DataFrame(results)
    df.insert(0, 'text', lines)

    # Save to CSV
    output_file = 'detoxify_results.csv'
    df.to_csv(output_file, index=False)
    print(f"Evaluation complete. Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, required=True, help='Path to the file with text samples')
    args = parser.parse_args()
    evaluate_file(args.file_path)