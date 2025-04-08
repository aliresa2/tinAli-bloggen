import os
from datetime import datetime

BLOG_DIR = "blog_posts"
INDEX_TEMPLATE = "templates/index_template.html"
OUTPUT_INDEX = "index.html"

def extract_title_and_date(filename):
    # نمونه: 20250408-how-ai-can-change-content.html
    name = os.path.splitext(filename)[0]
    try:
        date_str, slug = name.split("-", 1)
        date = datetime.strptime(date_str, "%Y%m%d").strftime("%B %d, %Y")
        title = slug.replace("-", " ").capitalize()
        return title, date, filename
    except ValueError:
        return None, None, None

def generate_post_list():
    files = sorted(os.listdir(BLOG_DIR), reverse=True)
    list_items = []
    for f in files:
        if f.endswith(".html"):
            title, date, filename = extract_title_and_date(f)
            if title and date:
                list_items.append(
                    f'<li>\n<a href="{BLOG_DIR}/{filename}">{title}</a>\n<span class="date">{date}</span>\n</li>'
                )
    return "\n".join(list_items)

def update_index():
    with open(INDEX_TEMPLATE, encoding="utf-8") as f:
        template = f.read()

    posts_html = generate_post_list()
    filled_template = template.replace("{{ posts }}", posts_html)

    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        f.write(filled_template)
    
    print("✅ index.html updated with post list.")

if __name__ == "__main__":
    update_index()
