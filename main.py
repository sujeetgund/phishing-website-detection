from phishdetector.pipelines.preprocessing import PreprocessingPipeline
from phishdetector.entity.config_entity import PreprocessingPipelineConfig
from phishdetector.entity.artifact_entity import PreprocessingPipelineArtifact

from phishdetector.entity.config_entity import (
    TrainingPipelineConfig,
    ModelTrainingConfig,
)
from phishdetector.entity.artifact_entity import ModelTrainingArtifact
from phishdetector.components.model_training import ModelTraining


def run_preprocessing(
    config: PreprocessingPipelineConfig,
) -> PreprocessingPipelineArtifact:
    """
    Run the preprocessing pipeline with the given configuration.

    Args:
        config (PreprocessingPipelineConfig): Configuration for the preprocessing pipeline.

    Returns:
        PreprocessingPipelineArtifact: The artifact containing results of the preprocessing steps.
    """
    preprocessing = PreprocessingPipeline(config=config)
    return preprocessing.run()


def run_model_training(config: ModelTrainingConfig) -> ModelTrainingArtifact:
    """
    Run the model training pipeline with the given configuration.

    Args:
        config (ModelTrainingConfig): Configuration for the model training pipeline.
    """
    model_training = ModelTraining(config=config)
    return model_training.train_model()


def main():
    run_preprocessing(config=PreprocessingPipelineConfig())
    training_pipeline_config = TrainingPipelineConfig()
    run_model_training(config=ModelTrainingConfig(config=training_pipeline_config))


if __name__ == "__main__":
    main()
