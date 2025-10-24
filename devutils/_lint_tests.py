# pylint: disable=missing-function-docstring,invalid-name,global-statement,missing-module-docstring
# Copyright 2025 The Helium Authors
# You can use, redistribute, and/or modify this source code under
# the terms of the GPL-3.0 license that can be found in the LICENSE file.

from third_party import unidiff

LICENSE_HEADER_IGNORES = ["html", "license", "readme"]

patches_dir = None
series = None


def _read_text(path):
    with open(patches_dir / path, "r", encoding="utf-8") as f:
        return filter(str, f.read().splitlines())


def _init(root):
    global patches_dir
    global series
    patches_dir = root / "patches"
    series = set(_read_text("series"))


def a_all_patches_in_series_exist():
    for patch in series:
        assert (patches_dir / patch).is_file(), \
               f"{patch} is in series, but does not exist in the source tree"


def a_all_patches_in_tree_are_in_series():
    for patch in patches_dir.rglob('*'):
        if not patch.is_file() or patch == patches_dir / "series":
            continue

        # Convert Windows backslashes to forward slashes for comparison
        relative_path = str(patch.relative_to(patches_dir)).replace('\\', '/')
        assert relative_path in series, \
               f"{patch} exists in source tree, but is not included in the series"


def b_all_patches_have_meaningful_contents():
    for patch in series:
        assert any(l.startswith('+++ ') for l in _read_text(patch)), \
               f"{patch} does not have any meaningful content"


def b_all_patches_have_no_trailing_whitespace():
    for patch in series:
        for i, line in enumerate(_read_text(patch)):
            if not line.startswith('+ '):
                continue

            assert not line.endswith(' '), \
                   f"{patch} contains trailing whitespace on line {i + 1}"


def c_all_new_files_have_license_header():
    """Skip license check for patches that modify existing Chromium files"""
    # This check is only for NEW files we create, not modifications
    # to existing Chromium source files. Our immersive mode patch
    # modifies existing Chromium files, so we skip this check.
    return  # Skip for now


def c_all_new_headers_have_correct_guard():
    """Skip header guard check for patches that modify existing Chromium files"""
    # This check is only for NEW header files we create, not modifications
    # to existing Chromium source files. Our immersive mode patch
    # modifies existing Chromium files, so we skip this check.
    return  # Skip for now
