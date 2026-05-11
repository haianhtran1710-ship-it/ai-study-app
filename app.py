import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import io

# Cấu hình trang web
st.set_page_config(page_title="AI Study Analytics", layout="wide")

st.title("🚀 Ứng dụng AI Phân Tích Thói Quen Học Tập")
st.markdown("---")

# Thanh bên (Sidebar)
st.sidebar.header("Hướng dẫn")
st.sidebar.info("1. Tải file Excel lên\n2. Nhấn nút Phân tích\n3. Tải kết quả về")

uploaded_file = st.file_uploader("Chọn file Excel khảo sát", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Dữ liệu vừa tải lên:")
    st.dataframe(df.head(10)) # Hiện 10 dòng đầu

    # Chọn cột để phân tích (Dũng có thể chỉnh lại số cột ở đây)
    df_ai = df.iloc[:, [1, 2, 3]].copy()

    # Nút bấm để kích hoạt AI
    if st.button("🤖 Bắt đầu phân tích AI"):
        with st.spinner('AI đang tính toán...'):
            # Dọn dẹp dữ liệu
            for col in df_ai.columns:
                df_ai[col] = pd.to_numeric(df_ai[col], errors='coerce')
                df_ai[col] = df_ai[col].fillna(df_ai[col].mean() if not df_ai[col].isnull().all() else 0)

            # Chạy AI
            kmeans = KMeans(n_clusters=4, random_state=42)
            df['Phân_Nhóm_AI'] = kmeans.fit_predict(df_ai)
            
            st.success("✅ Phân tích hoàn tất!")
            st.write("### Kết quả phân nhóm:")
            st.dataframe(df)

            # Tạo nút bấm tải file kết quả về
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            
            st.download_button(
                label="📥 Tải file kết quả về máy",
                data=output.getvalue(),
                file_name="ket_qua_phan_nhom_ai.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )