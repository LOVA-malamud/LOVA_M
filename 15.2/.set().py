guest_list = ['alice', 'bob','charlie', 'alice', 'david', 'bob', ]
guest_list_copy = set(guest_list)
guest_list_copy.discard('emma')
if not 'emme' in guest_list_copy:
    guest_list_copy.add('emma')
print(len(guest_list))
print(guest_list_copy)