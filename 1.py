from queue import Queue
from faker import Faker

queue = Queue()


def generate_request():
    action = {
        'name': Faker().name(),
        'id': Faker().random_int(),
        'action': Faker().random_element(elements=('create', 'update', 'delete'))
    }

    queue.put(action)


def process_request():
    if not queue.empty():
        action = queue.get()
        print(f"Processing request: {action['name']} with id {action['id']} and action {action['action']}")


while True:
    try:
        generate_request()
        process_request()
    except KeyboardInterrupt:
        break
