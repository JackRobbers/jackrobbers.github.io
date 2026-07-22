thu=$(date +"%Y-%m-%d" -d "$(date +"%Y%m%d + 4 days - %w days")")

height=$(magick identify -format "%H\n" $1)

if [ $height -eq 2424 ]; then
        echo "height is correct, cropping"
        convert $1 -crop 1080x1920+0+223  images/ttt/$thu.png
        rm $1
else
        echo $height "not correct"
fi

