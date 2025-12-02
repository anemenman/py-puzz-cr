"""
Automatons, or Finite State Machines (FSM), are extremely useful to programmers when it comes to software design.
You will be given a simplistic version of an FSM to code for a basic TCP session.
The outcome of this exercise will be to return the correct state of the TCP FSM based on the array of events given.
The input array of events will consist of one or more of the following strings:

APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
The states are as follows and should be returned in all capital letters as shown:

CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
The input will be an array of events. The initial state is CLOSED. Your job is to traverse the FSM as determined by the
events, and return the proper final state as shown above.

If an event is not applicable to the current state, your code will return 'ERROR'.

Action of each event upon each state:
(the format is INITIAL_STATE: EVENT -> NEW_STATE)

CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED

Examples
['APP_PASSIVE_OPEN', 'APP_SEND', 'RCV_SYN_ACK'] =>  'ESTABLISHED'
['APP_ACTIVE_OPEN'] =>  'SYN_SENT'
['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'APP_CLOSE', 'RCV_FIN_ACK', 'RCV_ACK'] =>  'ERROR'
"""


def traverse_tcp_states(events):
    state = 'CLOSED'

    transitions = {
        'CLOSED': {
            'APP_PASSIVE_OPEN': 'LISTEN',
            'APP_ACTIVE_OPEN': 'SYN_SENT'
        },
        'LISTEN': {
            'RCV_SYN': 'SYN_RCVD',
            'APP_SEND': 'SYN_SENT',
            'APP_CLOSE': 'CLOSED'
        },
        'SYN_RCVD': {
            'APP_CLOSE': 'FIN_WAIT_1',
            'RCV_ACK': 'ESTABLISHED'
        },
        'SYN_SENT': {
            'RCV_SYN': 'SYN_RCVD',
            'RCV_SYN_ACK': 'ESTABLISHED',
            'APP_CLOSE': 'CLOSED'
        },
        'ESTABLISHED': {
            'APP_CLOSE': 'FIN_WAIT_1',
            'RCV_FIN': 'CLOSE_WAIT'
        },
        'FIN_WAIT_1': {
            'RCV_FIN': 'CLOSING',
            'RCV_FIN_ACK': 'TIME_WAIT',
            'RCV_ACK': 'FIN_WAIT_2'
        },
        'CLOSING': {
            'RCV_ACK': 'TIME_WAIT'
        },
        'FIN_WAIT_2': {
            'RCV_FIN': 'TIME_WAIT'
        },
        'TIME_WAIT': {
            'APP_TIMEOUT': 'CLOSED'
        },
        'CLOSE_WAIT': {
            'APP_CLOSE': 'LAST_ACK'
        },
        'LAST_ACK': {
            'RCV_ACK': 'CLOSED'
        }
    }

    for event in events:
        if event in transitions[state]:
            state = transitions[state][event]
        else:
            return 'ERROR'

    return state


assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'RCV_FIN']) == 'CLOSE_WAIT'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK']) == 'ESTABLISHED'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'RCV_FIN', 'APP_CLOSE']) == 'LAST_ACK'
assert traverse_tcp_states(['APP_ACTIVE_OPEN']) == 'SYN_SENT'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE', 'APP_SEND']) == 'ERROR'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE']) == 'FIN_WAIT_1'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK']) == 'ESTABLISHED'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN']) == 'SYN_RCVD'
assert traverse_tcp_states(['APP_PASSIVE_OPEN']) == 'LISTEN'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'APP_CLOSE']) == 'CLOSED'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN', 'APP_CLOSE', 'RCV_FIN', 'RCV_ACK']) == 'TIME_WAIT'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN', 'APP_CLOSE', 'RCV_FIN', 'RCV_ACK', 'APP_TIMEOUT']) == 'CLOSED'
assert traverse_tcp_states(['RCV_SYN', 'RCV_ACK', 'APP_CLOSE']) == 'ERROR'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN', 'APP_CLOSE', 'RCV_ACK']) == 'FIN_WAIT_2'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'RCV_FIN']) == 'CLOSE_WAIT'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'RCV_FIN', 'APP_CLOSE']) == 'LAST_ACK'
assert traverse_tcp_states(['APP_ACTIVE_OPEN']) == 'SYN_SENT'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'APP_CLOSE']) == 'CLOSED'
assert traverse_tcp_states(['APP_ACTIVE_OPEN', 'RCV_SYN_ACK', 'APP_CLOSE']) == 'FIN_WAIT_1'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_PASSIVE_OPEN']) == 'ERROR'
assert traverse_tcp_states(
    ['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE', 'RCV_FIN_ACK', 'APP_TIMEOUT', 'APP_ACTIVE_OPEN', 'RCV_SYN',
     'APP_CLOSE', 'RCV_FIN', 'RCV_ACK']) == 'TIME_WAIT'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE', 'RCV_SYN']) == 'ERROR'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'APP_CLOSE', 'RCV_SYN']) == 'ERROR'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE']) == 'FIN_WAIT_1'
assert traverse_tcp_states(['APP_PASSIVE_OPEN', 'RCV_SYN', 'RCV_ACK', 'APP_CLOSE', 'RCV_FIN']) == 'CLOSING'
