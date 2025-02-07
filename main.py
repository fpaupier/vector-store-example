import os
import csv
import chromadb
from sentence_transformers import SentenceTransformer

# Configuration (adjust as needed)
DATA_DIR = "data"  # Subdirectory containing your CSV
CSV_FILE = "book_data.csv"
CSV_PATH = os.path.join(DATA_DIR, CSV_FILE)
DB_PATH = "books_db"
COLLECTION_NAME = "books"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
BATCH_SIZE = 100


def create_chroma_db(csv_file, db_path, collection_name, embedding_model_name, batch_size):
    """Creates a ChromaDB database from a CSV file in a subdirectory."""
    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"CSV file not found: {csv_file}")

    if not os.path.exists(db_path):
        os.makedirs(db_path)

    client = chromadb.PersistentClient(path=db_path)
    if collection_name not in client.list_collections():
        collection = client.create_collection(name=collection_name)
    else:
        collection = client.get_collection(name=collection_name)
        print(f"Collection {collection_name} loaded from disk.")

    model = SentenceTransformer(embedding_model_name)

    with open(csv_file, 'r', encoding='utf-8', errors='replace') as csvfile:  # Handle encoding
        reader = csv.DictReader(csvfile)  # Read as dictionaries

        embeddings = []
        metadatas = []
        ids = []

        for row in reader:
            try:
                description = row["book_desc"]
                if description:
                    embedding = model.encode(description)
                    embeddings.append(embedding)
                    metadata = row  # Entire row as metadata
                    metadatas.append(metadata)
                    ids.append(str(row['book_id']))
                else:
                    print(f"Warning: Missing description for book ID: {row['book_id']}")

                if len(embeddings) == batch_size:  # Add in batches
                    try:
                        collection.add(embeddings=embeddings, metadatas=metadatas, ids=ids)
                        print(f"Added a batch of {batch_size} books")
                        embeddings = []  # Clear the batch
                        metadatas = []
                        ids = []

                    except Exception as e:
                        print(f"Error adding batch: {e}")

            except Exception as e:
                print(f"Error processing book ID: {row['book_id']}: {e}")

        # Add any remaining books after processing the loop
        if embeddings:  # Check if there are any remaining embeddings
            try:
                collection.add(embeddings=embeddings, metadatas=metadatas, ids=ids)
                print(f"Added the last batch of {len(embeddings)} books")
            except Exception as e:
                print(f"Error adding last batch: {e}")

    print("ChromaDB database created/updated successfully.")


# Run the database creation
if __name__ == '__main__':
    create_chroma_db(CSV_PATH, DB_PATH, COLLECTION_NAME, EMBEDDING_MODEL, BATCH_SIZE)
