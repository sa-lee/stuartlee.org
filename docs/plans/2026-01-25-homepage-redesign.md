# Homepage Redesign

## Goal

Transform the minimal index page into a personal showcase that expresses personality alongside professional content.

## Sections

### 1. Hero

- Circular photo (`headshot-slee.jpeg`) with subtle border
- Name as Fraunces h1 with gradient
- Two-line bio: "Data scientist working in genomics. I build tools that make complex data accessible."
- Three buttons: About, Publications, Writing
- Warm aurora gradient accent behind

### 2. Plyranges Spotlight

- Section label: "Something I built"
- Single glass card featuring plyranges
- Brief description: "Tidy data principles for genomic ranges. Part of the tidyomics ecosystem."
- Links: GitHub, Documentation

### 3. Rooms

Five small cards linking to placeholder pages:

| Room | Color | Future Content |
|------|-------|----------------|
| Coffee | peach | Coffee spots, brewing notes |
| Film | violet | Film thoughts, favorites |
| Books | green | Reading log, recommendations |
| Notes + Quotes | coral | Collected quotes, short notes |
| Internet | sky | Links to interesting corners of the web |

Cards use existing room-label color system. Wrap to 2-3 rows on mobile.

### 4. Now

Simple list showing current media consumption:

- **Reading**: Breaking Things at Work (Gavin Mueller), The Wall (Marlen Haushofer)
- **Watching**: Twin Peaks: The Return

Easy to update manually. Can add Playing/Listening categories later.

## Page Flow

```
Hero (welcome + photo)
    ↓
Plyranges Spotlight (credibility)
    ↓
Rooms (personality + exploration)
    ↓
Now (freshness + return visits)
```

## Files to Create/Modify

- `index.qmd` - Complete rewrite with new sections
- `styles.scss` / `styles-dark.scss` - Add hero, rooms grid, now section styles
- `rooms/coffee.qmd` - Placeholder
- `rooms/film.qmd` - Placeholder
- `rooms/books.qmd` - Placeholder
- `rooms/notes.qmd` - Placeholder
- `rooms/internet.qmd` - Placeholder

## Design Tokens

Uses existing Aurora Editorial theme:
- Colors: aurora-peach, aurora-coral, aurora-violet, aurora-green, aurora-sky
- Fonts: Fraunces (headings), Nunito (body)
- Glass card effect for plyranges spotlight
- Room-label color dots already in CSS
