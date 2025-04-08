@echo off
echo 📝 Generating blog post...
python generator.py

echo 🔄 Updating blog index...
python update_index.py

echo 📦 Committing changes...
git add .
git commit -m "✍️ New blog post on auto-deploy"
git push

echo ✅ Deployment complete!
pause
