from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    """Artifact for data ingestion containing paths for the data source, ingestion report, and ingested datasets.
    """
    ingested_train_filepath: Path
    ingested_test_filepath: Path


@dataclass
class DataValidationArtifact:
    """Artifact for data validation containing paths for validation report and validated datasets.
    """
    validation_report_filepath: Path
    validated_train_filepath: Path
    validated_test_filepath: Path


@dataclass
class PreprocessingPipelineArtifact:
    """Artifact for the preprocessing pipeline containing results of data ingestion and validation steps."""
    
    data_ingestion_artifact: DataIngestionArtifact
    data_validation_artifact: DataValidationArtifact
    preprocessing_report_filepath: Path

    def __post_init__(self):
        if not isinstance(self.data_ingestion_artifact, DataIngestionArtifact):
            raise TypeError(
                "data_ingestion_artifact must be of type DataIngestionArtifact"
            )
        if not isinstance(self.data_validation_artifact, DataValidationArtifact):
            raise TypeError(
                "data_validation_artifact must be of type DataValidationArtifact"
            )

@dataclass
class ModelTrainingArtifact:
    """Artifact for model training containing paths for the trained model and training report."""
    trained_model_filepath: Path
    training_report_filepath: Path