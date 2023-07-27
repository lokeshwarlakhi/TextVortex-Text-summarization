from TextVortex.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextVortex.logging import logger
from TextVortex.pipeline.stage_02_data_validation import DatavalidationtTrainingPipeline

STAGE_NAME = "data ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "data Validation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_validation = DataIngestionTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e