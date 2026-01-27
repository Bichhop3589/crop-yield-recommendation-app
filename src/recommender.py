import pandas as pd

class CropRecommender:
    def __init__(self, predictor):
        self.predictor = predictor

    def recommend_top_k(self, features, k=3):
        results = []

        for crop in self.predictor.crop_list:
            pred = self.predictor.predict(features, crop)
            results.append({
                "crop_type": crop,
                "predicted_yield": pred["predicted_yield"]
            })

        df = pd.DataFrame(results)
        df = df.sort_values("predicted_yield", ascending=False)

        return df.head(k)
