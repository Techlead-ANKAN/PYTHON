# Pseudo Quote generator

import requests

tags = '''
age
alone
amazing
anger
architecture
art
attitude
beauty
best
birthday
business
car
change
communications
computers
cool
courage
dad
dating
death
design
dreams
education
environmental
equality
experience
failure
faith
family
famous
fear
fitness
food
forgiveness
freedom
friendship
funny
future
god
good
government
graduation
great
happiness
health
history
home
hope
humor
imagination
inspirational
intelligence
jealousy
knowledge
leadership
learning
legal
life
love
marriage
medical
men
mom
money
morning
movies
success
'''
category = input("Enter category of quotes: ")
if category.lower() in tags:
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'enPuGiX1GylEhmZLSADCuA==rMqNbwh3idAEXEmh'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)