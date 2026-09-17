CREATE TABLE IF NOT EXISTS memory_items (id BIGSERIAL PRIMARY KEY, user_id TEXT NOT NULL, content TEXT NOT NULL, created_at TIMESTAMPTZ DEFAULT now());
CREATE INDEX IF NOT EXISTS ix_memory_user ON memory_items(user_id);
