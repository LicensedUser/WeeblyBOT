import os
import webbrowser
import pyautogui
import time
import pyperclip
import csv

import numpy as np
import cv2

def find_with_opencv(template_path, threshold=0.85):
    # Take a screenshot and convert it to OpenCV format (grayscale)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    # Load the template image and convert to grayscale too
    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
    if template is None:
        print(f"Error: {template_path} not found or failed to load.")
        return None

    # If template has alpha channel, drop it
    if len(template.shape) == 3 and template.shape[-1] == 4:
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)
    elif len(template.shape) == 3:
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Match the template on the screen
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Debug output
    print(f"[DEBUG] Match confidence: {max_val:.3f}")

    # If match is strong enough, return the center position
    if max_val >= threshold:
        template_h, template_w = template.shape[:2]
        center_x = max_loc[0] + template_w // 2
        center_y = max_loc[1] + template_h // 2
        print(f"Found {template_path} at ({center_x}, {center_y})")
        return (center_x, center_y)

    return None


def locate_and_click(image_path, retries=3, threshold=0.85):
    for attempt in range(retries):
        coords = find_with_opencv(image_path, threshold)
        if coords:
            time.sleep(1)
            pyautogui.click(coords)
            return True
        else:
            print(f"{image_path} not found, retrying ({attempt + 1}/{retries})...")
            time.sleep(2)
    print(f"{image_path} not found after {retries} attempts.")
    return False


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

# Try to find and click the image "1.png"
if not locate_and_click("Edit-Site.png"):
    print("ErrorNoEDIT")
time.sleep(20)

# Try to find and click the image "1.png"
if not locate_and_click("Pages.png"):
    print("ErrorNoPage")
time.sleep(20)

# Try to find and click the image "1.png"
if not locate_and_click("Add-Page.png"):
    print("ErrorNoAddPage")
time.sleep(20)

# Try to find and click the image "1.png"
if not locate_and_click("Standart-Page.png"):
    print("ErrorNoAddPageStandart")
time.sleep(20)

pyautogui.write(short_page_name)
time.sleep(5)

# Try to find and click the image "1.png"
if not locate_and_click("Seo-Settings.png"):
    print("ErrorNoSeoSettings")
time.sleep(20)

# Try to find and click the image "1.png"
if not locate_and_click("Page-Title.png"):
    print("ErrorNoPage_Title")
time.sleep(20)

pyautogui.write(seo_title)
time.sleep(5)

pyautogui.press('tab')
tiem.sleep(2)

pyautogui.write(seo_permalink)
time.sleep(5)

pyautogui.press('delete', presses=5, interval=1)  # 0.1s between presses

pyautogui.press('tab')
tiem.sleep(2)

pyautogui.write(seo_description)
time.sleep(5)

pyautogui.press('tab')
tiem.sleep(2)

pyautogui.write(seo_keywords)
time.sleep(5)

# Try to find and click the image "1.png"
if not locate_and_click("Back-From-Seo.png"):
    print("ErrorNoBackFromSeo")
time.sleep(20)

# Try to find and click the image "1.png"
if not locate_and_click("Done.png"):
    print("ErrorNoDone")
time.sleep(20)
