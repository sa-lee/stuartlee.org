# Accessibility Fixes Plan

## Overview

Address WCAG 2.1 AA compliance issues identified in the Aurora Editorial theme.

## P0 Fixes (Critical)

### 1. Add Focus States

Add visible `:focus-visible` styles for all interactive elements:

```scss
// Focus styles using aurora colors
a:focus-visible,
button:focus-visible,
.btn:focus-visible,
input:focus-visible,
select:focus-visible,
textarea:focus-visible {
  outline: 3px solid $aurora-peach;
  outline-offset: 2px;
}

// Dark mode uses brighter outline
// Same pattern but with adjusted colors
```

Apply to: links, buttons, form inputs, room cards, nav links.

### 2. Fix Link Contrast

**Light mode:**
- Current: `#c96b54` (~3.5:1)
- Fix: Darken to `#b85a45` or similar (~4.8:1)

**Dark mode:**
- Current: `#ffb385` - actually OK at ~8:1
- Keep as-is

### 3. Fix Button Contrast

**Light mode primary button:**
- Current: White text on coral/peach gradient
- Fix: Use `$warm-gray-900` (#2d2a26) for text instead of white

**Light mode secondary button:**
- Current: `$warm-gray-700` on light blue
- Should be OK, verify after primary fix

## P1 Fixes (Important)

### 4. Add Reduced Motion Support

```scss
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### 5. Gradient Text Fallback

```scss
h1.hero-title {
  color: $aurora-coral; // Fallback for high contrast mode
  background: linear-gradient(...);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;

  @media (forced-colors: active) {
    background: none;
    -webkit-text-fill-color: currentColor;
  }
}
```

## P2 Fixes (Nice to Have)

### 6. Increase Touch Targets

```scss
.btn,
a.btn-primary,
a.btn-secondary {
  min-height: 44px;
  min-width: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

### 7. Hide Decorative Star

```scss
.section-label::before {
  content: '✦';
  // ... existing styles
  speak: never; // Hide from screen readers
}
```

Or in HTML, wrap with `aria-hidden="true"`.

### 8. Skip Link (Optional)

Add to site layout - requires Quarto template customization. Lower priority.

## Files to Modify

- `styles.scss` - Light theme fixes
- `styles-dark.scss` - Dark theme fixes

## Testing

After implementation:
1. Tab through entire site - verify focus visible on all interactive elements
2. Use browser contrast checker on links and buttons
3. Enable "reduce motion" in OS settings - verify no animations
4. Test with Windows High Contrast Mode
5. Test with screen reader (VoiceOver/NVDA)
