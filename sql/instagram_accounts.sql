-- instagram_accounts schema (generic SQL)
CREATE TABLE instagram_accounts (
  account_id INT PRIMARY KEY,
  "profile pic" BOOLEAN,
  "nums/length username" FLOAT,
  "fullname words" INT,
  "nums/length fullname" FLOAT,
  "name==username" BOOLEAN,
  "description length" INT,
  "external URL" BOOLEAN,
  "private" BOOLEAN,
  "#posts" INT,
  "#followers" INT,
  "#follows" INT,
  "fake" BOOLEAN
);
