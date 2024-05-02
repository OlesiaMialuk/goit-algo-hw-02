import queue
import time
import random
# Створення черги заявок
request_queue = queue.Queue()
# Функція для генерації нової заявки
def generate_request(request_queue, request_id):
    request_data = f"Application №{request_id}"
    request_queue.put(request_data)
    print(f"A new application has been created: {request_data}")
  
# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видалення заявки з черги
        request = request_queue.get()
        print(f"Application processed: {request}")
        time.sleep(random.uniform(0.5, 2.0))
    else:
        print("The queue is empty. There are no applications to process.")

# Головний цикл програми
def main():
    request_queue = queue.Queue()
    request_id = 0

    try:
        while True:
            time.sleep(5)      
            if random.choice([True, False]):
                request_id += 1
                generate_request(request_queue, request_id)
                # Обробка заявок
            if random.choice([True, False]):
                process_request()

    except KeyboardInterrupt:
        print("\nThe program is terminated by the user")
        
if __name__ == "__main__":
    main()