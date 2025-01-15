import re

def clean_text(text):
    """
    ทำความสะอาดข้อความ เช่น ลบลิงก์และสัญลักษณ์พิเศษ
    """
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # ลบ URL
    text = re.sub(r'[^a-zA-Zก-๙\s]', '', text)  # ลบสัญลักษณ์พิเศษ
    text = text.strip().lower()  # แปลงเป็นตัวพิมพ์เล็กและลบช่องว่างส่วนเกิน
    return text
