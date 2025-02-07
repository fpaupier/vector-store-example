import numpy as np  # Often used with binary files containing numerical data
import struct  # For unpacking binary data if needed


def investigate_bin_file(bin_file_path: str, data_type=None, count=None):
    """Opens and investigates the content of a binary file.

    Args:
        bin_file_path: Path to the binary file.
        data_type: The data type of the elements in the file (e.g., 'float32', 'int16', etc.). If None, tries to read as bytes.
        count: The number of elements to read. If None, reads the entire file (if possible).
    """

    try:
        with open(bin_file_path, 'rb') as f:
            if data_type:  # If a specific data type is provided
                try:  # Try to read with numpy
                    data = np.fromfile(f, dtype=data_type, count=count)
                    print(f"Read {len(data)} elements of type {data_type} using numpy:")
                    print(data)  # Print the data
                except Exception as e:  # Handle any exceptions
                    print(f"Error reading with numpy: {e}")
                    print("Trying to read with struct...")
                    f.seek(0)  # Reset file pointer
                    try:  # Try to read with struct
                        if count:
                            data = struct.unpack(f"{count}{data_type}", f.read(struct.calcsize(data_type) * count))
                        else:
                            data = struct.unpack(f"{data_type}", f.read())  # Read all
                        print(f"Read {len(data)} elements of type {data_type} using struct:")
                        print(data)
                    except Exception as e:
                        print(f"Error reading with struct: {e}")
                        print("Could not read binary file with provided data type")
            else:  # If no data type is provided, read as bytes
                data = f.read()
                print(f"Read {len(data)} bytes:")
                # Print a limited number of bytes for large files (e.g., the first 100)
                if len(data) > 100:
                    print(data[:100])  # Print the first 100 bytes
                    print("...")  # Indicate that there are more bytes
                else:
                    print(data)

    except FileNotFoundError:
        print(f"Error: Binary file not found at {bin_file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    # Example Usage 1 (Reading as bytes):
    bin_file_path = "./books_db/2f0e7074-3fc8-49b0-b1ef-2b9a9d9d65dd/length.bin"  # Replace with the actual path
    investigate_bin_file(bin_file_path)

    # Example Usage 2 (Reading as specific data type, e.g., float32):
    investigate_bin_file(bin_file_path, data_type='float32', count=100)  # Read 100 float32 values

    # Example Usage 3 (Reading as specific data type, e.g., int16):
    investigate_bin_file(bin_file_path, data_type='int16')  # Read all int16 values
