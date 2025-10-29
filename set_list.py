from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Bohemian Rhapsody", "artista": "Queen", "url": "teste.com"},
    {"id": 2, "titulo": "Shape of You", "artista": "Ed Sheeran", "url": "teste.com"}
]

@app.route("/tracks", methods=["GET"])
def get_tracks():
    return jsonify({"playlist": playlist, "total": len(playlist)})

@app.route("/tracks", methods=["GET"])
def get_track_by_id(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify({"mensagem": "Música encontrada!", "musica": musica})

    return jsonify({"mensagem": "Música não encontrada!"}), 404

@app.route("/tracks", methods=["POST"])
def add_track():
    nova_musica = request.json

    nova_musica["id"] = len(playlist) + 1

    playlist.append(nova_musica)
    return jsonify({"mensagem": "Música adicionada!", "musica": nova_musica})

@app.route("/tracks", methods=["PUT"])
def update_track(id):
    dados = request.json

    for musica in playlist:
        if musica["id"] == id:
            musica.update(dados)
            return jsonify({"mensagem": "Música atualizada!"})
        
    return jsonify({"erro": "Música não encontrada!"}), 404

@app.route("/tracks/<int:id>", methods=["DELETE"])
def delete_track(id):
    for musica in playlist:
        if musica["id"] == id:
            playlist.remove(musica)
            return jsonify({"mensagem": "Música apagada!"})
        
        return jsonify({"erro": "Música não encontrada!"}), 404
