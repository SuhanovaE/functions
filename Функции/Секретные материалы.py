def print_document(pages):
    match = 0
    for i in pages:
        if i[:8] == 'Секретно':
            match += 1
            break
        elif i[:8] != 'Секретно':
            match += 0
            print(i, end='\n')
    if match == 0:
        print('Напечатано без купюр')
    else:
        print('Дальнейшие материалы засекречены')


print_document(["Обычная страница", "И еще страница",
                "Секретно Вот этот вот текст не показывать", "Никому",
                "Никогда"])
print()
print_document(["Пустой трёп", "который", "никому не интересен"])
