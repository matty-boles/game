import cx_Freeze

executables = [cx_Freeze.Executable("my-first-game.py")]

cx_Freeze.setup(
    name="Minion CRash",
    options={"build_exe": {"packages":["pygame"]
                           ,"include_files":["minion3.xcf"] }},
    executables = executables
)