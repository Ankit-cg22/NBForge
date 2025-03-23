import uuid
import chromadb

class ChromaDBClient:
    def __init__(self, collection_name):
        self.client = chromadb.PersistentClient('vectorstore')
        self.collection = self.client.get_or_create_collection(name=collection_name)

    def add_documents(self, df):
        if not self.collection.count():
            for _, row in df.iterrows():
                self.collection.add(documents=row["Techstack"],
                                   metadatas={"links": row["Links"]},
                                   ids=[str(uuid.uuid4())])

    def query(self, query_texts, n_results):
        return self.collection.query(query_texts=query_texts, n_results=n_results)