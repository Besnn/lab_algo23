declare -a rates=(0.01 0.05 0.1 0.5 1 5 10)

for r in ${rates[@]}
do
awk '{print $1, 10000}' ../data/${r}-10k_avg >> ${r}-regular
awk '{print $1, 5000}' ../data/${r}-5k_avg >> ${r}-regular
awk '{print $1, 1000}' ../data/${r}-1k_avg >> ${r}-regular


awk '{print $2, 10000}' ../data/${r}-10k_avg >> ${r}-alt
awk '{print $2, 5000}' ../data/${r}-5k_avg >> ${r}-alt
awk '{print $2, 1000}' ../data/${r}-1k_avg >> ${r}-alt

awk '{print $3, 10000}' ../data/${r}-10k_avg >> ${r}-lg
awk '{print $3, 5000}' ../data/${r}-5k_avg >> ${r}-lg
awk '{print $3, 1000}' ../data/${r}-1k_avg >> ${r}-lg

mv *regular *alt *lg ../data/plot_data
done

