import requests
# Función para buscar DOI usando la API de CrossRef
def get_reference_from_crossref(title, i):
    search_url = f"https://api.crossref.org/works?query={title.replace(' ', '+')}&rows=1"
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        if data['message']['items']:
            # Obtener los detalles del primer artículo encontrado
            item = data['message']['items'][0]
            doi = item.get('DOI')
            title = item.get('title', ['No Title'])[0]
            authors = item.get('author', [])
            journal = item.get('container-title', ['No Journal'])[0]
            volume = item.get('volume', 'N/A')
            issue = item.get('issue', 'N/A')
            year = item.get('published-print', {}).get('date-parts', [[None]])[0][0]
            pages = item.get('page', 'N/A')

            # Formatear los autores
            author_names = []
            for author in authors:
                given_name = author.get('given', '')
                family_name = author.get('family', '')
                # Si no hay 'given', solo usar el 'family', si no, combinar ambos
                if given_name and family_name:
                    author_names.append(f"{given_name} {family_name}")
                elif family_name:
                    author_names.append(family_name)
                elif given_name:
                    author_names.append(given_name)

            author_str = ", ".join(author_names)
            
            # Construir la referencia en formato IEEE
            ieee_reference = f"[{i}] {author_str}, \"{title},\" *{journal}*, vol. {volume}, no. {issue}, pp. {pages}, {year}. DOI: https://doi.org/{doi}."
            return ieee_reference
    return "No se encontró la referencia"

# Función para obtener el formato IEEE de las referencias
def find_reference_ieee(title, i):
    ieee_ref = get_reference_from_crossref(title, i)
    return ieee_ref

# Títulos de las referencias para buscar
titles = [
    "A Survey on Hash Functions: The Principles and Applications",
    "Cryptography and Network Security: Principles and Practice",
    "Introduction to Computer Security",
    "Introduction to Modern Cryptography",
    "HMAC: Keyed-Hashing for Message Authentication",
    "Optimal Asymmetric Encryption",
    "The MD5 Message-Digest Algorithm",
    "SHA-3 Standard: Permutation-Based Hash and Extendable Output Functions",
    "Cryptanalysis of HMAC/SHA-1",
    "Introduction to Modern Cryptography",
    "The Security of HMAC",
    "Cryptography Engineering: Design Principles and Practical Applications",
    "The Knowledge Complexity of Interactive Proof-Systems",
    "The TLS Protocol Version 1.0",
    "Security Architecture for the Internet Protocol",
    "Network Security: Private Communication in a Public World",
    "Secrets and Lies: Digital Security in a Networked World",
    "Designing Secure Cloud Storage",
    "Security Engineering: A Guide to Building Dependable Distributed Systems",
    "Selecting secure hash functions for cryptographic applications",
    "Cryptography Engineering: Design Principles and Practical Applications",
    "Salted Password Hashing",
    "Security Engineering: A Guide to Building Dependable Distributed Systems",
    "Security analysis of hash functions and their cryptographic applications",
    "The security of triple encryption in the Cascade model"
]

# Buscar las referencias y mostrar en formato IEEE
i = 1
for title in titles:
    ieee_ref = find_reference_ieee(title, i)
    i += 1
    print(f"{ieee_ref}")
