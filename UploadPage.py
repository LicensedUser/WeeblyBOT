import os
import webbrowser
import pyautogui
import time
import pyperclip

webbrowser.open("https://www.weebly.com")
# Wait 60 seconds for page to load
time.sleep(60)

clipboard_data = pyperclip.paste()

# Step 2: Write to TempCSV.csv
temp_csv = "TempCSV.csv"
with open(temp_csv, "w", newline="", encoding="utf-8") as f:
    f.write(clipboard_data)

# Step 3: Read the CSV
with open(temp_csv, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    row = next(reader)

#PAGE-NAME,#PAGE-TITLE,#PAGE-PERMA-LINK-.HTML,#PAGE-DESCRIPTION,#META-KEYWORDS,#ARTICLE-NAME,#ARTICLE-HTML
