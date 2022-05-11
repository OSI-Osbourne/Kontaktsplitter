from Models.Person import Person
from Controller.FrontendHelper import load_list, TITLES_FILE, FEMALE_FILE, MALE_FILE, EXTRAS_FILE

def find_names(name_parts):
    # empty or invalid input
    if len(name_parts) <= 1:
        return None, None, None

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
        while i >= -len(name_parts) and name_parts[i] in extras_list:
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
    i = 0
    for title in title_list:
        if title in name:
            if i == 0:
                titles.append(title)
                i+=1
            else:
                titles.append(' ' + title)
            name = name.replace(title, '')

    return titles


def find_gender_and_salutation(salutation):
    # load gender lists
    female_list = load_list(FEMALE_FILE)
    male_list = load_list(MALE_FILE)

    # check first parameter for salutation - female
    if salutation in female_list:
        return salutation, 'weiblich'
    elif salutation in male_list:
        return salutation, 'männlich'
    else:
        return None, None


def find(name):
    name = name.replace('\n', '')
    parts = name.split(' ')
    person = Person()

    if len(parts) == 1:
        parts.append('')

    person.salutation, person.gender = find_gender_and_salutation(parts[0])

    # find name parts
    person.prename, person.name, person.name_extra = find_names(parts)
    # find titles
    person.titles = find_titles(name)

    return person
