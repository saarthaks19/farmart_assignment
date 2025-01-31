import sys
import os

def extract_logs(log_file, target_date, output_dir="output"):
    """Extracts log entries for a specific date from a large log file efficiently."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(target_date):
                    outfile.write(line)

        print(f"Logs for {target_date} extracted to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    log_file = "test_logs.log"  # Path to the large log file
    target_date = sys.argv[1]
    
    extract_logs(log_file, target_date)