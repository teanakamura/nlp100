f1 = open("./nlp100/hightemp.txt", 'r')
f2 = open("./nlp100/hightemp_11.txt", 'w')   #本当はファイルを二つ用意せずにr+で実行する。
f2.write(f1.read().replace("\t", " "))
f1.close
f2.close


# Unix command
# expand -t 1 ./nlp100/hightemp.txt > ./nlp100/hightemp_11u1.txt
# tr "\t" " " < ./nlp100/hightemp.txt > ./nlp100/hightemp_11u2.txt
# sed -e 's/[[:space:]]/ /g' ./nlp100/hightemp.txt > ./nlp100/hightemp_11u3.txt
# sed -e $'s/\t/ /g' ./nlp100/hightemp.txt > ./nlp100/hightemp_11u3.txt
# sed -e 's/\t/ /g' ./nlp100/hightemp.txt > ./nlp100/hightemp_11u3.txt はタブ認定されないので注意
