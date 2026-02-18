import duckdb

path = r"all_reviews.csv"
parquet_path = r"steam_reviews.parquet"
con = duckdb.connect()

con.execute(f"""
COPY (
    SELECT
        recommendationid,
        appid,
        game,
        author_steamid,
        author_num_games_owned,
        author_num_reviews,
        author_playtime_forever,
        author_playtime_last_two_weeks,
        author_playtime_at_review,

        TO_TIMESTAMP(timestamp_created) AS timestamp_created,
        TO_TIMESTAMP(timestamp_updated) AS timestamp_updated,
        TO_TIMESTAMP(author_last_played) AS author_last_played,

        CAST(voted_up AS BOOLEAN) AS voted_up,
        CAST(steam_purchase AS BOOLEAN) AS steam_purchase,
        CAST(received_for_free AS BOOLEAN) AS received_for_free,
        CAST(written_during_early_access AS BOOLEAN) AS written_during_early_access,

        votes_up,
        votes_funny,
        weighted_vote_score,
        comment_count,
        language
        -- removing review row for now to greatly improve file size but might add it later
        -- review

    FROM read_csv_auto('{path}', sample_size=100000, max_line_size=20000000)
)
TO '{parquet_path}'
(FORMAT PARQUET, COMPRESSION ZSTD);
""")