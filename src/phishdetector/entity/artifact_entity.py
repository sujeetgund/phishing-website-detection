from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    ingested_train_filepath: Path
    ingested_test_filepath: Path


@dataclass
class DataValidationArtifact:
    validation_report_filepath: Path
    validated_train_filepath: Path
    validated_test_filepath: Path
