# import streamlit as st
# import pandas as pd

# from config import Config
# from src.model_pipeline import CropYieldPredictor
# from src.recommender import CropRecommender
# from src.ai_assistant import AIAssistant

# # ===============================
# # PAGE CONFIG
# # ===============================
# st.set_page_config(
#     page_title=Config.APP_TITLE,
#     layout="wide"
# )

# st.title(Config.APP_TITLE)
# st.caption(Config.APP_DESCRIPTION)

# # ===============================
# # LOAD MODELS (NO CACHE – SAFE)
# # ===============================
# predictor = CropYieldPredictor(
#     model_path=Config.MODEL_PATH,
#     metadata_path=Config.METADATA_PATH
# )

# recommender = CropRecommender(predictor)
# assistant = AIAssistant()

# # ===============================
# # SIDEBAR - INPUT FEATURES
# # ===============================
# st.sidebar.header("🌦️ Điều kiện khí hậu")

# features = {}
# for feature_name, cfg in Config.FEATURE_RANGES.items():
#     features[feature_name] = st.sidebar.slider(
#     label=f"{feature_name} ({cfg['unit']})",
#     min_value=float(cfg["min"]),
#     max_value=float(cfg["max"]),
#     value=float(cfg["default"]),
#     step=float(cfg["step"])
# )


# # ===============================
# # MAIN TABS
# # ===============================
# tab1, tab2 = st.tabs(["🔍 Dự đoán từng cây", "🌱 Đề xuất cây trồng"])

# # ===============================
# # TAB 1: SINGLE CROP PREDICTION
# # ===============================
# with tab1:
#     st.subheader("🔍 Dự đoán năng suất cho từng loại cây")

#     crop = st.selectbox(
#         "Chọn loại cây trồng",
#         predictor.crop_list
#     )

#     if st.button("📈 Dự đoán năng suất"):
#         result = predictor.predict(features, crop)

#         st.metric(
#             label="Năng suất dự đoán (kg/ha)",
#             value=f"{result['predicted_yield']:.2f}"
#         )

#         advice = assistant.get_advice(result)
#         st.info(advice)

# # ===============================
# # TAB 2: RECOMMEND TOP 3 CROPS
# # ===============================
# with tab2:
#     st.subheader("🌱 Đề xuất Top 3 cây trồng phù hợp")

#     if st.button("🚜 Đề xuất cây trồng"):
#         top3 = recommender.recommend_top_k(features, k=3)

#         st.dataframe(
#             top3.reset_index(drop=True),
#             use_container_width=True
#         )

#         st.success("✅ Đề xuất dựa trên mô hình Machine Learning đã huấn luyện")

# # ===============================
# # FOOTER
# # ===============================
# st.markdown("---")
# st.caption("Big Data & Machine Learning Project | Crop Yield Prediction")
import streamlit as st
import pandas as pd

from config import Config
from src.model_pipeline import CropYieldPredictor
from src.recommender import CropRecommender
from src.ai_assistant import AIAssistant

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title=Config.APP_TITLE,
    layout="wide"
)
st.markdown(
    """
    <style>
    /* ===== MAIN COLORS ===== */
    :root {
        --green-main: #2e7d32;
        --green-light: #e8f5e9;
        --white: #ffffff;
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background-color: var(--green-light);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label {
        color: var(--green-main);
        font-weight: 600;
    }

    /* ===== TITLE ===== */
    .main-title {
        text-align: center;
        color: var(--green-main);
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    /* ===== SUBTITLE BOX ===== */
    .subtitle-box {
        border: 2px solid #2e7d32;   /* viền xanh lá đậm */
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        color: #2e7d32;              /* chữ xanh lá đậm */
        font-size: 16px;
        margin-bottom: 25px;
        background-color: transparent;  /* không fill */
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="main-title">
        Hệ thống Đề xuất cây trồng thông minh tích hợp AI Tư vấn
    </div>

    <div class="subtitle-box">
        Ứng dụng dự đoán năng suất cây trồng và đề xuất cây trồng thông minh 
        dựa trên điều kiện khí hậu cụ thể.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>

/* ===== TAB CONTAINER ===== */
div[data-baseweb="tab-list"] {
    background-color: #2e7d32;
    border-radius: 16px;
    padding: 18px 0;
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    margin-bottom: 26px;
    position: relative;
}

/* ===== DẤU NGĂN DỌC ===== */
div[data-baseweb="tab-list"]::after {
    content: "";
    position: absolute;
    top: 20%;
    bottom: 20%;
    left: 50%;
    width: 2px;
    background-color: rgba(255,255,255,0.4);
}

/* ===== TAB CHUNG ===== */
button[data-baseweb="tab"] {
    background: transparent !important;
    border: none;
    color: rgba(255,255,255,0.75) !important;
    font-size: 22px;
    font-weight: 600;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
}

/* ===== TAB ACTIVE ===== */
button[data-baseweb="tab"][aria-selected="true"] {
    color: #ffffff !important;
    font-weight: 800;
}

/* ===== HOVER ===== */
button[data-baseweb="tab"]:hover {
    color: #ffffff !important;
}

/* ===== TẮT GẠCH CHÂN ===== */
div[data-baseweb="tab-highlight"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)

# st.title(Config.APP_TITLE)
# st.caption(Config.APP_DESCRIPTION)

# ===============================
# LOAD CORE OBJECTS (NO CACHE)
# ===============================
predictor = CropYieldPredictor(
    model_path=Config.MODEL_PATH,
    metadata_path=Config.METADATA_PATH
)

recommender = CropRecommender(predictor)
assistant = AIAssistant()

# ===============================
# SIDEBAR - INPUT FEATURES
# ===============================
# st.sidebar.header("🌦️ Điều kiện khí hậu")

# features = {}
# for feature_name, cfg in Config.FEATURE_RANGES.items():
#     features[feature_name] = st.sidebar.slider(
#         label=f"{feature_name} ({cfg['unit']})",
#         min_value=float(cfg["min"]),
#         max_value=float(cfg["max"]),
#         value=float(cfg["default"]),
#         step=float(cfg["step"])
#     )
st.sidebar.header("🌦️ Điều kiện khí hậu")

FEATURE_LABELS = {
    "avg_temp": "🌡️ Nhiệt độ trung bình (°C)",
    "total_rain": "🌧️ Lượng mưa trung bình (mm)",
    "avg_humidity": "💧 Độ ẩm trung bình (%)",
    "avg_pressure": "🌬️ Áp suất khí quyển trung bình (hPa)"
}

features = {}
for feature_name, cfg in Config.FEATURE_RANGES.items():
    label = FEATURE_LABELS.get(feature_name, feature_name)

    features[feature_name] = st.sidebar.slider(
        label=label,
        min_value=float(cfg["min"]),
        max_value=float(cfg["max"]),
        value=float(cfg["default"]),
        step=float(cfg["step"])
    )

st.sidebar.markdown("---")
st.sidebar.header("Về thông tin ứng dụng")

st.sidebar.markdown("""
**📌 Mô hình huấn luyện:**  
Random Forest Regression  

**📊 Dữ liệu:**  
- FAO Crop Data
- NASA POWER Weather Data

**AI:**
- Google Gemini API
- Natural Language Processing
                    
**👥 Nhóm thực hiện:**  
Big Data – Nhóm 5  

**👨‍💻 Thành viên tham gia:**  
- Huỳnh Mẫn Mẫn
- Trần Thị Bích Hợp 
- Nguyễn Thị Hồng Ngọc  
""")

# ===============================
# MAIN TABS
# ===============================
tab1, tab2 = st.tabs(["🧠 Dự đoán từng cây", "🌱 Đề xuất cây trồng"])

# =========================================================
# TAB 1: SINGLE CROP PREDICTION + GENAI EXPLANATION
# =========================================================
with tab1:
    st.subheader("🧠 Dự đoán năng suất cho từng loại cây")

    crop = st.selectbox(
        "Chọn loại cây trồng",
        predictor.crop_list
    )

    if st.button("📈 Dự đoán năng suất"):
        result = predictor.predict(features, crop)

        st.metric(
            label="Năng suất dự đoán (kg/ha)",
            value=f"{result['predicted_yield']:.2f}"
        )

        # ===== GENAI PROMPT (RÕ RÀNG – THẦY ĐỌC LÀ GẬT) =====
        question = f"""
Hãy phân tích kết quả dự đoán năng suất cho cây {crop}.

Yêu cầu:
1. Đánh giá mức năng suất này (cao / trung bình / thấp)
2. Điều kiện khí hậu hiện tại có phù hợp không
3. Đưa ra 2–3 khuyến nghị canh tác thực tế cho nông dân
"""

        with st.spinner("🤖 AI đang phân tích kết quả..."):
            advice = assistant.get_advice(result, question)

        st.info(advice)

# =========================================================
# TAB 2: TOP 3 RECOMMENDATION + GENAI ANALYSIS
# =========================================================
with tab2:
    st.subheader("🌱 Đề xuất Top 3 cây trồng phù hợp")

    if st.button("🌿 Đề xuất cây trồng"):
        top3 = recommender.recommend_top_k(features, k=3)
        # Đổi tên cột cho thân thiện người dùng
        top3 = top3.rename(columns={
            "crop_type": "Loại cây trồng",
            "predicted_yield": "Năng suất dự kiến (kg/ha)"
        })


        st.dataframe(
            top3.reset_index(drop=True),
            use_container_width=True
        )

# ===== PREPARE DATA FOR GENAI (SAFE FOR STREAMLIT) =====

# Ensure crop_type exists as a column
if "crop_type" not in top3.columns:
    top3 = top3.reset_index()

if "crop_type" not in top3.columns:
    top3["crop_type"] = "Unknown crop"

summary_text = ""
for _, row in top3.iterrows():
    crop = row.get("crop_type", "Unknown crop")
    yield_val = row.get("predicted_yield", 0)

    summary_text += f"- {crop}: {yield_val:.1f} kg/ha\n"

question = f"""
Dựa trên kết quả dự đoán năng suất sau:

{summary_text}

Yêu cầu:
1. Giải thích vì sao các cây này được đề xuất
2. So sánh cây có năng suất cao nhất với các cây còn lại
3. Gợi ý lựa chọn cây trồng phù hợp nhất để canh tác
"""

fake_result = {
    "crop_type": "Top cây trồng",
    "predicted_yield": float(top3.iloc[0]["predicted_yield"]),
    "features": features
}

with st.spinner("🤖 AI đang tổng hợp và tư vấn..."):
    advice = assistant.get_advice(fake_result, question)

st.info(advice)

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("Big Data & Machine Learning Project | Crop Yield Prediction + GenAI")
