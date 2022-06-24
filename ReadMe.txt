In dieser Readme wird erst kurz der Experimentablauf beschrieben, die Benutzerführung, sowie die allgemeine und die technische Struktur des Programms.

Ablauf des Experiment:

Das Experiment zur Vagusnerv Stimulation ist in zwei Teile geteilt A und B. Diese unterteilen sich in nochmals in je zwei Versuche. Diese Versuche sind in das „Encoding“ und das „Recognition“.
Das „Encoding“ erfolgt im Labor. Das „Recognition“ führt der Probandn 24-48 Stunden später am eigenen Rechner aus.
Bei dem „Encoding“ werden erst Gesichtsausdrücke Stimmungen zu geordnet und anschließend werden Worte Stimmungen zu geordnet.
Bei dem „Recognition“ versucht die Versuchsperson Gesichtsausdrücke wieder zu erkennen und auf einer Skaler von 1-11 anzugeben wie sicher sie sich der Antwort ist. 
Dann sollen die Versuchsperson Worte wieder erkennen und auch da auf einer Skaler von 1-11 an geben wie sicher sie sich der Antwort ist. 
Alle Werte werden dabei in .txt , .csv und .xlsx Dateien gespeichert. 
Das Programm ließt die Dateien ein, wandelt diese um und gibt sie in einer großen Tabelle aus.


Benutzerführung des Programmes für die Ausführung:

Im folgenden wird der Ablauf der Programm-Aufforderungen geklärt fürs Encoding (Recognition funktioniert Analog). 
Der Benutzer wird nacheinander aufgefordert mehrere Verzeichnisse auszuwählen. 
Bei der 1. Aufforderung soll das Verzeichnis, in dem die Stimuli Listen abgelegt sind, angegeben werden.
Bei der 2 Aufforderung soll das Verzeichnis, in dem die Datei Encodings Teil A (Recognition A) abgelegt ist, angegeben werden.
Bei der 3 Aufforderung soll das Verzeichnis, in dem die Datei Encodings Teil B (Recognition B) abgelegt ist, angegeben werden. 
Bei der 4. Aufforderung soll das Verzeichnis gewählt werden in dem die Ausgabe Tabelle abgelegt wird.


Allgemeine Struktur:

Zu beginn liest das Programm aus dem Verzeichnis der Stimuli Listen alle Daten ein. D.h. die Bezeichnungen für „Faces“ und „Words“ werden aus den Listen mit der entsprechenden Codierung und den Teilen A und B in einer Tabelle zwischen gespeichert.
Anschließend werden aus dem Verzeichnis Encoding (Recognition) die Meta-Daten der Versuchsperson, sowie die Daten der Experimente mit der Auswahl der Stimuli eingelesen, nach Versuchsperson den Teilen A und B geordnet und zwischen gespeichert. 
Sind Daten nicht vorhanden, werden diese mit „NaN“ in der Tabelle bezeichnet.
Anschließend wird die Zieltabelle erstellt. Das Programm ordnet aus den Zwischenspeicher den Tabellen die Daten den entsprechenden Feldern zu, dass für alle Probanden und gibt zum Ende eine .csv oder .xlsx Tabelle aus.


Technische Struktur:

Die Datenverarbeitung erfolg mit Panda Dataframes. Darüber werden die Dateien eingelesen, verarbeitet und gereinigt (keine dupleten). Für die Zuordnung und Ausgabe der Meta-Daten, der Stimulus-Listen werden auf den Panda Datarames Operation durchgeführt.
Zur Erhaltung der Ordnung in den Programm werden Hashmaps aus der Python Libary verwendet. Dabei nutzt das Programm zur Ordnung die Versuchsperson Nummer (VP).
