#!/usr/bin/env python3

import subprocess


illegal_paths = [
  'vendor/',
  'Formula/',
  '.github/',
  '.cmake/',
  '.docs/',
  '.po/',
]


def main():
  file_paths = filter_file_paths(get_file_paths())
  print(file_paths)


def get_file_paths():
  file_paths_process = subprocess.run([
    'git', 'ls-files', '--cached', '--exclude-standard',# '--others',
  ], stdout=subprocess.PIPE)

  file_paths = file_paths_process.stdout.decode('utf-8').split('\n')

  return file_paths


def filter_file_paths(file_paths):
  clean = []

  for file_path in file_paths:
    for illegal_path in illegal_paths:
      if file_path.startswith(illegal_path):
        break
      else:
        clean.append(file_path)
        break
        
  return clean


# for file_path in file_paths:
#   if file_path.endswith(('.c', '.cpp', '.h')):
#     subprocess.run(['clang-format', '-i', file_path])
#   elif file_path.endswith(('.html', '.css', '.js')):
#     subprocess.run(
#       ['npx', 'prettier', '--write', file_path],
#       stdout=subprocess.DEVNULL
#     )
#   elif file_path.endswith(('.py')):
#     print('python black bullshit')
#   elif file_path.endswith(('.go')):
#     print('go gofmt bullshit')
#   elif file_path.endswith(('.hs')):
#     print('haskell hindent bullshit')
#     #subprocess.run(['hindent', file_path])

if __name__ == '__main__':
  main()
