import csv
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def read_suggestions_from_csv(filename):
    suggestions = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                suggestions.extend(row)
    except FileNotFoundError:
        pass
    return suggestions

def write_suggestions_to_csv(filename, suggestion):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([suggestion])

suggestions_file = 'suggestions.csv'

PRIME = 5

def calc_hash(s):
        hash_val = 0
        for i in range(len(s)):
            hash_val += ord(s[i]) * (PRIME ** i)
        return hash_val

def str_hash(old_hash, old_char, new_char, pattern_length):
    new_hash = (old_hash - ord(old_char)) / PRIME
    new_hash += ord(new_char) * (PRIME ** (pattern_length - 1))
    return new_hash

def rabin_karp(text, pattern):
    

    pattern_length = len(pattern)
    str_hash_val = calc_hash(text[:pattern_length])
    pattern_hash = calc_hash(pattern)

    matches = []

    for i in range(len(text) - pattern_length + 1):
        if str_hash_val == pattern_hash and text[i:i + pattern_length] == pattern:
            matches.append(i)
        if i < len(text) - pattern_length:
            str_hash_val = str_hash(str_hash_val, text[i], text[i + pattern_length], pattern_length)

    return matches


@app.route('/search', methods=['GET', 'POST'])

def search():
    if request.method == 'POST':
        query = request.json.get('query')
        shouldappend = request.json.get('shouldappend')
        print(shouldappend)
        match = []
        suggestions = read_suggestions_from_csv(suggestions_file)
        for suggestion in suggestions:
            matches = rabin_karp(suggestion.lower(), query.lower())
            if matches:
                match.append(suggestion)
        if shouldappend and query and query.lower() not in (suggestion.lower() for suggestion in suggestions):
            write_suggestions_to_csv(suggestions_file, query)
            print("Inside shouldappend", shouldappend)
        return jsonify(match)
    elif request.method == 'GET':
        return "Enter the query in the request body."

if __name__ == '__main__':
    app.run(debug = True)