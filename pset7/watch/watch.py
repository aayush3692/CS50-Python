import re
import sys

def main():
    # Prompt the user to input HTML and print the parsed YouTube URL
    print(parse(input("HTML: ")))

def parse(s):
    # Search for the 'src' attribute in the HTML input and extract the URL
    x = re.search(r'src="([^"]+)"', s)
    if x:
        url = x.group(1)  # Extract the URL from the 'src' attribute
        
        # Replace "http://" with "https://" to ensure the URL is secure
        url = url.replace("http://", "https://")
        
        # Replace "http://www." and "https://www." with "https://"
        # This removes "www." from the beginning of the URL
        url = url.replace("http://www.", "https://")
        url = url.replace("https://www.", "https://")

        # Check if the URL is a YouTube embed link and convert it to a short URL
        if "youtube.com/embed/" in url:
            # Replace "youtube.com/embed/" with "youtu.be/" to create a short URL
            new_url = url.replace("youtube.com/embed/", "youtu.be/")
            return new_url  # Return the modified YouTube URL
        else:
            return None  # Return None if the URL does not match the expected pattern

if __name__ == "__main__":
    main()
