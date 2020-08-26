import re

# css_links = ['normalize', 'main', 'headerfooter', 'articles']
#
# nav_links = ['about', 'articles']
#
# footer_links = []
#
# 'set up facebook, twitter instagram for jason havill tutorials, filler for now'
# social_links = ['https://facebook.com/jasonhavilltutorials/',
#                 'https://instagram.com/jasonhavilltutorials/',
#                 'https://twitter.com/jasonhavilltutorials/']

#global variables
hidden_solution = False

# def create_html(sections):
#     html = create_head(sections[0].split('\n')[0])
#     html += create_body(sections)
#     html += '</html>\n'
#     return html

# def create_head(line):
#     title = line.strip('\n').strip().strip('#').strip()
#     head = f'<!DOCTYPE html>\n' \
#                      f'<html lang="en">\n' \
#                      f'<head>\n' \
#                      f'<meta charset="UTF-8">\n' \
#                      f'<title>{title}</title>\n'
#     for css in css_links:
#         head += f'<link rel="stylesheet" href="css/{css}.css">\n'
#     head += '</head>\n'
#     return head

# def create_body(sections):
#     body = '<body>\n'
#     body += create_header()
#     body += create_main(sections)
#     body += create_footer()
#     body += '</body>\n'
#     return body

# def create_header():
#     header = '<header>\n' \
#              '<nav class="topnav">\n' \
#              '<a href="index.html" id="homepage">JASON HAVILL</a>\n' \
#              '<div class="mainnav">\n'
#     for link in nav_links:
#         header += f'<a href="{link}.html" id="{link}">{link.upper()}</a>\n'
#     header += '</div>\n' \
#              '<hr>\n' \
#              '</nav>\n' \
#              '</header>\n'
#     return header


def create_main(sections):
    firstline = sections[0].split('\n')[0]
    title = firstline.strip('\n').strip().strip('#').strip()
    main = f'<main>\n' \
           f'<h1>{title}</h1>'
    sections[0] = sections[0][len(firstline):]
    for section in sections:
        main += create_section(section)
    main += '</main>\n'
    return main

def create_section(section):
    output = "<section>\n"
    section = section.split('\n')
    output += f"<h2>{section.pop(0).strip()}</h2>\n"
    while section:
        line = section.pop(0)
        if line:
            if line[0] == '`':
                section, result = create_code(section)
                output += result
            elif line[0] == '-':
                output += '<hr>\n'
            else:
                output += create_paragraph(line)


    output += "</section>\n"
    return output


def create_code(section):
    global hidden_solution
    if hidden_solution:
        hidden_solution = False
        output = '<div class="code">\n' \
                 '<div class="hiddencode"><code>'
    else:
        output = '<div class="code">\n' \
                 '<div><code>'
    result = False
    while section:
        line = section.pop(0)
        if line != '':
            if line[0] == '`':
                break
            elif line[0:6] == 'OUTPUT':
                firstline = line
                section, result = create_output(section, firstline)
                continue
            line = add_colour(line)
        output += f'{line}\n'
    output = output[:-1] + '</code>\n' \
              '</div></div>\n'
    if result:
        output += result
    return section, output


def create_output(section, firstline):
    output = f'<div class="output">\n' \
             f'<code>{firstline}\n'
    while section:
        line = section.pop(0)
        if line != '':
            if line[0] == '`':
                break
        if line[0:6] == 'OUTPUT' or line[0:9] == 'USERINPUT':
            output += f'{line}\n'
        else:
            output += f'\t{line}\n'
    output.rstrip('\n')
    output += '</code>\n' \
              '</div>\n'
    section.insert(0, '```')
    return section, output


def create_paragraph(line):
    global hidden_solution

    line = re.sub(r"<", r"&lt;", line)
    line = re.sub(r">", r"&gt;", line)

    if re.match(r"### ", line):

        line = re.sub(r"(### )(.*)", r"<h3>\2</h3>", line)
        return line
    if re.search(r"hover below to see a possible solution", line, re.IGNORECASE):
        hidden_solution = True

    line = re.sub(r'`(.*?)`', r"<code> \1 </code>", line)
    lines = line.split('</code>')

    if len(lines) > 1:
        for index, part in enumerate(lines):
            part = re.sub(r"(<code>.*?)(\+|-|/|%|\*|&gt;|&lt;)", r"\1<span class='symbol'>\2</span>", part)
            part = re.sub(r"(<code>.*?)(if|else|elif|for|in|while|and|or|not|def|return|True|False|as|continue|break|==|!|>=|<=|&lt;|&gt;)",
                         r"\1<span class='keyword'>\2</span>", part)
            part = re.sub(r"(<code>.*?)(\b(print|int|str|chr|list|tuple|set|dict|quit|enumerate|range))", r"\1<span class='nativeFunc'>\2</span>", part)
            part = re.sub(r"(<code>.*?)([^a-zA-Z])([0-9]+)", r"\1\2<span class='number'>\3</span>", part)
            part = re.sub(r'(<code>.*?)(".*?")', r"\1<span class='string'>\2</span>", part)
            part = re.sub(r"(<code>.*?)(,)", r"\1<span class='keyword'>\2</span>", part)
            part = re.sub(r"(<code>.*?)(:)", r"\1<span class='keyword'>\2</span>", part)
            lines[index] = part
        line = '</code>'.join(lines)
    return f'<p>{line}</p>'

# todo right now stops on first '<' need to make it stop on first full </code>


def add_colour(line):
    line = re.sub(r"<", r"&lt;", line)
    line = re.sub(r">", r"&gt;", line)
    line = re.sub(r"(\+|-|/|%|\*)", r"<span class='symbol'>\1</span>", line)
    line = re.sub(r"(\b(if|else|elif|for|in|while|and|or|not|def|return|True|False|as|continue|break|==|!|>=|<=|&lt;|&gt;)\b)", r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(,)",  r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(:$)", r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(\b(print|int|str|chr|list|tuple|set|dict|quit|enumerate|range)\b)", r"<span class='nativeFunc'>\1</span>", line)
    line = re.sub(r"([^a-zA-Z])([0-9]+)", r"\1<span class='number'>\2</span>", line)
    line = re.sub(r'(".*?")', r"<span class='string'>\1</span>", line)
    line = re.sub(r'(#.*$)', r"<span class='lineComment'>\1</span>", line)
    return line


def create_span(word, classtype):
    return f'<span class="{classtype}">{word}</span>'


# def create_footer():
#   footer = '<header>\n' \
#            '<nav class="topnav">\n' \
#            '<a href="index.html" id="homepage">JASON HAVILL</a>\n' \
#            '<div class="mainnav">\n'
#   for link in social_links:
#     website = re.search(r'https://(.*?).com', link).group(1)
#     print(website)
#     footer += f'<a href="index.html" id="{link}">{link.upper()}</a>\n'
#   footer += '</div>\n' \
#             '<hr>\n' \
#             '</nav>\n' \
#             '</header>\n'
#   return footer

def convert(file):
    with open(f"{file}", "r") as f:
        sections = f.read().split("\n## ")
        output = create_main(sections)
        return output

def output(file):
    file_name = file.split('.')[0]
    with open(f'{file_name}', 'w') as f:
        f.write(output)


