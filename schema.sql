drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title varchar(255) not null,
  artist varchar(255),
  album varchar(255),
  new_title varchar(255),
  new_artist varchar(255),
  new_album varchar(255),
  update_status varchar(100) not null,
  notes text
);
