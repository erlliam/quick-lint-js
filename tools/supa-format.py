#!/usr/bin/env python3

import subprocess


def main():
    file_paths = get_file_paths()

    for file_path in file_paths:
        if file_path.startswith("vendor/"):
            continue
        elif file_path.startswith("benchmark/benchmark-lsp/corpus/"):
            continue

        if file_path.endswith((".c", ".cpp", ".h")):
            subprocess.run(["clang-format", "-i", file_path])
        elif file_path.endswith((".html", ".css", ".js")):
            subprocess.run(["./node_modules/.bin/prettier", "--write", file_path])
        elif file_path.endswith((".py")):
            subprocess.run(["venv/bin/black", file_path])
        elif file_path.endswith((".go")):
            subprocess.run(["gofmt", "-w", file_path])
        elif file_path.endswith((".hs")):
            subprocess.run(["/home/altair/.local/bin/hindent", file_path])


def get_file_paths():
    file_paths_process = subprocess.run(
        [
            "git",
            "ls-files",
            "--cached",
            "--exclude-standard",
            #'--others'
        ],
        stdout=subprocess.PIPE,
    )
    file_paths = file_paths_process.stdout.decode("utf-8").split("\n")
    return file_paths


if __name__ == "__main__":
    main()
