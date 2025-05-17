1️⃣ Basic Cleanup – Removes https:// and http:// from URLs.
2️⃣ Intermediate Cleanup – Removes www. subdomains.
3️⃣ Full Cleanup – Removes domain extensions (.com, .org, etc.), leaving only core domain names.

Installation and usage:
git clone https://github.com/RickV3/Domain-Refiner.git
cd Domain-Refiner
python main.py

Input List:
websites = [
    "https://www.google.com",
    "http://www.wikipedia.org",
    "https://www.amazon.net",
    "https://www.microsoft.edu",
]

🔹 Level 1: www.google.com, www.wikipedia.org, www.amazon.net, www.microsoft.edu  
🔹 Level 2: google.com, wikipedia.org, amazon.net, microsoft.edu  
🔹 Level 3: google, wikipedia, amazon, microsoft  

Modify the refinement level by adjusting the parameter in process_domains(n) within the script.
