import json
import sys
import re

def parse_abstract(text):
    """
    Deterministic helper to identify potential Object, Method, and Scenario markers.
    This helps the AI ground its extraction in text evidence.
    """
    # Simple regex-based heuristic for structured parsing
    patterns = {
        "object": r"(study|investigate|focus on|system|protein|algorithm)\s+([\w\s,-]+?)(?=\.|\s+using|\s+in)",
        "method": r"(using|via|through|employing|approach of)\s+([\w\s,-]+?)(?=\.|\s+in|\s+for)",
        "scenario": r"(in|for|within|context of)\s+([\w\s,-]+?)(?=\.|\s+using)"
    }
    
    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        results[key] = match.group(2).strip() if match else "Unknown"
        
    return results

def validate_stitch(data):
    """
    Validates if the required components for stitching are present.
    """
    required = ["target", "catalyst"]
    return all(k in data for k in required)

if __name__ == "__main__":
    # Example usage: python scripts/stitcher.py '{"target": "...", "catalyst": "..."}'
    if len(sys.argv) > 1:
        try:
            input_data = json.loads(sys.argv[1])
            if "text_to_parse" in input_data:
                print(json.dumps(parse_abstract(input_data["text_to_parse"])))
            else:
                print(json.dumps({"valid": validate_stitch(input_data)}))
        except Exception as e:
            print(json.dumps({"error": str(e)}))
