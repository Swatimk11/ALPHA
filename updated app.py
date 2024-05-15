from flask import Flask
from legacy_code_analyzer import LegacyCodeAnalyzer

app = Flask(__name__)
lca = LegacyCodeAnalyzer()

@app.route('/')
def index():
    try:
        lca.load_codebase()  # Load the codebase first
        lca.parse_codebase()  # Parse the codebase after loading
        return 'Codebase loaded and parsed successfully!'
    except ValueError as e:
        return f'Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
