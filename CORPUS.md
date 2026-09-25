# مكتبة المقارنة: النصوص والمخطوطات

هذا فهرس للمصادر، وليس حكماً بصحة رواية أو نسبة مؤلّف. `نص محفوظ` يعني نسخة إنجليزية تاريخية كاملة من **الإصدار المذكور** في `texts/gutenberg/`، مع إشعار المصدر، وليس جميع النسخ والمخطوطات أو النص بلغته الأصلية. `رابط مرجعي` يعني أن صورة المخطوط أو قاعدة البيانات باقية لدى الجهة الحافظة؛ لم تُنسخ إلى المستودع.

## الكتب المحفوظة بنصها الكامل حسب الإصدار

| المطلوب | الإصدار المحفوظ | الملف بعد المزامنة | القيد |
| --- | --- | --- | --- |
| **التناخ كاملاً بالعبرية (التوراة، الأنبياء، الكتابات)** | [Westminster Leningrad Codex](https://tanach.us/) عبر [midvash bible-data](https://github.com/midvash/bible-data/tree/main/versions/he/wlc) | [تنزيل النص المضغوط TSV](texts/tanakh/tanakh-hebrew-wlc.tsv.gz) | 39 ملف سفر بحسب التقسيم التقني، 929 إصحاحاً، 23,318 آية؛ مرتّب في الأقسام الثلاثة، مع الحركات العبرية، وسفر دانيال ضمن الكتابات. فكّه بـ `gzip -d`؛ SHA-256 للملف المضغوط: `9c4a98fa7cb8981bc83149531111289fe4ed248bc4b7f32510f1717ad6dff25c`؛ البصمة للنص المفكوك: `8067c47de7cc7b6865b21cc5937e825aa2fb8a088fc6ca3507f8626e49083d67`، وترخيص النص العبري يسمح بالنقل. |
| التوراة، العهد القديم، العهد الجديد، سفر دانيال | [King James Version، Project Gutenberg #10](https://www.gutenberg.org/ebooks/10) | `texts/gutenberg/pg10.txt`، و[مقتطف دانيال المستقل](texts/daniel-kjv-excerpt.txt) | ترجمة إنجليزية للكتاب المقدس؛ يشمل أسفار موسى الخمسة ودانيال والعهد الجديد، وليس نصاً عبرياً أو يونانياً أو مخطوطاً |
| **الكتاب المقدس بالعربية: العهد القديم والعهد الجديد** | [ترجمة سميث فان دايك، البيانات والنص](https://github.com/midvash/bible-data/tree/main/versions/ar/svd) | [تنزيل النص العربي المضغوط TSV](texts/bible/smith-van-dyck-arabic.tsv.gz) | إصدار عربي من 66 سفراً، 1,189 إصحاحاً، 31,104 آيات حسب ترقيم مصدره، ملك عام؛ يفك بـ `gzip -d`. SHA-256: `b97e641a22de9bf46497ceb9f6bb34157e324e3a301f8abcdfe951699db71b3b`، وليس تصويراً لمخطوطة قديمة. |
| المهابهارتا 1/4 | [Ganguli #15474](https://www.gutenberg.org/ebooks/15474) | `texts/gutenberg/pg15474.txt` | ترجمة إنجليزية، المجلد الأول |
| المهابهارتا 2/4 | [Ganguli #15475](https://www.gutenberg.org/ebooks/15475) | `texts/gutenberg/pg15475.txt` | المجلد الثاني |
| المهابهارتا 3/4 | [Ganguli #15476](https://www.gutenberg.org/ebooks/15476) | `texts/gutenberg/pg15476.txt` | المجلد الثالث |
| المهابهارتا 4/4 | [Ganguli #15477](https://www.gutenberg.org/ebooks/15477) | `texts/gutenberg/pg15477.txt` | المجلد الرابع |
| الإلياذة | [Homer، ترجمة Samuel Butler #2199](https://www.gutenberg.org/ebooks/2199) | `texts/gutenberg/pg2199.txt` | ترجمة إنجليزية كاملة لهذا الإصدار |
| الأوديسة | [Homer، ترجمة Samuel Butler #1727](https://www.gutenberg.org/ebooks/1727) | `texts/gutenberg/pg1727.txt` | ترجمة إنجليزية كاملة لهذا الإصدار |
| كتاب الموتى | [Budge، The Book of the Dead #7145](https://www.gutenberg.org/ebooks/7145) | `texts/gutenberg/pg7145.txt` | كتاب Budge كامل؛ دراسة وعرض منتقى، **ليس جميع برديات كتاب الموتى** |
| الأساطير المصرية | [Budge، Legends of the Gods #9411](https://www.gutenberg.org/ebooks/9411)، [The Literature of the Ancient Egyptians #15932](https://www.gutenberg.org/ebooks/15932) | `pg9411.txt`, `pg15932.txt` | طبعتان مترجمتان من أوائل القرن العشرين |
| جلجامش | [Jastrow/Clay، An Old Babylonian Version #11000](https://www.gutenberg.org/ebooks/11000) | `texts/gutenberg/pg11000.txt` | إصدار عن نسخة بابلية قديمة، لا يضم كل الألواح والنسخ اللاحقة |
| إنوما إيليش | [Budge، The Babylonian Legends of the Creation #9914](https://www.gutenberg.org/ebooks/9914) | `texts/gutenberg/pg9914.txt` | عرض وترجمة تاريخية لقصة الخلق البابلية؛ فيه نص إنوما إيليش وليس صورة الألواح |

التنزيلات محفوظة بترميز UTF-8 ونص Gutenberg كما هو، والبصمات في [gutenberg-manifest.json](gutenberg-manifest.json). إذا لم يظهر `texts/gutenberg/` بعد، شغّل `python3 fetch_classics.py` وتحقق من البصمات قبل الاعتماد على أي ملف.

**للقراءة بالعربية:** [الكتاب المقدس بترجمة فان دايك](https://ebible.org/find/details.php?id=arb-vd) متاح في موقع eBible بوصفه ملكية عامة، مع خيارات تنزيل للكتاب كله. رابط المصدر الأصلي مضاف، والنص العربي الكامل مضغوط ومرفوع في الجدول أعلاه.

## الفيدا الأربع والأفيستا والنصوص التبتية

| المجموعة | المرجع | الحالة |
| --- | --- | --- |
| رِغ فيدا | [ترجمة Griffith، Sacred Texts](https://sacred-texts.com/hin/rigveda/index.htm) | رابط مرجعي؛ لا تدّعي الترجمة الإنجليزية تمثيل كل الشروح أو المخطوطات السنسكريتية |
| ساما فيدا | [ترجمة Griffith](https://sacred-texts.com/hin/sv.htm) | رابط مرجعي |
| ياجور فيدا | [White Yajurveda، ترجمة Griffith](https://sacred-texts.com/hin/wyv/index.htm) | رابط مرجعي لفرع «الأبيض»؛ لا يشمل كل مدارس الياجور فيدا |
| أثارفا فيدا | [ترجمة Griffith](https://sacred-texts.com/hin/av/index.htm) | رابط مرجعي |
| الأفيستا | [Avesta.org: فهرس النصوص الأصلية والترجمات](https://www.avesta.org/)؛ [Zend-Avesta، ترجمة Darmesteter الجزء الأول](https://sacred-texts.com/zor/sbe04/index.htm) و[الثاني](https://sacred-texts.com/zor/sbe23/sbe2300.htm) | رابط مرجعي؛ الأفيستا مجموعة نصوص، لا مجلد واحد موحّد |
| النصوص التبتية | [BDRC / BUDA](https://library.bdrc.io/)؛ [84000 Reading Room](https://84000.co/reading-room) | رابطان لمجموعتين ضخمتين، ولم يُختر نص تيبتي بعينه أو تُنسخ ترجمات 84000 الحديثة |

## مخطوطات ونقوش: صور الأصل وفهارسها

| المجموعة | المصدر الحافظ أو العلمي | ما الذي يعرضه الرابط |
| --- | --- | --- |
| مخطوطات البحر الميت | [Leon Levy Dead Sea Scrolls Digital Library، هيئة الآثار الإسرائيلية](https://www.deadseascrolls.org.il/?locale=en_US) | صور وفهرس آلاف القطع؛ ليست مخطوطة واحدة |
| المخطوطة السينائية | [Codex Sinaiticus Project](https://www.codexsinaiticus.org/en/manuscript.aspx) | صور أوراق ونص يوناني لأسفار محفوظة؛ تختلف عن نص ترجمة KJV |
| نجع حمادي | [Nag Hammadi Archive، Claremont Colleges](https://ccdl.claremont.edu/digital/collection/nha) | صور المخطوطات القبطية |
| مصحف برمنغهام | [جامعة برمنغهام: المخطوط Mingana Islamic Arabic 1572a](https://www.birmingham.ac.uk/facilities/cadbury/birmingham-quran-mingana-collection/mingana-collection/digitized-manuscripts) | أوراق قرآنية مبكرة مصورة؛ لا تمثل مصحفاً كاملاً |
| مصحف صنعاء | [Corpus Coranicum: مخطوط صنعاء DAM 20-33.1](https://corpuscoranicum.de/en/manuscripts/114/page/1)؛ [طبقة سفلى من طرس 86/2003-I](https://corpuscoranicum.de/en/manuscripts/427/page/1v) | نماذج محددة من مخطوطات صنعاء وطرس ذي طبقتين؛ لا تجمع كل الموجود في صنعاء |
| بردية ديرفيني | [المتحف الأثري في سالونيك](https://www.amth.gr/en/exhibitions/highlights) | وصف القطعة الأصلية؛ الطبعات اليونانية وترجماتها منفصلة |
| أناجيل غاريمة | [Ethiopian Heritage Fund](https://www.ethiopianheritagefund.org/completed-project-3-the-abuna-garima-gospels) | حفظ المخطوطتين الأثيوبيتين ووصفهما، لا نص رقمي كامل في هذا المستودع |
| «كتاب الذهب» الإتروسكاني | [وصف عرض القطعة في المتحف الوطني التاريخي بصوفيا](https://scholarsarchive.byu.edu/insights/vol23/iss5/1/) | خبر عن ست صفائح ذهبية؛ لم أجد هنا نشرة محققة أو نصاً كاملاً موثوقاً للكتابة |
| النقوش السومرية | [Oxford ETCSL](https://etcsl.orinst.ox.ac.uk/)؛ [Oracc: النقوش الملكية السومرية](https://oracc.museum.upenn.edu/etcsri/) | نصوص سومرية منقحرة، ترجمات، وفهارس للقطع |
| النقوش البابلية وألواح الخلق | [CDLI](https://cdli.earth/about)؛ [قطعة من إنوما إيليش في المتحف البريطاني](https://www.britishmuseum.org/collection/object/W_K-5419-c) | كتالوجات ونماذج من ألواح أصلية؛ الترجمة المحفوظة أعلاه إصدار مختلف |
| أساطير مصر ونقوش المعابد | [بعثة التوثيق النقشي، جامعة شيكاغو](https://isac.uchicago.edu/research-projects/epigraphic-survey)؛ [بردية كتاب الموتى في المتحف المتروبوليتان](https://www.metmuseum.org/art/collection/search/553673) | توثيق نقوش المعابد ومثال لقطعة أصلية؛ لا توجد «ميثولوجيا مصرية» واحدة مكتملة |

## قاعدة للمقارنة

سجّل لكل استشهاد: **النص/رقم اللوح أو الورقة/اللغة/الطبعة أو الترجمة/موضع السطر/الفجوات والاستدراكات/الرابط**. لا تستنتج تاريخ النص الأصلي من تاريخ النسخة المحفوظة وحده، ولا تساوِ بين الترجمة والمخطوط.
