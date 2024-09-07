# Psychology_Experiment
_This Codebase deals with a Vagus-Nerve Stimulation Experiment, conducted by [Manon Giraudier](https://www.uni-potsdam.de/de/emobio/team/manon-giraudier) at the Institute of Biological Psychology and Affective Science of the University of Potsdam in 2022. The further documentation of the Codebase is given below in German._

## Installation
* Python-Version: 3.9 

Die Installation von python-tk ist auf dem Zielsystem mit Unix vonnöten. 
Andere Abhängigkeiten müssen mit pip installiert werden.
```bash
pip install -r requirements.txt
```

## Benutzung
Für einen Durchlauf mit Encoding-Daten bitte nach der Installation folgenden Befehl verwenden:
```bash
python -c 'import Main; Main.run_build_encoding_table()'
```
Für Recognition-Daten erfolgt der analoge Befehl:
```bash
python -c 'import Main; Main.run_build_recognition_table()'
```
Sollen sowohl die Encoding- als auch die Recognition-Daten in eine einheitliche Tabelle gebündelt werden, so gilt der folgende Befehl:
```bash
python -c 'import Main; Main.run_build_unified_table()'
```
_Hinweis: Bei der gebündelten Tabelle gibt es nachfolgend eine Abfrage für den Stimuluslisten-Pfad, 2 Abfragen für die Encoding- und 2 Abfragen für die Recognition-Pfade. Sollen nicht .csv sondern .xlsx -Dateien ausgegeben werden, so sind für die vorigen Befehle noch das Argument "excel" einzufügen._
___
In dieser Readme wird erst kurz der Experimentablauf beschrieben, die Benutzerführung, sowie die allgemeine und die technische Struktur des Programms.

## Ablauf des Experiment:
Das Experiment zur Vagusnerv Stimulation ist in zwei Teile unterteilt, A und B. Diese unterteilen sich in nochmals in je zwei Versuche. Diese Versuche sind in das „Encoding“ und das „Recognition“.
Das „Encoding“ erfolgt im Labor. Das „Recognition“ führt der Proband 24-48 Stunden später am eigenen Rechner aus.
Bei dem „Encoding“ werden erst Gesichtsausdrücke Stimmungen zu geordnet und anschließend werden Worte Stimmungen zugeordnet.
Bei dem „Recognition“ versucht die Versuchsperson eben jene Gesichtsausdrücke und anschließend die Worte aus dem "Encoding" wieder zu erkennen und auf einer Skala von 1-11 anzugeben wie sicher sie sich der Antwort ist. 
Alle Werte werden dabei in .txt-Dateien gespeichert. Meta-Informationen über die Probanden sind in  .csv und .xlsx Dateien hinterlegt. 
Das in diesem Rahmen entwickelte Programm liest die Dateien ein, ordnet die gefundenen Daten den Probanden und den Stimuli zu und gibt sie in einer großen Tabelle aus.


## Benutzerführung des Programmes für die Ausführung:
Im Folgenden wird der Ablauf der Benutzerführung des Programmes anhand des Beispiels für das Encoding (Recognition funktioniert analog). 
Der Benutzer wird nacheinander aufgefordert mehrere Verzeichnisse auszuwählen. 
Bei der 1. Aufforderung soll das Verzeichnis, in dem die Stimuli Listen abgelegt sind, angegeben werden.
Bei der 2 Aufforderung soll das Verzeichnis, in dem die Datei Encodings Teil A (bzw. Recognition A) abgelegt ist, angegeben werden.
Bei der 3 Aufforderung soll das Verzeichnis, in dem die Datei Encodings Teil B (bzw. Recognition B) abgelegt ist, angegeben werden. 
Bei der 4. Aufforderung soll das Verzeichnis gewählt werden in dem die Ausgabe Tabelle abgelegt wird.


## Allgemeine Struktur:
Zu Beginn liest das Programm aus dem Verzeichnis der Stimulilisten alle Daten ein. D.h. die Bezeichnungen für „Faces“ und „Words“ werden aus den Listen für das Encoding und Recognition, hierbei jeweils für Faces und Words innerhalb dessen für die Teile A und B in jeweils eigenen Tabellen zwischengespeichert. Es entstehen also 8 Tabellen.
Anschließend werden aus dem Verzeichnis Encoding (Recognition) die Meta-Daten der Versuchsperson, entsprechend auch die hinterlegten Datensätze für das Encoding und Reconition, bzw. auch die Versuchspersons-Nummern, eingelesen. Diese Daten sind strukturiert nach den Versuchspersonen, und innerhalb dessen nach den Encoding und den Recognition-Werten. Auch Einträge von Versuchspersonen, die nicht alle Teilexperimente abgeschlossen haben, werden berücksichtigt.
Die einzelnen Versuchsdaten werden dann eingelesen. Der Schritt des Verbindens der Versuchsperson-Daten und der Stimuluslisten erfolgt danach und erfolgt zunächst für jede Versuchsperson einzeln. Somit wird eine Unabhängigkeit der Daten für jede Versuchsperson hergestellt, eigene Tabellen könnten entsprechend auch für jede Person ausgegeben werden. Abschließend werden alle Daten zusammengeführt und es entsteht, je nach Programmaufruf, eine gesamte Zieltabell für das Encoding oder das Recognition. 
Diese Tabelle kann wahlweise als .csv oder als .xlsx Datei ausgegeben werden.

## Technische Struktur:
Die Datenverarbeitung erfolgt vorrangig mit Panda-Dataframes. Darüber werden die Dateien eingelesen und verarbeitet. Für die Zuordnung und Ausgabe der Meta-Daten, der Stimulus-Listen werden auf den Panda Datarames Operation durchgeführt.
Die Strukturierung der eingelesenen und verarbeiteten Daten erfolgt aufgeschlüsselt nach Versuchspersonen, Dateityp und Versuchsdurchführung. Hierfür werden als Dateityp Python-Dictionaries verwendet, die eine effiziente und simple Umsetzung von Hashmaps mit Schlüssel- und Werte-Paaren ist. 
