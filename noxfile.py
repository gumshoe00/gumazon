import textwrap
from pathlib import Path

import nox

nox.options.sessions = ["check", "generate"]

MODULE_FILE='gumazon.__main__'
# Keep versions in sync with .github/workflows/check.yml
@nox.session(
    python=["2.6", "2.7", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9"]
)
def check(session):
    """Ensure that MODULE_FILE.py for various Python versions, works on that version."""

    # Find the appropriate MODULE_FILE.py file
    public = Path("public")
    locations = [
        public / session.python / "MODULE_FILE.py",
        public / "MODULE_FILE.py",
    ]
    for location in locations:
        if location.exists():
            break
    else:  # AKA nobreak
        raise RuntimeError("There is no public MODULE_FILE.py")

    # Get rid of provided-by-nox pip
    session.run("python", "-m", "pip", "uninstall", "pip", "--yes")
    # Run the MODULE_FILE.py file
    session.run("python", str(location))
    # Ensure that pip is installed
    session.run("python", "-m", "pip", "--version")
    session.run("pip", "--version")


@nox.session
def generate(session):
    """Update the scripts, to the latest versions."""
    session.install("packaging", "requests", "cachecontrol[filecache]", "rich")

    session.run("python", "scripts/generate.py")


@nox.session(name="update-for-release")
def update_for_release(session):
    """Automation to run after a pip release."""
    allowed_upstreams = [
        "git@github.com:pypa/MODULE_FILE.git",
        "https://github.com/pypa/MODULE_FILE.git",
    ]

    if len(session.posargs) != 1:
        session.error("Usage: nox -s update-for-release -- <released-pip-version>")

    (release_version,) = session.posargs

    session.install("release-helper")
    session.run("release-helper", "version-check-validity", release_version)
    session.run("release-helper", "git-check-tag", release_version, "--does-not-exist")
    session.run("release-helper", "git-check-remote", "upstream", *allowed_upstreams)
    session.run("release-helper", "git-check-branch", "main")
    session.run("release-helper", "git-check-clean")

    release_branch = f"release/{release_version}"
    session.run("git", "branch", release_branch, external=True)
    session.run("git", "checkout", release_branch, external=True)

    # Generate the scripts.
    generate(session)

    # Make the commit and present it to the user.
    session.run("git", "add", ".", external=True)
    session.run("git", "commit", "-m", f"Update to {release_version}", external=True)
    session.run("git", "show", "HEAD", "--stat", external=True)

    input(
        textwrap.dedent(
            f"""\
            **********************************************
            * IMPORTANT: Check which files got modified. *
            **********************************************
            This script will now generate a "signed" git tag for this commit and
            push the tag and release branch to pypa/MODULE_FILE. You will need to:
            - File a PR from the `{release_branch}` branch.
            - Merge it once the CI passes (no need to wait on reviews).
            - Delete the `{release_branch}` branch on pypa/MODULE_FILE.
            """
        )
    )

    session.run(
        # fmt: off
        "git", "tag", release_version, "-m", f"Release {release_version}",
        "--annotate", "--sign",
        external=True,
        # fmt: on
    )
    session.run("git", "push", "upstream", "HEAD", release_version, external=True)
    session.run("git", "checkout", "main", external=True)
