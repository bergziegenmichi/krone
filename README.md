# SKRIPT ZUM AUSFÜLLEN EINER KRONE-UMFRAGE
Unsere liebe Kronenzeitung hat eine Umfrage veröffentlicht: [https://www.krone.at/2560444][0]
Es geht darum ob man die heutigen Demos in Wien gerechtfertigt findet.

Diese Umfrage wird wahrscheinlich morgen am Titelblatt sein, vertritt jedoch nicht die Mehrheit Österreichs.
Deshalb bitte ich euch dieses Skript ein wenig laufen zu lassen um das Ergebnis in die andere Richtung zu drücken.
Danke euch!

## Verwendung
Man benötigt: python, selenium, geckodriver, Internetverbindung
Selenium (python Bibliothek) installiert man mit ```pip install selenium```
Den geckodriver bekommt man hier: [https://github.com/mozilla/geckodriver/releases][1]

Danach dieses Skript herunterladen und öffnen. Zeilen 11 und 12 bearbeiten.
Ausführen mit ```python main.py```

Dies kann man auch mehrfach parallel ausführen ;)

## Funktionsweise
Die Website verwendet cookies um zu speichern ob die Umfrage durchgeführt wurde.
Deshalb ist es möglich durch das Löschen der cookies mehrmals abzustimmen.


Inspiriert durch diesen [Reddit post][2]

[0]: https://www.krone.at/2560444
[1]: https://github.com/mozilla/geckodriver/releases
[2]: https://www.reddit.com/r/Austria/comments/qye13a/also_was_die_schwurbler_k%C3%B6nnen_k%C3%B6nnen_wir_schon/?utm_medium=android_app&utm_source=share
