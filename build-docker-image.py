from subprocess import run
from typing_extensions import Annotated
import typer


def build_docker_image(
    path: Annotated[
        str,
        typer.Option("--path", "-p", help="The directory or URL of a build context"),
    ] = "cam-python",
    push: Annotated[
        bool, typer.Option(help="Whether to push the image to the Docker Hub")
    ] = False,
    user: Annotated[
        str,
        typer.Option(
            "--user", "-u", help="The first part of the image name: user/repo:tag"
        ),
    ] = "mhoelzl",
    repo: Annotated[
        str,
        typer.Option(
            "--repo", "-r", help="The second part of the image name: user/repo:tag"
        ),
    ] = "",
    tag: Annotated[
        str, typer.Option("--tag", "-t", help="The tag of the image")
    ] = "0.0.1",
    latest: Annotated[
        bool, typer.Option(help="Additionally tag the image as :latest")
    ] = True,
    yes: Annotated[
        bool,
        typer.Option("--yes", "-y", help="Do not ask for confirmation", is_flag=True),
    ] = False,
):
    if not repo:
        # This will probably not work very well for URLs...
        repo = path.split("/")[-1]
    image_name = f"{user}/{repo}"
    latest_msg = f" and {image_name}:latest" if latest else ""
    typer.echo(f"Building {image_name}:{tag}{latest_msg} from {path}")
    if not yes:
        typer.confirm("Do you want to continue?", abort=True)

    run(["docker", "build", "--tag", f"{image_name}:{tag}", path])
    if latest:
        run(["docker", "tag", f"{image_name}:{tag}", f"{image_name}:latest"])

    if push:
        typer.echo(f"Pushing {image_name}:{tag}{latest_msg} to Docker Hub")
        run(["docker", "push", f"{image_name}:{tag}"])
        if latest:
            run(["docker", "push", f"{image_name}:latest"])


if __name__ == "__main__":
    typer.run(build_docker_image)
