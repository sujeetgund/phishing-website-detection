from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionArtifact:
    train_filepath: Path
    test_filepath: Path