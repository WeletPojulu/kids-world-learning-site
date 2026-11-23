"""Builds the public pages for the Kids World Learning iPad app (GitHub Pages).

    python3 generate.py

writes index.html (Privacy Policy) and support.html (Help and support).
Edit the text below, run it again, then commit and push.
"""
import html
import pathlib

EMAIL = "weletpojulu@gmail.com"
MAKER = "Welet Pojulu"
UPDATED = "November 23, 2026"

CSS = """:root{--ink:#1F2A44;--muted:#4E5A78;--brand:#0E6E69;--tint:#DDF4F2;--bg:#F3F6FB;--card:#FFFFFF;--line:#DCE3EF}
@media(prefers-color-scheme:dark){:root{--ink:#E9EDF6;--muted:#A8B2CA;--brand:#7FE3DC;--tint:#15363A;--bg:#11172A;--card:#1A2238;--line:#2B3552}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 16px 64px}
.strip{display:flex;gap:6px;margin-bottom:20px}.strip span{width:28px;height:8px;border-radius:4px}
nav{display:flex;gap:18px;flex-wrap:wrap;margin-bottom:24px;font-size:15px}nav a{color:var(--brand);text-decoration:none;font-weight:700}nav a:hover{text-decoration:underline}nav a[aria-current]{color:var(--ink)}
h1{font-size:34px;line-height:1.15;margin:0 0 12px;font-family:ui-rounded,"SF Pro Rounded",-apple-system,sans-serif}
.date{display:inline-block;background:var(--tint);color:var(--brand);font-size:13px;font-weight:700;padding:5px 12px;border-radius:99px}
.lede{color:var(--muted);margin:16px 0 24px}
section{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 22px;margin:14px 0}
h2{font-size:20px;margin:0 0 10px;font-family:ui-rounded,"SF Pro Rounded",-apple-system,sans-serif}
h3{font-size:17px;margin:16px 0 6px}
section p{margin:0 0 10px}section ul{margin:0 0 10px;padding-left:22px}section li{margin:4px 0}
.table{overflow-x:auto;margin:6px 0 12px}table{border-collapse:collapse;width:100%;min-width:520px;font-size:15px}
th,td{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line)}th{font-size:13px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
a{color:var(--brand)}
.contact{background:var(--brand);color:#fff;border-radius:18px;padding:20px 22px;margin-top:20px}.contact h2{color:#fff}.contact a{color:#fff;font-weight:700}
@media(prefers-color-scheme:dark){.contact{color:#0B1B1A}.contact h2,.contact a{color:#0B1B1A}}
footer{margin-top:32px;color:var(--muted);font-size:13px}"""

STRIP = "".join(f'<span style="background:{c}"></span>' for c in
                ["#F2836B", "#F2C14E", "#5AA8F0", "#5CC08A", "#F39A4A", "#E87AB8", "#A98BFF", "#3FC9C2"])


def nav(current):
    links = [("index.html", "Privacy Policy"), ("support.html", "Help and support")]
    current_attr = ' aria-current="page"'
    return "<nav>" + "".join(
        f'<a href="{href}"{current_attr if href == current else ""}>{label}</a>' for href, label in links
    ) + "</nav>"


def page(fname, title, lede, sections):
    body = "".join(f"<section><h2>{html.escape(h)}</h2>{b}</section>" for h, b in sections)
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kids World Learning - {title}</title>
<meta name="description" content="Kids World Learning {title}">
<style>{CSS}</style></head><body><main>
<div class="strip" aria-hidden="true">{STRIP}</div>
{nav(fname)}
<h1>{title}</h1><span class="date">Last updated {UPDATED}</span><p class="lede">{lede}</p>
{body.replace("{EMAIL}", mail)}
<div class="contact"><h2>Questions?</h2><p>Write to us any time and we'll reply as soon as we can, within 30 days at most.</p><p>{mail}</p></div>
<footer>&copy; 2026 {MAKER}. Kids World Learning is made by {MAKER}.</footer>
</main></body></html>
"""
    pathlib.Path(fname).write_text(doc)


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


PRIVACY = [
    ("The short version",
     "<p>Kids World Learning collects only what it needs to save each child's learning progress for their family, and nothing more.</p>"
     + ul("A <strong>grown-up</strong> creates the account with an email address or Sign in with Apple. Children never sign in.",
          "For each <strong>child</strong>, the grown-up enters a first name, age and learning level. We never ask for a last name, photo, voice or location.",
          "The app saves <strong>lesson progress and stars</strong>, so they're there on every iPad the family uses.",
          "<strong>No ads, no tracking and no chat.</strong> We never sell or share anyone's information for marketing.",
          "The app is free to download. One optional purchase, the <strong>Family unlock</strong>, is made through Apple and only in the grown-up area.",
          "A grown-up can <strong>change or delete</strong> a child's profile, or the whole account, at any time in the app.")),
    ("Who we are and how to reach us",
     f"<p>Kids World Learning is made by <strong>{MAKER}</strong> (\"we\" or \"us\"). For any question about this policy or your family's information, or to make a request, email {{EMAIL}}. We'll reply as soon as we can, and within 30 days at most.</p>"),
    ("Information we collect",
     "<p>We collect only what a grown-up types in, plus the progress the app records as a child plays.</p>"
     + table(["What", "Details", "Who provides it", "Why we need it"], [
         ["Grown-up account", "Email address and password, or Sign in with Apple", "The grown-up", "To sign in and keep the family's learners together"],
         ["Child profile", "First name, age, learning level, chosen picture and teacher", "The grown-up, behind the grown-up gate", "To show each child their own lessons at the right level"],
         ["Learning settings", "Captions on or off, reading speed and similar lesson settings", "The grown-up", "To run lessons the way the family wants"],
         ["Lesson progress", "Lessons finished, stars earned, date each was finished", "Recorded by the app as the child plays", "To unlock the next lessons and show progress to the grown-up"],
     ])
     + "<p><strong>Passwords</strong> are handled by our sign-in provider and stored scrambled (hashed). We never see them.</p>"
     + "<p><strong>With Sign in with Apple</strong>, Apple shares only an email address with us. You can choose Apple's “Hide My Email”, and then we receive a private relay address instead. We don't ask Apple for your name.</p>"
     + "<p><strong>We never collect</strong> last names, photos, video, voice recordings, location, contacts, or anything a child types or says. The app doesn't use the camera, microphone or location. Tracing practice in Writing and drawings in the art studio stay on the screen and are never saved or uploaded. The teacher's voice is made on the iPad itself, so no text or audio is sent anywhere to be read aloud. We don't use advertising IDs, analytics or tracking tools.</p>"
     + "<p><strong>Technical logs.</strong> Like most online services, the servers that hold the account may keep short-term technical logs, such as the IP address and time of a request, to keep the service secure and working.</p>"),
    ("The Family unlock purchase",
     "<p>Kids World Learning is free to download, and some lessons, games and word sets are part of an optional one-time <strong>Family unlock</strong>. Only a grown-up can buy it, after the grown-up gate. Children see a key and “Ask a grown-up”, never a price or a buy button.</p>"
     + "<p>The purchase is made and processed entirely by <strong>Apple</strong> under your Apple Account. We never see card or payment details. The app only asks Apple whether this Apple Account owns the unlock, and keeps that yes-or-no answer on the iPad so it works offline. Nothing about the purchase is saved in our database. Refunds are handled by Apple.</p>"),
    ("How we use information",
     "<p>We use it only to run Kids World Learning for your family:</p>"
     + ul("to sign the grown-up in and keep the account secure;",
          "to show each child their own name, teacher and lessons at the right level;",
          "to save progress and stars, and keep them in sync across the family's iPads;",
          "to show the grown-up a progress summary in the grown-up area;",
          "to send account emails a grown-up asks for, such as confirming an email address or resetting a password.")
     + "<p>We don't use it for advertising or profiling, we don't sell it, and we don't send marketing emails.</p>"),
    ("Where it's stored and who we share it with",
     "<p>Information is saved in two places:</p>"
     + ul("<strong>On the iPad</strong>, in the app's private storage with iPadOS file protection, so lessons work offline. Signing out removes it from that iPad.",
          "<strong>In our online database</strong>, run by Supabase, so progress follows the family to their other iPads. It is stored on servers in <strong>the United States</strong>.")
     + "<p>We don't sell or rent anyone's information, and we don't share it with advertisers or data brokers. We share it only with the companies that run the app for us, and only for that job:</p>"
     + table(["Provider", "What they do for us", "What they receive"], [
         ['<a href="https://supabase.com/privacy">Supabase</a>', "Sign-in, database and account emails", "The grown-up's email, child profiles and progress"],
         ['<a href="https://www.apple.com/legal/privacy/">Apple</a>', "Sign in with Apple, the Family unlock purchase, app delivery and TestFlight", "An email address for Sign in with Apple, the purchase, plus what Apple's own services need"],
     ])
     + "<p>If you've chosen in your iPad's settings to share analytics with app developers, Apple may also send us anonymous crash reports and app usage numbers. We may share information if the law requires it, for example to answer a valid legal request.</p>"),
    ("Children's privacy",
     "<p>Kids World Learning is made for children ages 3 to 10, and a grown-up is always in charge of their information.</p>"
     + ul("<strong>Only a grown-up can create the account and add a child.</strong> Adding or changing a child, opening Settings or Progress, buying the Family unlock, and deleting data all sit behind a grown-up gate: press and hold for 3 seconds, then enter a PIN.",
          "<strong>The grown-up gives the child's information and consents to its use</strong> by creating the child's profile. We collect only what's listed above, and never more than the app needs.",
          "<strong>Children can't share anything.</strong> There's no chat, messaging, posting, photos, purchases, or links to other apps or websites in the children's area.",
          "<strong>Parents stay in control.</strong> A parent or guardian can review a child's information in Progress and Settings, change it, or delete it at any time. Deleting the child's profile stops any further collection. You can also email us to ask what we hold or to have it deleted.")
     + "<p>We built the app with the U.S. Children's Online Privacy Protection Act (COPPA) and similar laws in other countries in mind. If you believe a child's information reached us without a parent's consent, email us and we'll delete it.</p>"),
    ("Keeping, changing and deleting information",
     "<p>We keep information only while the account is open, and a grown-up can change or delete it at any time:</p>"
     + ul("<strong>Change</strong> a child's name, age, level, picture or teacher in <strong>Settings</strong> (grown-up area).",
          "<strong>Delete a child's profile</strong> in <strong>Settings ▸ Delete profile</strong>. Their profile, stars and progress are removed from the iPad and from our database.",
          "<strong>Delete the whole account</strong> in <strong>Progress ▸ Account ▸ Delete account</strong>. This removes the grown-up account and every child's profile and progress, and it can't be undone.",
          "<strong>Signing out</strong> removes the family's saved information from that iPad. It stays in the account for the next sign-in.")
     + "<p>Deleted information is removed from our live database right away. Our provider's backups may keep it for up to 7 days before it's overwritten.</p>"
     + "<p>Depending on where you live (for example the EU, the UK or California), you may have the right to access, correct, delete or get a copy of your information, or to object to how it's used. Email us and we'll help within 30 days.</p>"),
    ("How we protect information",
     ul("Everything between the app and our database travels over an encrypted connection (HTTPS).",
        "Database security rules lock each family's information to their own account, so one family can never see another's.",
        "On the iPad, saved information uses iPadOS file protection, so it's encrypted while the iPad is locked.",
        "Grown-up settings and the Family unlock sit behind a hold-and-PIN gate, so children can't change or buy anything.")
     + "<p>No system is perfectly secure. If we ever learn of a breach that affects your information, we'll tell you as the law requires.</p>"),
    ("Changes to this policy",
     "<p>If we change this policy, we'll update the date at the top and tell grown-ups in the app or by email. If a change affects how we use children's information, we'll ask for a parent's consent again before it applies.</p>"),
]

SUPPORT = [
    ("Getting into the grown-up area",
     "<p>Tap <strong>Grown-ups</strong>, press and hold the circle for 3 seconds until the ring fills, then enter your family's 4-digit PIN. Progress, Settings, Account and the Family unlock are all in there.</p>"
     + "<p><strong>Forgot the PIN?</strong> Tap <strong>Forgot PIN?</strong> on the lock screen. After you confirm your account password, or Sign in with Apple, you can choose a new PIN. It changes on every family iPad.</p>"),
    ("Signing in and passwords",
     ul("<strong>Forgot your password?</strong> On the sign-in page tap <strong>Forgot password?</strong>. We email you a 6-digit code; type it with a new password. Each code works once and expires after an hour.",
        "<strong>No email arrived?</strong> Check your junk or spam folder, wait a minute and tap <strong>Send again</strong>.",
        "<strong>Same progress on another iPad:</strong> sign in there with the same email, or the same Apple Account for Sign in with Apple.")),
    ("The Family unlock",
     "<p>Pre-K, Kindergarten, the first lesson of every higher level, the art studio and the first word set in each language are free. The one-time <strong>Family unlock</strong> opens every other lesson, Memory match, Pop the bubbles, Picture puzzle and every word set. There's no subscription.</p>"
     + ul("<strong>To buy:</strong> open the grown-up area and tap the key button, or tap any gold key and choose <strong>Get a grown-up</strong>.",
          "<strong>New iPad or reinstalled the app?</strong> Go to <strong>Grown-ups ▸ Account ▸ Restore purchase</strong>.",
          "<strong>Family Sharing:</strong> with Apple Family Sharing turned on, the unlock works for everyone in your family group.",
          "<strong>“Waiting for approval”:</strong> Ask to Buy is on for that Apple Account. The family organizer approves it on their own device.",
          '<strong>Refunds</strong> are handled by Apple at <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.')),
    ("Sound and voices",
     ul("<strong>No sound?</strong> Check the iPad's volume and that it isn't on silent, then tap the speaker button on the screen to hear the line again.",
        "<strong>Spanish, French or Arabic words sound English?</strong> The iPad is missing a voice for that language. Open the iPad's <strong>Settings ▸ Accessibility ▸ Spoken Content ▸ Voices</strong>, pick the language and download a voice (the Enhanced ones sound best).",
        "<strong>For the most natural English teacher voice</strong>, download a Premium or Enhanced English voice in the same place, then choose it in <strong>Grown-ups ▸ Settings ▸ Reading aloud</strong>.")),
    ("Children and accounts",
     ul("<strong>Add a child:</strong> Grown-ups ▸ Add learner.",
        "<strong>Change a child's name, level, picture or teacher:</strong> Grown-ups ▸ Settings.",
        "<strong>Delete a child's profile:</strong> Grown-ups ▸ Settings ▸ Delete profile.",
        "<strong>Delete the whole account:</strong> Grown-ups ▸ Account ▸ Delete account. This can't be undone.")),
    ("What you need",
     "<p>An iPad with iPadOS 17 or later. An internet connection is needed to sign in and to sync between iPads; lessons keep working offline.</p>"
     + "<p>When you write to us, it helps to include the app version, shown in <strong>Grown-ups ▸ Account ▸ Help and privacy</strong>.</p>"),
]

page("index.html", "Privacy Policy",
     "How Kids World Learning handles your family's information. In short: only what's needed to save each child's progress, never ads or tracking, and a grown-up is always in charge.",
     PRIVACY)
page("support.html", "Help and support",
     "Answers to common questions about Kids World Learning, the learning app for children from Pre-K to Grade 5 on iPad.",
     SUPPORT)
print("Wrote index.html and support.html")
