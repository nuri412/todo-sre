# Concert Ticket System - SRE Implementation

This project demonstrates the implementation of Site Reliability Engineering (SRE) principles for a concert ticket booking system.

## Service Level Indicators (SLIs)

1. **Availability**
   - Endpoint health checks
   - Service uptime monitoring
   - Success rate of API requests

2. **Latency**
   - Request response time
   - 95th percentile latency for all endpoints

3. **Error Rate**
   - Rate of 5xx errors
   - Rate of 4xx errors
   - Failed transaction rate

## Service Level Objectives (SLOs)

1. **Availability**
   - Service uptime: 99.9%
   - API endpoint success rate: 99.95%

2. **Latency**
   - 95% of requests complete within 500ms
   - 99% of requests complete within 1000ms

3. **Error Rate**
   - Error rate below 0.1% for 5xx errors
   - Error rate below 1% for 4xx errors

## Monitoring Setup

The monitoring stack consists of:
- Prometheus for metrics collection
- Grafana for visualization
- Custom application metrics
- Alerting rules for incident detection

### Key Metrics

1. **Application Metrics**
   - `concert_requests_total`: Total number of requests by endpoint and status
   - `concert_response_time_seconds`: Response time histogram
   - `concert_tickets_sold_total`: Number of tickets sold by concert

2. **System Metrics**
   - CPU usage
   - Memory usage
   - Network I/O

## Setup Instructions

1. **Prerequisites**
   - Docker
   - Docker Compose

2. **Installation**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd concert-ticket-system

   # Start the services
   docker-compose up -d
   ```

3. **Access Points**
   - Application: http://localhost:5000
   - Prometheus: http://localhost:9090
   - Grafana: http://localhost:3000 (admin/admin)

## Incident Response

1. **Alert Severity Levels**
   - Critical: Immediate response required (24/7)
   - Warning: Response required within business hours
   - Info: No immediate response required

2. **Response Procedures**
   - Check application logs
   - Review metrics in Grafana
   - Follow incident response playbook
   - Document in post-mortem

## Development

1. **Local Development**
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Run the application
   python app.py
   ```

2. **Running Tests**
   ```bash
   pytest test_app.py
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License 