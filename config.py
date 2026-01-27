import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # APP
    APP_TITLE = "🌾 Hệ thống Đề xuất cây trồng thông minh tích hợp AI Tư vấn"
    APP_DESCRIPTION = "Ứng dụng dự đoán năng suất cây trồng và đề xuất cây trồng thông minh dựa trên điều kiện khí hậu cụ thể"
    APP_VERSION = "1.0.0"

    # PATH
    MODEL_PATH = "models/yield_models_by_crop.joblib"
    METADATA_PATH = "models/model_metadata.joblib"

    # GOOGLE GENAI
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # FEATURE CONFIG
    FEATURE_RANGES = {
        "avg_temp": {"min": 10, "max": 40, "default": 26, "step": 0.5, "unit": "°C"},
        "total_rain": {"min": 0, "max": 300, "default": 80, "step": 5, "unit": "mm"},
        "avg_humidity": {"min": 30, "max": 100, "default": 75, "step": 1, "unit": "%"},
        "avg_pressure": {"min": 95, "max": 105, "default": 98, "step": 0.1, "unit": "hPa"},
    }
