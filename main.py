"""entry point script."""

from appModules import cli,init

def main():
    cli.typerApp(prog_name=init.appname)

if __name__ == "__main__":
    main()