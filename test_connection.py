import os
import google.generativeai as genai

# اگر کلید رو در env ست کردی، خودش می‌خونه، اگر نه، مستقیم بذار
API_KEY = os.getenv("GEMINI_API_KEY", "your api here")

genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content("سلام! آیا وصل هستم؟")
    print("نتیجه:", response.text)
except Exception as e:
    print("خطا:", repr(e))
