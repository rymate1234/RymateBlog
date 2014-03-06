drop table if exists entries;
drop table if exists users;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);

create table users# (
  id integer primary key autoincrement,
  username text not null,
  password text not null
);