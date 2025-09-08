
import unittest
import json
from app import app, PLAYLIST

class PlaylistApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Reset simples do seed para previsibilidade entre testes
        PLAYLIST.clear()
        PLAYLIST.extend([
            {"id": 1, "titulo": "Astronomia", "artista": "Tony Igy", "duracao": 236, "url": "https://example.com/astronomia"},
            {"id": 2, "titulo": "Numb", "artista": "Linkin Park", "duracao": 185, "url": "https://example.com/numb"},
            {"id": 3, "titulo": "Blue Bird", "artista": "Ikimono-gakari", "duracao": 228, "url": "https://example.com/blue-bird"},
        ])

    def test_health(self):
        r = self.client.get('/health')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["status"], "ok")

    def test_list_tracks(self):
        r = self.client.get('/tracks')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.get_json()), 3)

    def test_get_track_ok(self):
        r = self.client.get('/tracks/1')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["id"], 1)

    def test_get_track_404(self):
        r = self.client.get('/tracks/999')
        self.assertEqual(r.status_code, 404)

    def test_create_track_ok(self):
        payload = {"titulo": "Song X", "artista": "Someone", "duracao": 120}
        r = self.client.post('/tracks', json=payload)
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.get_json()["titulo"], "Song X")

    def test_create_track_400(self):
        r = self.client.post('/tracks', json={"titulo": "No Artist"})
        self.assertEqual(r.status_code, 400)

    def test_update_track_ok(self):
        r = self.client.put('/tracks/1', json={"titulo": "Astronomia (Remix)"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_json()["titulo"], "Astronomia (Remix)")

    def test_update_track_404(self):
        r = self.client.put('/tracks/999', json={"titulo": "X"})
        self.assertEqual(r.status_code, 404)

    def test_delete_track_ok(self):
        r = self.client.delete('/tracks/2')
        self.assertEqual(r.status_code, 204)

    def test_delete_track_404(self):
        r = self.client.delete('/tracks/999')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()
