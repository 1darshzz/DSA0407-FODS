import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

def calculate_word_frequency(review_text):
    words = word_tokenize(review_text.lower()) 
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist = FreqDist(words)

    return freq_dist

def main():
    customer_reviews = [
        "I really like this product. It's amazing!",
        "Not satisfied with the quality. Will not buy again.",
        "Excellent customer service. Highly recommended.",
        "The product is okay, but the delivery was delayed.",
        "Worst purchase ever. Waste of money.",
    ]
    all_reviews_text = " ".join(customer_reviews)
    freq_distribution = calculate_word_frequency(all_reviews_text)
    print("Word Frequency Distribution:")
    for word, frequency in freq_distribution.most_common():
        print(f"{word}: {frequency}")

if _name_ == "_main_":
    main()
