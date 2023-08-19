for i in $(ls ../data/)
do
touch "../data/${i}_avg"; echo $(./avg.awk < ../data/$i) > "../data/${i}_avg"
done
