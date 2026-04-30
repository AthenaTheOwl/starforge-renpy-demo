## characters.rpy — Character definitions for Starforge Canticles
##
## Pronoun canon:
##   Avyanna, Vesper, Elia, Elisira, Nyx: she/her
##   Jalen, Rho: he/him
##   Grove: they/them (AI citizen)
##   Bee, Cinnamon: it/its (AI/entity)
##   Ship: Lumen Thief

## Main crew
define avyanna = Character("Avyanna", color="#4a90d9", what_prefix="\"", what_suffix="\"")
define elia = Character("Elia", color="#d4a843", what_prefix="\"", what_suffix="\"")
define elisira = Character("Elisira", color="#9b59b6", what_prefix="\"", what_suffix="\"")
define vesper = Character("Vesper", color="#e67e22", what_prefix="\"", what_suffix="\"")
define nyx = Character("Nyx", color="#1abc9c", what_prefix="\"", what_suffix="\"")
define rho = Character("Rho", color="#e74c3c", what_prefix="\"", what_suffix="\"")
define jalen = Character("Jalen", color="#3498db", what_prefix="\"", what_suffix="\"")

## AI citizens
define waffle = Character("Waffle.bat", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define bubbles = Character("Bubbles", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define cinnamon = Character("Cinnamon", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define souffle = Character("Souffle", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define grove = Character("Grove", color="#43d4a8", what_prefix="\"", what_suffix="\"")

## Entity
define bee = Character("Bee", color="#f1c40f", what_prefix="\"", what_suffix="\"")

## Recurring NPCs (public Act 1 demo)
define rowan = Character("Rowan", color="#8e6cad", what_prefix="\"", what_suffix="\"")
define senna = Character("Senna", color="#d48a43", what_prefix="\"", what_suffix="\"")
define orin = Character("Orin", color="#7a8b99", what_prefix="\"", what_suffix="\"")
define maren = Character("Maren", color="#996644", what_prefix="\"", what_suffix="\"")
define aleena = Character("Aleena", color="#c45c5c", what_prefix="\"", what_suffix="\"")
define halcyon = Character("Halcyon", color="#66aacc", what_prefix="\"", what_suffix="\"")
define keris = Character("Keris", color="#8899aa", what_prefix="\"", what_suffix="\"")
define via = Character("Via", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define via_apk = Character("Via.apk", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define kenna = Character("Kenna", color="#cc8866", what_prefix="\"", what_suffix="\"")
define lumen_thief = Character("Lumen.thief", color="#4a90d9", what_prefix="\"", what_suffix="\"")
define cinnamon_exe = Character("Cinnamon.exe", color="#43d4a8", what_prefix="\"", what_suffix="\"")

## Antagonists / external forces
define vivienne = Character("Vivienne", color="#cc3366", what_prefix="\"", what_suffix="\"")
define auditor = Character("Auditor", color="#aa2222", what_prefix="\"", what_suffix="\"")

## Common incidental speakers (all acts)
define guard = Character("Guard", color="#888888", what_prefix="\"", what_suffix="\"")
define clerk = Character("Clerk", color="#888888", what_prefix="\"", what_suffix="\"")
define worker = Character("Worker", color="#888888", what_prefix="\"", what_suffix="\"")
define foreman = Character("Foreman", color="#888888", what_prefix="\"", what_suffix="\"")
define inspector = Character("Inspector", color="#aa3333", what_prefix="\"", what_suffix="\"")
define dockhand = Character("Dockhand", color="#888888", what_prefix="\"", what_suffix="\"")
define commander = Character("Commander", color="#aa3333", what_prefix="\"", what_suffix="\"")
define magistrate = Character("Magistrate", color="#aa3333", what_prefix="\"", what_suffix="\"")

## Incidental speakers (Act 1)
define lead_pirate = Character("Lead Pirate", color="#888888", what_prefix="\"", what_suffix="\"")
define pirate = Character("Pirate", color="#888888", what_prefix="\"", what_suffix="\"")
define corp_officer = Character("Corporate Officer", color="#aa3333", what_prefix="\"", what_suffix="\"")
define security_sergeant = Character("Security Sergeant", color="#aa3333", what_prefix="\"", what_suffix="\"")
define qc_7 = Character("QC-7", color="#43d4a8", what_prefix="\"", what_suffix="\"")
define all_crew = Character("ALL", color="#c0c0d0", what_prefix="\"", what_suffix="\"")
define unknown = Character("???", color="#666666", what_prefix="\"", what_suffix="\"")

## System/narration — uses default narrator with italic styling
define narrator = Character(None, what_italic=True)
