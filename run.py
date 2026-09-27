from src.main.rabbitmq_config.consumer import RabbitMqConsumer

if __name__ == "__main__":
    consumer = RabbitMqConsumer()
    consumer.start()
    