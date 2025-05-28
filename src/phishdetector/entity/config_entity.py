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
        self.train_filepath = config.feature_store_dir / "train.csv"
        self.test_filepath = config.feature_store_dir / "test.csv"
