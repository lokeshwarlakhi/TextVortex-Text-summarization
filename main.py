from TextVortex.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from TextVortex.pipe import DataIngestionTrainingPipeline
from TextVortex.logging import logger
from TextVortex.pipeline.stage_02_data_validation import DatavalidationtTrainingPipeline
from TextVortex.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextVortex.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextVortex.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
import torch


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
    
# Set the maximum GPU memory to 4 GB
# gpu_memory_limit = 4096  # In MB
# torch.cuda.memory_allocated()  # Current GPU memory usage
# torch.cuda.memory_cached()  # Current GPU memory cache

# with torch.cuda.device(0):  # Replace 0 with the GPU device number if you have multiple GPUs
#     torch.cuda.empty_cache()  # Clear GPU cache to free up some memory
#     torch.cuda.reset_max_memory_allocated()

#     # Your code that uses GPU

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e


#     # Check if memory limit exceeded
# allocated_memory = torch.cuda.max_memory_allocated() / (1024 * 1024)  # In MB
# if allocated_memory > gpu_memory_limit:
#     print("Memory limit exceeded. Reduce batch size or model size.")

# torch.cuda.empty_cache() 

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_training = ModelEvaluationPipeline()
    model_training.main()
    logger.info(f">>>>>>>>>> stage{STAGE_NAME} completed <<<<<<<\n\n x==============x")

except Exception as e:
    logger.exception(e)
    raise e