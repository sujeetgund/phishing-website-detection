from pathlib import Path


class PreprocessingPipelineConfig:
    def __init__(self):
        self.artifacts_dir = Path("artifacts")
        self.models_dir = self.artifacts_dir / "models"
        self.feature_store_dir = self.artifacts_dir / "feature_store"
        self._create_base_dirs()

    def _create_base_dirs(self):
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.feature_store_dir.mkdir(parents=True, exist_ok=True)


class DataIngestionConfig:
    def __init__(self, config: PreprocessingPipelineConfig):
        """
        Initializes the DataIngestionConfig with paths for data ingestion.

        Args:
            config (PreprocessingPipelineConfig): An instance of PreprocessingPipelineConfig that contains base directories for artifacts and feature store.
        """
        self.config = config
        self.data_source = Path("data") / "phishingData.csv"
        self.ingestion_report_filepath = (
            config.artifacts_dir / "data_ingestion_report.json"
        )
        self.ingested_train_filepath = (
            config.feature_store_dir / "ingested" / "train.csv"
        )
        self.ingested_test_filepath = config.feature_store_dir / "ingested" / "test.csv"
        self._create_ingested_dirs()

    def _create_ingested_dirs(self):
        (self.ingested_train_filepath.parent).mkdir(parents=True, exist_ok=True)
        (self.ingested_test_filepath.parent).mkdir(parents=True, exist_ok=True)


class DataValidationConfig:
    def __init__(self, config: PreprocessingPipelineConfig):
        """
        Initializes the DataValidationConfig with paths for data validation.

        Args:
            config (PreprocessingPipelineConfig): An instance of PreprocessingPipelineConfig that contains base directories for artifacts and feature store.
        """
        self.config = config
        self.data_schema_filepath = Path("data") / "schema.yaml"
        self.validation_report_filepath = (
            config.artifacts_dir / "data_validation_report.yaml"
        )
        self.validated_train_filepath = (
            config.feature_store_dir / "validated" / "validated_train.csv"
        )
        self.validated_test_filepath = (
            config.feature_store_dir / "validated" / "validated_test.csv"
        )
        self._create_validated_dirs()

    def _create_validated_dirs(self):
        (self.validated_train_filepath.parent).mkdir(parents=True, exist_ok=True)
        (self.validated_test_filepath.parent).mkdir(parents=True, exist_ok=True)
