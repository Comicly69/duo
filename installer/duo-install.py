import os
import urllib.request

# Download the file
url = 'https://raw.githubusercontent.com/Comicly69/duo/main/duo.sh'
filename = 'duo.sh'
urllib.request.urlretrieve(url, filename)

# Set executable permission
os.chmod(filename, 0o755)

# Move file to /usr/local/bin
os.system(f"sudo mv {filename} /usr/local/bin")

configurl = "https://raw.githubusercontent.com/Comicly69/duo/main/.duo/config.json"

os.mkdir(".duo")
urllib.request.urlretrieve(configurl, ".duo/config.json")

# Print message to reload terminal
print("Reload terminal to use duo.")
