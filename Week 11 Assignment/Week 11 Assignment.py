import requests
import pandas as pd

def get_nyt_bestsellers(api_key, list_name="hardcover-fiction"):
    url = f"https://api.nytimes.com/svc/books/v3/lists/current/{list_name}.json"
    
    response = requests.get(url, params={'api-key': api_key})
    data = response.json()
    
    # Convert books to DataFrame
    books = data['results']['books']
    df = pd.DataFrame(books)
    
    return df

# Usage
api_key = "gxizjT2nY7Awh1vXvXeJonKkVXyjAokH"
df = get_nyt_bestsellers(api_key)

print(f"Found {len(df)} bestsellers")
print(df[['rank', 'title', 'author', 'weeks_on_list']])