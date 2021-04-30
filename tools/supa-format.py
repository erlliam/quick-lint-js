#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool


def main():
    file_paths = get_file_paths()
    subprocess_run_args = []

    for file_path in file_paths:
        if file_path.startswith("vendor/"):
            continue
        elif file_path.startswith("benchmark/benchmark-lsp/corpus/"):
            continue

        if file_path.endswith((".c", ".cpp", ".h")):
            subprocess_run_args.append(["clang-format", "-i", file_path])
        elif file_path.endswith((".html", ".css", ".js")):
            subprocess_run_args.append(
                ["./node_modules/.bin/prettier", "--write", file_path]
            )
        elif file_path.endswith((".py")):
            subprocess_run_args.append(["venv/bin/black", file_path])
        elif file_path.endswith((".go")):
            subprocess_run_args.append(["gofmt", "-w", file_path])
        elif file_path.endswith((".hs")):
            subprocess_run_args.append(["/home/altair/.local/bin/hindent", file_path])

    with Pool(8) as p:
        p.map(subprocess.run, subprocess_run_args)


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
