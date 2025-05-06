from flask import Flask, render_template, request, redirect
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    chain = blockchain.chain
    invalid_indices = blockchain.get_invalid_blocks()
    return render_template('index.html', chain=chain, invalid_indices=invalid_indices)

@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.form['data']
    blockchain.add_block(data)
    return redirect('/')

@app.route('/edit_block/<int:index>', methods=['POST'])
def edit_block(index):
    new_data = request.form['new_data']
    blockchain.edit_block(index, new_data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)