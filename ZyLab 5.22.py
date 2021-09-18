
#Annabelle Poer PSID:1798854

my_services = {'Oil change': 35,
               'Tire rotation': 19,
               'Car wash': 7,
               'Car wax': 12,
               'No service': 0}

print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')

first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

if first_service == '-':
    first_service = 'No service'
if second_service == '-':
    second_service = 'No service'

print()

print('Davy\'s auto shop invoice\n')

if first_service == 'No service':
    print('Service 1: No service')
else:
    print('Service 1: {}, ${}'.format(first_service, my_services[first_service]))

if second_service == 'No service':
    print('Service 2: No service')
else:
    print('Service 2: {}, ${}'.format(second_service, my_services[second_service]))


print()
print('Total: ${}'.format(int(my_services[first_service]) + int(my_services[second_service])))
