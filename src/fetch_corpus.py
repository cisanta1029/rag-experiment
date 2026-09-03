"""
fetch_corpus.py

Pulls a curated set of Wikipedia articles on causal inference / experimentation
topics and saves each as a markdown file in corpus/, with a source-attribution
header (required by Wikipedia's CC-BY-SA license).

Calls Wikipedia's API directly (rather than the unmaintained `wikipedia`
pip package, which several users have reported breaking due to missing
User-Agent headers being rejected by Wikipedia's servers).

Usage:
    pip install requests
    python src/fetch_corpus.py
"""

import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://en.wikipedia.org/w/api.php"

# Wikipedia asks that requests identify themselves with a descriptive
# User-Agent, ideally including contact info. Set CONTACT_EMAIL in your
# .env to identify your own requests; the default is deliberately generic
# so no personal information is committed to the repo.
CONTACT = os.environ.get("CONTACT_EMAIL", "https://github.com/cisanta1029")

HEADERS = {
    "User-Agent": f"rag-experimentation-kb/1.0 (personal learning project; {CONTACT})"
}

# Curated list of topics relevant to experimentation / causal inference,
# chosen to mirror the RCT/DiD/holdout methodology background this corpus
# is meant to support retrieval over.
TOPICS = [
    "A/B testing",
    "Randomized controlled trial",
    "Difference in differences",
    "Propensity score matching",
    "Confounding",
    "Instrumental variable",
    "Simpson's paradox",
    "Selection bias",
    "Statistical significance",
    "Statistical hypothesis testing",
    "Regression discontinuity design",
    "Synthetic control method",
    "Causal inference",
    "Natural experiment",
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "corpus")


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "_", slug)
    return slug


def fetch_article(title: str):
    """Fetch plain-text extract + canonical URL for a Wikipedia article."""
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|info",
        "explaintext": 1,
        "inprop": "url",
        "redirects": 1,
        "titles": title,
    }
    resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=15)
    resp.raise_for_status()  # raises clearly if we got a non-200

    data = resp.json()
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        return None

    page = next(iter(pages.values()))
    if "missing" in page:
        return None

    return {
        "title": page.get("title", title),
        "url": page.get("fullurl", f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"),
        "content": page.get("extract", ""),
    }


def fetch_and_save(title: str) -> None:
    article = fetch_article(title)
    if not article or not article["content"]:
        print(f"  [skip] No content found for '{title}'")
        return

    filename = f"{slugify(title)}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    header = (
        f"# {article['title']}\n\n"
        f"> Source: [{article['url']}]({article['url']})  \n"
        f"> Retrieved from Wikipedia, licensed under CC BY-SA 4.0.\n\n"
        "---\n\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header + article["content"])

    print(f"  [saved] {filename}  ({len(article['content'])} chars)")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Fetching {len(TOPICS)} articles into {os.path.abspath(OUTPUT_DIR)}\n")
    for title in TOPICS:
        print(f"Fetching: {title}")
        try:
            fetch_and_save(title)
        except requests.exceptions.RequestException as e:
            print(f"  [error] Request failed for '{title}': {e}")
    print("\nDone.")


if __name__ == "__main__":
    main()
