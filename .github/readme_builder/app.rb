require 'rugged'
require 'linguist'

# Load Linguist
repo = Rugged::Repository.new('../../')
project = Linguist::Repository.new(repo, repo.head.target_id)

# Prepare base values
stats = project.languages      #=> { "Ruby" => 119387 }
stats = stats.sort_by { |_key, value| -value }.to_h
total = project.languages.values.sum

# Build statistics
language_stats = []
stats.each do | language, value |
  language_stats += ["%s%.2f%%" % [ language.ljust(20, "."), (value.to_f/total.to_f)*100 ]]
end
body = language_stats.join("\n")

# Build README using template
template = File.read('template.md')
template["{ language_stats }"] = body
File.write("../../README.md", template)
