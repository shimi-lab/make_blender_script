import click

@click.group()
def main():
    pass

@main.command('docs')
def document():
    from streamlit import util
    util.open_browser("https://shimi-lab.github.io/mk-blender-scr_Document/")
    
if __name__ == '__main__':
    main()