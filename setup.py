from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

executables = [
    Executable('rsb.py', 'Console')
]

setup(name='Ryouba Soundboard',
      version = '1.0',
      description = 'Simple soundboard',
      options = dict(build_exe = buildOptions),
      executables = executables)
