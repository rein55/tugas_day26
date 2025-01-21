from src.data.data_loader import DataLoader
from src.data.data_processor import DataProcessor
from src.utils.logger import default_logger as logger

if __name__ == "__main__":
    try:
        logger.info("Inistializing DataLoader")
        data_loader = DataLoader()
        data_processor = DataProcessor()

        logger.info("Loading data")
        df = data_loader.load_data()
        logger.info("Data loaded successfully")

        logger.info("Inistializing DataProcessor")
        X, y = data_processor.fit_transform(df)
    except Exception as e:
        logger.info("Data loading failed")