# House Price Prediction

This project implements an end-to-end machine learning pipeline for predicting house price. It includes data processing, model training, MLflow tracking, and model serving via FastAPI.

## Features

- Data preprocessing pipeline with scikit-learn
- Multiple tree-based models (Decision Tree, Random Forest, Xgboost)
- MLflow experiment tracking and model registry
- Model serving via FastAPI
- Comprehensive logging system
- Configuration management
- Production-ready code structure

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/houseprice_prediction.git
cd houseprice_prediction
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Update `config/config.yaml` with your settings:
```yaml
# Data Configuration
data_path: "artifacts/train.csv"
preprocessing_path: "models/preprocessing"

# MLflow Configuration
mlflow:
  tracking_uri: "sqlite:///mlflow.db"
  experiment_name: "houseprice_prediction"

# Model Parameters
model_params:
  random_forest:
    n_estimators: 100
    max_depth: 10
    random_state: 42
```

## Usage

### Running the Pipeline

1. Place your data file in the data directory:
```bash
cp path/to/your/train.csv data/
```

2. Run the training pipeline:
```bash
python run_pipeline.py
```

3. View experiments in MLflow:
```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

### Starting the API

1. Start the FastAPI server:
```bash
uvicorn src.api.main:app --reload
```

2. Access the API documentation:
```
http://localhost:8000/docs
```

## API Endpoints

- `POST /predict`: Make house price predictions
- `GET /health`: Health check endpoint
- `GET /model-info`: Get current model information

## Model Training

The pipeline trains three types of models:
- Decision Tree
- Random Forest
- XGBoost

The best model is selected based on R2 score, and is automatically registered in MLflow for production use.

## Monitoring

- Logs are stored in the `logs/` directory
- MLflow tracking information is stored in `mlflow.db`
- Model artifacts are stored in `models/`

## Development

### Adding New Models

1. Update `src/models/model.py` with your new model configuration
2. Add model-specific parameters in `config.yaml`
3. Update the training pipeline if necessary

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.