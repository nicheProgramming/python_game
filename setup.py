import cx_Freeze

executables = [
    cx_Freeze.Executable("my_game.py")
]

cx_Freeze.setup(
    name="Slither",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["apple.png", "snakehead.png"]}},
    description="Sliter Game Tutorial",
    executables=executables
)
