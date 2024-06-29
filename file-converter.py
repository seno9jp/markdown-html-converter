import markdown
import sys


def to_markdown(md_input, md_output):
    with open(md_input, "r", encoding="utf-8") as f:
        contents = f.read()

    html_contents = markdown.markdown(contents)
    
    with open(md_output, 'w', encoding="utf-8", errors="xmlcharrefreplace") as f:
        f.write(html_contents)
    

def main():
    args_input = sys.argv[2]
    output_filename = sys.argv[3]
    
    to_markdown(args_input, output_filename)
    
if __name__ == '__main__':
    sys.exit(main())