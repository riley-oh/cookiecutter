# -*- coding: utf-8 -*-
from cookiecutter import repository, exceptions

import pytest


def test_finds_local_repo():
    """A valid local repository should be returned."""
    project_dir = repository.determine_repo_dir(
        'tests/fake-repo',
        abbreviations={},
        clone_to_dir=None,
        checkout=None,
        no_input=True
    )

    assert 'tests/fake-repo' == project_dir


def test_local_repo_with_no_context_raises():
    """A local repository without a cookiecutter.json should raise a
    `RepositoryNotFound` exception.
    """
    with pytest.raises(exceptions.RepositoryNotFound):
        repository.determine_repo_dir(
            'tests/fake-repo-bad',
            abbreviations={},
            clone_to_dir=None,
            checkout=None,
            no_input=True
        )


def test_local_repo_typo():
    """An unknown local repository should raise a `RepositoryNotFound`
    exception.
    """
    with pytest.raises(exceptions.RepositoryNotFound):
        repository.determine_repo_dir(
            'tests/unknown-repo',
            abbreviations={},
            clone_to_dir=None,
            checkout=None,
            no_input=True
        )
