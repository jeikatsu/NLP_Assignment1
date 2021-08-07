from flask import Flask, request, render_template
from markov import MarkovChain
from document1 import training_doc1
from flask.json import jsonify

app = Flask(__name__)
  
  
@app.route("/", methods=["POST", "GET"])
def home():
    
    first_tuple_elements = []

          
    return render_template("index.html", languages=first_tuple_elements)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    text = request.args.get('q')
    text = str(text)
    my_markov = MarkovChain()
    my_markov.add_document(training_doc1)
    output = my_markov.generate_text(text.lower())
    print(output)
    results = [a_tuple[0] for a_tuple in output]
    return jsonify(results=results)

  
if __name__ == '__main__':
    app.run(debug=True)