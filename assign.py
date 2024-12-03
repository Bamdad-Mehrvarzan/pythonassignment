import re

def load_quotes(filename):
    """Load quotes from a file and return them as a list."""
    with open(filename, 'r') as file:
        content = file.read().strip()
    return [quote.strip() for quote in content.split('\n\n')]

def load_topics(filename):
    """Load topics from a file and return them as a set of lowercase strings."""
    with open(filename, 'r') as file:
        return {line.strip().lower() for line in file}

def clean_text(text):
    """Remove punctuation and convert text to lowercase."""
    return re.sub(r"^[ws]", '', text).lower()

def find_relevant_quotes(quotes, topics):
    """Find and return relevant quotes based on topics."""
    relevant_quotes = set()
    
    for quote in quotes:
        lines = quote.split('\n')
        author = lines[0].strip()
        quote_text = ' '.join(line.strip() for line in lines[1:]).strip()

        # Clean the quote text for matching
        cleaned_quote = clean_text(quote_text)

        # Check if any topic is present in the cleaned quote text
        if any(topic in cleaned_quote for topic in topics):
            # Truncate quote if longer than 50 characters
            truncated_quote = (quote_text[:50] + '...') if len(quote_text) > 50 else quote_text
            relevant_quotes.add(f"{author} - {truncated_quote}")

    return relevant_quotes

def main():
    quotes = load_quotes('quotes.txt')
    topics = load_topics('topics.txt')
    
    relevant_quotes = find_relevant_quotes(quotes, topics)
    
    for quote in relevant_quotes:
        print(quote)

if __name__ == '__main__':
    main()
