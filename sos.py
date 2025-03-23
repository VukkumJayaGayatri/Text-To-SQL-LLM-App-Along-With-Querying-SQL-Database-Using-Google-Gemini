
import google.generativeai as genai

genai.configure(api_key='AIzaSyAkwWrCieDWuGl4NO4y4GAwbIeclChpeZ0')

# Use the latest Gemini Pro model
model = genai.GenerativeModel('gemini-1.5-pro-002')
