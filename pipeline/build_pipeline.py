from pydantic_core.core_schema import CustomErrorSchema

from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStore
from dotenv import load_dotenv
from src.utils import get_logger, custom_exception, CustomException

load_dotenv()
logger = get_logger(__name__)


def main():
    try:
        logger.info(f"********* Starts building pipeline ***********")

        loader=AnimeDataLoader("data/anime_with_synopsis.csv","data/processed_anime_with_synopsis.csv")
        processed_csv=loader.load_processed_data()

        logger.info(f"********* Data Loaded and processed ***********")

        vector_builder=VectorStore(processed_csv)
        vector_builder.builder_vector_store()

        logger.info(f"******** Vector Building Completed ***********")
        logger.info(f"******** Pipeline Completed ***********")
        print('yes')
    except Exception as e:
        logger.error(f" Failed to execute building pipeline {str(e)}")
        print('no')
        raise CustomException("Error building pipeline",e)


if __name__ == '__main__':
    main()








