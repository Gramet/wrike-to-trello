import json
from trello import TrelloApi
import pandas as pd
import argparse
from tqdm import tqdm


def xls_to_trello(args):
    with open("secrets.json", "r") as f:
        d = json.load(f)

    TRELLO_KEY = d["apikey"]
    TRELLO_TOKEN = d["token"]

    trello = TrelloApi(TRELLO_KEY)
    trello.set_token(TRELLO_TOKEN)

    if args.board_id is None:
        board = trello.boards.new(args.board_name)
        BOARD_ID = board["id"]
    else:
        BOARD_ID = args.board_id

    df = pd.read_excel(args.path)
    lists = {}
    for name in df["Custom status"].unique():
        lists[name] = trello.boards.new_list(board["id"], name)

    for _, row in tqdm(df.iterrows(), desc="Exporting tasks", total=len(df)):
        list_id = lists[row["Custom status"]]["id"]
        trello.lists.new_card(
            list_id,
            row["Title"],
            due=None if pd.isna(row["End Date"]) else row["End Date"],
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="XLS to trello")
    parser.add_argument("--path", type=str, help="The xls from wrike", default=None)
    parser.add_argument(
        "--board-id",
        type=str,
        default=None,
        help="board id if already existing",
    )
    parser.add_argument(
        "--board-name",
        type=str,
        default="testapi",
        help="board id if already existing",
    )

    args = parser.parse_args()
    xls_to_trello(args)
