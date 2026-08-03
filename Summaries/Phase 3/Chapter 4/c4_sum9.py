'''
Chapter4, topic - migrations basics
'''
# =====================================================================
# 🧠 CORE DEFINITIONS & MECHANICS
# =====================================================================
# Migrations -> Version control blueprints for database structure state.
# Alembic     -> The Python engine comparing code models against real tables.
# upgrade()   -> Auto-generated instructions to push database changes forward.
# downgrade() -> Auto-generated rollback code acting as a precise undo button.
#
# =====================================================================
# ⚡ THE PROFESSIONAL 3-STEP WORKFLOW
# =====================================================================
# Step 1: Edit your local database classes inside `models.py`.
# Step 2: Run `alembic revision --autogenerate -m "descriptive_message"`.
# Step 3: Execute `alembic upgrade head` to safely alter your database layout.
#
# =====================================================================
# ⚠️ LANDMINES & PRODUCTION GUARDRAILS
# =====================================================================
# ❌ NEVER manually delete old migration files from your project history.
# ❌ NEVER push a new NOT NULL column to tables with existing records.
#   - FIX: Use `nullable=True` or provide an explicit default value string.
# 🚀 ALWAYS verify your rollback script locally via `alembic downgrade -1`.
# 🚀 ALWAYS hook your migration command into your cloud deployment step.
