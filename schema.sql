drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title varchar(255) not null,
  artist varchar(255),
  album_art varchar(100),
  song_quality varchar(100),
  update_status varchar(100) not null,
  text text not null
);
