import spacy
from collections import defaultdict

class LegacyCodeAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.codebase = ""
        self.parsed_code = None
        self.function_map = defaultdict(list)
        self.dependency_map = defaultdict(list)

    def load_codebase(self, code):
        self.codebase = code

    def parse_codebase(self):
        if not self.codebase:
            raise ValueError("Codebase not loaded. Use load_codebase() first.")
        
        self.parsed_code = self.nlp(self.codebase)
        
        for token in self.parsed_code:
            if token.pos_ == "VERB":
                function_name = token.text
                self.function_map[function_name].append(token.sent)
                for child in token.children:
                    if child.dep_ == "dobj":
                        dependency = child.text
                        self.dependency_map[function_name].append(dependency)

    def analyze_code(self):
        if not self.parsed_code:
            raise ValueError("Codebase not parsed. Use parse_codebase() first.")

        print("Functions:")
        for func, sentences in self.function_map.items():
            print(f"- {func}:")
            for sent in sentences:
                print(f"  - {sent}")
        
        print("\nDependencies:")
        for func, deps in self.dependency_map.items():
            print(f"- {func}: {deps}")

# Example usage:
if __name__ == "__main__":
    lca = LegacyCodeAnalyzer()
    code = """
    def calculate_total_cost(price, quantity):
        return price * quantity
    
    def display_results(result):
        print(f"The result is {result}")
    
    total = calculate_total_cost(10, 5)
    display_results(total)
    """
    lca.load_codebase(code)
    lca.parse_codebase()
    lca.analyze_code()
