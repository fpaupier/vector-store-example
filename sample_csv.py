import os
import csv
import random


def sample_csv(input_csv, output_csv, sample_percentage=0.05):
    """Samples a percentage of lines from an input CSV and writes them to a new CSV.

    Args:
        input_csv: Path to the input CSV file.
        output_csv: Path to the output CSV file.
        sample_percentage: The percentage of lines to sample (e.g., 0.10 for 10%).
    """

    try:
        with open(input_csv, 'r', encoding='utf-8', errors='replace') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Read and store the header row
            lines = list(reader)  # Read all remaining lines into memory (for shuffling)

        random.shuffle(lines)  # Shuffle the lines randomly

        sample_size = int(len(lines) * sample_percentage)
        sampled_lines = lines[:sample_size]

        with open(output_csv, 'w', encoding='utf-8', newline='') as outfile:  # newline='' to prevent extra blank lines
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write the header row
            writer.writerows(sampled_lines)  # Write the sampled lines

        print(f"Sampled {sample_size} lines ({int(sample_percentage*100)}%) and wrote them to {output_csv}")

    except FileNotFoundError:
        print(f"Error: Input CSV file not found at {input_csv}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    input_csv_path = "data/book_data.csv"
    output_csv_path = "data/mini_books.csv"
    sample_csv(input_csv_path, output_csv_path)
