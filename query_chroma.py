import chromadb
from sentence_transformers import SentenceTransformer

# Configuration (adjust as needed)
DB_PATH = "books_db"
COLLECTION_NAME = "books"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


def query_chroma_db(db_path: str, collection_name: str, query_text: str,
                    book_format: str = "Paperback"):  # Added book_format parameter
    """Queries the ChromaDB database with text and metadata filtering."""

    client = chromadb.PersistentClient(path=db_path)
    if collection_name not in client.list_collections():
        raise ValueError(f"Collection '{collection_name}' not found in database '{db_path}'.")

    collection = client.get_collection(name=collection_name)
    model = SentenceTransformer(EMBEDDING_MODEL)
    query_embedding = model.encode(query_text)

    # Construct the where clause for metadata filtering
    where_clause = {"book_format": book_format}  # Filter for Paperback

    results = collection.query(
        query_embeddings=[query_embedding],
        where=where_clause,  # Apply metadata filter
        n_results=10  # Number of results to return (adjust as needed)
    )

    # Process and print the results
    if results and results['documents'] and results['metadatas']:
        print(f"Query: {query_text}")
        for i, (document, metadata, distance) in enumerate(
                zip(results['documents'][0], results['metadatas'][0], results['distances'][0])):
            print(f"\nResult {i + 1}:")
            print(f"  Title: {metadata.get('book_title', 'N/A')}")  # Access metadata fields safely
            print(f"  Description: {document}")
            print(f"  Format: {metadata.get('book_format', 'N/A')}")  # added book format
            print(f"  Distance: {distance}")
    else:
        print("No results found.")


if __name__ == '__main__':
    query_text = input("Enter your query: ")  # Get query from user
    # query_chroma_db(DB_PATH, COLLECTION_NAME, query_text)  # , book_format="Paperback"
    query_chroma_db(DB_PATH, COLLECTION_NAME, query_text, book_format="Hardcover") # Example with Hardcover filter
    # query_chroma_db(DB_PATH, COLLECTION_NAME, query_text, book_format="Ebook") # Example with Ebook filter
