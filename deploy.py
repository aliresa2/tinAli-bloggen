import os

# Generate new blog post
print("📝 Generating blog post...")
os.system("python generator.py")

# Update index.html
print("🔄 Updating blog index...")
os.system("python update_index.py")

# Git operations
print("📦 Committing changes...")
os.system("git add .")
os.system('git commit -m "✍️ New blog post on auto-deploy"')
os.system("git push")

print("✅ Deployment complete!")
