from phishdetector.pipelines.preprocessing import PreprocessingPipeline
from phishdetector.pipelines.training import TrainingPipeline
from phishdetector.entity.config_entity import (
    PreprocessingPipelineConfig,
    TrainingPipelineConfig,
)
from phishdetector.entity.artifact_entity import (
    PreprocessingPipelineArtifact,
    TrainingPipelineArtifact,
)


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


def run_training(config: TrainingPipelineConfig) -> TrainingPipelineArtifact:
    """
    Run the training pipeline with the given configuration.

    Args:
        config (TrainingPipelineConfig): Configuration for the training pipeline.

    Returns:
        TrainingPipelineArtifact: The artifact containing results of the training steps.
    """
    training = TrainingPipeline(config=config)
    return training.run()


def main():
    run_preprocessing(config=PreprocessingPipelineConfig())
    run_training(config=TrainingPipelineConfig())


if __name__ == "__main__":
    main()
