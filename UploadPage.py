import os
import webbrowser
import pyautogui
import time
import pyperclip
import csv

# Open Weebly
webbrowser.open("https://www.weebly.com")

# Wait for manual login / page load
time.sleep(60)

# Get CSV data from clipboard
clipboard_data = pyperclip.paste()

# Write clipboard data to temp CSV
temp_csv = "TempCSV.csv"
with open(temp_csv, "w", newline="", encoding="utf-8") as f:
    f.write(clipboard_data)

# Read CSV
with open(temp_csv, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    row = next(reader)  # first row

# Access fields using your new headers
short_page_name  = row["#SHORT-PAGE-NAME"]
seo_title        = row["#SEO-PAGE-TITLE"]
seo_permalink    = row["#SEO-PAGE-PERMA-LINK-.HTML"]
seo_description  = row["#SEO-PAGE-DESCRIPTION"]
seo_keywords     = row["#SEO-META-KEYWORDS"]
article_name     = row["#ARTICLE-NAME"]
article_html     = row["#ARTICLE-HTML"]

# Debug output
print("Short Page Name:", short_page_name)
print("SEO Title:", seo_title)
print("Permalink:", seo_permalink)
print("SEO Description:", seo_description)
print("SEO Keywords:", seo_keywords)
print("Article Name:", article_name)
print("Article HTML:", article_html)
