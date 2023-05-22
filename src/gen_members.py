import yaml
from lxml import etree
from yattag import Doc


with open("src/members.yaml", "r") as file:
    members = yaml.safe_load(file)


doc, tag, text = Doc().tagtext()
title_map = {
    "PI": "Principal Investigators",
    "PD": "Postdoctoral Fellows",
    "GS": "Graduate Students",
    "US": "Undergraduate Students",
    "Alumni": "Alumni",
}

for role in ["PI", "PD", "GS", "US", "Alumni"]:
    with tag("h3"):
        text(title_map[role])

    with tag("div", ("class", "team-container")):
        for member in [member for member in members if members[member]["role"] == role]:
            with tag(
                "a",
                ("class", "team-member"),
                href=members[member]["href"],
                target="_blank",
                rel="noopener noreferrer",
            ):
                with tag(
                    "img",
                    ("class", "team-member-icon"),
                    src="imgs/"
                    + (
                        members[member]["img"]
                        if "img" in members[member]
                        else "UniversitySeal.png"
                    ),
                    alt=member,
                ):
                    pass
                with tag("div", ("class", "team-member-name")):
                    text(member)

result = doc.getvalue()
with open("members.html", "w") as file:
    file.write(result)
