#!/usr/bin/env python3
"""Check WCAG 2 contrast of the theme's text and icon colors. Exits 1 on failure."""
import json,sys
def lum(c):
    c=[x/255 for x in c]; c=[x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def cr(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+0.05)/(lb+0.05)
m=json.load(open(sys.argv[1] if len(sys.argv)>1 else "manifest.json"))["theme"]["colors"]
pairs=[("tab_text","toolbar",4.5),("tab_background_text","background_tab",4.5),
("tab_background_text","frame",4.5),("tab_background_text_inactive","background_tab_inactive",4.5),
("tab_background_text_inactive","frame_inactive",4.5),
("tab_background_text_incognito","frame_incognito",4.5),("tab_background_text_incognito_inactive","frame_incognito_inactive",4.5),
("toolbar_button_icon","toolbar",3),("toolbar_text","toolbar",4.5),("bookmark_text","toolbar",4.5),
("omnibox_text","omnibox_background",4.5),("ntp_text","ntp_background",4.5),("ntp_link","ntp_background",4.5),
("ntp_text","ntp_header",4.5)]
failed=0
for f,b,req in pairs:
    r=cr(m[f],m[b]); ok=r>=req; failed+=not ok
    print(f"{'OK  ' if ok else 'FAIL'} {r:5.2f} (need {req}) {f} on {b}")
sys.exit(1 if failed else 0)
