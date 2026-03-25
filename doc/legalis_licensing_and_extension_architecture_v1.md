# Legalis – Licensing and Extension Architecture v1

## Zweck dieses Dokuments

Dieses Dokument beschreibt das Lizenz-, Signatur- und Erweiterungsmodell von **Legalis v1**.
Es konkretisiert die bereits in Projektfahrplan und Module Catalog angelegte Trennung zwischen **Core**, **Configuration** und **Extensions** und definiert einen schlanken technischen Rahmen für:

- Open-Core-Auslieferung
- Premium- und Enterprise-Erweiterungen
- Schutz offizieller Standardprozesse
- Offline-fähige Lizenzierung ohne permanenten Lizenzserver
- zeitlich befristete Abo-Freischaltungen
- Auditierbarkeit lizenz- und paketbezogener Entscheidungen

Das Dokument ist als Architekturgrundlage gedacht. Es ersetzt noch keine Implementierungsspezifikation, legt aber verbindliche Leitlinien fest.

---

## 1. Ausgangslage und Zielsetzung

Legalis soll langfristig als **standardorientiertes Betriebsmodell für brasilianische Kanzleien** aufgebaut werden. Gleichzeitig muss das Produkt wirtschaftlich paketierbar bleiben. Daraus ergeben sich zwei Anforderungen:

1. Der Basiskern soll klar, offen, nachvollziehbar und erweiterbar sein.
2. Premium- und Enterprise-Mehrwert soll kontrolliert ausgeliefert und nicht durch triviale lokale Konfigurationsänderungen freischaltbar sein.

Da Legalis zunächst **keinen permanent verfügbaren Lizenzserver** betreiben soll, muss die Lösung bewusst **offline-first** funktionieren.

---

## 2. Grundmodell

### 2.1 Architekturprinzip

Legalis folgt für Lizenzierung und Paketierung dem Modell:

> **Open Core + signierte kommerzielle Erweiterungen + signierte offizielle Fachartefakte**

### 2.2 Kernaussage

Nicht der gesamte Code wird geschützt, sondern vor allem:

- autorisierte Premium-/Enterprise-Erweiterungen
- offizielle Standardprozess-Pakete
- Governance-relevante Freischaltungen
- kontrollierte Änderungsrechte an geschützten Standardartefakten

### 2.3 Nicht-Ziel

Dieses Modell garantiert **keinen absoluten Kopierschutz** auf fremder Hardware. Es soll stattdessen:

- Missbrauch erschweren
- autorisierte von nicht autorisierten Erweiterungen technisch trennen
- Abo-Nutzung zeitlich sauber begrenzen
- Standardprozesse vor unkontrollierter Veränderung schützen
- belastbare Auditspuren liefern

---

## 3. Auslieferungsmodell

## 3.1 OSS-Core

Der OSS-Core enthält nur die Bestandteile, die für ein lauffähiges Grundsystem notwendig sind:

- Basismodelle
- Rollen- und Audit-Kern
- Konfigurationssystem
- Plugin-Loader
- Workflow-Runtime-Grundgerüst
- Signatur- und Lizenzprüfung
- APIs und Extension Points
- Standardpaket ohne Premium-spezifische Businesslogik

Der Core darf keine triviale interne Freischaltung für Premium oder Enterprise durch einfache Flags enthalten.

## 3.2 Kommerzielle Erweiterungspakete

Premium- und Enterprise-Funktionen werden als **separate Erweiterungspakete** ausgeliefert, zum Beispiel:

- `legalis-premium-workflow`
- `legalis-premium-knowledge`
- `legalis-premium-finance-reporting`
- `legalis-enterprise-governance`
- `legalis-enterprise-connectors`

Diese Pakete werden **nicht Bestandteil** des Open-Source-Kerns.

## 3.3 Signierte Fachartefakte

Zusätzlich zu Codepaketen können auch fachliche Artefakte separat paketiert und signiert werden, insbesondere:

- offizielle Standardprozesse
- Vorlagenbibliotheken
- Clause Libraries
- Connector-Definitionen
- Governance-Policies
- Freischalt- oder Unlock-Tokens

---

## 4. Lizenzierungsprinzip

## 4.1 Kein permanenter Lizenzserver

Legalis soll im Grundmodell **ohne dauerhaften Online-Lizenzserver** funktionieren.

Dafür werden signierte Dateien verwendet, die lokal importiert und vom System mit einem eingebetteten öffentlichen Schlüssel geprüft werden.

## 4.2 Zwei-Ebenen-Modell

Zur Trennung von Grundberechtigung und laufender Abo-Nutzung werden zwei Ebenen eingeführt:

### A. Base License
Definiert die grundsätzliche Berechtigung eines Kunden.

Typische Inhalte:

- `license_id`
- `customer_id`
- `edition`
- erlaubte Module
- zulässige Sitzanzahl oder Organisationsgröße
- Gültigkeitszeitraum der Basislizenz
- optionale Installationsbindung
- Signatur

### B. Subscription Lease
Definiert die **aktuell aktive**, zeitlich begrenzte Nutzungsfreigabe für abonnierte Module.

Typische Inhalte:

- `lease_id`
- `customer_id`
- freigeschaltete Abo-Module
- `valid_from`
- `valid_until`
- optionale Grace Period
- Signatur

### Technische Bedeutung

Ein Premium- oder Enterprise-Modul darf **nur dann geladen werden**, wenn:

1. das Paket selbst gültig signiert ist,
2. die Base License das Modul grundsätzlich erlaubt,
3. eine gültige Lease für den aktuellen Zeitraum vorliegt.

Damit bleibt das Paket zwar lokal installierbar, aber nicht dauerhaft lauffähig.

---

## 5. Signaturmodell

## 5.1 Signaturalgorithmus

Für Lizenzen, Leases, Paketmanifeste und Prozesspakete wird **Ed25519** als Standardsignaturverfahren verwendet.

Begründung:

- modern und effizient
- kleine Schlüssel und Signaturen
- gute Bibliotheksunterstützung
- für den vorgesehenen Zweck technisch angemessen

## 5.2 Schlüsselhierarchie

Empfohlen wird eine kleine, klare Schlüsselhierarchie:

- **Root Key**: nur offline aufbewahren, nicht im Tagesbetrieb nutzen
- **License Signing Key**: für Base Licenses und Leases
- **Package Signing Key**: für Erweiterungspakete
- **Process Pack Signing Key**: für offizielle Prozess- und Policy-Pakete

Der OSS-Core enthält nur die zugehörigen **Public Keys**.

## 5.3 Vertrauensmodell

Private Schlüssel verlassen niemals die kontrollierte Herausgeberumgebung.
Der Kunde erhält nur:

- signierte Dateien
- Prüfroutinen im Core
- keine Möglichkeit, gültige neue Signaturen selbst zu erzeugen

---

## 6. Paket- und Plugin-Modell

## 6.1 Plugin Loader

Der Core enthält einen Plugin Loader, der Erweiterungspakete aus einem definierten Verzeichnis oder Registry-Mechanismus lädt.

Ein Paket wird nur registriert, wenn alle folgenden Prüfungen erfolgreich sind:

1. Paket vorhanden
2. Manifest vorhanden
3. Hashes konsistent
4. Signatur gültig
5. API-/Core-Kompatibilität gegeben
6. Base License erlaubt das Modul
7. Lease erlaubt den aktuellen Betrieb

## 6.2 Manifest-Struktur

Jedes Erweiterungspaket enthält mindestens ein Manifest mit:

- Paketname
- Modul-ID
- Paketversion
- Ziel-API-Version
- Hashwerten relevanter Artefakte
- Exportpunkten / Registrierungsfunktion
- erforderlicher Edition
- Signatur

## 6.3 Verhalten bei Fehlschlag

Schlägt eine Prüfung fehl, gilt:

- Paket wird nicht geladen
- zugehörige API-Routen werden nicht registriert
- UI-Elemente des Pakets erscheinen nicht
- ein Audit-Eintrag wird erzeugt
- ein administrativer Hinweis wird angezeigt

---

## 7. Standardprozesse und Custom Extensions

## 7.1 Grundsatz

Legalis unterscheidet strikt zwischen:

- **offiziellen Standardprozessen**
- **kundenspezifischen Erweiterungen / Custom Extensions**

## 7.2 Offizielle Standardprozesse

Offizielle Standardprozesse sind:

- Teil eines signierten Prozesspakets
- als `origin = legalis_standard` gekennzeichnet
- versioniert
- schreibgeschützt
- nur unter kontrollierten Bedingungen austauschbar oder ersetzbar

## 7.3 Kundenspezifische Prozesse

Kundenspezifische Prozesse sind:

- als `origin = customer_extension` gekennzeichnet
- frei anpassbar im erlaubten Modellrahmen
- klar von offiziellen Standardprozessen getrennt
- separat versionierbar

## 7.4 Ziel dieser Trennung

Diese Trennung soll sicherstellen, dass:

- Referenzprozesse nachvollziehbar bleiben
- offizielle Standardprozesse nicht stillschweigend verfälscht werden
- kundenspezifische Abweichungen technisch sichtbar sind
- Support und Governance sauber differenzieren können

---

## 8. Unlock Tokens für geschützte Änderungen

## 8.1 Zweck

Bestimmte geschützte Aktionen dürfen nicht allein durch Rollenrechte im System freigeschaltet werden. Stattdessen kann Legalis dafür signierte **Unlock Tokens** vorsehen.

Beispiele:

- Bearbeitung eines offiziellen Standardprozesses
- Freischaltung eines speziellen Connector-Pakets
- zeitlich begrenzter Zugriff für Consultants / Partner
- Pilotzugriff auf Enterprise-Funktionen

## 8.2 Eigenschaften

Ein Unlock Token enthält mindestens:

- Token-Typ
- Kunde / Zielinstallation
- erlaubte Aktion
- Scope
- Gültigkeitszeitraum
- optionale Nutzungsbegrenzung
- Signatur

## 8.3 Bedeutung

Unlock Tokens ermöglichen feingranulare Freischaltungen ohne permanenten Serverbetrieb.

---

## 9. Abo-Schutz ohne Dauer-Lizenzserver

## 9.1 Problemstellung

Wird ein Premium-Paket dauerhaft lokal ausgeliefert, könnte ein Kunde sonst einmal abonnieren, das Paket installieren und danach versuchen, es ohne weitere Zahlung weiterzunutzen.

## 9.2 Lösung

Abo-Module werden technisch nur über **kurzlebige Subscription Leases** aktiviert.

Die Installation eines Pakets allein genügt nicht.

## 9.3 Laufzeitregel

Ein abonnierter Premium-Baustein darf nur laufen, wenn eine **aktuelle, signierte Lease** vorhanden ist.

Empfehlung:

- Laufzeit pro Lease: 30 Tage
- optionale Grace Period: 7 bis 14 Tage
- nach Kündigung oder Nichtverlängerung wird keine neue Lease mehr ausgestellt

## 9.4 Verhalten nach Ablauf

Nach Ablauf einer Lease gilt:

- Premium-Modul wird nicht mehr aktiv geladen
- bestehende Daten bleiben erhalten
- betroffene Funktionen wechseln in **read-only** oder **deaktiviert**
- keine destruktive Datenlöschung
- keine Sperre des Gesamtsystems

Damit bleibt das System operativ sauber und rechtlich weniger angreifbar.

---

## 10. Audit und Nachvollziehbarkeit

Lizenz- und Paketentscheidungen müssen im Audit nachvollziehbar sein.

Zu protokollieren sind mindestens:

- Import und Aktivierung von Base Licenses
- Import und Aktivierung von Subscription Leases
- Laden oder Ablehnen von Erweiterungspaketen
- Signaturfehler
- Ablauf von Leases
- Verwendung von Unlock Tokens
- Änderung oder Austausch geschützter Standardprozesse

Diese Ereignisse sind sowohl technisch als auch administrativ relevant.

---

## 11. Optionaler nativer Verify-Kern

## 11.1 Ziel

Kritische Prüffunktionen können optional in eine kleine native Bibliothek ausgelagert werden, etwa in **C** oder **Rust**.

## 11.2 Geeignete Funktionen

Sinnvoll auslagerbar sind insbesondere:

- Signaturprüfung
- Hash-Prüfung
- Manifest-Validierung
- Lizenz- und Lease-Parsing mit strikter Validierung

## 11.3 Nicht-Ziel

Die native Bibliothek ist **kein DRM-Ersatz** und keine absolute Sicherheitsgrenze. Sie dient lediglich dazu,

- den kritischen Prüfpfad klein zu halten
- triviales Monkeypatching etwas zu erschweren
- den Trusted Computing Core klarer abzugrenzen

---

## 12. Datenhaltungsmodell (konzeptionell)

Für die Umsetzung werden mindestens folgende persistente Objekte empfohlen:

### `installed_license`
- license_id
- customer_id
- edition
- valid_from
- valid_until
- signature_valid
- raw_payload
- installed_at

### `subscription_lease`
- lease_id
- customer_id
- module_scope
- valid_from
- valid_until
- grace_until
- signature_valid
- installed_at

### `installed_extension`
- module_id
- package_version
- package_hash
- signature_valid
- loaded_state
- installed_at

### `process_registry`
- process_id
- process_version
- origin
- source_package
- signature_valid
- locked_state
- active_state

### `authorization_token`
- token_id
- token_type
- scope
- valid_from
- valid_until
- signature_valid
- used_at

### `audit_entry`
- actor
- event_type
- object_type
- object_id
- result
- reason
- metadata
- created_at

---

## 13. Bedrohungsmodell und realistische Grenzen

Dieses Architekturmodell schützt gut gegen:

- triviale UI-Freischaltung über Konfiguration
- bloßes Setzen eines Feature-Flags
- Nachinstallieren unsignierter Pakete
- stillschweigende Manipulation offizieller Standardprozesse
- naive Dauernutzung eines abgelaufenen Abo-Moduls

Es schützt **nicht absolut** gegen:

- Root-Zugriff auf die Kundeninstallation
- hartes Patchen von Interpreter, Laufzeit oder Binärmodulen
- vollständige Forks des Open-Source-Kerns
- eigenständige Nachimplementierung offener Schnittstellen durch Dritte

Das Modell ist daher als **wirtschaftlich vernünftige Kontrollarchitektur**, nicht als absoluter Kopierschutz zu verstehen.

---

## 14. Implementierungsprioritäten

## 14.1 Für MVP / frühe Produktphase

Unbedingt umsetzen:

1. Plugin Loader im Core
2. Ed25519-Prüfung für Lizenzdateien
3. signierte Erweiterungsmanifeste
4. signierte Prozesspakete
5. strikte Herkunftskennzeichnung `legalis_standard` vs. `customer_extension`
6. Audit für Lizenz-, Lease- und Paketentscheidungen

## 14.2 Für Phase 2

Danach ergänzen:

1. Unlock Tokens
2. Partner-/Consultant-Zertifikate
3. signierte Connector-Pakete
4. signierte Policy Bundles
5. optionaler nativer Verify-Kern

## 14.3 Vorläufig nicht priorisieren

Nicht priorisieren:

- permanenten 24/7-Lizenzserver
- aggressive Obfuskation als Hauptschutz
- Hardware-Dongles
- komplexe Remote Attestation
- destruktive Sperrmechanismen bei Abo-Ende

---

## 15. Architekturentscheidung v1

Für Legalis v1 gilt vorläufig folgende Architekturentscheidung:

> **Legalis wird als Open-Core-System mit signierten Premium-/Enterprise-Erweiterungen, signierten offiziellen Prozesspaketen und offline importierbaren, kryptographisch verifizierbaren Lizenz- und Lease-Dateien aufgebaut.**

> **Ein Abonnement wird nicht allein durch Installation eines Moduls wirksam, sondern nur durch eine gültige, zeitlich begrenzte Subscription Lease.**

> **Offizielle Standardprozesse bleiben von kundenspezifischen Erweiterungen technisch und governance-seitig klar getrennt.**

---

## 16. Nächste technische Folgedokumente

Auf dieses Dokument sollten später mindestens folgen:

1. **JSON Schemas and Validation Rules v1**
2. **Plugin Loader and Package Manifest Spec v1**
3. **Process Pack Signing and Governance Rules v1**
4. **License / Lease State Machine v1**
5. **SQLAlchemy Model Draft v1**

