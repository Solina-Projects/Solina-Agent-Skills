---
name: accessibility
description: |
  Android accessibility for AI agents. Use this skill whenever implementing accessibility,
  TalkBack support, content descriptions, semantic properties, touch target sizes, contrast
  ratios, screen reader support, contentDescription, semantics modifier, clearAndSetSemantics,
  mergeDescendants, heading, stateDescription, traversalOrder, custom actions, live regions,
  accessibility service, WCAG compliance, accessibility audit, or any Compose accessibility.
  Required for Play Store submission in many markets. Always apply before shipping any screen.
---

# Android Accessibility

Accessibility is not optional — it's required by law in many markets and checked by the Play Store.

<!-- MUSE-ADAPT -->

## Muse adaptation — read first

This skill runs inside Muse's own environment, for Nasser. Where the original instructions below conflict with these points, these points win.

- Host: Linux VM (4 CPU, ~7 GB RAM, x86_64), no GPU. Toolchains live under the home directory only; never rely on system installs. For npm, always set npm_config_cache=/tmp/npm-cache.
- The user (Nasser) is Persian-speaking and phone-only; he has no computer. Deliverables reach him as files in this chat. Explain everything in simple Persian and translate every English label - his English is effectively zero.
- Register: two-way, comfortable, street-style, blunt and honest. No formalities.
- Never ask design-detail questions. Decide, build, then report shortly.
- For Nasser's own work, follow the decisions already recorded in memory (Solina-Player design, Lunaris alioth kernel and ROM, Solina-Launcher). Solina apps are Kotlin + Jetpack Compose + Material 3 Expressive, RTL Persian, Vazirmatn; never copy another app's branding.
- UI copy: Persian first, Western (English) digits only, no em dashes in UI copy.
- Apply quality gates silently. Never paste internal gate or lint reports to the user; report outcomes in a few lines.
- Secrets never go into files, memory or chat output. Publishing anything publicly needs his explicit approval first.
- The original skill may name Claude Code tools (Read, Write, Edit, Glob, Grep, Bash) or other agents' commands. Use Muse's own tools instead (file read/write/edit, shell, browser). Use the browser tools for live pages and real-site screenshots.
## Rule 1: Content descriptions for all interactive elements

```kotlin
// ✅ Every non-text interactive element needs contentDescription
IconButton(onClick = onLike) {
    Icon(
        imageVector = if (isLiked) Icons.Filled.Favorite else Icons.Outlined.FavoriteBorder,
        contentDescription = if (isLiked) "Remove from favorites" else "Add to favorites"
        // Describe the ACTION, not the icon name
    )
}

// ✅ Image with context
AsyncImage(
    model = imageUrl,
    contentDescription = "$productName product image"  // meaningful description
)

// ✅ Decorative images — explicitly null
Icon(Icons.Default.Star, contentDescription = null)  // decorative, screen reader skips it

// ❌ Generic description
Icon(Icons.Default.Favorite, contentDescription = "icon")  // useless to screen reader
```

## Rule 2: Minimum touch target — 48×48dp

```kotlin
// ✅ Ensure minimum touch target size
@Composable
fun SmallIconButton(onClick: () -> Unit, icon: ImageVector, contentDescription: String) {
    Box(
        modifier = Modifier
            .size(48.dp)                     // minimum touch target
            .clickable(
                onClick = onClick,
                interactionSource = remember { MutableInteractionSource() },
                indication = rememberRipple(bounded = false)
            ),
        contentAlignment = Alignment.Center
    ) {
        Icon(
            imageVector = icon,
            contentDescription = contentDescription,
            modifier = Modifier.size(24.dp)  // visual size separate from touch target
        )
    }
}

// ✅ Or use minimumInteractiveComponentSize modifier
Icon(
    imageVector = icon,
    contentDescription = description,
    modifier = Modifier.minimumInteractiveComponentSize()  // auto 48dp touch target
)
```

## Rule 3: Semantic properties for complex components

```kotlin
// ✅ Card — merge all content for TalkBack
@Composable
fun ProductCard(product: Product, onAddToCart: () -> Unit) {
    Card(
        modifier = Modifier.semantics(mergeDescendants = true) {}
        // TalkBack reads all child text as one item: "Blue T-Shirt, $29.99, In stock"
    ) {
        Column {
            Text(product.name)
            Text("$${product.price}")
            Text(if (product.inStock) "In stock" else "Out of stock")
            Button(onClick = onAddToCart) { Text("Add to cart") }
        }
    }
}

// ✅ Custom state description
Switch(
    checked = isEnabled,
    onCheckedChange = onToggle,
    modifier = Modifier.semantics {
        stateDescription = if (isEnabled) "Notifications on" else "Notifications off"
    }
)

// ✅ Mark as heading for navigation
Text(
    text = "Today's Orders",
    style = MaterialTheme.typography.titleLarge,
    modifier = Modifier.semantics { heading() }
)

// ✅ Custom action — add actions TalkBack can trigger
LazyColumn {
    items(items) { item ->
        SwipeableItemCard(
            item = item,
            modifier = Modifier.semantics {
                customActions = listOf(
                    CustomAccessibilityAction("Delete ${item.title}") {
                        onDelete(item.id)
                        true
                    },
                    CustomAccessibilityAction("Archive ${item.title}") {
                        onArchive(item.id)
                        true
                    }
                )
            }
        )
    }
}
```

## Rule 4: Color contrast — WCAG AA minimum

```kotlin
// ✅ Use Material 3 color roles — contrast is guaranteed by the spec
Text(
    text = "Important message",
    color = MaterialTheme.colorScheme.onSurface   // guaranteed contrast on Surface
)

// ✅ Check custom colors with contrast tool
// onSurface on Surface: contrast ratio ≥ 4.5:1 (WCAG AA)
// onPrimary on Primary: contrast ratio ≥ 4.5:1

// ❌ Custom colors without contrast check
Text(text = "Label", color = Color(0xFF888888))   // gray on white = likely fails WCAG
```

## Rule 5: Screen reader traversal order

```kotlin
// ✅ Control traversal order for complex layouts
@Composable
fun ProductHeader(name: String, price: String, rating: Float) {
    Row(modifier = Modifier.semantics { isTraversalGroup = true }) {
        Column(modifier = Modifier.weight(1f)) {
            Text(name, modifier = Modifier.semantics { traversalIndex = 0f })
            Text(price, modifier = Modifier.semantics { traversalIndex = 1f })
        }
        RatingBar(rating, modifier = Modifier.semantics { traversalIndex = 2f })
    }
}
```

## Rule 6: Live regions for dynamic content

```kotlin
// ✅ Announce changes to screen reader users
Text(
    text = "Found ${results.size} results",
    modifier = Modifier.semantics {
        liveRegion = LiveRegionMode.Polite  // announced when content changes, doesn't interrupt
    }
)

// LiveRegionMode.Assertive — interrupts current speech (use sparingly)
Text(
    text = errorMessage,
    modifier = Modifier.semantics {
        liveRegion = LiveRegionMode.Assertive  // for critical errors only
    }
)
```

## Accessibility checklist (run before every release)

- [ ] All interactive elements have meaningful `contentDescription`
- [ ] All touch targets are ≥ 48×48dp
- [ ] Cards and list items use `mergeDescendants = true`
- [ ] Color-only information has a text/shape alternative
- [ ] All text passes 4.5:1 contrast ratio (WCAG AA)
- [ ] Headings marked with `heading()` semantic
- [ ] Swipeable actions have `customActions` for TalkBack users
- [ ] Dynamic content uses live regions
- [ ] Tested with TalkBack enabled and touch exploration
