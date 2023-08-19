declare -a rates=(0.01 0.05 0.1 0.5 1 5 10)

for r in ${rates[@]}
do
	gnuplot -e "set terminal png size 640,480; \
		set output '${r}_plot.png'; \
		set xlabel 'number of nodes'; \
		set ylabel 'height'; \
		plot '../data/plot_data/${r}-regular' u 2:1 smooth bezier \
		w lines t 'regular', \
		'../data/plot_data/${r}-alt' u 2:1 smooth bezier \
		w lines t 'alternating', \
		'../data/plot_data/${r}-lg' u 2:1 smooth bezier \
	 	w lines t 'list-grouped'"
done

