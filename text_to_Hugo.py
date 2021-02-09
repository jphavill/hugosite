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

#------global variables
#used to keep track of whether or not the upcoming code is a practice problem.
# Done by matching a line in a paragraph, then the next code block is treated as the pradtice problem
# todo add option for practice outputs as well, if an output directly follows a practice problem also hide it button says check your answer
practiceProblem = False
# tracks if a hidden code button is anywhere in the file, if yes add the javascript for it.
# todo add a tag instead of directly adding the javascript, then use partials for all css and javscript links
# todo add support for broken paragraphs?
hiddenCodeUsed = False

def rip_tags(section):
    """returns the tags of an article (denoted by -[TAG]) from the first section as a list"""
    lines = section.split('\n')
    tags = []
    if lines[0][0] == '-':
        line = lines[0]
        # all tags are listed in a row, while still in the lists of tags
        while line[0] == '-':
            tags.append(line.strip('-'))
            # did this for a meme because tags are listed first so it works
            line = lines[len(tags)]
    return tags


def create_main(sections):
    """takes the sections of an article (split by headers) and recombines them as html content
    returns the html, the title (first header of the file) and the tags (before first header -[TAG]"""
    global hiddenCodeUsed
    tags = rip_tags(sections[0])
    firstline = sections[0].split('\n')[len(tags)]
    title = firstline.strip('\n').strip().strip('#').strip()
    main = ''
    # add extra 2 to each tag 1 for '-' 1 for \n
    # add extra 1 for the first line for \n
    sections[0] = sections[0][sum([len(i)+2 for i in tags])+len(firstline)+1:]
    for section in sections:
        main += create_section(section)
    # if the buttons for revealing hidden code is used, include the script for it
    if hiddenCodeUsed:
        main += '<script src="/js/solution.js"></script>'
    return main, title, tags

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
    global practiceProblem
    global hiddenCodeUsed
    if practiceProblem:
        hiddenCodeUsed = True
        practiceProblem = False
        output = '<div class="code">\n' \
                 '<div class="practiceProblem"><code>'
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
    global practiceProblem
    line = re.sub(r"<", r"&lt;", line)
    line = re.sub(r">", r"&gt;", line)

    if re.match(r"### ", line):

        line = re.sub(r"(### )(.*)", r"<h3>\2</h3>", line)
        return line
    if re.search(r"you can reveal it with the button below", line, re.IGNORECASE):
        practiceProblem = True

    line = re.sub(r'`(.*?)`', r"<code>\1</code>", line)
    lines = line.split('</code>')

    if len(lines) > 1:
        for index, part in enumerate(lines):
            parts = part.split('<code>')
            if len(parts)>1:
                non_code, code = parts
            elif '<code>' in part:
                code = parts[0]
                non_code = ''
            else:
                non_code = parts[0]
                code = ''
            code = add_colour(code)
            lines[index] = non_code + ('<code>' if '<code>' in part else '') + code
        line = '</code>'.join(lines)
    return f'<p>{line}</p>'


def add_colour(line):
    line = re.sub(r"<", r"&lt;", line)
    line = re.sub(r">", r"&gt;", line)
    line = re.sub(r"(\+|-|/|%|\*)", r"<span class='symbol'>\1</span>", line)
    line = re.sub(r"(\b(if|else|elif|for|in|while|and|or|not|def|return|True|False|as|continue|break|==|!|>=|<=|&lt;|&gt;)\b)", r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(,)",  r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(:$)", r"<span class='keyword'>\1</span>", line)
    line = re.sub(r"(\b(print|int|str|chr|list|tuple|set|dict|quit|enumerate|range)\b)", r"<span class='nativeFunc'>\1</span>", line)
    line = re.sub(r"([0-9]+)", r"<span class='number'>\1</span>", line)
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
        output, title, tags = create_main(sections)
        return output, title, tags

def output(file):
    file_name = file.split('.')[0]
    with open(f'{file_name}', 'w') as f:
        f.write(output)


