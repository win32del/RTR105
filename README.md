# RTR105
Datormācibas kursa elektroniskā klade
    1  man uname - parāda lietotāja komandas
    2  uname - Operētājsistēmas nosaukums
    3  echo $0 - programmēšanas valodas dialekts
    4  echo 0$ - programmēšanas valoda
    5  whoami - parāda kas es esmu datorā
    6  who - parāda kas man atrodas blakus
    7  pwd - atrašanās vieta datorā
    8  ls - parāda publiski pieejamās mapes un failus
    9  man ls - manuālās grāmatas skaidrojums ls funkcijai
   10  ls -l - parāda plaši izklāstītu failu un mapju aprakstu
   11  ls -a - parāda visas mapes, kuras ir pieejamas uz datora.
   12  ls -la - parāda detalizētu informāciju par mapēm, to saturu, izveidošanas datumu, īpašnieku.
   13  clear - notīrīt darba virsmu
   history >> history_20180912.txt - izveidot teksta failu ar šodienas vēsturi
    
    

    9  cd Music - Mainit direktoriju
   17  cd . - solis direktorijaa uz vietas
   19  cd .. - pariet uz augstak stavosu mapi
   32  cd Home/Birthrepelant
   33  cd home
   35  cd home/user
   36  cd /home/birthrepelant/
   38  cd / - parvietoties uz pasu sakumu
   43  cd ~ - tikt uz majam
   50  mkdir rib - izveidot direktoriju
   58  rmdir rib/ - izdzest mapi
   70  rm -r - izdzest direktoriju neskatoties uz to, ka mape ir saturs
   77  echo  "text" - terminali pasaka ievadito tekstu
   79  echo "teksts
teksts
teksts" - pasaka tekstu vairakas rindas
   81  man echo
   82  echo -e "es\nes\nes" - pasaka tekstu vairakas rindas
   86  echo "best" > fails1.txt
   88  cat fails1.txt - pasaka faila saturu
   89  less fails1.txt  - pasaka faila saturu
   90  echo "best" > fails1.txt redige faila saturu uz ievadito
   95  more fails1.txt  - pasaka faila saturu
  103  nano fails1.txt - atver teksta redaktoru
  106  chmod 540 fails1.txt - izmaina faila pieejamibu
  118  mv *1*.txt Music/ - parvieto visus failus kas satur ierakstito simbolu uz noradito mapi
    4  nano skripts_mans_skripts.sh - izveidot sava skripta failu
    5  cat skripts_mans_skripts.sh parbaudit sava skripta faila saturu
   13  echo $PATH - parada visus celus uz galvenajam direktorijam
   14  ./skripts_mans_skripts.sh - palaist skriptu
   15  /home/user/skripts_mans_skripts.sh
   19  chmod 764 skripts_mans_skripts.sh - izmainit skripta faila ipasibas
   21  echo $PATH
   22  PATH=$PATH:/home/user - pievienot jaunu galveno celu
   27  git clone https://github.com/win32del/RTR105 - lejupieladet githuba repozitariju

print(123) - parāda ievadīto iekavās
print("yeeee") - Ar pēdiņām parāda tekstu
float(a) - pārveido nodefinēto simbolu par decimālou
int(a) - ārveido nodefinēto simbolu par skaitli
str(a) - ārveido nodefinēto simbolu par  vārdu vai burtu
10 % 9 = 1 - parāda atlikumu no dalījuma
2 ** 3 - kāpinājums
