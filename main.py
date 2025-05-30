from phishdetector.pipelines.preprocessing import PreprocessingPipeline
from phishdetector.entity.config_entity import PreprocessingPipelineConfig
from phishdetector.entity.artifact_entity import PreprocessingPipelineArtifact


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
    pipeline = PreprocessingPipeline(config=config)
    return pipeline.run()


def main():
    run_preprocessing(config=PreprocessingPipelineConfig())



if __name__ == "__main__":
    main()
