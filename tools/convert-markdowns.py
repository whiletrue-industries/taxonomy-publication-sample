import os
import markdown

def render_markdown_to_html(markdown_file):
    """Convert markdown file content to HTML."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.replace('==>', '←')
        html_content = markdown.markdown(text)
    return html_content

def create_index_html(directory, html_content):
    """Create an index.html file in the directory with the HTML content and RTL direction."""
    index_file = os.path.join(directory, 'index.html')
    title = directory.replace('.', '').strip('/')
    title = ' - '.join(filter(None, ['טקסונומיית משרד הרווחה', title]))
    
    # HTML template with RTL direction
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
        <style type="text/css">
            * {{
                font-family: "Open Sans", sans-serif;
                font-optical-sizing: auto;
            }}
            body {{
                margin: 0;
                padding: 20px;
                direction: rtl;
                display: flex;
                flex-flow: column;
                align-items: center;                
            }}
            body > div {{
                width: 100%;
                max-width: 720px;
            }}
        </style>
    </head>
    <body>
        <div>
            {html_content}
        </div>
    </body>
    </html>
    """
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    print(f"Created {index_file}")

def traverse_directory(base_directory):
    """Traverse the directory tree and create index.html files."""
    for root, _, files in os.walk(base_directory):
        if 'readme.md' in files:
            markdown_file = os.path.join(root, 'readme.md')
            html_content = render_markdown_to_html(markdown_file)
            create_index_html(root, html_content)

if __name__ == "__main__":
    base_directory = '.'  # Replace with your directory
    traverse_directory(base_directory)
