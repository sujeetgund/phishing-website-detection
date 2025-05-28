from phishdetector import logger
from phishdetector.entity.config_entity import (
    PreprocessingPipelineConfig,
    DataIngestionConfig,
)
from phishdetector.components.data_ingestion import DataIngestion


def main():
    try:
        # Initialize the preprocessing pipeline configuration
        preprocessing_config = PreprocessingPipelineConfig()

        # Initialize the data ingestion
        data_ingestion_config = DataIngestionConfig(config=preprocessing_config)
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        data_ingestion_artifact = data_ingestion.ingest_data()
        logger.info(f"Data ingestion artifact created: {data_ingestion_artifact}")
    except Exception as e:
        logger.error(f"An error occurred during the data ingestion process: {e}")
        raise e


if __name__ == "__main__":
    main()
