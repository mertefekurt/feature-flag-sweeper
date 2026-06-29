from __future__ import annotations

from feature_flag_sweeper.models import Rule

PROJECT_NAME = 'feature-flag-sweeper'
DESCRIPTION = 'Find stale and risky feature flags in config inventories.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'flag old_checkout enabled true created 2023 owner unknown permanent'
MEDIUM_SAMPLE = '\\b(permanent|no expiry|expires\\s*[:=]\\s*(none|null))\\b'
CLEAN_SAMPLE = 'flag new_search rollout 10 owner product expires 2026-09-01'

RULES = (
    Rule(
        code='ownerless-flag',
        severity='high',
        pattern='\\b(owner\\s*[:=]\\s*(unknown|none|null)|owner unknown)\\b',
        message='feature flag has no owner',
        recommendation='Assign a responsible owner before rollout.',
    ),
    Rule(
        code='permanent-flag',
        severity='medium',
        pattern='\\b(permanent|no expiry|expires\\s*[:=]\\s*(none|null))\\b',
        message='flag has no cleanup date',
        recommendation='Add an expiry date or removal ticket.',
    ),
    Rule(
        code='global-enabled',
        severity='low',
        pattern='\\b(enabled\\s*[:=]\\s*true|rollout\\s*[:=]\\s*100)\\b',
        message='flag appears globally enabled',
        recommendation='Confirm whether the flag can be removed.',
    ),
)
