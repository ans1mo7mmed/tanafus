import streamlit as st
import os

# إعدادات الصفحة
st.set_page_config(page_title="الصفحة الشخصية", layout="centered")

# قراءة ملف الـ HTML من داخل مجلد templates
template_path = os.path.join("templates", "index.html")

if os.path.exists(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # عرض التصميم داخل المنصة
    st.components.v1.html(html_code, height=400, scrolling=False)
else:
    st.error("لم يتم العثور على ملف index.html داخل مجلد templates!")