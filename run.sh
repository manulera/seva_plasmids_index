curl https://seva-plasmids.com/v2/data.js > data.js
cat data.js | sed -E 's/var json_data[[:space:]]*=[[:space:]]*//g' | sed -E 's/;\s*$//g'| jq '.' > index.json





