import pickle


def visualize_pickle_file(pickle_file_path):
    """Opens and visualizes the content of a pickle file."""

    try:
        with open(pickle_file_path, 'rb') as f:  # Open in binary read mode ('rb')
            data = pickle.load(f)

            # Basic Visualization/Inspection:
            if isinstance(data, dict):  # If it's a dictionary
                print("Pickle file contains a dictionary:")
                for key, value in data.items():
                    print(f"{key}: {value}")  # Print key-value pairs
            elif isinstance(data, list) or isinstance(data, tuple) or isinstance(data,
                                                                                 set):  # If it's a list, tuple or a set
                print(f"Pickle file contains a {type(data).__name__}:")
                for item in data:
                    print(item)  # Print each item
            elif hasattr(data, '__dict__'):  # If it's a class instance
                print("Pickle file contains a class instance:")
                print(data.__dict__)  # Print the instance's dictionary
            else:  # If it's another simple type
                print(f"Pickle file contains: {data}")  # Print the data directly

            # More Advanced Visualization (If Applicable):
            # If the pickle file contains specific types of data (e.g., NumPy arrays, Pandas DataFrames),
            # you can add more specialized visualization code here.

    except FileNotFoundError:
        print(f"Error: Pickle file not found at {pickle_file_path}")
    except pickle.UnpicklingError as e:
        print(f"Error: Could not unpickle the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    pickle_file_path = "./books_db/2f0e7074-3fc8-49b0-b1ef-2b9a9d9d65dd/index_metadata.pickle"  # Replace with the actual path
    visualize_pickle_file(pickle_file_path)
