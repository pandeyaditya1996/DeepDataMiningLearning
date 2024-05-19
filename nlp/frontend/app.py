from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the models (assuming summarization, translation, and question answering)
models = {
    "summarization": pipeline("summarization"),
    "translation": pipeline("translation_en_to_de"),
    "qa": pipeline("question-answering")
}

@app.route('/perform_task', methods=['POST'])
def perform_task():
    data = request.json
    task = data['task']
    text = data['text']
    
    # Check if the task is valid and text is provided
    if task not in models or not text:
        return jsonify({"error": "Invalid task or no text provided"}), 400

    # Process the text with the corresponding model
    if task == "translation":
        result = models[task](text, max_length=40)
    elif task == "summarization":
        result = models[task](text, max_length=130, min_length=30)
    elif task == "qa":
        question, context = text.split('|')  # Expecting 'question|context' format
        result = models[task](question=question, context=context)
    
    # Return the result
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
