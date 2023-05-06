rm -rf Main
dotnet new console --language "VB" --force -o Main
cp $1 Main/Program.vb
cd Main
dotnet run
cd ../
