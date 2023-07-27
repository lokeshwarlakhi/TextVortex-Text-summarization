from TextVortex.config.configuration import ConfigurationManager
from TextVortex.components.data_validation import  DataValidation
from TextVortex.logging import logger


class DatavalidationtTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validaton_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validaton_config)
        data_validation.validate_all_files_exist()