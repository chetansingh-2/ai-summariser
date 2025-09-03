# import requests
# from langchain_community.document_loaders import UnstructuredURLLoader
# from typing import List, Optional
# from langchain_core.documents import Document

# def extract_documents_from_url(url: str) -> Optional[List[Document]]:
#     """
#     Performs a pre-flight check on a URL and then uses UnstructuredURLLoader
#     to extract and partition the content into LangChain Document objects.
#     """
#     # 1. Pre-flight check with a lightweight HEAD request
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         }
#         # Use a GET request with stream=True to be more robust than HEAD, but only read headers.
#         with requests.get(url, headers=headers, timeout=10, allow_redirects=True, stream=True) as response:
#             response.raise_for_status() # Raises an error for non-2xx status codes

#             content_type = response.headers.get('Content-Type', '')
#             if 'text/html' not in content_type:
#                 print(f"Validation failed: URL is not an HTML page (Content-Type: {content_type}).")
#                 return None

#     except requests.RequestException as e:
#         print(f"Pre-flight check failed for URL {url}: {e}")
#         return None

#     # 2. If validation passes, proceed with content extraction
#     print("Pre-flight check passed. Extracting content with UnstructuredURLLoader...")
#     try:
#         loader = UnstructuredURLLoader(urls=[url], continue_on_failure=False)
#         documents = loader.load()
#         return documents

#     except Exception as e:
#         print(f"Error processing URL {url} with UnstructuredURLLoader: {e}")
#         return None




import requests
from bs4 import BeautifulSoup
from typing import Optional

def extract_main_content(url: str) -> Optional[str]:
    """
    Implements an enhanced, compliant content extraction algorithm.

    This version uses a more resilient "voting" system to better handle
    complex layouts like e-commerce sites, without violating the assignment's
    constraints on using third-party density analysis libraries.
    """
    # 1. Pre-flight check and HTML fetching
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        }
        # Make only ONE request. stream=True allows us to check headers first.
        # Increased timeout for more resilience with slow sites.
        with requests.get(url, headers=headers, timeout=15, allow_redirects=True, stream=True) as response:
            response.raise_for_status()
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                print(f"Validation failed: URL is not an HTML page (Content-Type: {content_type}).")
                return None
            
  
            html_content = response.text
            
    except requests.RequestException as e:
        print(f"Failed to fetch URL {url}: {e}")
        return None



    # 2. Parse and get title
    soup = BeautifulSoup(html_content, 'lxml')
    title_text = soup.title.get_text(separator=' ', strip=True) if soup.title else ""


    # 3. Clean the document by removing noisy tags
    tags_to_remove = ['script', 'link', 'meta' 'style', 'nav', 'footer', 'header', 'aside', 'form', 'figure']
    for tag in soup.find_all(tags_to_remove):
        tag.decompose()


    #4. Heuristic 1: Look for these tags. usually for articles/blogs
    main_content_tag = soup.find('main') or soup.find('article')
    if main_content_tag:
        main_text = main_content_tag.get_text(separator=' ', strip=True)
        return f"{title_text}\n\n{main_text}"

    # 5. "Voting" System Heuristic 2
    best_element = None
    max_score = -1
    
    positive_keywords = ['content', 'article', 'post', 'body', 'product', 'description', 'detail', 'item', 'articleBody']
    negative_keywords = ['sidebar', 'comment', 'ad', 'footer', 'nav', 'menu', 'related', 'promo']

    for element in soup.find_all(['div', 'section', 'td']):
        text = element.get_text(separator=' ', strip=True)
        text_length = len(text)
        
        if text_length < 200:
            continue

        score = text_length

        # A) Give a big bonus for paragraphs
        num_paragraphs = len(element.find_all('p'))
        score += num_paragraphs * 50

        # B) Adjust score based on class/id keywords
        class_id_string = " ".join(element.get('class', [])) + " " + element.get('id', '')
        if any(keyword in class_id_string for keyword in positive_keywords):
            score += 75
        if any(keyword in class_id_string for keyword in negative_keywords):
            score -= 75
        
        # C) Penalize heavily for high link density
        num_links = len(element.find_all('a'))
        if num_links > 2: # Ignore 1-2 links
            link_density = num_links / text_length if text_length > 0 else 0
            if link_density > 0.05:
                score *= 0.5 

        if score > max_score:
            max_score = score
            best_element = element

    if best_element:
        main_text = best_element.get_text(separator=' ', strip=True)
        return f"{title_text}\n\n{main_text}"


    return title_text if title_text else None

