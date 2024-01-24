from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>> The {STAGE_NAME} has started >>>>>>>>>")
    ing = DataIngestionPipeline()
    ing.main()
    logger.info(f">>>>>>>>> The {STAGE_NAME} has completed succefully >>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e