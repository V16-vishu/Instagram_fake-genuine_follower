-- Basic counts
SELECT
  COUNT(*) AS total_accounts,
  SUM(CASE WHEN "fake" = TRUE THEN 1 ELSE 0 END) AS total_fake,
  SUM(CASE WHEN "fake" = FALSE THEN 1 ELSE 0 END) AS total_genuine
FROM instagram_accounts;

-- Profile picture vs fake/genuine
SELECT
  "profile pic" AS has_profile_pic,
  "fake",
  COUNT(*) AS cnt
FROM instagram_accounts
GROUP BY 1, 2
ORDER BY 1, 2;

-- Follower/Following ratio
SELECT
  account_id,
  "#followers" AS follower_count,
  "#follows"   AS following_count,
  CASE WHEN "#follows" = 0 THEN NULL
       ELSE ROUND(CAST("#followers" AS NUMERIC) / "#follows", 2) END AS follower_following_ratio,
  "fake"
FROM instagram_accounts;

-- Username/fullname patterns
SELECT
  "fake",
  AVG("nums/length username") AS avg_username_metric,
  AVG("nums/length fullname") AS avg_fullname_metric,
  AVG("fullname words")       AS avg_fullname_words
FROM instagram_accounts
GROUP BY "fake";

-- Private vs fake/genuine
SELECT
  "private",
  "fake",
  COUNT(*) AS cnt
FROM instagram_accounts
GROUP BY 1, 2
ORDER BY 1, 2;
