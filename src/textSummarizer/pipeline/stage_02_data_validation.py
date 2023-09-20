from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig
from textSummarizer.config.configuration import Configurationmanager
from textSummarizer.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configurationmanager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files_exist()