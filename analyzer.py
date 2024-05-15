# analyzer.py

def count_lines_of_code(file_path):
    """Count the number of lines of code in a given file."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return -1  # File not found error code
