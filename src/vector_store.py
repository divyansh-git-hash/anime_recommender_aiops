from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

from src.utils import get_logger

logger=get_logger(__name__)

load_dotenv()
_model_name="sentence-transformers/all-MiniLM-L6-v2"

class VectorStore:
    def __init__(self,csv_file:str, persist_dir:str="chroma_db"):
        self.csv_file = csv_file
        self.persist_dir = persist_dir
        self.embeddings = HuggingFaceEmbeddings(model_name=_model_name)


    def builder_vector_store(self):
        loader=CSVLoader(self.csv_file,encoding="utf-8",metadata_columns=[])
        data=loader.load()

        logger.info(f"Data Loaded and processed ***********")

        splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        logger.info(f"final-1")
        texts=splitter.split_documents(data)

        logger.info(f"final-2")

        db=Chroma.from_documents(texts,self.embeddings,persist_directory=self.persist_dir)
        logger.info(f"final-3")
        db.persist()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embeddings)