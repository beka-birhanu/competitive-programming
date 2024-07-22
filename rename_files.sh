#!/bin/bash

# Function to rename .txt files to .go
rename_txt_to_go() {
  local dir="$1"
  find "$dir" -type f -name "*.txt" | while read -r file; do
    local new_file="${file%.txt}.go"
    mv "$file" "$new_file"
    echo "Renamed $file to $new_file"
  done
}

# Call the function with the root directory
rename_txt_to_go "."
