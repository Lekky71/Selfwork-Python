with open('female_names') as g:
    name_lines = g.readlines()
    name_lines = [name[:-2] for name in name_lines]
    big_list = name_lines

def generator():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    file_end_name = []
    for letter in alphabet[0:4]:
        for lett in alphabet:
            file_end_name.append('x' + letter + lett)
    file_end_name = file_end_name[:-18]
    return file_end_name


end_name_array = generator()


def find_female_mails(filename, result_number):
    with open('/Users/oluwalekefakorede/Downloads/facebook_split/' + filename, 'r') as f:
        lines = f.readlines()
        n = [line.split(',') for line in lines]
        nn = {}
        for x in n:
            if len(x) > 1:
                email = x[0]
                name = x[1]
                nn[name] = email
        q = []
        for name in nn:
            try:
                if name.lower() in big_list:
                    email = nn[name]
                    q.append(email + '\n')
                    # q.append(name + ',' + email + '\n')
            except IndexError:
                pass
    with open('/Users/oluwalekefakorede/Downloads/facebook_split/result_fold/result' + result_number + '.txt', 'w')\
            as j:
        j.writelines(q)


result_num = 1
for end_name in end_name_array:
    find_female_mails(end_name, str(result_num))
    result_num = result_num + 1


