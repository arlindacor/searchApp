from googlesearch import search

def search_google(query, num_results=5):
     try:
         print(f"Search: {query}\n")
         search_results = search(query, num_results=num_results, stop=num_results)
        
         for i, result in enumerate(search_results, start=1):
             print(f"{i}. {result}")

     except Exception as e:
         print(f"An error occurred: {e}")

if __name__ == "__main__":
     user_query = input("Enter your search query: ")
     search_google(user_query)
