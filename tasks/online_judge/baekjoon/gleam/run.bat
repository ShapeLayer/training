@echo off
rmdir /s /q main
gleam new main
copy /Y %1 "main/src/main.gleam"
cd main
@echo on
gleam add gleam_erlang
gleam run
@echo off
cd ../
