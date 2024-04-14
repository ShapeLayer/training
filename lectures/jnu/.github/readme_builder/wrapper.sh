for each in `find . ! -path . -type d -maxdepth 1`
do
    if [ "$each" != "./.github" ]
    then
        echo "$each"
        python3 ./.github/readme_builder/app.py "$each/manifest.toml" "$each/template.md" "$each/README.md" 2> /dev/null && echo "$each Done." || echo "$each Passed."
    fi
done
