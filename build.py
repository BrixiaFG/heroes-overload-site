#!/usr/bin/env python3
"""Builds the Heroes Overload website (GitHub Pages) from the texts below, in English and Italian.

    python3 build.py            writes index.html, privacy.html, terms.html, support.html and the same in it/
    python3 build.py --preview  the same, with a stand-in support address (never published)

Every page is plain HTML with the site's own fonts and no scripts, cookies, analytics or outside requests.
Edit the texts here, run the script, and commit the pages it writes.
"""
import html, sys, pathlib

EMAIL = ''                      # the game's support Gmail (Brixia creates it); the game's Settings use the same address
UPDATED = {'en': '17 November 2026', 'it': '17 novembre 2026'}
ROOT = pathlib.Path(__file__).parent

if not EMAIL:
    if '--preview' not in sys.argv: sys.exit('Set EMAIL first (or run with --preview for a local look).')
    EMAIL = 'support-address@example.com'

M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

NAV = {'en': [('index', 'Home'), ('support', 'Support'), ('privacy', 'Privacy'), ('terms', 'Terms')],
       'it': [('index', 'Home'), ('support', 'Assistenza'), ('privacy', 'Privacy'), ('terms', 'Termini')]}

PAGES = {
 'index': {
  'en': ('Heroes Overload', 'A card battle game for iPhone.', f'''
<p class="lead">Build a squad of five, pick your Hero, and watch the battle play out. Clear the Campaign, climb the Ranked leagues
and grow your Stronghold.</p>
<div class="cards">
  <div><h3>Campaign</h3><p>Season by season, stage by stage, with rewards for every first win.</p></div>
  <div><h3>Ranked</h3><p>Your Attacking squad against other players' Defending squads, from Bronze to Immortal.</p></div>
  <div><h3>Stronghold</h3><p>Expeditions, Research, the Merchant, the Watchtower and your friends.</p></div>
</div>
<p>Coming to the App Store.</p>
<p class="small">Questions? Write to {M}.</p>'''),
  'it': ('Heroes Overload', 'Un gioco di battaglie di carte per iPhone.', f'''
<p class="lead">Crea una squadra di cinque, scegli il tuo Eroe e guarda la battaglia. Completa la Campagna, scala le leghe
della Classificata e fai crescere la tua Fortezza.</p>
<div class="cards">
  <div><h3>Campagna</h3><p>Stagione dopo stagione, tappa dopo tappa, con una ricompensa per ogni prima vittoria.</p></div>
  <div><h3>Classificata</h3><p>La tua squadra d'attacco contro le squadre di difesa degli altri giocatori, dal Bronzo all'Immortale.</p></div>
  <div><h3>Fortezza</h3><p>Spedizioni, Ricerca, il Mercante, la Torre di guardia e i tuoi amici.</p></div>
</div>
<p>Presto sull'App Store.</p>
<p class="small">Domande? Scrivi a {M}.</p>'''),
 },
 'support': {
  'en': ('Support', 'Help with Heroes Overload.', f'''
<h2>Contact us</h2>
<p>Write to {M}. We answer in English or Italian, usually within two working days.</p>
<p>In the game, <b>Stronghold › Profile › Settings › Report a problem</b> opens an email with your game details already filled in.
Please include your <b>player ID</b> (Settings › Account) so we can find your profile.</p>
<h2>Purchases</h2>
<p>Crystals are bought through the App Store. If crystals you paid for didn't arrive, close and reopen the game, or tap
<b>Settings › Restore purchases</b>. If they still don't arrive, write to us with the date of the purchase.</p>
<p>Refunds are handled by Apple: <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>Your profile</h2>
<p>Playing as a guest keeps your progress on this iPhone's account only. <b>Sign in with Apple</b> (Settings › Account) keeps it
safe if you change phone.</p>
<p>To delete your profile and everything we keep about it, tap <b>Settings › Delete profile</b>. This can't be undone.</p>'''),
  'it': ('Assistenza', 'Aiuto per Heroes Overload.', f'''
<h2>Contattaci</h2>
<p>Scrivi a {M}. Rispondiamo in italiano o in inglese, di solito entro due giorni lavorativi.</p>
<p>Nel gioco, <b>Fortezza › Profilo › Impostazioni › Segnala un problema</b> apre un'email con i dati del gioco già compilati.
Indica il tuo <b>ID giocatore</b> (Impostazioni › Account) così possiamo trovare il tuo profilo.</p>
<h2>Acquisti</h2>
<p>I cristalli si acquistano tramite l'App Store. Se i cristalli che hai pagato non sono arrivati, chiudi e riapri il gioco,
oppure tocca <b>Impostazioni › Ripristina acquisti</b>. Se ancora non arrivano, scrivici con la data dell'acquisto.</p>
<p>I rimborsi sono gestiti da Apple: <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
<h2>Il tuo profilo</h2>
<p>Giocando come ospite i progressi restano legati a questo iPhone. <b>Accedi con Apple</b> (Impostazioni › Account) li
conserva anche se cambi telefono.</p>
<p>Per eliminare il tuo profilo e tutto ciò che conserviamo, tocca <b>Impostazioni › Elimina profilo</b>. Non si può annullare.</p>'''),
 },
 'privacy': {
  'en': ('Privacy Policy', 'What Heroes Overload keeps about you, and why.', f'''
<p class="lead">Short version: we keep only what the game needs to work and to get better. No ads, no tracking, and we never
sell your data.</p>
<h2>Who we are</h2>
<p>Heroes Overload is made by Brixia, who is responsible for your data. Contact: {M}.</p>
<h2>What we keep</h2>
<ul>
<li><b>Your account</b>: a player ID made when you first open the game (as a guest), or your Sign in with Apple account. With Apple
we receive an ID and, if you share it, an email address (often a private relay address from Apple). Your player name and
friend code.</li>
<li><b>Your game</b>: cards, Heroes, coins, crystals, Aether, packs, Campaign stages, Ranked points and history, your squads,
Stronghold progress, gifts, and friends and blocks.</li>
<li><b>Purchases</b>: what you bought and when, from Apple through RevenueCat. We never see your card or payment details.</li>
<li><b>How you play</b>: the days you play, visits and their length, which screens you open, fights left partway, tutorial steps,
and reminder taps. We use these only to understand what to improve.</li>
<li><b>Your device</b>: the app version, your language, and, if you allow notifications, the phone's push address.</li>
<li><b>Internet address</b>: seen by our server host for a short time to keep the game safe (for example, limiting new guest
accounts). We don't store it with your profile.</li>
</ul>
<h2>Why</h2>
<p>To run the game and keep your progress (our contract with you), to stop cheating and abuse, and to improve the game
(our legitimate interest). Notifications only with your permission, and you can turn them off in Settings at any time.</p>
<h2>Who else sees it</h2>
<ul>
<li><b>Other players</b> see your player name, Hero, league and your Defending squad. Friends also see your friend profile.</li>
<li><b>Supabase</b> hosts our servers and database. <b>RevenueCat</b> checks App Store purchases. <b>Apple</b> runs Sign in with
Apple, the App Store and notifications. They process data only for us.</li>
</ul>
<p>No advertising networks, no third-party analytics, no data brokers.</p>
<h2>How long</h2>
<p>Your profile stays as long as you play. Records of how you play are deleted after 90 days. A guest profile that hasn't been
used for a long time and never bought anything may be deleted. Purchase records may be kept longer where the law requires.</p>
<h2>Your choices and rights</h2>
<ul>
<li><b>Delete everything</b>: Settings › Delete profile. This also ends Sign in with Apple for the game.</li>
<li>You can ask us for a copy of your data, to correct it, or to stop using it, by writing to {M}.</li>
<li>If you are in the EU, you can also complain to your data protection authority.</li>
</ul>
<h2>Children</h2>
<p>The game is not made for children under 13. If you are under 16, please ask a parent before playing or buying.</p>
<h2>Changes</h2>
<p>If this policy changes, we update this page and its date. Big changes are also shown in the game.</p>'''),
  'it': ('Informativa sulla privacy', 'Cosa conserva Heroes Overload su di te, e perché.', f'''
<p class="lead">In breve: conserviamo solo ciò che serve al gioco per funzionare e migliorare. Niente pubblicità, nessun
tracciamento, e non vendiamo mai i tuoi dati.</p>
<h2>Chi siamo</h2>
<p>Heroes Overload è creato da Brixia, titolare del trattamento dei tuoi dati. Contatto: {M}.</p>
<h2>Cosa conserviamo</h2>
<ul>
<li><b>Il tuo account</b>: un ID giocatore creato alla prima apertura del gioco (come ospite), oppure il tuo account Accedi con
Apple. Con Apple riceviamo un ID e, se lo condividi, un indirizzo email (spesso un indirizzo privato di inoltro di Apple).
Il tuo nome giocatore e il codice amico.</li>
<li><b>La tua partita</b>: carte, Eroi, monete, cristalli, Etere, pacchetti, tappe della Campagna, punti e cronologia della
Classificata, le tue squadre, i progressi della Fortezza, i regali, gli amici e i blocchi.</li>
<li><b>Acquisti</b>: cosa hai comprato e quando, da Apple tramite RevenueCat. Non vediamo mai i dati della tua carta o del pagamento.</li>
<li><b>Come giochi</b>: i giorni in cui giochi, le visite e la loro durata, le schermate che apri, le battaglie lasciate a metà,
i passi del tutorial e i tocchi sui promemoria. Li usiamo solo per capire cosa migliorare.</li>
<li><b>Il tuo dispositivo</b>: la versione dell'app, la lingua e, se consenti le notifiche, l'indirizzo push del telefono.</li>
<li><b>Indirizzo internet</b>: visto per poco tempo dal fornitore dei nostri server per tenere il gioco al sicuro (per esempio,
limitare i nuovi account ospite). Non lo conserviamo con il tuo profilo.</li>
</ul>
<h2>Perché</h2>
<p>Per far funzionare il gioco e conservare i tuoi progressi (il nostro contratto con te), per fermare imbrogli e abusi, e per
migliorare il gioco (nostro legittimo interesse). Le notifiche solo con il tuo permesso, e puoi disattivarle quando vuoi nelle
Impostazioni.</p>
<h2>Chi altro li vede</h2>
<ul>
<li><b>Gli altri giocatori</b> vedono il tuo nome giocatore, l'Eroe, la lega e la tua squadra di difesa. Gli amici vedono anche
il tuo profilo amico.</li>
<li><b>Supabase</b> ospita i nostri server e il database. <b>RevenueCat</b> verifica gli acquisti dell'App Store. <b>Apple</b>
gestisce Accedi con Apple, l'App Store e le notifiche. Trattano i dati solo per nostro conto.</li>
</ul>
<p>Nessuna rete pubblicitaria, nessuna analisi di terze parti, nessun commerciante di dati.</p>
<h2>Per quanto tempo</h2>
<p>Il tuo profilo resta finché giochi. I dati su come giochi vengono cancellati dopo 90 giorni. Un profilo ospite inutilizzato
da molto tempo e senza acquisti può essere cancellato. I dati sugli acquisti possono essere conservati più a lungo quando la
legge lo richiede.</p>
<h2>Le tue scelte e i tuoi diritti</h2>
<ul>
<li><b>Cancella tutto</b>: Impostazioni › Elimina profilo. Termina anche Accedi con Apple per il gioco.</li>
<li>Puoi chiederci una copia dei tuoi dati, di correggerli o di smettere di usarli, scrivendo a {M}.</li>
<li>Se sei nell'UE, puoi anche presentare reclamo all'autorità per la protezione dei dati del tuo paese.</li>
</ul>
<h2>Minori</h2>
<p>Il gioco non è pensato per bambini sotto i 13 anni. Se hai meno di 16 anni, chiedi a un genitore prima di giocare o acquistare.</p>
<h2>Modifiche</h2>
<p>Se questa informativa cambia, aggiorniamo questa pagina e la sua data. I cambiamenti importanti vengono mostrati anche nel gioco.</p>'''),
 },
 'terms': {
  'en': ('Terms of Service', 'The rules for playing Heroes Overload.', f'''
<p class="lead">By playing Heroes Overload you agree to these terms. Apple's standard licence for App Store apps also applies.</p>
<h2>Your account</h2>
<p>You can play as a guest or with Sign in with Apple. Keep your Apple account safe: whoever controls it controls your profile.
One person, one profile; don't sell, share or buy profiles.</p>
<h2>Fair play</h2>
<ul>
<li>No cheating, hacking, bots, modified apps, or using bugs to gain coins, crystals, cards or Ranked points.</li>
<li>No offensive, hateful or misleading player names.</li>
<li>Don't try to reach other players' data or overload our servers.</li>
</ul>
<p>If you break these rules we may remove what was gained unfairly, block or delete the profile. If you think we got it wrong,
write to {M}.</p>
<h2>Crystals and other game items</h2>
<p>Crystals, coins, Aether, packs, cards and Heroes are part of the game. You get a licence to use them in the game; they have
no money value, can't be exchanged for money and can't be moved to another profile. Pack contents are random, with the odds
shown in the Shop. Purchases are final once delivered, except where the law or Apple's refund rules say otherwise. If Apple
refunds a purchase, the crystals it gave are taken back, and your crystal count can go below zero.</p>
<h2>The game changes</h2>
<p>We keep improving the game: we may change cards, prices, rewards and rules, add or remove features, and run seasons. We
try to be fair to players when we do. We may need to stop the game one day; if so we'll tell players in advance.</p>
<h2>Our responsibility</h2>
<p>We work hard to keep the game running, but it is offered as it is, and it may sometimes be unavailable or have bugs.
Nothing here limits the rights you have as a consumer under the law of the country you live in.</p>
<h2>Privacy</h2>
<p>How we treat your data is in the <a href="privacy.html">Privacy Policy</a>.</p>
<h2>Contact</h2>
<p>{M}</p>'''),
  'it': ('Termini di servizio', 'Le regole per giocare a Heroes Overload.', f'''
<p class="lead">Giocando a Heroes Overload accetti questi termini. Vale anche la licenza standard di Apple per le app dell'App Store.</p>
<h2>Il tuo account</h2>
<p>Puoi giocare come ospite o con Accedi con Apple. Proteggi il tuo account Apple: chi lo controlla controlla il tuo profilo.
Una persona, un profilo; non vendere, condividere o comprare profili.</p>
<h2>Gioco leale</h2>
<ul>
<li>Niente imbrogli, hacking, bot, app modificate, né uso di errori del gioco per ottenere monete, cristalli, carte o punti
della Classificata.</li>
<li>Niente nomi giocatore offensivi, d'odio o ingannevoli.</li>
<li>Non cercare di accedere ai dati degli altri giocatori o di sovraccaricare i nostri server.</li>
</ul>
<p>Se non rispetti queste regole possiamo togliere ciò che è stato ottenuto in modo scorretto, bloccare o cancellare il profilo.
Se pensi che abbiamo sbagliato, scrivi a {M}.</p>
<h2>Cristalli e altri oggetti del gioco</h2>
<p>Cristalli, monete, Etere, pacchetti, carte ed Eroi fanno parte del gioco. Ricevi una licenza per usarli nel gioco; non hanno
valore in denaro, non si possono convertire in denaro né spostare su un altro profilo. Il contenuto dei pacchetti è casuale,
con le probabilità indicate nel Negozio. Gli acquisti sono definitivi una volta consegnati, salvo quanto previsto dalla legge
o dalle regole di rimborso di Apple. Se Apple rimborsa un acquisto, i cristalli ricevuti vengono ripresi e il saldo dei
cristalli può andare sotto zero.</p>
<h2>Il gioco cambia</h2>
<p>Continuiamo a migliorare il gioco: possiamo cambiare carte, prezzi, ricompense e regole, aggiungere o togliere funzioni e
organizzare stagioni. Cerchiamo di essere corretti con i giocatori quando lo facciamo. Un giorno potremmo dover chiudere il
gioco; in quel caso avviseremo i giocatori in anticipo.</p>
<h2>La nostra responsabilità</h2>
<p>Ci impegniamo a mantenere il gioco attivo, ma è offerto così com'è e a volte può non essere disponibile o avere errori.
Niente in questi termini limita i diritti che hai come consumatore secondo la legge del paese in cui vivi.</p>
<h2>Privacy</h2>
<p>Come trattiamo i tuoi dati è descritto nell'<a href="privacy.html">Informativa sulla privacy</a>.</p>
<h2>Contatti</h2>
<p>{M}</p>'''),
 },
}

UPD = {'en': 'Last updated', 'it': 'Ultimo aggiornamento'}
OTHER = {'en': ('it', 'Italiano'), 'it': ('en', 'English')}

def page(key, lang):
    title, sub, body = PAGES[key][lang]
    up = '../' if lang == 'it' else ''
    olang, oname = OTHER[lang]
    other = (f'it/{key}.html' if lang == 'en' else f'../{key}.html')
    nav = ''.join(f'<a href="{k}.html"{" aria-current=page" if k == key else ""}>{t}</a>' for k, t in NAV[lang])
    full = 'Heroes Overload' if key == 'index' else f'{title} · Heroes Overload'
    date = '' if key in ('index', 'support') else f'<p class="small">{UPD[lang]}: {UPDATED[lang]}</p>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(sub)}">
<link rel="icon" href="{up}assets/icon.png">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{up}assets/fonts/fonts.css">
<link rel="stylesheet" href="{up}assets/site.css">
<link rel="alternate" hreflang="{olang}" href="{other}">
</head>
<body>
<header><a class="logo" href="index.html"><img src="{up}assets/logo.webp" alt="Heroes Overload" width="168" height="61"></a>
<nav>{nav}<a class="lang" href="{other}" lang="{olang}">{oname}</a></nav></header>
<main>
<h1>{html.escape(title)}</h1>
<p class="sub">{html.escape(sub)}</p>
{body.strip()}
{date}
</main>
<footer>© 2026 Brixia · Heroes Overload</footer>
</body>
</html>
'''

for lang in ('en', 'it'):
    d = ROOT if lang == 'en' else ROOT / 'it'
    d.mkdir(exist_ok=True)
    for key in PAGES:
        (d / f'{key}.html').write_text(page(key, lang), encoding='utf-8')
print('ok', EMAIL)
