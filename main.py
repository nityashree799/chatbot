from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/research_papers")
async def retrieve_research_papers(research_topic: str):
    # Define the URL to scrape data from.
    search_url = f"https://sci-hub.se/.jsp={Artificial_Intelligence}"

    try:
        # Send an HTTP GET request to the URL and parse the HTML content.
        response = requests.get(search_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract the paper links from the HTML using BeautifulSoup.
            paper_links = [a['href'] for a in soup.find_all('a', href=True)]

            # Generate a response with paper links.
            response_text = f"Here are some research papers on {research_topic}: {', '.join(paper_links)}"
            return {"fulfillmentText": response_text}

        else:
            return {"fulfillmentText": "Failed to retrieve data from the website."}

    except Exception as e:
        return {"fulfillmentText": "An error occurred while scraping data."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
