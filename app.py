from flask import Flask, request, jsonify

app = Flask(__name__)

# Примерная база данных концертов
concerts = [
    {'id': 1, 'name': 'Imagine Dragons', 'available_tickets': 50},
    {'id': 2, 'name': 'Coldplay', 'available_tickets': 100}
]

# Получить список всех концертов
@app.route('/concerts', methods=['GET'])
def list_concerts():
    return jsonify(concerts)

# Купить билет
@app.route('/buy', methods=['POST'])
def buy_ticket():
    data = request.get_json()
    concert_id = data.get('concert_id')
    quantity = data.get('quantity', 1)

    for concert in concerts:
        if concert['id'] == concert_id:
            if concert['available_tickets'] >= quantity:
                concert['available_tickets'] -= quantity
                return jsonify({'message': 'Tickets purchased successfully'}), 200
            else:
                return jsonify({'error': 'Not enough tickets'}), 400

    return jsonify({'error': 'Concert not found'}), 404

# Домашняя страница
@app.route('/')
def home():
    return "🎫 Welcome to the Concert Ticket API! Visit /concerts to browse shows."

# Запуск сервера
if __name__ == '__main__':
    if __name__ == '__main__':
        app.run()

