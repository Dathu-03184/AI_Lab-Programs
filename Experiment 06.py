def vacuum_cleaner(state):
    location, status_a, status_b = state

    print("Initial State:", state)

    if location == 'A':
        if status_a == 'Dirty':
            print("Cleaning A")
            status_a = 'Clean'
        print("Moving to B")
        location = 'B'
    if location == 'B':
        if status_b == 'Dirty':
            print("Cleaning B")
            status_b = 'Clean'

    print("Final State:", (location, status_a, status_b))

# Example usage:
# (Location, A status, B status)
# Location can be 'A' or 'B', status can be 'Dirty' or 'Clean'

initial_state = ('A', 'Dirty', 'Dirty')
vacuum_cleaner(initial_state)
