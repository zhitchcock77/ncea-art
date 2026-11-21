---
name: The Art Room
description: Colourful art-room workbook for NCEA Painting.
colors:
  paper: "#faf8f2"
  white: "#fffefa"
  ink: "#292720"
  muted: "#615e54"
  line: "#d2cfc5"
  pink: "#b41f55"
  cobalt: "#2443ac"
  orange: "#a83b20"
  yellow: "#e8ed86"
  soft: "#efeae1"
  chapter-light-1: "#e7edfa"
  chapter-light-2: "#fae7d8"
  chapter-light-3: "#f6e0e8"
  cover-apricot: "#f3e6d7"
  chapter-band-1: "#2c49b7"
  chapter-band-3: "#bf2f5b"
  reference-light-1: "#e2e8fc"
  reference-light-2: "#f6dfcd"
  reference-light-3: "#f8e1ea"
  field-border: "#8c877c"
typography:
  display:
    fontFamily: "Bricolage, 'DM Sans', sans-serif"
    fontSize: "clamp(2.65rem, 6.5vw, 5.8rem)"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Bricolage, 'DM Sans', sans-serif"
    fontSize: "clamp(1.8rem, 3.6vw, 3rem)"
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Bricolage, 'DM Sans', sans-serif"
    fontSize: "1.27rem"
    fontWeight: 700
    lineHeight: 1.25
  body:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.65
  small:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: "0.86rem"
    lineHeight: 1.6
  button:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: "0.9rem"
    fontWeight: 600
    lineHeight: 1.4
rounded:
  control: "4px"
  reference: "50%"
spacing:
  gutter: "clamp(1.25rem, 4vw, 4.5rem)"
  section: "4rem"
  paragraph: "1.15rem"
  sheet-section: "3.4rem"
  compact: "0.65rem"
  regular: "1rem"
  roomy: "1.5rem"
  wide: "2rem"
  column-gap: "3rem"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.65rem 1.05rem"
  button-primary-hover:
    backgroundColor: "{colors.pink}"
    textColor: "white"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "0.65rem 1.05rem"
  button-secondary-hover:
    backgroundColor: "{colors.yellow}"
  field:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.55rem 0.75rem"
  notes-field:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0.75rem 0.9rem"
  reference-1:
    backgroundColor: "{colors.reference-light-1}"
    textColor: "{colors.cobalt}"
    rounded: "{rounded.reference}"
    width: "60px"
    height: "60px"
  checkpoint:
    backgroundColor: "{colors.yellow}"
    padding: "1.2rem 1.4rem"
  assessment-note-1:
    backgroundColor: "{colors.chapter-light-1}"
    padding: "1rem 1.2rem"
---
# Design System: The Art Room

## Overview

**Creative North Star: "Colourful art-room workbook"**

The Art Room uses the confirmed colourful art-room workbook direction: personable display lettering, warm paper, vivid chapter fields and calm reading columns. It supports reading, making notes and printing classroom sheets. Real artworks retain their natural proportions and visible attribution.

Colour indexes levels and distinguishes useful teaching furniture; long task prose stays on paper. Standard numbers remain conspicuous throughout the ordinary link navigation. The same language carries the library, level introductions, task sheets, artist directory and teacher guidance.

**Key Characteristics:**
- Warm paper and ink, with fuchsia identity and three chapter themes.
- Large Bricolage headings paired with readable DM Sans.
- Flat, ruled document surfaces and compact native controls.
- Numbered standards, numbered studio steps and a locally saved evidence checklist.
- Print-specific type, spacing and source addresses.

## Colors

The palette combines warm paper neutrals, ink text and saturated chapter markers. Frontmatter records the actual CSS values; names below explain their roles.

### Primary

- **Workbook fuchsia** (`pink`): masthead identity, selected main navigation, focus outline, primary-button hover and Level 3 theme.
- **Chapter cobalt** (`cobalt`): Level 1 task numbers, headings and reference text.
- **Deep orange** (`orange`): Level 2 task numbers, headings and reference text.

### Secondary

- **Studio yellow** (`yellow`): checkpoints, the artist invitation strip, the Level 2 home chapter band, selection and secondary-button hover.
- **Pale chapter papers** (`chapter-light-1`, `chapter-light-2`, `chapter-light-3`): task toolbars, assessment notes and grade-table headings.
- **Home chapter fields** (`chapter-band-1`, `chapter-band-3`): the cobalt-blue and raspberry ends of the home chapter strip; white type on both.
- **Reference papers** (`reference-light-1`, `reference-light-2`, `reference-light-3`): pale circular standard markers.

### Neutral

- **Warm paper** (`paper`): page ground and masthead.
- **Clean paper** (`white`): fields, the artwork mount and selected reading surfaces.
- **Painting ink** (`ink`): primary reading text, button fill and strong rules.
- **Quiet pencil** (`muted`): captions, secondary metadata and source notes.
- **Paper rule** (`line`): table rows, dividers and section boundaries.
- **Soft stock** (`soft`): teacher notes, linked artwork placeholders and source-table headings.
- **Apricot cover** (`cover-apricot`): the home cover ground.
- **Field edge** (`field-border`): input, textarea and teacher-writing rules.

**The Chapter Index Rule.** Use cobalt for Level 1, deep orange for Level 2 and fuchsia for Level 3 task headings, reference numbers and pale chapter fields. The home chapter strip is its own existing treatment: cobalt-blue, yellow and raspberry. Do not infer a yellow Level 2 task theme from that strip.

## Typography

**Display Font:** Bricolage, falling back to DM Sans then sans-serif. The selfhosted variable file is `dist/assets/display.ttf` (weights 400–800).

**Body Font:** DM Sans, falling back to sans-serif. The selfhosted variable file is `dist/assets/body.ttf` (weights 400–700). Both use `font-display: swap`; synthetic faces are disabled.

**Character:** Bricolage supplies expressive but readable headings and numerical indexes. DM Sans keeps task paragraphs, assessment guidance, captions and forms calm.

### Hierarchy

- **Display:** the frontmatter display role is the default page heading. Covers and task headings use narrower contextual clamps; preserve the source variants rather than forcing every heading to one size.
- **Headline:** default section headings use the headline role. Task-sheet section headings use 2.1rem / 1.15, becoming 1.9rem on narrow screens.
- **Title:** third-level headings use the title role; task links use 1.25rem, weight 600 and line height 1.2.
- **Body:** the frontmatter body role is the desktop root. At 720px and below the root becomes 16px. Leads use 1.18rem; task-purpose text uses 1.16rem and weight 600.
- **Small:** secondary text uses the small role; metadata uses 0.8rem. Artwork captions use 0.76rem / 1.5 with a stronger artist name at 0.86rem.
- **Labels and buttons:** sentence case, DM Sans, weight 600. Navigation is 0.9rem / weight 500 on wide screens and 0.82rem on narrow screens.

**The Reading Column Rule.** Keep task prose within the established 70ch reading width on wide screens. Collapse the navigation rail above the reading column on narrow screens.

## Layout

The document uses a fluid outer gutter and a maximum main width of 1580px. The masthead inner row tops out at 1440px. Broad introductions often use two columns; the home cover uses 1.06fr / 1fr. The three home chapter links remain three columns on mobile.

Task pages align the large standard number and sticky contents rail with a 170px leading column and a 3rem gap. At 1000px the heading number column becomes 115px and the contents rail becomes 150px, both with 2rem gaps. At 720px the task layout becomes a single column, the contents rail becomes a static wrapping list and broad content grids stack. Artist entries alternate image side on desktop and return to document order on mobile.

Use the observed spacing tokens as a vocabulary rather than a forced mathematical scale. Sections use the section spacing token, task-body sections the sheet-section token; paragraphs use the paragraph token. Narrow screen sections use 2.6rem vertical padding and task-body sections use 2.7rem bottom spacing. The library is a ruled table, with the redundant final action column hidden below 1000px.

Print is an A4 document with 16mm top/bottom and 15mm left/right page margins. The print root is 10.5pt / 1.45. Headings become 29pt, 19pt and 13pt. Task-body sections use 7mm bottom spacing; the task heading uses a 20mm number column, 4mm gap and 7mm bottom padding and margin. The reading column becomes full width. Source links append their addresses. Artwork, evidence rows, grade rows and artist connection items avoid internal page breaks; headings avoid breaks immediately after them. Paragraphs and list items request three orphan/widow lines.

## Elevation & Depth

The system is flat: no box shadows. Warm and clean papers, pale chapter fields, rules and generous margins create separation. The home artwork sits on a clean-paper mount with a small 1.3-degree rotation; that rotation is removed on mobile and in print. It is a local artwork treatment, not a card pattern.

**The Flat Workbook Rule.** Use paper colour, one-pixel rules and spacing to separate content. The shipped system has no box shadows.

## Shapes

Document blocks are square edged. Buttons, search/select controls and textareas share gently eased corners through the control radius. Standard reference links are circles through the reference radius and shrink from 60px to 46px on narrow screens. Borders are generally one pixel; main-navigation state uses a two-pixel underline. Numbered studio steps use a leading-zero text counter, not decorative icon glyphs.

## Components

### Buttons

Compact, labelled workbook actions. Primary buttons use ink fill, clean-paper text and a matching border; hover changes fill and border to fuchsia. Secondary buttons keep a transparent ground, ink text and ink border; hover adds studio yellow. Both use the button typography and control radius tokens, with a 46px minimum height. Disabled buttons use 0.55 opacity and a default cursor. Text actions remain underlined links or plain text buttons rather than another filled variant.

### Inputs / Fields

Search and select controls use clean paper, field-edge borders, the control radius and a 48px minimum height. Selects use the shipped SVG chevron. Textareas have a 100px minimum height, vertical resizing and roomier padding. Labels are visible above fields. Placeholder text uses quiet pencil at full opacity. The shared keyboard treatment is a three-pixel fuchsia outline offset by five pixels. Carets use fuchsia and checkbox accents follow the current chapter. The build has no custom error-state vocabulary.

### Navigation

Use ordinary anchors for main navigation, breadcrumbs, standard circles, contents links and next-task links. Main-navigation current and hover states share fuchsia text and a fuchsia bottom rule. Breadcrumbs and the sticky sheet contents use restrained small text with underline on hover. Mobile navigation wraps; there is no hidden menu. A skip link appears on keyboard focus. Default body links remain visibly underlined, with a thicker underline on hover.

### Chapter links and standard markers

Home chapter links are large coloured blocks with the level, a learning phrase and explicit task numbers. Their only transition is background over 0.2 seconds with ease timing; hover gives ink background and white text. Circular reference links identify the standard in Bricolage, with pale level paper and chapter-colour numbers; hover becomes ink and white. There is no independent chip/tag vocabulary.

### Teaching containers

Assessment notes use pale chapter paper and compact padding. Studio-conversation checkpoints use studio yellow and roomier padding. Teacher notes use soft stock, a heading and native open disclosure; these containers have square edges and no shadow. Grade comparisons use a ruled table with pale chapter headers and a distinct grade-name column.

### Evidence checklist and working notes

Evidence rows are divided by paper rules, with a real checkbox aligned beside the text. Checking a row strikes through its text and changes it to quiet pencil. A live count appears when JavaScript runs. Checkboxes and reflection textareas save per sheet in browser storage, with visible saved/restored/unavailable status and a clear action. If storage fails, the controls remain usable and status advises printing or copying notes. The site does not submit these notes as assessment evidence.

### Artwork

Keep reproductions in natural aspect ratio and use `object-fit: contain` where height limits apply. Captions include artist, title/date and source/rights links. Artist-directory entries may use a flat soft-stock linked-art placeholder when no reproduction is supplied; it is not a fabricated image.

### Print and reduced motion

Print hides the masthead, footer, breadcrumbs, contents navigation, toolbar, buttons and JavaScript-only controls. Colour fields turn to white where defined; text, rules and source URLs preserve structure. Checkboxes become outlined writing boxes while checked state remains visible. Reflection fields print as bordered writing areas without placeholder text. Teacher notes print only when the explicit inclusion checkbox is selected; JavaScript opens their disclosure for printing and restores it afterwards. It also expands note fields for their contents. Linked-art placeholders are hidden and their directory entries become block flow to avoid empty image columns. Reduced-motion preference disables smooth scrolling, transitions and animations.

## Do's and Don'ts

### Do:

- **Do** use the established chapter theme for numbered standards and teaching accents.
- **Do** preserve native links, labelled form controls and the visible keyboard focus outline.
- **Do** show artwork at its natural aspect ratio with an artist, title and source/rights caption.
- **Do** retain the checklist count, browser-storage feedback and clear action when extending saved working notes.
- **Do** check print styles when extending a task sheet; source URLs and readable evidence rows must survive.

### Don't:

- **Don't** spread chapter colour over the long reading prose.
- **Don't** replace standard numbers with decorative identifiers.
- **Don't** add shadows or rounded card shells to ordinary document sections.
- **Don't** imply that completing an evidence checklist guarantees a grade or submits evidence.
