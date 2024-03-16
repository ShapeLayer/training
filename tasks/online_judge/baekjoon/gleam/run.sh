rm -rf main
gleam new main
cp $1 main/src/main.gleam
cd main
gleam run
cd ../
