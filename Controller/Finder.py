from Models.Person import Person


ADDRESS_FILE = "Models/address.txt"
TITLES_FILE = "Models/titles.txt"
EXTRAS_FILE = "Models/name_extras.txt"


def load_list(file):
    list = []
    with open(file) as f:
        for line in f:
            list.append(line.replace('\n', ''))
    return list


def find_names(name_parts):
    # load extras list
    extras_list = load_list(EXTRAS_FILE)

    prename = ""
    name = ""
    name_extra = ""

    if name_parts[-2].endswith(','):
        name = name_parts[-2].replace(',', '')
        prename = name_parts[-1]

        i = -3
        # iterate known name extras
        while name_parts[i] in extras_list:
            name_extra = name_parts[i] + ' ' + name_extra
            i -= 1
    else:
        name = name_parts[-1]
        i = -2
        # iterate last name for known name extras
        while name_parts[i] in extras_list:
            name_extra = name_parts[i] + ' ' + name_extra
            i -= 1
        prename = name_parts[i]

    # shorten last space char
    if name_extra.endswith(' '):
        name_extra = name_extra[:-1]

    # name_extra None as default
    if name_extra == '':
        name_extra = None

    return prename, name, name_extra


def find_titles(name):
    # load title list
    title_list = load_list(TITLES_FILE)

    # sort title list: longest to shortest
    title_list = sorted(title_list, key=len, reverse=True)

    # find all known titles
    titles = []
    for title in title_list:
        if title in name:
            titles.append(title)
            name = name.replace(title, '')

    return titles


def find(name):
    # load knowing things
    address_list = load_list(ADDRESS_FILE)

    name = name.replace('\n', '')
    parts = name.split(' ')
    person = Person()

    # check first parameter for addresses
    if parts[0] in address_list:
        person.salutation = parts[0]
    # find name parts
    person.prename, person.name, person.name_extra = find_names(parts)
    # find titles
    person.titles = find_titles(name)

    return person
