# relalational-search
A search algorithm that aims to search beyond the keywords.



# Relational-Search Library Documentation
## Overview
Relational-Search is a Python library designed to analyze textual data and perform semantic search operations that go beyond simple keyword matching. It computes relationships and trends in data by analyzing word distributions and creating statistical models that capture the relationships between documents.
The library is particularly useful for:
- Text analysis and corpus examination
- Document similarity measurement
- Semantic search operations
- Identifying patterns and relationships in textual data

## Core Concepts
### Data Points
The fundamental unit of analysis is a , which represents a document with a unique identifier and a matrix of word occurrences. Each datapoint captures the frequency of words in a specific document. `datapoint`
### Master Dictionary
The class maintains a global dictionary of all words across the entire corpus, along with their statistical information such as frequency and distribution. This serves as the baseline for comparison. `mater_dict`
### Distribution Maps
The library uses a to track relationships between documents, which enables semantic search capabilities beyond simple keyword matching. `byzdis_disubution_map`
## Main Components
### Data Classes
1. **datapoint**
    - Represents a single document in the corpus
    - Contains the document's unique identifier and word frequency matrix
    - Provides methods to query word occurrences and retrieve document information

2. **mater_dict**
    - Maintains a matrix of all words in the corpus with frequency data
    - Provides methods for word lookup, frequency analysis, and top word extraction
    - Supports statistical analysis of word distributions

3. **byzdis_disubution_map**
    - Maps relationships between documents based on word distributions
    - Enables semantic search and document similarity measures

4. **NullIterable**
    - Utility class that implements an empty iterator
    - Used for handling edge cases in data processing

5. **searchdict**
    - Provides search functionality over the master dictionary
    - Returns keywords from the master dictionary

### Key Functions
1. **string_to_dict(fullstring, numofdoc)**
    - Converts a string into a master dictionary object
    - Computes word frequencies and normalizes by document count
    - Returns a structured representation of word distribution

2. **string_to_datapoint_without_relations(name, data_as_string)**
    - Creates a datapoint object from a string
    - Assigns a unique name to the datapoint
    - Computes the word frequency matrix for the document

3. **list_of_data_points_to_dict(point_list)**
    - Combines multiple datapoints into a master dictionary
    - Aggregates word statistics across all documents
    - Computes average occurrences for each word

4. **list_of_poins_to_map(listofpoints, mat_dict)**
    - Creates a distribution map from a list of datapoints
    - Computes relationships between documents based on word distributions
    - Returns a byzdis_disubution_map object

5. *_searchalgo(search_terms, compleat_data_as_points_list, master_ditionary, byzdisrubution_map, term_filtering_stranth)_
    - Performs semantic search on the corpus
    - Filters results based on term importance
    - Returns a ranked list of document identifiers that match the search terms

6. **string_in_dataset_to_matrix(string_in_data)**
    - Converts a string into a word frequency matrix
    - Counts occurrences of each word
    - Returns a dictionary of word counts

### Utility Functions
1. **remove_duplicates(lst)**
    - Removes duplicate entries from a list while preserving order
    - Uses OrderedDict for efficient processing

2. **file_to_clean_str(file)**
    - Reads a file and cleans the text by removing punctuation
    - Normalizes to lowercase and removes extra whitespace

3. **cleaner(lin)**
    - Cleans a single line of text
    - Removes non-alphanumeric characters and normalizes whitespace

## File Processing
The library includes a companion module that provides utilities for: `canopener`
1. **can_opener_tsv(file)**
    - Processes TSV files into a format suitable for analysis
    - Returns cleaned text and datapoints

2. **can_opener_pdf(file)**
    - Extracts and cleans text from PDF documents
    - Requires PyPDF2 library

3. **Findurlin(string)**
    - Extracts URLs from a text string using regex

## Usage Examples
### Basic Usage
``` python
# Import the library
import search as se

# Load and process a TSV file
filepath = "data.tsv"
full_string, datapoints, count = can.can_opener_tsv(filepath)

# Create a master dictionary
master_dict = se.string_to_dict(full_string, count)

# Create a distribution map
bizmap = se.list_of_poins_to_map(datapoints, master_dict)

# Perform a search
results = se.searchalgo("keyword", datapoints, master_dict, bizmap)
print(results)
```
### Finding Top Words
``` python
# Create a master dictionary
master_dict = se.string_to_dict(document_text, document_count)

# Get top 100 words by frequency (using sort pattern 1)
top_words = master_dict.topwords(100, 1, 0)
print(top_words)
```
### Creating a Datapoint
``` python
# Clean text data
clean_text = se.cleaner(raw_text)

# Create a datapoint
document = se.string_to_datapoint_without_relations("document1", clean_text)

# Query word occurrences
frequency, exists = document.word_ocerenses("keyword")
if exists:
    print(f"'keyword' appears {frequency} times")
else:
    print("'keyword' does not appear in the document")
```
## Command Line Interface
The library includes a simple command-line interface in using the Click library: `cli.py`
``` python
import click

@click.command()
def main():
    """Run the relational-search tool."""
    click.echo("relational-search CLI is running!")

if __name__ == "__main__":
    main()
```
This CLI can be extended to provide easy access to the library's functionality from the command line.
## Installation

``` bash
pip install pip install relational-search
```
## License
This project is licensed under the GNU General Public License v2.0 or later. See the license header in each file for more details.
## Author
Kai Broadbent 'BlazarKnight' Contact: kai.broadbentohs@gmail.com

