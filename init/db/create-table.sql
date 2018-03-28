drop table if exists tkrprices;
create table tkrprices(tkr VARCHAR(36), csvd LONGTEXT, csvh LONGTEXT, csvs LONGTEXT);

drop table if exists features;
create table features(tkr VARCHAR(36), csv LONGTEXT);

drop table if exists unsplit_prices;
create table unsplit_prices(tkr VARCHAR(36), csvd LONGTEXT, csvh LONGTEXT, csvs LONGTEXT);

drop table if exists predictions;
create table  IF NOT EXISTS
    predictions(
    tkr          VARCHAR(36)
    ,yrs         INTEGER
    ,mnth        VARCHAR(100)
    ,features    VARCHAR(100)
    ,algo        VARCHAR(100)
    ,algo_params VARCHAR(100)
    ,csv         LONGTEXT
    ,kmodel_h5   LONGBLOB
);