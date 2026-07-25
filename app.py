import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(page_title="منصة تنافس", layout="wide")

# حقن CSS لإخفاء رأس ستريمليت الزائد ودفع المحتوى لأسفل قليلاً
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        /* إخفاء شريط أدوات ستريمليت العلوي المزعج إن أمكن، أو إزاحة الـ iframe */
        iframe {
            margin-top: 20px !important;
            width: 100vw !important;
            height: 95vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# قراءة ملف الـ HTML
template_path = os.path.join("templates", "index.html")

if os.path.exists(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    st.components.v1.html(html_code, height=950, scrolling=True)
else:
    st.error("لم يتم العثور على ملف index.html داخل مجلد templates!")
