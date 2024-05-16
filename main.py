from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/mistral')
def mistral_endpoint():
    ask_param = request.args.get('ask')
    if ask_param:
        # Faire une requête à l'URL fourni
        api_url = f"https://ai-1stclass-nemory-project.vercel.app/api/mistral?ask={ask_param}"
        response = requests.get(api_url)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({'error': 'Erreur lors de la requête à l\'API externe'}), 500
    else:
        return jsonify({'error': 'Paramètre \'ask\' manquant dans la requête'}), 400

if __name__ == '__main__':
    app.run(debug=True)
