drop table if exists entries;
drop table if exists billboard100;
create table entries (
  id integer primary key autoincrement,
  title varchar(255) not null,
  artist varchar(255),
  album varchar(255),
  new_title varchar(255),
  new_artist varchar(255),
  new_album varchar(255),
  quality varchar(100),
  edits varchar(255),
  update_status varchar(100) not null,
  notes text
);

create table billboard100(
  rank integer primary key not null,
  title varchar(255) not null,
  artist varchar(255) not null,
  album varchar(255),
  peakPos integer not null,
  lastPos integer not null,
  weeks integer not null,
  rankChange varchar(100) not null
);
