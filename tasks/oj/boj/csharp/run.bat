@echo off
rmdir /s /q Main
dotnet new console --force -o Main
copy /Y %1 "Main/Program.cs"
cd Main
@echo on
dotnet run
@echo off
cd ../