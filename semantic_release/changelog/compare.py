from typing import Optional

from ..settings import config
from ..vcs_helpers import get_repository_owner_and_name

import os


def get_github_compare_url(from_version: str, to_version: str) -> str:
    """
    Get the GitHub comparison link between two version tags.

    :param from_version: The older version to compare.
    :param to_version: The newer version to compare.
    :return: Link to view a comparison between the two versions.
    """
    github_domain = os.environ.get("GH_DOMAIN", "github.com")
    owner, name = get_repository_owner_and_name()
    return (
        f"https://{github_domain}/{owner}/{name}" f"/compare/v{from_version}...v{to_version}"
    )


def compare_url(version: str, previous_version: str = None, **kwargs) -> Optional[str]:
    if config.get("hvcs").lower() == "github" and previous_version:
        compare_url = get_github_compare_url(previous_version, version)
        return f"**[See all commits in this version]({compare_url})**"

    return None
