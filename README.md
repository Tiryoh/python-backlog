# pbl
Backlog API V2対応のラッパーライブラリ

# Usage

Install

```bash
pip install python-backlog
```


Code snipet

```python
import base64
import json
from backlog.util import load_conf
from backlog.base import BacklogAPI


def main():
    """
    Load conf.yml
    """
    conf = load_conf("conf.yml")["backlog"]
    api = BacklogAPI(conf["space"], conf["api_key"])

    """
    Project API
    """
    # list project users
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-project-list/
    print("# list project users")
    users = api.project.list_users("SampleProject")
    print(json.dumps(users, indent=2))


    """
    Wiki API
    """
    # list wikis
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-wiki-page-list/
    print("# list wikis")
    wikis = api.wiki.list("SampleProject")
    print(json.dumps(wikis[0], indent=2))

    # get attachment
    # https://developer.nulab-inc.com/ja/docs/backlog/api/2/get-issue-attachment/
    print("# get attachment")
    wiki = [w for w in api.wiki.list("SampleProject") if len(w["attachments"]) > 0][0]
    attachment = api.wiki.get_attachment(
        wikiId=wiki["id"],
        attachmentId=wiki["attachments"][0]["id"])
    attachment["data"] = base64.b64encode(attachment["data"]).decode()
    print(json.dumps(attachment, indent=2))


if __name__ == "__main__":
    main()
```

# Auth

Oct 2018, Currently API Key is supported. NOT support OAuth2 yet.

API Client object is initialized with arguments credentials(space and api_key).

This package provides a helper function to loading config yaml. This helper function is provided by `backlog.util.load_conf` .

load_conf takes an argument path to yaml file. By defalt, `./conf.yml` is given.

# See also

Qiita https://qiita.com/hassaku_63/items/b9eb2a1c7ecd3c19507d

# Contact

Twitter: [hassaku63](https://twitter.com/hassaku_63)

# License

## Acknowledgements

### [netmarkjp/pybacklog](https://github.com/netmarkjp/pybacklog)

```
Copyright 2017 Toshiaki Baba

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
```

`backlog/base.py` includes codes from [pybacklog](https://github.com/netmarkjp/pybacklog/blob/78099cbd70c4997829f714dff82285eaa0fd8169/pybacklog/__init__.py#L17-L47).  See commit log( [`6ac57cb40f4a8c410c81abdab467e9b98575afa5`](https://github.com/hassaku63/pbl/commit/6ac57cb40f4a8c410c81abdab467e9b98575afa5) ) for details.
