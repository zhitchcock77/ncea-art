"""Teacher lesson plans: original classroom activities for AS91913."""
from html import escape as e

LESSONS = [
 dict(title='Find a place and a story', aim='Choose a personally meaningful place and an idea a painting could communicate.',
 success=['Name a place you can observe or document yourself.', 'Connect a specific visual detail to an idea or narrative.'],
 prep='Set out drawing books, pencils and plain paper. Bring your own example of a familiar place and a short story about it. Prepare a classroom still-life or window view for students who need an accessible starting point.',
 words='Idea / narrative · context · observation',
 starter='Ask students to list three places they know well. In pairs, describe one sound, object or memory connected to a place.',
 model='Model moving from “the beach” to a specific intention: a worn path and empty seat might communicate returning or absence. Show how two viewpoints suggest different meanings.',
 studio='Students choose a place, sketch two remembered details and write or orally record an intention. Arrange access to their own photographs or direct observation before Lesson 2. Offer the school grounds as an in-class option.',
 review='Pairs point to one drawn detail and explain its connection to the intention. Confer with students whose idea is still only a topic; ask what they want a viewer to notice or feel.',
 exit='Collect an intention and a source-gathering plan. Label books, return materials and check that any visit or photography follows school procedures.',
 evidence='A place, an initial intention and a feasible plan to gather original visual sources.',
 support='Offer a school-based place, a small selection of ordinary objects, sentence starters and oral recording. Personal disclosure is optional.',
 stretch='Ask how the same place could communicate two different ideas through viewpoint or omission.',
 next='Check source access and permissions. Provide time in school for anyone unable to gather sources elsewhere.'),
 dict(title='Observe and gather your own imagery', aim='Gather first-hand visual information that can sustain a painting.',
 success=['Record distinctive shapes, tones and textures from your own source.', 'Choose imagery that helps communicate your intention.'],
 prep='Have pencils, viewfinders made from scrap card and drawing paper ready. Students bring their own photographs or observe an accessible school view or arranged objects. Check permission before photographing people or restricted places.',
 words='Viewpoint · cropping · tone · primary source',
 starter='Students show a source or identify the classroom view they will use. Ask: what makes this particular place recognisable to you?',
 model='Demonstrate looking before drawing: block in large shapes, compare light and dark, then select a meaningful detail. Use a viewfinder to change the crop without tracing an existing artwork.',
 studio='Students make a broad tonal observation and a close detail study. They may take their own reference photographs where permitted. Ask them to record where and when the sources were made and select a useful viewpoint.',
 review='Students compare sources against their intention. Ask which visual information is still missing and how they can obtain it. Check that reference images are their own or appropriately sourced for local assessment conditions.',
 exit='Photograph or collect the studies, label sources and clean the work area. Each student records one gap to fill.',
 evidence='Original source imagery and observation studies showing useful visual information.',
 support='Use a nearby still-life, a viewfinder and large-format drawing tools. Allow verbal observations alongside drawing.',
 stretch='Compare an unusual crop with a wider view. Explain how each changes the narrative.',
 next='Identify students needing more observation time. Select artist references relevant to the places and intentions emerging.'),
 dict(title='Learn from painting conventions', aim='Identify painting conventions in context and test a method using your own subject.',
 success=['Describe a specific pictorial or material choice in a referenced artwork.', 'Try that method using your own imagery and acknowledge the artist.'],
 prep='Open the linked artist sources in the unit overview or prepare permitted reference material in advance. Select two relevant works with artist, title and context available. Set out water-based paint, brushes and small paper.',
 words='Convention · pictorial space · edge · palette',
 starter='Show a selected work. Give quiet looking time, then ask what students can point to as evidence of how it was made.',
 model='Compare a specific decision in each work: spatial structure, edges, colour relationships or paint layers. Read the artists’ contexts alongside the images; distinguish learning a method from copying their subject or culturally significant imagery.',
 studio='Students choose one useful convention and make two small painted trials from their own source. They label the artist, source and method tested, then note how that method could serve their own intention.',
 review='Partners identify the tested convention from the painted evidence. Ask: what did you change to make the method appropriate to your subject?',
 exit='Keep and label the trials, wash brushes and clear palettes. Record a convention worth investigating further.',
 evidence='Acknowledged artist references and painted trials that apply a relevant convention.',
 support='Provide a short vocabulary list and model one technique at a time. Discuss orally before writing.',
 stretch='Compare two methods and justify which better communicates the intention, using the trials as evidence.',
 next='Check that methods and references suit each student’s intention. Revisit context or attribution where necessary.'),
 dict(title='Test colour and paint handling', aim='Choose paint processes and colour relationships that support your idea.',
 success=['Mix and repeat useful colours with increasing control.', 'Explain how a material choice affects the mood or meaning.'],
 prep='Provide school-approved acrylic or watercolour, suitable paper, water pots, rags and a limited set of colours. Prepare a dry sample to show layering. Keep wet trials separate from books until dry.',
 words='Hue · value · opacity · layering · consistency',
 starter='Students choose a trial from Lesson 3 and name one technical problem they need to solve.',
 model='Demonstrate a light-to-dark colour range, appropriate paint consistency and a hard and soft edge. Show how to clean a brush between mixtures. Connect the demonstration to a real passage in your own example.',
 studio='Students make a small palette test, then paint the same source detail in two ways. Change one variable such as value range, opacity or edge. Label mixtures or processes so a useful effect can be repeated.',
 review='Students place trials beside their source. Ask which treatment best supports their intention and whether they can reproduce it. Offer a focused reteach to students struggling with paint consistency.',
 exit='Store wet tests flat, clean equipment and record a useful mixture or process.',
 evidence='A repeatable palette or handling test and a reason for the selected approach.',
 support='Limit the palette, offer larger brushes or adapted grips and use a single source detail. Provide a dry example to handle and inspect.',
 stretch='Keep a consistent value structure while changing temperature; compare the effect on atmosphere.',
 next='Allow additional practice where paint handling is still preventing the intended effect. Keep successful recipes available.'),
 dict(title='Compose the painting', aim='Develop and select a composition that communicates your intention.',
 success=['Compare genuinely different arrangements of your own imagery.', 'Explain how placement, scale and tonal structure guide attention.'],
 prep='Provide source studies, paper, pencils and paint for a small colour study. Bring a viewfinder and an example showing how a changed crop alters a composition.',
 words='Composition · focal area · negative space · tonal structure',
 starter='Ask students to describe where they want a viewer to look first and why that matters to their idea.',
 model='Demonstrate several quick arrangements of the same source: change crop, overlap, scale or empty space. Reduce one arrangement to three tones to check its structure.',
 studio='Students make several small alternatives, then develop a promising arrangement in tone or limited colour. They compare it against the intention and retain an alternative rather than choosing only the neatest sketch.',
 review='Pairs describe the viewing path before hearing the artist’s explanation. Students use that feedback to select or revise their proposal.',
 exit='Label the selected plan and keep alternatives. Clear materials and record the next technical question.',
 evidence='Composition alternatives and a reasoned selection linked to the idea.',
 support='Use movable paper shapes derived from the student’s own drawings and a limited tonal range. Let students explain their selection orally.',
 stretch='Develop an unexpected arrangement and test whether it communicates the idea more clearly than the first choice.',
 next='Check that the selected composition offers enough depth for a substantial painting and that students have the sources they need.'),
 dict(title='Agree the scope and production plan', aim='Plan a substantial single painting with suitable scale, depth and technical finish.',
 success=['Explain how the proposed painting will communicate the idea at its chosen scale.', 'Plan practical stages and test a demanding passage.'],
 prep='Prepare available supports, rulers and sample surfaces. Set out the current student task sheet, standard and exemplars for teacher reference. Have a simple calendar of available studio sessions and drying or storage constraints.',
 words='Scale · depth · technical finish · production',
 starter='Students show their selected composition and identify the part most likely to be technically difficult.',
 model='Explain how scale, complexity, production time and finish work together. A large support alone does not establish substantial scope. Model a short production plan and testing a passage at the intended working scale.',
 studio='Students test a challenging passage and draft a proposal: intention, conventions, support, scale, materials and stages. Hold short conferences to agree a feasible scope and enough production time; students retain ownership of choices.',
 review='Students check the proposal against their actual tests. Ask what must be practised or adjusted before committing to the final support.',
 exit='Record agreed materials and the next stage. Store tests and return equipment. Schedule further planning where the proposal needs development.',
 evidence='An agreed substantial scope, a production plan and a relevant working-scale test.',
 support='Provide a planning checklist and break the production into manageable stages. Adapt tools or support without removing the necessary scope.',
 stretch='Ask students to justify a consequential choice of surface or scale through a comparison test.',
 next='Confirm readiness individually. Extend preparation rather than requiring everyone to start the final work on the same day.'),
 dict(title='Prepare the surface and block in', aim='Establish a sound surface and the main structure of the final painting.',
 success=['Prepare a support appropriate to the chosen medium.', 'Establish the main forms and tonal relationships from the selected plan.'],
 prep='Have agreed supports, approved grounds if needed, brushes, sources and plans ready. Prepare surfaces in advance if drying exceeds the lesson. Allocate named drying and storage spaces; follow school procedures for all media.',
 words='Support · ground · underpainting · block-in',
 starter='Students check their plan and surface. Ask what preparation this material needs before paint is added.',
 model='Demonstrate the relevant surface preparation on a separate sample. Show how to locate large shapes and tonal masses without committing too early to small detail.',
 studio='Students prepare or use a pre-prepared support, establish the composition and block in major relationships. Pause halfway to compare the painting with the intention and plan. Students decide whether any proportions or placements need changing.',
 review='View work from a distance. Students identify whether the main structure is legible and select one adjustment before further development.',
 exit='Take a dated progress photograph where appropriate, record the next stage, clean tools and store work safely.',
 evidence='A prepared support and a purposeful beginning of the single final painting.',
 support='Use enlarged student-made plans, accessible tools and a brief individual check of the main forms. Demonstrate on separate material.',
 stretch='Test whether an underlayer can contribute to the intended atmosphere rather than simply cover the support.',
 next='Repeat or extend this stage when preparation or drying needs it. Resolve structural problems before adding detail.'),
 dict(title='Build the painting relationships', aim='Develop the painting while maintaining consistent colour, space and paint handling.',
 success=['Connect a working decision to the intention and selected conventions.', 'Manage paint handling across connected areas of the painting.'],
 prep='Return dry paintings, source material, successful tests and mixing notes. Prepare the agreed media and a separate demonstration surface. Allow students to be at different production stages.',
 words='Relationship · consistency · focal area · layering',
 starter='Students inspect the whole painting and set one specific studio goal, pointing to the passage they will work on.',
 model='Demonstrate a shared technical need identified in the class, such as joining adjacent colours or layering over a dry passage. Keep the example separate from student work and connect it to the effect it produces.',
 studio='Students develop connected areas using their tests and plan. Prompt regular distance checks. Confer through questions: what is happening here, what effect are you seeking, and which option will you test? Record progress without prescribing solutions.',
 review='Students compare the beginning and end of the session. Ask what changed in the painting and whether the change supports the intention. Identify any issue needing a fresh trial.',
 exit='Record a short next-step note, photograph progress when useful, clean and store work. Keep mixtures or process notes for continuity.',
 evidence='Visible progress in the final painting and an identifiable student-led decision.',
 support='Agree one achievable goal, provide a visual sequence for tool use and offer a short technique recap on separate material.',
 stretch='Ask students to sustain the same quality of handling through a less successful passage, rather than adding more detail to a strong one.',
 next='Repeat this studio plan with a new student-set goal as needed. Reserve a midpoint review before the work becomes too settled.'),
 dict(title='Review the painting at midpoint', aim='Use evidence from the painting to decide what needs strengthening.',
 success=['Describe what the painting currently communicates.', 'Choose and test a revision that addresses a visible issue.'],
 prep='Arrange space to view paintings upright and from a distance. Return intentions, source studies and dated progress images. Have scrap paper or spare supports ready for tests before changes to the final painting.',
 words='Critique · intention · evidence · revision',
 starter='Ask students to look at their painting silently and note where the intended idea is most and least clear.',
 model='Model descriptive feedback: “I notice … because …” followed by a question. Separate observations from preferences. Show how a small trial can help evaluate a possible revision.',
 studio='Pairs or small groups describe what they see before hearing the intention. Each artist selects an issue, tests a possible change on spare material or in a study, then decides whether to apply it. Hold brief individual conferences.',
 review='Students point to the test and explain the decision. Ask whether the proposed change addresses the issue identified, and what evidence would show that it worked.',
 exit='Keep a dated before-and-after record or review note, then clean and store the work.',
 evidence='A focused review, a relevant test and a decision grounded in the painting.',
 support='Use a small feedback group, descriptive sentence starters and oral or recorded responses. Keep feedback focused on one visible issue.',
 stretch='Invite a revision that strengthens relationships across the whole composition rather than repairing an isolated detail.',
 next='Plan further studio sessions from the review. Redirect unfinished technical learning to a separate trial before continuing.'),
 dict(title='Resolve a demanding passage', aim='Strengthen technical command where the painting needs it most.',
 success=['Identify a specific handling problem and practise a useful solution.', 'Apply a selected process consistently in the final work.'],
 prep='Review midpoint notes and group students by technical need where useful. Set out spare supports, chosen media, dry samples and each student’s successful tests. Prepare a focused demonstration based on observed needs.',
 words='Control · fluency · transition · surface',
 starter='Students point to a demanding passage and describe the intended effect rather than simply saying it needs to be “better”.',
 model='Demonstrate one relevant process on a separate surface: a tonal transition, an intentional edge, controlled layering or a repeated brush mark. Discuss the decisions and material conditions that make the effect repeatable.',
 studio='Students practise their selected process, compare the trial with the intended effect and apply it when ready. Encourage checks across adjoining passages so the technique supports the whole painting.',
 review='Students compare the revised passage with a related area. Ask whether the handling is consistent and what remains unresolved. Avoid treating a technique exercise as a substitute for the final artwork.',
 exit='Keep a useful trial, record the next priority, clean equipment and store paintings.',
 evidence='An improved passage that contributes to consistent handling in the final painting.',
 support='Reduce simultaneous technical demands and provide adapted tools or a short process card. Reteach on separate material.',
 stretch='Ask students to vary handling intentionally while preserving coherence and the clarity of their idea.',
 next='Repeat this lesson or Lesson 8 with a fresh goal until the painting is ready for whole-work resolution. Adjust the schedule individually.'),
 dict(title='Unify and finish the painting', aim='Bring the painting to a coherent technical and communicative resolution.',
 success=['Review the whole painting against the intention and chosen conventions.', 'Make purposeful finishing decisions and recognise when to stop.'],
 prep='Provide upright viewing space, suitable lighting, clean brushes and agreed media. Return intentions and progress records. Check drying time before the presentation lesson; plan extra studio time where necessary.',
 words='Resolution · unity · technical finish · coherence',
 starter='Students stand back and identify the most distracting unresolved relationship in the painting.',
 model='Model a whole-work review on separate material: composition, colour relationships, edges, surface and focal emphasis. Discuss when a change strengthens the work and when further detail might weaken it.',
 studio='Students prioritise a small set of finishing decisions and work through them. Pause for distance checks and compare the effect with the intention. Use neutral conferencing questions; the student decides the final changes.',
 review='Students explain whether the work is resolved and identify the evidence. Agree further production time if the substantial artwork remains unfinished.',
 exit='Record final decisions, check safe storage and drying, clean tools and arrange the next presentation stage.',
 evidence='A single substantial painting approaching or reaching a coherent finish.',
 support='Use a whole-work review checklist and help students order tasks without choosing their pictorial solutions.',
 stretch='Ask how restraint, selective emphasis or a final subtle adjustment could clarify the idea more effectively than added detail.',
 next='Do not force a final declaration for an unresolved work. Confirm readiness and local assessment dates before presentation.'),
 dict(title='Present, reflect and review evidence', aim='Present the resolved painting and explain the decisions that communicate its idea.',
 success=['Present the single painting with its title and clear identification.', 'Use visible evidence to explain selected conventions and technical decisions.'],
 prep='Prepare a dry, safe display space and photography setup if used. Confirm the school’s evidence, authenticity and moderation procedures. Bring process records and the student task sheet; gather reflection responses without imposing an extra assessment threshold.',
 words='Presentation · reflection · authenticity · acknowledgement',
 starter='Students check that their work is dry, identified and ready to be viewed. Revisit the initial intention.',
 model='Model a concise reflection that points to a particular painted passage, names a technical choice and explains its contribution. Clarify the locally agreed presentation and source-acknowledgement process.',
 studio='Students title and present the single painting, document it as required locally and prepare a short written or oral reflection. Keep sources and progress studies available to support process and authenticity. View peers’ work respectfully.',
 review='Students share one choice that communicates the idea and one future learning goal. Teacher checks completeness and authentic process; make assessment judgements separately against the official standard and normal moderation procedures.',
 exit='Collect or record the agreed evidence, return resources and leave display and storage areas ready for the next class.',
 evidence='The final resolved painting, with locally agreed identification and supporting process records available.',
 support='Offer an oral reflection or scribed access arrangement where appropriate. Use a clear presentation checklist and accessible viewing options.',
 stretch='Compare the starting intention with the final painting and explain how a significant decision changed the communicated meaning.',
 next='Assess the substantial final artwork holistically. Use current NZQA guidance to calibrate judgements; reflect on teaching needs for the next unit.'),
]


def lesson_file(n):
 return f'lesson-1-2-{n:02d}.html'


def lesson_pdf(n):
 return f'print/lesson-1-2-{n:02d}.pdf'


def lesson_pages(n, lesson):
 def para(text): return f'<p>{e(text)}</p>'
 def block(title, text): return f'<h3>{title}</h3>{para(text)}'
 outcomes=''.join(f'<li>{e(x)}</li>' for x in lesson['success'])
 rows=''.join(f'<tr><th scope="row">{time}<span>{label}</span></th><td>{e(lesson[key])}</td></tr>' for time,label,key in [
  ('0–5 min','Connect','starter'),('5–13 min','Teach & model','model'),('13–38 min','Studio practice','studio'),('38–45 min','Review & check','review'),('45–50 min','Record & clean up','exit')])
 return f'''<article class="lesson-plan" id="lesson-{n}">
 <section class="lesson-paper lesson-brief" aria-labelledby="lesson-{n}-title">
 <h2 id="lesson-{n}-title">Lesson {n}: {e(lesson['title'])}</h2>
 <p class="lesson-meta">Visual Arts 1.2 · AS91913 v4 · 50 minutes · Teacher plan</p>
 <p class="lesson-admin">Teacher / class: <span></span> Date: <span></span></p>
 {block('Learning intention',lesson['aim'])}
 <h3>Students are learning to</h3><ul>{outcomes}</ul>
 {block('Materials & preparation',lesson['prep'])}
 {block('Language to make visible',lesson['words'])}
 <div class="lesson-adapt">{block('Support & access',lesson['support'])}{block('Extend the learning',lesson['stretch'])}</div>
 <div class="lesson-writing"><h3>Class adjustments</h3><div></div></div>
 <p class="paper-footer">The Art Room · 1.2 · Lesson {n} · Teaching brief 1 of 2</p>
 </section>
 <section class="lesson-paper lesson-sequence" aria-labelledby="sequence-{n}">
 <h2 id="sequence-{n}">Lesson {n}: classroom sequence</h2>
 <p class="lesson-meta">{e(lesson['title'])} · 50 minutes, including clean-up</p>
 <table class="lesson-timing"><caption class="sr-only">Lesson {n} timed teaching sequence</caption><thead><tr><th scope="col">Time / phase</th><th scope="col">Teaching and learning</th></tr></thead><tbody>{rows}</tbody></table>
 {block('Check for learning',lesson['evidence'])}
 {block('Before the next lesson',lesson['next'])}
 <div class="lesson-writing"><h3>Teacher reflection / next steps</h3><div></div></div>
 <p class="paper-footer">The Art Room · 1.2 · Lesson {n} · Classroom sequence 2 of 2</p>
 </section></article>'''


def unit_pages(standard, exemplar, artists):
 rows=''.join(f'<tr><th scope="row">{n}</th><td><a href="#lesson-{n}">{e(d["title"])}</a></td></tr>' for n,d in enumerate(LESSONS,1))
 refs=''.join(f'<li><a href="{e(artists[k]["url"],quote=True)}">{e(artists[k]["name"])}</a> · {e(artists[k].get("source_label","Artist reference"))}</li>' for k in ['gossage','maughan','sherald'])
 return f'''<section class="lesson-paper unit-overview"><h2>1.2: One place, one painting</h2>
 <p class="lesson-meta">AS91913 v4 · Level 1 · 5 credits · Internal assessment · Painting focus</p>
 <p>A flexible teaching unit leading to one substantial, resolved painting about a personally meaningful place. These original plans extend the student task sheet with teacher preparation, timed activities and checks for learning.</p>
 <h3>How to use the sequence</h3><p>Twelve lesson plans of 50 minutes each. Repeat Lessons 8 and 10 with fresh goals to provide sustained painting time, and revisit preparation or reviews when needed. At three lessons a week, 24–30 sessions allows around 8–10 weeks: the twelve plans plus 12–18 additional studio sessions. Adjust to your timetable, students and the scope of the work.</p>
 <p>Place the midpoint review after a meaningful period of production. Leave Lessons 11 and 12 until the work is ready; add studio time rather than reduce the substantial scope to fit a fixed lesson count.</p>
 <table class="lesson-map"><caption>Teaching route · repeat studio sessions as needed</caption><thead><tr><th scope="col">Lesson</th><th scope="col">Focus</th></tr></thead><tbody>{rows}</tbody></table>
 <p class="paper-footer">The Art Room · 1.2 · Unit overview 1 of 2</p></section>
 <section class="lesson-paper unit-preparation"><h2>Prepare the unit</h2>
 <h3>Before the first lesson</h3><p>Confirm the current standard, exemplars, local assessment conditions, dates and authenticity procedures. Agree available materials, drying and storage space, and accessible source-gathering options. Plan a suitable water-based painting approach and follow school studio procedures.</p>
 <h3>Materials across the unit</h3><p>Drawing books, pencils, scrap paper and viewfinders; student-made photographs and observations; approved acrylic or watercolour, brushes, palettes, water pots and rags; trial surfaces and agreed final paper or board; permitted artist references; a way to date progress records. Photography and projection are optional: prepare references in advance for an offline class.</p>
 <h3>Artist connections</h3><p>Choose relevant works from the existing artist directory. Investigate Gossage’s relationship to place, Maughan’s constructed garden spaces or Sherald’s figure–ground decisions. Read the linked context with the works. Students apply a useful method to their own imagery; references are not templates or student exemplars.</p><ul>{refs}</ul>
 <p>Respect tikanga, permissions and the distinct contexts of Māori artists. Students need not disclose personal or cultural information; a school view or ordinary objects can offer an accessible starting point.</p>
 <h3>Assessment and teaching boundaries</h3><p>The assessment focus is the substantial final artwork. Source studies, tests and progress records help learning and authenticity; quantities of trials, reflections and lessons are teaching suggestions. Use official criteria for judgements: suitable conventions at Achievement, consistent media management at Merit and skilful handling at Excellence. Do not turn the plans into a response template or a grade checklist.</p>
 <p>Model processes on separate material. Adapt assistance to local conditions and approved access arrangements. Students choose their subject, composition, methods and revisions. Keep normal internal moderation and assessment records.</p>
 <h3>Primary assessment references</h3><ul class="lesson-sources"><li><a href="{e(standard,quote=True)}">NZQA AS91913 · achievement standard (PDF)</a></li><li><a href="{e(exemplar,quote=True)}">NZQA AS91913 · annotated exemplars</a></li></ul>
 <p class="small">Standard checked 22 November 2026. Confirm current guidance before assessment. Independent teaching resources; not NZQA-approved assessments.</p>
 <p class="paper-footer">The Art Room · 1.2 · Unit overview 2 of 2</p></section>'''


def build_lesson_pages(write, standard_url, exemplar_url, task, artists):
 common=dict(current='teacher',bodyclass='theme-1',additional_css='assets/lessons.css')
 intro='''<header class="page-intro screen-only"><h1>1.2 lesson plans</h1><p class="lead">One place, one painting. Twelve adaptable teacher plans for 50-minute classes, with repeatable studio sessions.</p></header>'''
 tools='''<div class="lesson-tools screen-only"><button class="button button-dark print-button js-only" type="button">Print complete pack</button><a class="button" href="print/lessons-1-2.pdf" download>Download lesson pack (PDF)</a><a href="task-1-2.html">Student task sheet</a><p>Print on A4 at 100% scale. Turn browser headers and footers off. Each lesson uses two pages; the complete pack is 26 pages. Without JavaScript, use your browser’s Print command.</p></div>'''
 index='<nav class="lesson-index screen-only" aria-label="Individual lesson plans"><h2>Open or print a lesson</h2><ol>'+''.join(f'<li><a href="{lesson_file(n)}">{e(d["title"])}</a><a href="{lesson_pdf(n)}" download aria-label="Download lesson {n} PDF">PDF</a></li>' for n,d in enumerate(LESSONS,1))+'</ol></nav>'
 papers=unit_pages(standard_url(task),exemplar_url(task),artists)+''.join(lesson_pages(n,d) for n,d in enumerate(LESSONS,1))
 write('lessons-1-2.html','1.2 printable lesson plans',f'<main id="main" class="lesson-page"><div class="breadcrumbs"><a href="teacher.html#lesson-plans">For teachers</a><span>/</span>1.2 lesson plans</div>{intro}{tools}{index}<div class="lesson-papers">{papers}</div></main>',description='Twelve printable 50-minute teaching plans for NCEA Visual Arts 1.2 / AS91913. Includes a unit overview, classroom sequences, differentiation and checks for learning.',**common)
 for n,d in enumerate(LESSONS,1):
  toolbar=f'''<div class="lesson-tools screen-only"><button class="button button-dark print-button js-only" type="button">Print this lesson</button><a class="button" href="{lesson_pdf(n)}" download>Download lesson {n} (PDF)</a><a href="lessons-1-2.html#lesson-{n}">Complete 1.2 pack</a><p>50 minutes · Two A4 pages. Use your browser’s Print command if JavaScript is unavailable.</p></div>'''
  nav='<nav class="lesson-neighbours screen-only" aria-label="Lesson sequence">'+(f'<a href="{lesson_file(n-1)}">Previous lesson</a>' if n>1 else '')+f'<a href="lessons-1-2.html">All 1.2 lesson plans</a>'+(f'<a href="{lesson_file(n+1)}">Next lesson</a>' if n<len(LESSONS) else '')+'</nav>'
  write(lesson_file(n),f'1.2 lesson {n} · {d["title"]}',f'<main id="main" class="lesson-page"><div class="breadcrumbs"><a href="teacher.html#lesson-plans">For teachers</a><span>/</span><a href="lessons-1-2.html">1.2 plans</a><span>/</span>Lesson {n}</div><h1 class="lesson-screen-title screen-only">Lesson {n}: {e(d["title"])}</h1>{toolbar}<div class="lesson-papers">{lesson_pages(n,d)}</div>{nav}</main>',description=f'Printable 50-minute teacher lesson plan for NCEA 1.2: {d["title"]}.',**common)
