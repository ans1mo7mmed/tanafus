import streamlit as st
import os

# إعدادات الصفحة لتكون بعرض الشاشة بالكامل (wide)
st.set_page_config(page_title="منصة تنافس", layout="wide")

# إزالة الهوامش الزائدة والتداخلات الخاصة بمنصة ستريمليت من الأعلى والجانبين
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        iframe {
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# قراءة ملف الـ HTML من داخل مجلد templates
template_path = os.path.join("templates", "index.html")

if os.path.exists(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # عرض التصميم ليمتلئ بالشاشة بالكامل
    st.components.v1.html(html_code, height=900, scrolling=True)
else:
    st.error("لم يتم العثور على ملف index.html داخل مجلد templates!")
