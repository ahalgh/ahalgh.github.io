# Project thumbnails

Drop an image here named `<id>.png` (or `.jpg` / `.webp`) and it will appear on
the matching project card. The `<id>` is the value in `_data/projects.yaml`.

Current ids:
- tactical-llm-chatbot
- hea-strength-prediction
- nmt-en-de
- autonomous-ai

Override behavior: if you set the `image:` field on a project explicitly
(e.g. `image: "/images/projects/custom.jpg"`), that wins over the auto-resolved
`/images/projects/<id>.png` path.

Suggested dimensions: ~600×400 px (3:2 aspect ratio renders cleanly at the
180×130 card size).
