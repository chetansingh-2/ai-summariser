

import requests
from bs4 import BeautifulSoup
from typing import Optional

class ContentExtractor:
    """
    A concise, object-oriented class for fetching and extracting main content from a URL.
    This class implements the custom, compliant heuristic algorithm.
    """
    def __init__(self, url: str):
        self.url = url
        self.soup = None
        self.title_text = ""
    
    def _fetch_and_parse(self) -> bool:
        """
        Fetches the URL, validates it, and parses it into a BeautifulSoup object.
        Returns True on success, False on failure.
        """
        try:
            headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
                }
            with requests.get(self.url, headers=headers, timeout=15, allow_redirects=True, stream=True) as response:
                response.raise_for_status()
                content_type = response.headers.get('Content-Type', '')
                if 'text/html' not in content_type:
                    print(f"Validation failed: URL is not an HTML page.")
                    return False
                
                self.soup = BeautifulSoup(response.text, 'lxml')
                return True
        except requests.RequestException as e:
            print(f"Failed to fetch URL {self.url}: {e}")
            return False

    def _clean_soup(self):
        """Removes noisy tags from the parsed HTML."""
        tags_to_remove = ['script', 'link', 'meta', 'style', 'nav', 'footer', 'header', 'aside', 'form', 'figure']
        for tag in self.soup.find_all(tags_to_remove):
            tag.decompose()

    def _get_main_text(self) -> Optional[str]:
        """
        Finds the main content using a layered heuristic approach.
        """
        # Heuristic 1: Look for semantic tags first.
        main_content_tag = self.soup.find('main') or self.soup.find('article')
        if main_content_tag:
            return main_content_tag.get_text(separator=' ', strip=True)

        # Heuristic 2: Custom "Voting" System.
        best_element = None
        max_score = -1
        positive_keywords = ['content', 'article', 'post', 'body', 'product', 'description', 'detail', 'item', 'articleBody']
        negative_keywords = ['sidebar', 'comment', 'ad', 'footer', 'nav', 'menu', 'related', 'promo']

        for element in self.soup.find_all(['div', 'section', 'td']):
            text = element.get_text(separator=' ', strip=True)
            if len(text) < 200:
                continue

            score = len(text)
            score += len(element.find_all('p')) * 50
            
            class_id_str = " ".join(element.get('class', [])) + " " + element.get('id', '')
            if any(k in class_id_str for k in positive_keywords): score += 75
            if any(k in class_id_str for k in negative_keywords): score -= 75
            
            num_links = len(element.find_all('a'))
            if num_links > 2 and len(text) > 0:
                if (num_links / len(text)) > 0.05:
                    score *= 0.5

            if score > max_score:
                max_score, best_element = score, element
        
        return best_element.get_text(separator=' ', strip=True) if best_element else None

    def extract(self) -> Optional[str]:
        """
        The main public method that orchestrates the entire extraction process.
        """
        if not self._fetch_and_parse():
            return None
        
        self.title_text = self.soup.title.get_text(separator=' ', strip=True) if self.soup.title else ""
        self._clean_soup()
        
        main_text = self._get_main_text()

        if main_text:
            return f"{self.title_text}\n\n{main_text}"
        
        # Fallback to title only if no main text is found
        return self.title_text if self.title_text else None

