from django.db import models


class TypeChoices(models.TextChoices):
    RALLY = "Rally", "Rally",
    OPENWHEEL = "Open-wheel", "Open-wheel",
    KART = "Kart", "Kart",
    DRAG = "Drag", "Drag",
    OTHER = "Other", "Other",
