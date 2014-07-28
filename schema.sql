drop table if exists billboard100;

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
