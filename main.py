from TextVortex.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextVortex.logging import logger
from TextVortex.pipeline.stage_02_data_validation import DatavalidationtTrainingPipeline
from TextVortex.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "data ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataIngestionTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e