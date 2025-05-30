from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, Histogram
import time
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Custom metrics
REQUESTS_TOTAL = Counter(
    'concert_requests_total',
    'Total number of requests by endpoint and status',
    ['endpoint', 'status']
)

RESPONSE_TIME = Histogram(
    'concert_response_time_seconds',
    'Response time in seconds',
    ['endpoint']
)

TICKETS_SOLD = Counter(
    'concert_tickets_sold_total',
    'Total number of tickets sold by concert',
    ['concert_name']
)

# Примерная база данных концертов
concerts = [
    {'id': 1, 'name': 'Imagine Dragons', 'available_tickets': 50},
    {'id': 2, 'name': 'Coldplay', 'available_tickets': 100}
]

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(request, 'start_time'):
        resp_time = time.time() - request.start_time
        RESPONSE_TIME.labels(endpoint=request.endpoint).observe(resp_time)
        REQUESTS_TOTAL.labels(endpoint=request.endpoint, status=response.status_code).inc()
    return response

# Получить список всех концертов
@app.route('/concerts', methods=['GET'])
def list_concerts():
    logger.info('Fetching list of all concerts')
    return jsonify(concerts)

# Купить билет
@app.route('/buy', methods=['POST'])
def buy_ticket():
    try:
        data = request.get_json()
        if not data:
            logger.error('No JSON data received')
            return jsonify({'error': 'No data provided'}), 400

        concert_id = data.get('concert_id')
        quantity = data.get('quantity', 1)

        if not isinstance(quantity, int) or quantity <= 0:
            logger.error(f'Invalid quantity requested: {quantity}')
            return jsonify({'error': 'Invalid quantity'}), 400

        for concert in concerts:
            if concert['id'] == concert_id:
                if concert['available_tickets'] >= quantity:
                    concert['available_tickets'] -= quantity
                    TICKETS_SOLD.labels(concert_name=concert['name']).inc(quantity)
                    logger.info(f'Successfully sold {quantity} tickets for concert {concert["name"]}')
                    return jsonify({'message': 'Tickets purchased successfully'}), 200
                else:
                    logger.warning(f'Not enough tickets available for concert {concert["name"]}')
                    return jsonify({'error': 'Not enough tickets'}), 400

        logger.error(f'Concert with ID {concert_id} not found')
        return jsonify({'error': 'Concert not found'}), 404

    except Exception as e:
        logger.error(f'Error processing ticket purchase: {str(e)}')
        return jsonify({'error': 'Internal server error'}), 500

# Домашняя страница
@app.route('/')
def home():
    return "🎫 Welcome to the Concert Ticket API! Visit /concerts to browse shows."

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({'status': 'healthy'}), 200

# Запуск сервера
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

