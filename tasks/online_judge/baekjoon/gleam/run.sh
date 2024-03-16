rm -rf main
gleam new main
cp $1 main/src/main.gleam
cd main
gleam add gleam_erlang
gleam run
cd ../
