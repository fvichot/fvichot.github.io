#!/bin/bash
shopt -s nullglob nocaseglob
DIR=$1
if [ ! -d "$DIR" ]
then
  echo "I need a photos directory, mate."
  exit 1
fi

TRIPFILE=$2
if [ ! -f "$TRIPFILE" ]
then
  echo "I need a trip file, mate."
  exit 2
fi
cp $TRIPFILE ${TRIPFILE}.bak

for PIC in $DIR/*.jpg
do
  NAME=$(basename $PIC)
  COMMENT=$(exiftool -S -caption-abstract $PIC | cut -c 19-)
  if [ -z "$COMMENT" ]
  then
    # Don't erase existing comments with nothing
    continue
  fi
  echo "Setting comment on $NAME..."
  sed -i '' -E "s/^$NAME($| .*$)/$NAME $COMMENT/g" $TRIPFILE
done
