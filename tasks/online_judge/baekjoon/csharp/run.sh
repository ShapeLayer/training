rm -rf Main
dotnet new console --force -o Main
cp $1 Main/Program.cs
cd Main
dotnet run
cd ../
