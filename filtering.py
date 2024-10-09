import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import PyPDF2

# Download stopwords dari NLTK jika belum ada
nltk.download('punkt')
nltk.download('stopwords')

# Fungsi untuk ekstraksi komentar dari file PDF
def extract_comments_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        comments = ''
        for page in range(len(reader.pages)):
            comments += reader.pages[page].extract_text()
        return comments

# Fungsi untuk melakukan filtering stopwords
def filter_stopwords(text):
    # Tokenisasi
    tokens = word_tokenize(text.lower())

    # Stopwords Bahasa Inggris dari NLTK
    stopwords_en = set(stopwords.words('english'))

    # Stopwords Bahasa Indonesia menggunakan Sastrawi
    factory = StopWordRemoverFactory()
    stopwords_id = set(factory.get_stop_words())

    # Menghapus stopwords
    filtered_tokens = [word for word in tokens if word not in stopwords_en and word not in stopwords_id]

    return filtered_tokens

# Fungsi untuk menyimpan hasil filtering ke file .txt
def save_filtered_comments_to_txt(filtered_comments, output_file):
    with open(output_file, 'w') as file:
        file.write(' '.join(filtered_comments))

# Main Program
def main():
    # Nama file PDF yang berisi komentar pengguna
    pdf_file = 'komentar_pengguna.pdf'

    # Ekstraksi komentar dari file PDF
    comments = extract_comments_from_pdf(pdf_file)
    print("Komentar yang diekstraksi:")
    print(comments)

    # Filtering stopwords
    filtered_comments = filter_stopwords(comments)
    print("\nKomentar setelah dihapus stopwords:")
    print(filtered_comments)

    # Menyimpan hasil filtering ke file .txt
    output_file = 'filtered_comments.txt'
    save_filtered_comments_to_txt(filtered_comments, output_file)
    print(f"\nHasil filtering disimpan di: {output_file}")

# Jalankan program
if __name__ == "__main__":
    main()
