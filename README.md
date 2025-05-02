# Weather Dashboard Project

This is a real-time weather dashboard project that collects weather data for 10 cities (plus Berlin) using Apache Kafka, stores it in Amazon S3, and visualizes it in Power BI. The project demonstrates a data pipeline for processing and analyzing global weather data.

## Features
- Collects weather data in real-time for cities like London, New York, Tokyo, Sydney, Paris, Mumbai, Cape Town, Toronto, Beijing, Rio de Janeiro, and Berlin.
- Uses Kafka for message queuing and S3 for data storage.
- Visualizes data in an interactive Power BI dashboard (work in progress).

## Project Structure
- `scripts/`: Contains Python scripts for Kafka producer, consumer, and S3 data processing.
- `configs/`: Configuration files (excluding sensitive credentials).
- `docker/`: Docker Compose files for setting up Kafka and ZooKeeper.
- `.gitignore`: Excludes data files, Power BI files, and credentials.

## Setup Instructions
1. **Prerequisites**:
   - Install Docker and Docker Compose.
   - Install Python 3.x and required libraries (e.g., `kafka-python`, `boto3`).
   - Set up an AWS S3 bucket and configure credentials (store them securely in environment variables).
2. **Run the Project**:
   - Navigate to the project folder: `cd E:\Project_Environments\weather_dashboard`.
   - Start Docker containers: `docker-compose -f docker/docker-compose.yml up`.
   - Run the producer script: `python scripts/kafka_producer.py`.
   - Run the consumer script: `python scripts/kafka_consumer.py`.
   - Process S3 data: `python scripts/process_s3_data.py`.
3. **Build the Dashboard**:
   - Open `weather_dashboard.pbix` in Power BI Desktop and follow the visualization steps.

## Future Improvements
- Complete the Power BI dashboard with advanced visuals.
- Add automated testing for the data pipeline.
- Enhance documentation with usage examples.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (add a `LICENSE` file if desired).
