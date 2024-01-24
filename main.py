from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_data_preprocessing import DataPreprocessingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>> The {STAGE_NAME} has started >>>>>>>>>")
    ing = DataIngestionPipeline()
    ing.main()
    logger.info(f">>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Preprocessing"
try:
    logger.info(f">>>>>>>>>> The {STAGE_NAME} has started >>>>>>. ")
    preprocess = DataPreprocessingPipeline()
    preprocess.main()
    logger.info(f">>>>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e