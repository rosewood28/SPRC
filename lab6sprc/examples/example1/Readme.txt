Stan Sabina - 341C3

Laborator 6 - Web Cache LFU

In clasa WebCacheEntry, am adaugat un camp frequency pe care il incrementez la fiecare accesare a paginii.
In WebCache am actualizat metoda de verificare a paginilor ce trebuiesc sterse astfel incat sa reflecte cerintele
LFU si sa aleaga pagina cu cel mai mic numar de accesari (cu cea mai mica fecventa). De asemenea, am printat momentul
cand o pagina este accesata sau adaugata/starsa din cache, precum si starea cache-ului inainte ca o pagina sa fie eliminata.
In ClientTest am accesat paginile din input intr-o bucla infinita.

In fisierul build.xml am adaugat "<redirector output="output.txt" alwayslog="true"/>" pentru a redirecta outputul
intr-un fisier la oprirea executiei.

Un exemplu de aplicare a LFU este acesta:

Pagina http://www.yahoo.com a fost adaugata in cache, 1 accesari
Pagina http://google.com era deja in cache, 3 accesari
Pagina http://www.yahoo.com era deja in cache, 1 accesari
Pagina http://google.com era deja in cache, 4 accesari

Continut cache:
http://google.com, 5 accesari
http://www.yahoo.com, 2 accesari
http://httpforever.com, 1 accesari
Eliminare http://httpforever.com din cache, a avut 1 accesari (LFU)

Se poate observa ca pagina http://httpforever.com a avut cel mai mic numar de accesari, anume una, fiind astfel
prima pagina stearsa din cache.