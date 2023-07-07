def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages = [badge_maker(name) for name in names]
    return badge_messages

def assign_rooms(names):
    room_list = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    return room_list

def printer(names):
    badge_messages = batch_badge_creator(names)
    for badge_message in badge_messages:
        print(badge_message) 
        
    assign_list = assign_rooms(names)
    for assign in assign_list:
        print(assign)
