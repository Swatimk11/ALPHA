from flask import Flask, render_template, request
from legacy_code_analyzer import LegacyCodeAnalyzer

app = Flask(__name__)
lca = LegacyCodeAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["code"]
        lca.load_codebase(code)  # Load the codebase first
        lca.parse_codebase()  # Then parse the codebase
        return render_template("results.html", functions=lca.function_map, dependencies=lca.dependency_map)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
