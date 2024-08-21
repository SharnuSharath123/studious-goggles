from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    # Process the data, e.g., save to database, calculate scores
    return jsonify({"message": "Quiz submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
