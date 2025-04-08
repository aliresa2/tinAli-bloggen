import os
import json
import datetime
from string import Template

# 🔧 تنظیمات اصلی
with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

TITLE = config["title"]
DESCRIPTION = config["description"]
CONTENT = config["content"]
OUTPUT_DIR = "blog_posts"
TEMPLATE_PATH = "templates/post_template.html"

# 🧱 ساخت نام فایل خروجی
date_str = datetime.datetime.now().strftime("%Y-%m-%d")
slug = TITLE.lower().replace(" ", "-")
filename = f"{date_str}-{slug}.html"
output_path = os.path.join(OUTPUT_DIR, filename)

# 🧩 لود کردن قالب HTML
with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    template = Template(f.read())

# 📝 جایگذاری محتوای واقعی داخل قالب
html_content = template.substitute(
    title=TITLE,
    description=DESCRIPTION,
    date=date_str,
    content=CONTENT
)

# 💾 ذخیره پست HTML در پوشه خروجی
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ پست ساخته شد: {output_path}")
