---
title: {{ .Title | jsonify }}
url: {{ .Permalink | jsonify }}
{{- with .Description }}
description: {{ . | jsonify }}
{{- end }}
{{- if not .Date.IsZero }}
date: {{ .Date.Format "2006-01-02T15:04:05Z07:00" | jsonify }}
{{- end }}
{{- with .Params.tags }}
tags: {{ . | jsonify }}
{{- end }}
{{- with .Params.categories }}
categories: {{ . | jsonify }}
{{- end }}
---

{{ transform.HTMLToMarkdown .Content | htmlUnescape }}
