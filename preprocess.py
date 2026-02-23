import duckdb

path = r"all_reviews.csv"
parquet_path = r"steam_reviews.parquet"
clean_path = r"steam_reviews_clean.parquet"
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
        language,
        review
        
    FROM read_csv_auto('{path}', sample_size=100000, max_line_size=20000000)
)
TO '{parquet_path}'
(FORMAT PARQUET, COMPRESSION ZSTD);
""")


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
        language,
        (timestamp_updated > timestamp_created) AS is_edited
        -- removing review row to greatly improve file size as decided it was unnecesarry to include

    FROM read_csv_auto(
        '{path}',
        sample_size=100000,
        max_line_size=20000000
    )
    WHERE 
        language = 'english' AND
        author_num_reviews <= 600 AND
        author_playtime_forever >= 10 AND
        TO_TIMESTAMP(timestamp_created) < TIMESTAMP '2023-11-01' AND
        review IS NOT NULL AND LENGTH(review) < 5000
)
TO '{clean_path}'
(FORMAT PARQUET, COMPRESSION ZSTD);
""")
