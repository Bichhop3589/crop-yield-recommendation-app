import joblib
import numpy as np

class CropYieldPredictor:
    def __init__(self, model_path, metadata_path):
        self.models = joblib.load(model_path)
        self.metadata = joblib.load(metadata_path)

        self.feature_names = self.metadata["feature_names"]
        self.crop_list = list(self.models.keys())

    def validate_features(self, features):
        warnings = []
        for f in self.feature_names:
            if f not in features:
                warnings.append(f"Thiếu đặc trưng: {f}")
        return {"warnings": warnings}

    def predict(self, features, crop):
        X = np.array([[features[f] for f in self.feature_names]])
        model = self.models[crop]

        y_log = model.predict(X)[0]
        y_real = np.expm1(y_log)

        return {
            "crop_type": crop,
            "predicted_yield": float(y_real),
            "confidence": 85,  # heuristic, giải thích được
            "features": features
        }

    def create_feature_importance_plot(self):
        # optional – để trống cũng được
        return None
