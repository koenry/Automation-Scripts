$url = Read-host "Please copy your repo url"
    git init
    git add .
    git commit -m "First Commit"
    git remote add origin $url
    git pull origin main --allow-unrelated-histories # Wont pull if you added a README when creating a repo without allowing unrelated histories
    git push origin main
