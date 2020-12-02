import click


def process(input_file):
    with open(input_file, "r") as my_file:
        data = my_file.read().splitlines()

    print(data)


@click.command()
@click.option("--input_file", help="Path to input file")
def cli(input_file):
    process(input_file)


if __name__ == "__main__":
    cli()
