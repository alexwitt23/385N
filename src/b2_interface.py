"""Module for downloading image dumps from Backblaze B2."""

import pathlib
import subprocess
import tempfile

_CACHE_DIR = pathlib.Path("cached_data")


def download_archive(archive_name: str) -> pathlib.Path:
    """Download an archive from the B2 storage."""

    # Assert this archive must be .tar.zst compressed
    assert archive_name.rsplit(".")[-2:] == ["tar", "zst"]

    # Save path for the _extracted archive_
    save_path = _CACHE_DIR / archive_name.replace(".tar.zst", "")
    if save_path.is_dir():
        return save_path
    else:
        return _download_archive_impl(archive_name, save_path)


def _download_archive_impl(archive_name: str, save_path: pathlib.Path) -> bool:

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_dir = pathlib.Path(tmp_dir)
        tmp_save_path = tmp_dir / archive_name
        subprocess.call([
            "b2", "download-file-by-name", "data-upload", archive_name,
            tmp_save_path
        ])
        if not tmp_save_path.is_file():
            raise ValueError(f"{archive_name} not properly downloaded!")

        subprocess.call(
            ["tar", "-I", "zstd", "-xf", tmp_save_path, "-C", save_path])

    return save_path
