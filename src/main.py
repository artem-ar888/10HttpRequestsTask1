import requests


def get_smart_superhero(names):
    url = 'https://superheroapi.com/api/'
    access_token = '2619421814940190'
    top_intelligence = -1
    top_name = ''
    for name in names_list:
        search_path = url + access_token + '/search/' + name
        resp = requests.get(search_path)
        resp.raise_for_status()
        intelligence = resp.json()['results'][0]['powerstats']['intelligence']
        full_name = resp.json()['results'][0]['name']
        if intelligence == 'null':
            print(f'\t{full_name} has no intelligence')
            continue
        intelligence = int(intelligence)
        print(f'\t{full_name} : {intelligence}')
        if intelligence > top_intelligence:
            top_intelligence = intelligence
            top_name = full_name
    print(f'{top_name} is the smartest (intelligence: {top_intelligence})')


# def capitalize_first_letters(s):
#     s = s.strip()
#     words = s.split()
#     result = []
#     for word in words:
#         first_letter = word[:1].upper()
#         rest_word = word[1:]
#         result.append(first_letter + rest_word)
#     return  ' '.join(result)

if __name__ == '__main__':

    names = input('Input superheroes separated by commas: ')
    if names == '':
        names_list = ['Hulk', 'Captain America', 'Thanos', 'ERG-1']
        print(f'So we use superheroes: {', '.join(names_list)}')
    else:
        names_list = names.split(',')
        for i in range(len(names_list)):
            # names_list[i] = capitalize_first_letters(names_list[i])
            names_list[i] = names_list[i].strip()

    get_smart_superhero(names_list)
