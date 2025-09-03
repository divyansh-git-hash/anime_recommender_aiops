from src.vector_store import VectorStore
from src.recommender import AnimeRecommendationSystem
from config.config import GROQ_API_KEY,MODEL_NAME
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chromadb"):
        try:
            logger.info("Initializing Anime Recommendation Pipeline")

            vector_build=VectorStore(csv_file="",persist_dir=persist_dir)
            retriever=vector_build.load_vector_store().as_retriever()
            self.recommender=AnimeRecommendationSystem(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipeline initialized successfully")

        except Exception as e:
            logger.error(f"Pipeline initialization failed: {e}")
            raise CustomException("Pipeline initialization failed") from e

    def recommend(self,user_query:str) -> str:
        try:
            logger.info(f"Receiving an query: {user_query}")
            recommendation=self.recommender.get_recommendations(user_query)
            logger.info(f"Recommendations are: {recommendation}")

        except Exception as e:
            logger.error(f"Recommendation retrieval failed: {e}")
            raise CustomException("Recommendation retrieval failed") from e
        return recommendation














