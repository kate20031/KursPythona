/usr/bin/time -v python program1.py 1000000 1500000 2>&1 1>/dev/null | grep  -E "wall|Max"
 perl -p -e "s/# Wersja2 //" program1.py > program2.py
 /usr/bin/time -v python program2.py 1000000 1500000 2>&1 1>/dev/null | grep  -E "wall|Max"
rm program2.py
