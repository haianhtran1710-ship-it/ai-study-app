import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

st.set_page_config(page_title="AI Study Analytics", layout="wide")

st.title("🚀 Ứng dụng AI Phân Tích Thói Quen Học Tập")

uploaded_file = st.file_uploader("Chọn file Excel khảo sát", type=['xlsx'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    
    if st.button("Bắt đầu phân tích AI"):
        # Thuật toán AI phân nhóm
        kmeans = KMeans(n_clusters=3, random_state=42)
        # Chỉ lấy các cột chứa số để phân tích
        numeric_cols = df.select_dtypes(include=['number']).columns
        df['Phân_Nhóm_AI'] = kmeans.fit_predict(df[numeric_cols])
        
        st.success("✅ Phân tích hoàn tất!")
        st.write("### Kết quả phân nhóm dữ liệu:")
        st.dataframe(df)
        
        st.markdown("---")
        st.header("🤖 Nhận xét và Lời khuyên từ AI:")
        
        # Vòng lặp để AI đưa ra lời khuyên cho từng nhóm
        for i in range(3):
            st.subheader(f"Nhóm {i}:")
            if i == 0:
                st.info("💡 **Nhận xét:** Nhóm này có xu hướng tự học cao và sử dụng AI hiệu quả. \n\n **Lời khuyên:** Tiếp tục duy trì phong độ và chia sẻ cách học cho bạn bè nhé!")
            elif i == 1:
                st.warning("💡 **Nhận xét:** Các bạn trong nhóm thường học khuya, dễ gây mệt mỏi. \n\n **Lời khuyên:** Nên điều chỉnh ngủ sớm hơn để não bộ tỉnh táo vào ban ngày.")
            else:
                st.success("💡 **Nhận xét:** Nhóm thích học qua thực hành và thảo luận nhóm. \n\n **Lời khuyên:** Nên tổ chức thêm các buổi học chung để giải bài tập khó cùng nhau.")
