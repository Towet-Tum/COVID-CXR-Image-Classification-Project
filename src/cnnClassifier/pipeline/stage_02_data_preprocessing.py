from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_preprocessing import DataPreprocessing

STAGE_NAME = "Data Preprocessing"

class DataPreprocessingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager()
        data_preprocess_config = config.get_data_preprocessing_config()
        data_preprocess = DataPreprocessing(config=data_preprocess_config)
        data_preprocess.split_data()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> The {STAGE_NAME} has started >>>>>>. ")
        preprocess = DataPreprocessingPipeline()
        preprocess.main()
        logger.info(f">>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e