import time
import random
from config import Config

class AIAssistant:
    def __init__(self):
        self.api_key = Config.GOOGLE_API_KEY
        self.model = None
        self.gemini_model = "models/gemini-pro-latest"

        self.system_prompt = """
Bạn là chuyên gia nông nghiệp tại Đông Nam Á.
Trả lời bằng tiếng Việt, thực tế, dễ hiểu.
Đưa ra khuyến nghị có thể hành động.
Giữ dưới 300 từ.
"""

        self._init_gemini()

    def _init_gemini(self):
        if not self.api_key:
            return
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.gemini_model)
        except:
            self.model = None

    def get_advice(self, prediction_result, question=None):
        if self.model:
            try:
                prompt = self._build_prompt(prediction_result, question)
                return self.model.generate_content(prompt).text
            except:
                pass
        return self._fallback(prediction_result)

    def _build_prompt(self, result, question):
        return f"""
{self.system_prompt}

Cây trồng: {result.get('crop_type')}
Năng suất: {result.get('predicted_yield'):.1f} kg/ha
Điều kiện khí hậu: {result.get('features')}

Câu hỏi: {question or "Phân tích và khuyến nghị canh tác"}
"""

    def _fallback(self, result):
        return f"""
🌱 **Phân tích nhanh**
- Cây trồng: {result.get('crop_type')}
- Năng suất dự đoán: {result.get('predicted_yield'):.1f} kg/ha

Khuyến nghị:
1. Theo dõi độ ẩm đất
2. Bón phân cân đối
3. Kiểm soát sâu bệnh định kỳ
"""
