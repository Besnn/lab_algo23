awk '{ sum1 += $1; sum2 += $2; sum3 += $3; n++ } END { if (n > 0) print sum1 / n, sum2 /n, sum3 / n }'
