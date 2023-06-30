# text_to_speech


Pour exécuter ce script, vous devez d'abord d'abord installer avec le code suivant "pip install pyttsx3"

pyttsx3 est une bibliothèque de conversion texte-parole en Python. Contrairement aux bibliothèques alternatives, il fonctionne hors ligne.

Configuration requise pour l'installation de Linux: Si vous etes sur un système Linux et si la sortie vocale ne fonctionne pas:
    Installez espeak, ffmpeg et libespeak1 comme indiqué ci-dessous:

    sudo apt update && sudo apt install espeak ffmpeg libespeak1

#############################################################################################
#############################################################################################
Version optimisé "corrected_version_main.py":

Dans cette version optimisée, j'ai ajouté une fonction "configure_engine" pour centraliser la configuration de l'objet "engine de pyttsx3". 
Cela permet de régler le volume, le taux de parole et la voix une seule fois, plutôt que de le faire à chaque exécution de la fonction "reader_name".

De plus, j'ai déplacé l'initialisation de l'objet engine à l'intérieur de la fonction reader_name. 
Cela garantit que chaque fois que la fonction est appelée, un nouvel objet engine est créé et correctement configuré. 
Cela évite également d'appeler "engine.runAndWait()" et "engine.stop()" à chaque exécution du programme, ce qui peut améliorer les performances.

Enfin, j'ai retiré l'importation inutile du module "pyttsx3" en haut du programme, puisqu'il est maintenant importé à l'intérieur de la fonction reader_name.


#############################################################################################
#############################################################################################


Pour plus d'informations: etienneselemani47@gmail.com

SelemDev