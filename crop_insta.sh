thu=$(date +"%Y-%m-%d" -d "$(date +"%Y%m%d + 4 days - %w days")")
convert $1 -crop 1080x1920+0+223  images/ttt/$thu.png
rm $1
