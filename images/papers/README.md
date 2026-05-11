# Paper thumbnails

Drop an image here named `<id>.png` (or `.jpg` / `.webp`) and it will appear on
the matching publication card. The `<id>` is the value in `_data/publications.yaml`.

Current ids:
- omscs-phd-transitions
- cerium-potential
- atomic-ordering
- holographic-imaging

Override behavior: if you set the `image:` field on a publication explicitly
(e.g. `image: "/images/papers/custom.jpg"`), that wins over the auto-resolved
`/images/papers/<id>.png` path.

Suggested dimensions: ~600×400 px (3:2 aspect ratio renders cleanly at the
180×130 card size).
