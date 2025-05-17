websites = [
    "https://www.google.com",
    "http://www.wikipedia.org",
    "https://www.amazon.net",
    "https://www.microsoft.edu",
    "https://www.github.io",
    "https://www.netflix.co",
    "https://www.reddit.info",
    "https://www.apple.biz",
    "https://www.yahoo.tv",
    "https://www.facebook.com",
    "https://www.erikwendland.de"
]

extensions = [
    ".com",
    ".org",
    ".net",
    ".edu",
    ".gov",
    ".io",
    ".co",
    ".info",
    ".biz",
    ".tv",
    ".de"
]

def process_domains(n):
    result = []
    for item in websites:
        cleaned = item
        
        if n >= 1:
            cleaned = cleaned.removeprefix("https://").removeprefix("http://")
        if n >= 2:
            cleaned = cleaned.removeprefix("www.")
        if n >= 3:
            for ext in extensions:
                if cleaned.endswith(ext):
                    cleaned = cleaned.removesuffix(ext)
                    break
        if n >= 4:
            cleaned = cleaned.strip().replace("/", "").replace("-", "").replace("_", "")

        result.append(cleaned)
    
    return result


def main():
    items_cleaned = process_domains(1)
    for item in items_cleaned:
        print(item)
    print("...................")

if __name__ == "__main__":
    main()
