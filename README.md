# Classical Archives

Python package to fetch information about classical composers from [Classical Archives](https://www.classicalarchives.com)


```python
from classical_archives import get_notable_composers, get_must_know_composers, get_all_composers, get_composer_data

# Get must-know composers
for composer in get_must_know_composers():
    print(composer)
    # {'composer_id': 2039, 'name': 'Albéniz, Isaac', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2039.jpg'}
    # {'composer_id': 2113, 'name': 'Bach, J.S.', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2113.jpg'}
    # {'composer_id': 2130, 'name': 'Barber, Samuel', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2130.jpg'}
    # {'composer_id': 2144, 'name': 'Bartók, Béla', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2144.jpg'}
    # {'composer_id': 2156, 'name': 'Beethoven, Ludwig van', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2156.jpg'}
    # ...

    
# Get notable composers
for composer in get_notable_composers():
    print(composer)
    # {'composer_id': 6220, 'name': 'Adams, John', 'country': 'USA', 'birth': '1947/02/15', 'death': None, 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/6220.jpg'}
    # 'composer_id': 2031, 'name': 'Agricola, Alexander', 'country': 'FLM', 'birth': '1446', 'death': '1506', 'image': None}
    # {'composer_id': 2039, 'name': 'Albéniz, Isaac', 'country': 'ESP', 'birth': '1860', 'death': '1909', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2039.jpg'}
    # {'composer_id': 2041, 'name': 'Albinoni, Tomaso Giovanni', 'country': 'ITA', 'birth': '1671', 'death': '1751', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/2041.jpg'}
    # {'composer_id': 13583, 'name': 'Antheil, George', 'country': 'USA', 'birth': '1900/07/08', 'death': '1959/02/12', 'image': 'https://www.classicalarchives.com/images/artists_cma/wp/13583.jpg'}
    # {'composer_id': 2075, 'name': 'Arcadelt, Jacob', 'country': 'FRA', 'birth': 'c. 1505', 'death': '1568', 'image': None}
    # ....
    

# Get composer data by ID
composer_id = '28676'
composer_data = get_composer_data(composer_id)
print(composer_data)
# {'composer_id': 28676, 
# 'name': 'Thorvald Aagaard', 
# 'country': 'DNK', 
# 'birth': None,
# 'death': '(1877/06/08-1937/03/22)',
# 'period': 'Modern', 
# 'image': None, 
# 'albums': [{'album_id': 20775, 'title': 'A Danish Christmas', 'label': 'Naxos', 'release_date': '1999-12-09', 'image': 'https://cdn.prs.net/cov/da/f2/daf2460007675cf392946f3e4eeb7659_100.jpg', 'n_disks': 1, 'n_tracks': 31, 'duration': 4593}, {'album_id': 23032, 'title': 'Danish Christmas Music', 'label': 'Naxos', 'release_date': '1997-12-09', 'image': 'https://cdn.prs.net/cov/26/cc/26cc88e044a8fa69ad69320d341f921f_100.jpg', 'n_disks': 1, 'n_tracks': 25, 'duration': 3887}, {'album_id': 69070, 'title': 'Drømte mig en drøm: Danske sange', 'label': 'OUR Recordings', 'release_date': '2013-01-01', 'image': 'https://cdn.prs.net/cov/72/c5/72c57bf3d48a8de8f3a3df3b16c73866_100.jpg', 'n_disks': 1, 'n_tracks': 22, 'duration': 3983}],
# 'works': [{'work_id': 282772, 'title': 'Sneflokke kommer vrimlende', 'category': 'Miscellaneous'}, {'work_id': 282781, 'title': 'Spurven sidder stum bag kvist', 'category': 'Miscellaneous'}, {'work_id': 955303, 'title': 'Spurven sidder stum bag kvist (The Sparrow Silent on the Bough), song', 'category': 'Vocal Works'}]}


# Get all composers
for composer in get_all_composers():
    print(composer)
    # {'composer_id': 28676, 'name': 'Aagaard, Thorvald', 'country': 'DNK', 'birth': '1877/06/08', 'death': '1937/03/22', 'image': None}
    # {'composer_id': 1, 'name': 'Aaires, André Abel', 'country': 'PRT', 'birth': '1987', 'death': None, 'image': None}
    # {'composer_id': 32055, 'name': 'Aaltoila, Heikki', 'country': 'FIN', 'birth': '1905', 'death': '1992', 'image': None}
    # {'composer_id': 95715, 'name': 'Abad, Eduardo Flores', 'country': 'ECU', 'birth': '1960', 'death': None, 'image': None}
    # ...
    


# Get all composers + query composer info
for composer in get_all_composers(data=True):
    print(composer)
    # {'composer_id': 28676, 
    # 'name': 'Thorvald Aagaard', 
    # 'country': 'DNK', 
    # 'birth': None,
    # 'death': '(1877/06/08-1937/03/22)',
    # 'period': 'Modern', 
    # 'image': None, 
    # 'albums': [{'album_id': 20775, 'title': 'A Danish Christmas', 'label': 'Naxos', 'release_date': '1999-12-09', 'image': 'https://cdn.prs.net/cov/da/f2/daf2460007675cf392946f3e4eeb7659_100.jpg', 'n_disks': 1, 'n_tracks': 31, 'duration': 4593}, {'album_id': 23032, 'title': 'Danish Christmas Music', 'label': 'Naxos', 'release_date': '1997-12-09', 'image': 'https://cdn.prs.net/cov/26/cc/26cc88e044a8fa69ad69320d341f921f_100.jpg', 'n_disks': 1, 'n_tracks': 25, 'duration': 3887}, {'album_id': 69070, 'title': 'Drømte mig en drøm: Danske sange', 'label': 'OUR Recordings', 'release_date': '2013-01-01', 'image': 'https://cdn.prs.net/cov/72/c5/72c57bf3d48a8de8f3a3df3b16c73866_100.jpg', 'n_disks': 1, 'n_tracks': 22, 'duration': 3983}],
    # 'works': [{'work_id': 282772, 'title': 'Sneflokke kommer vrimlende', 'category': 'Miscellaneous'}, {'work_id': 282781, 'title': 'Spurven sidder stum bag kvist', 'category': 'Miscellaneous'}, {'work_id': 955303, 'title': 'Spurven sidder stum bag kvist (The Sparrow Silent on the Bough), song', 'category': 'Vocal Works'}]}

```