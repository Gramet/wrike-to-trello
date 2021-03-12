# wrike-to-trello

Helper to import Wrike tasks into a new Trello Board

## Usage

1. Export your Wrike project as an Excel file ([tutorial](https://help.wrike.com/hc/en-us/articles/360037345013-Export-Data-to-Excel))
2. Find out your Trello Api Key and create a Trello Token. ([tutorial](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)) Then add those into the `secrets.json` file. 
3. Create a python virtual environment, pip install the requirements, etc...
4. Run `python xls_to_trello.py --board-name {board_name}` to create a new board and automatically import tasks into newly created lists. If you want to import tasks into an existing board, you can use the `--board-id` parameter instead.