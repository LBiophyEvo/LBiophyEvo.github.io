from scholarly import scholarly
import hashlib


def generate_unique_id(publication):
    """Generates a unique ID for each publication using its title and year."""
    title = publication['bib'].get('title', 'untitled').lower().replace(' ', '_')
    pub_year = publication['bib'].get('pub_year', 'unknown_year')

    # Use a combination of the title and year to generate a unique ID
    unique_string = f"{title}_{pub_year}"

    # Create a hash to ensure the ID is unique and doesn't break with special characters
    unique_id = hashlib.md5(unique_string.encode('utf-8')).hexdigest()
    return unique_id


def get_papers_by_authors_and_dates(author_name, start_year, end_year):
    all_papers = []

    search_query = scholarly.search_author(author_name)
    author = next(search_query)  # Retrieve the first result for simplicity
    scholarly.fill(author, sections=['publications'])  # Get all publications

    for pub in author['publications']:
        pub_year = pub.get('bib', {}).get('pub_year')
        if pub_year and start_year <= int(pub_year) <= end_year:
            # Check if the publication has an 'ENTRYTYPE', if not set a default type
            if 'ENTRYTYPE' not in pub['bib']:
                pub['bib']['ENTRYTYPE'] = 'article'  # Default to 'article' if missing

            pub['bib']['ID'] = generate_unique_id(pub)
            pub['bib']['year'] = pub_year

            # Remove the "pub_year" key if it exists
            if 'pub_year' in pub['bib']:
                del pub['bib']['pub_year']

            try:
                bibtex_entry = scholarly.bibtex(pub)  # Retrieve BibTeX entry
                all_papers.append(bibtex_entry)
            except KeyError as e:
                print(f"Skipping a publication due to missing key: {e}")

    return all_papers

# Example usage:
authors = [('vaitea opuu', 2023, 2030)]
bib_output = '../_bibliography/references.bib'

all_papers = []
for author, start_d, end_d in authors:
    all_papers += get_papers_by_authors_and_dates(author, 2023, 2030)

# Write all BibTeX entries to the file
with open(bib_output, 'w') as bibtex_file:
    for entry in all_papers:
        bibtex_file.write(entry + '\n\n')

print(f"Saved {len(all_papers)} papers to {bib_output}")
