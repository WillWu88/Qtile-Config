# This file configures the different work spaces
from libqtile.config import Group, Match

groups = [
        Group("1", layout="monadtall", label="SCH"),
        Group("2", label="DOC"),
        Group("3", label="ORG"),
        Group("4", label="PRO"),
        Group("5", label="ENT"),
        Group("6", layout="floating", label="FLT",
              matches=[Match(wm_class='MATLAB R2021a - academic use'),
              Match(wm_class='com-yworks-A-yEd')]),

]
