
class Contact(object):

    def __init__(self):
        self.name, self.email, self.phone, self.title = '', '', '', ''
contact = Contact()
contact.direct_line = '123'
contact.Phone_no = '345'
contact.mobile_phone = '567'

dic = contact.__dict__

print([dic[attr] for attr in dic])

contact.phones = ','.join([dic[attr] for attr in dic if (
    'line' in attr.lower() or 'phone' in attr.lower() and dic[attr] != '')])

print(contact.phones)
