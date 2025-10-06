def delete_html_tags(html_file, result_file = 'new_text.txt'):

    file = open("draft.html", 'r', encoding='utf-8')
    content = file.read()
    file.close()

    inside = False
    out = []
    for ch in content:
        if ch == '<':
            inside = True
        elif ch == '>':
            inside = False
            out.append(' ')
        elif not inside:
            out.append(ch)
    new_text = ''.join(out)
    with open(result_file, "w", encoding="utf-8") as  file:
        file.write(new_text)

delete_html_tags('draft.html', 'new_text.txt')