#! /bin/bash

echo "Do you want to play Rock Paper Scissors?"
read play

if [ $play == "yes" ]
then 
    python3 RSP.py
else
    echo "That's too bad, maybe next time"
fi
