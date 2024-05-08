from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Compute the similarity matrix for all books in the database
def compute_book_similarity_matrix(books):
    books['description'] = books['description'].fillna('')
    tfidf_matrix = TfidfVectorizer().fit_transform(books['description'])
    print("TFIDF matrix shape: ", tfidf_matrix.shape)
    similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
    print("Similarity matrix shape: ",similarity_matrix.shape)
    return similarity_matrix