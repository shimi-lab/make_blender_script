import click

@click.group()
def main():
    pass

@main.command('docs')
def document():
    import webbrowser
    url = "https://shimi-lab.github.io/mk-blender-scr_Document/"
    webbrowser.open(url, new=0, autoraise=True)
    
if __name__ == '__main__':
    main()