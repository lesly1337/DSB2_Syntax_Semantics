import sys

def send_instruction():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    clients_set = set(clients)
    participants_set = set(participants)
    recipients_set = set(recipients)



    if (sys.argv[1] == "call_center"):
        call_center_list = list(clients_set.difference(recipients_set))
        print(call_center_list)
    elif (sys.argv[1] == "potential_clients"):
        potential_clients_list =  list(participants_set.difference(clients_set))
        print(potential_clients_list)
    elif (sys.argv[1] == "loyalty_program"):
        loyalty_program_list =  list(clients_set.difference(participants_set))
        print(loyalty_program_list)
    else:
        raise ValueError("Wrong argument")


if __name__ == '__main__':
    send_instruction()