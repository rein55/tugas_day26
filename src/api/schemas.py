from pydantic import BaseModel, Field
from typing import Dict, Optional, List

class ModelMetrics(BaseModel):
    """Model metrics schema"""
    rmse : float = Field(..., description="Model RMSE")
    mae: float = Field(..., description="Model MAE")
    r2_score : float = Field(..., description="Model R2 Score")

class ModelInfo(BaseModel):
    """Model information schema"""
    run_id: str = Field(..., description="MLflow run ID")
    metrics: ModelMetrics = Field(..., description="Model metrics")

from pydantic import BaseModel, Field

class HousePricePredictionRequest(BaseModel):
    """Houseprice prediction request schema"""
    Id: int = Field(..., description="Unique identifier for the house")
    MSSubClass: int = Field(..., description="The building class")
    MSZoning: str = Field(..., description="The general zoning classification")
    LotFrontage: float = Field(..., description="Linear feet of street connected to property")
    LotArea: int = Field(..., description="Lot size in square feet")
    Street: str = Field(..., description="Type of road access")
    Alley: str = Field(..., description="Type of alley access")
    LotShape: str = Field(..., description="General shape of property")
    LandContour: str = Field(..., description="Flatness of the property")
    Utilities: str = Field(..., description="Type of utilities available")
    LotConfig: str = Field(..., description="Lot configuration")
    LandSlope: str = Field(..., description="Slope of property")
    Neighborhood: str = Field(..., description="Physical locations within Ames")
    Condition1: str = Field(..., description="Proximity to various conditions")
    Condition2: str = Field(..., description="Proximity to various conditions (if multiple)")
    BldgType: str = Field(..., description="Type of dwelling")
    HouseStyle: str = Field(..., description="Style of dwelling")
    OverallQual: int = Field(..., description="Overall material and finish quality")
    OverallCond: int = Field(..., description="Overall condition rating")
    YearBuilt: int = Field(..., description="Original construction date")
    YearRemodAdd: int = Field(..., description="Remodel date")
    RoofStyle: str = Field(..., description="Type of roof")
    RoofMatl: str = Field(..., description="Roof material")
    Exterior1st: str = Field(..., description="Exterior covering on house")
    Exterior2nd: str = Field(..., description="Exterior covering on house (if multiple)")
    MasVnrType: str = Field(..., description="Masonry veneer type")
    MasVnrArea: float = Field(..., description="Masonry veneer area in square feet")
    ExterQual: str = Field(..., description="Exterior material quality")
    ExterCond: str = Field(..., description="Present condition of material on exterior")
    Foundation: str = Field(..., description="Type of foundation")
    BsmtQual: str = Field(..., description="Height of the basement")
    BsmtCond: str = Field(..., description="General condition of the basement")
    BsmtExposure: str = Field(..., description="Walkout or garden level basement walls")
    BsmtFinType1: str = Field(..., description="Quality of basement finished area")
    BsmtFinSF1: float = Field(..., description="Type 1 finished square feet")
    BsmtFinType2: str = Field(..., description="Quality of basement finished area (if multiple)")
    BsmtFinSF2: float = Field(..., description="Type 2 finished square feet")
    BsmtUnfSF: float = Field(..., description="Unfinished square feet of basement area")
    TotalBsmtSF: float = Field(..., description="Total square feet of basement area")
    Heating: str = Field(..., description="Type of heating")
    HeatingQC: str = Field(..., description="Heating quality and condition")
    CentralAir: str = Field(..., description="Central air conditioning")
    Electrical: str = Field(..., description="Electrical system")
    FirstFlrSF: int = Field(..., description="First floor square feet")
    SecondFlrSF: int = Field(..., description="Second floor square feet")
    LowQualFinSF: int = Field(..., description="Low quality finished square feet")
    GrLivArea: int = Field(..., description="Above grade living area square feet")
    BsmtFullBath: int = Field(..., description="Basement full bathrooms")
    BsmtHalfBath: int = Field(..., description="Basement half bathrooms")
    FullBath: int = Field(..., description="Full bathrooms above grade")
    HalfBath: int = Field(..., description="Half baths above grade")
    BedroomAbvGr: int = Field(..., description="Bedrooms above grade")
    KitchenAbvGr: int = Field(..., description="Kitchens above grade")
    KitchenQual: str = Field(..., description="Kitchen quality")
    TotRmsAbvGrd: int = Field(..., description="Total rooms above grade")
    Functional: str = Field(..., description="Home functionality rating")
    Fireplaces: int = Field(..., description="Number of fireplaces")
    FireplaceQu: str = Field(..., description="Fireplace quality")
    GarageType: str = Field(..., description="Garage location")
    GarageYrBlt: int = Field(..., description="Garage year built")
    GarageFinish: str = Field(..., description="Interior finish of the garage")
    GarageCars: int = Field(..., description="Size of garage in car capacity")
    GarageArea: int = Field(..., description="Size of garage in square feet")
    GarageQual: str = Field(..., description="Garage quality")
    GarageCond: str = Field(..., description="Garage condition")
    PavedDrive: str = Field(..., description="Paved driveway")
    WoodDeckSF: int = Field(..., description="Wood deck area in square feet")
    OpenPorchSF: int = Field(..., description="Open porch area in square feet")
    EnclosedPorch: int = Field(..., description="Enclosed porch area in square feet")
    ThreeSsnPorch: int = Field(..., description="Three season porch area in square feet")
    ScreenPorch: int = Field(..., description="Screen porch area in square feet")
    PoolArea: int = Field(..., description="Pool area in square feet")
    PoolQC: str = Field(..., description="Pool quality")
    Fence: str = Field(..., description="Fence quality")
    MiscFeature: str = Field(..., description="Miscellaneous feature not covered in other categories")
    MiscVal: int = Field(..., description="Value of miscellaneous feature")
    MoSold: int = Field(..., description="Month Sold")
    YrSold: int = Field(..., description="Year Sold")
    SaleType: str = Field(..., description="Type of sale")
    SaleCondition: str = Field(..., description="Condition of sale")
    SalePrice: int = Field(..., description="Price of sale")

    class Config:
        schema_extra = {
            "example": {
                "Id": 1,
                "MSSubClass": 20,
                "MSZoning": "RL",
                "LotFrontage": 65.0,
                "LotArea": 8450,
                "Street": "Pave",
                "Alley": "NA",
                "LotShape": "Reg",
                "LandContour": "Lvl",
                "Utilities": "AllPub",
                "LotConfig": "Inside",
                "LandSlope": "Gtl",
                "Neighborhood": "CollgCr",
                "Condition1": "Norm",
                "Condition2": "Norm",
                "BldgType": "1Fam",
                "HouseStyle": "2Story",
                "OverallQual": 7,
                "OverallCond": 5,
                "YearBuilt": 2003,
                "YearRemodAdd": 2003,
                "RoofStyle": "Gable",
                "RoofMatl": "CompShg",
                "Exterior1st": "VinylSd",
                "Exterior2nd": "VinylSd",
                "MasVnrType": "BrkFace",
                "MasVnrArea": 196.0,
                "ExterQual": "Gd",
                "ExterCond": "TA",
                "Foundation": "PConc",
                "BsmtQual": "Gd",
                "BsmtCond": "TA",
                "BsmtExposure": "No",
                "BsmtFinType1": "GLQ",
                "BsmtFinSF1": 706.0,
                "BsmtFinType2": "Unf",
                "BsmtFinSF2": 0.0,
                "BsmtUnfSF": 150.0,
                "TotalBsmtSF": 856.0,
                "Heating": "GasA",
                "HeatingQC": "Ex",
                "CentralAir": "Y",
                "Electrical": "SBrkr",
                "FirstFlrSF": 856,
                "SecondFlrSF": 854,
                "LowQualFinSF": 0,
                "GrLivArea": 1710,
                "BsmtFullBath": 1,
                "BsmtHalfBath": 0,
                "FullBath": 2,
                "HalfBath": 1,
                "BedroomAbvGr": 3,
                "KitchenAbvGr": 1,
                "KitchenQual": "Gd",
                "TotRmsAbvGrd": 8,
                "Functional": "Typ",
                "Fireplaces": 0,
                "FireplaceQu": "NA",
                "GarageType": "Attchd",
                "GarageYrBlt": 2003,
                "GarageFinish": "RFn",
                "GarageCars": 2,
                "GarageArea": 548,
                "GarageQual": "TA",
                "GarageCond": "TA",
                "PavedDrive": "Y",
                "WoodDeckSF": 0,
                "OpenPorchSF": 61,
                "EnclosedPorch": 0,
                "ThreeSsnPorch": 0,
                "ScreenPorch": 0,
                "PoolArea": 0,
                "PoolQC": "NA",
                "Fence": "NA",
                "MiscFeature": "NA",
                "MiscVal": 0,
                "MoSold": 2,
                "YrSold": 2008,
                "SaleType": "WD",
                "SaleCondition": "Normal",
                "SalePrice": 208500
            }
        }


class HousePricePredictionResponse(BaseModel):
    """Houseprice prediction response schema"""
    Id: str = Field(..., description="Customer ID")
    houseprice_prediction: float = Field(..., description="House Price Prediction result")
    # model_info: ModelInfo = Field(..., description="Model information and metrics")