from phishdetector import logger
from phishdetector.entity.config_entity import (
    PreprocessingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
)
from phishdetector.components.data_ingestion import DataIngestion
from phishdetector.components.data_validation import DataValidation


def main():
    try:
        # Initialize the preprocessing pipeline configuration
        preprocessing_config = PreprocessingPipelineConfig()

        # Initialize the data ingestion
        data_ingestion_config = DataIngestionConfig(config=preprocessing_config)
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Run the data ingestion process
        data_ingestion_artifact = data_ingestion.ingest_data()
        logger.info(f"Data ingestion artifact created: {data_ingestion_artifact}")

        # Initialize the data validation
        data_validation_config = DataValidationConfig(config=preprocessing_config)
        data_validation = DataValidation(
            config=data_validation_config, ingestion_artifact=data_ingestion_artifact
        )

        # Run the data validation process
        data_validation_artifact = data_validation.validate_data()
        logger.info(f"Data validation artifact created: {data_validation_artifact}")

    except Exception as e:
        logger.error(f"An error occurred during the data ingestion process: {e}")
        raise e


if __name__ == "__main__":
    main()
