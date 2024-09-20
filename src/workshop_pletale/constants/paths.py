from pathlib import Path

import workshop_pletale
from workshop_pletale.constants import metadata

BASE_DIR = Path(workshop_pletale.__file__).resolve().parent

ARTIFACT_ROOT = Path(
    f"/mnt/team/simulation_science/pub/models/{metadata.PROJECT_NAME}/artifacts/"
)
