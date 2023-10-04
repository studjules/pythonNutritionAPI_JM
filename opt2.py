import requests

def get_recipe_title(url):
        # Make an HTTP GET request to the recipe URL
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the title
            title = soup.title.string if soup.title else "Title not found"
            return title
            print(title)
        else:
            return "Title not found"
        
get_recipe_title('http://norecipes.com/recipe/sous-vide-chicken-teriyaki/?')
