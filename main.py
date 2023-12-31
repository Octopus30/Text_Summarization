from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = 'data_ingestion_stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=============x")


except Exception as e:
    logger.exception(e)
    raise e

print('-' * 150) 
STAGE_NAME  = 'data_validation_stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x=============x")
except Exception as e:
    raise e