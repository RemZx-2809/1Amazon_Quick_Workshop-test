with open(r'e:\1Amazon_Quick_Workshop test\dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

style_start = None
style_end = None
script_start = None
script_end = None

for i, line in enumerate(lines):
    if '<style>' in line and style_start is None:
        style_start = i
    elif '</style>' in line and style_end is None:
        style_end = i
    elif '<script>' in line and script_start is None:
        script_start = i
    elif '</script>' in line and script_end is None:
        script_end = i

css_content = ''.join(lines[style_start+1:style_end]).strip() + '\n'
js_content = ''.join(lines[script_start+1:script_end]).strip() + '\n'

html_lines = lines[:style_start] + ['  <link rel="stylesheet" href="style.css">\n'] + lines[style_end+1:script_start] + ['  <script src="app.js"></script>\n'] + lines[script_end+1:]
html_content = ''.join(html_lines)

with open(r'e:\1Amazon_Quick_Workshop test\style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

with open(r'e:\1Amazon_Quick_Workshop test\app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

with open(r'e:\1Amazon_Quick_Workshop test\dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Separation complete successfully:')
print(f'- style.css ({len(css_content)} chars)')
print(f'- app.js ({len(js_content)} chars)')
print(f'- dashboard.html ({len(html_content)} chars)')
