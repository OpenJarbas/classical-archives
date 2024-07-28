import string
from typing import Iterable, Dict, Optional

import requests


def get_notable_composers() -> Iterable[Dict[str, Optional[str]]]:
    url = "https://www.classicalarchives.com/api/composer_list_notable.json"
    r = requests.get(url).json()
    for comp in r:
        img = comp.get("img")
        yield {
            "composer_id": comp["id"],
            "name": comp["n"],
            "country": comp.get("nat"),
            "birth": comp.get("b"),
            "death": comp.get("d"),
            "image": f"https://www.classicalarchives.com{img}" if img else None
        }


def get_must_know_composers() -> Iterable[Dict[str, Optional[str]]]:
    url = "https://www.classicalarchives.com/api/mustknow_composers.json"

    r = requests.get(url).json()
    for composer_id, title, img in r:
        yield {
            "composer_id": composer_id,
            "name": title,
            "image": f"https://www.classicalarchives.com{img}"
        }


def get_all_composers(data=False) -> Iterable[Dict[str, Optional[str]]]:
    for letter in string.ascii_uppercase:
        url = f"https://www.classicalarchives.com/api/composer_list_all.json?letter={letter}"
        r = requests.get(url).json()
        for comp in r:
            if data:
                d = get_composer_data(comp["id"])
                if "error" in d:
                    continue
                yield d
                continue

            img = comp.get("img")
            yield {
                "composer_id": comp["id"],
                "name": comp["n"],
                "country": comp.get("nat"),
                "birth": comp.get("b"),
                "death": comp.get("d"),
                "image": f"https://www.classicalarchives.com{img}" if img else None
            }


def get_composer_data(composer_id):
    url = f"https://www.classicalarchives.com/api/composer_page.json?composer_id={composer_id}"
    comp = requests.get(url).json()
    albums = [{
        "album_id": a["album_id"],
        "title": a["album_title"],
        "label": a["label_name"],
        "release_date": a["release_date"],
        "image": a["image"]["url"],
        "n_disks": a["n_dsk"],
        "n_tracks": a["n_trk"],
        "duration": a["dur"]
    } for a in comp.get("albums", [])]

    works = [{"work_id": work["id"], "title": work["title"], "category": w["title"]}
             for w in comp.get("works", []) for work in w["children"]]
    img = comp.get("img")
    if "error" in comp:
        return comp
    return {
        "composer_id": composer_id,
        "name": comp["name"],
        "country": comp.get("n"),
        "birth": comp.get("b"),
        "death": comp.get("d"),
        "period": comp.get("p"),
        "image": f"https://www.classicalarchives.com{img}" if img else None,
        "albums": albums,
        "works": works
    }


if __name__ == "__main__":
    for c in get_all_composers(data=True):
        print(c)
        break