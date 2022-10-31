#!/bin/bash
#
# нарезает большой файл на файлы разбиения файл_part[1,2,3...N]
# с копированием или без первой строки с заголовками
#


if [ "$1" = "" ] 
then
    echo "cutter.sh [имя файла] [количество разбиений, наприимер 3] [копирование 1ой строки, 0-нет или 1-да]" 
else
    echo "обрабатываем файл: $1"
    TotalLines=$(cat "$1" | wc --lines)
    Parts=$2
    let "LinesInPart = TotalLines / Parts + 1"
    echo "Строк в файле: $TotalLines Частей: $Parts Строк в части: ~$LinesInPart"
    
    BeginLine=1
    for (( i=1; i <= $Parts; i++ ))
    do
        let "EndLine = BeginLine + LinesInPart"
        fileout=$1"_part"$i
        echo "Создаем $fileout"
        
        diap="$BeginLine,$EndLine p"
        
        if [ "$3" == "0" ]
        then
            rm $fileout
        else
            if [ $i -ne 1 ] 
            then
                head -n 1 $1 > $fileout
            else
                rm $fileout
            fi
        fi
        
        sed -n "$diap" $1 >> "$fileout"
        let "BeginLine = EndLine + 1"
    done
    
fi

# вероятно следующий подход будет работать быстрее:
#exec 0< testfile
#count=1
#while read line
#do
#echo "Line #$count: $line"
#count=$(( $count + 1 ))
#done

