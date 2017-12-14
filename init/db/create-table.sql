drop table if exists tkrprices;
create table tkrprices(tkr varchar, csvd text, csvh text, csvs text);

drop table if exists features;
create table features(tkr varchar, csv text);

drop table if exists unsplit_prices;
create table unsplit_prices(tkr varchar, csvd text, csvh text, csvs text);

drop table if exists predictions;
create table  IF NOT EXISTS
    predictions(
    tkr          VARCHAR
    ,yrs         INTEGER
    ,mnth        VARCHAR
    ,features    VARCHAR
    ,algo        VARCHAR
    ,algo_params VARCHAR
    ,csv         TEXT
    ,kmodel_h5   BYTEA
);