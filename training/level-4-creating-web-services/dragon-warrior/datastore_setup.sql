drop table if exists friends;
create table friends (
  internal_id integer primary key autoincrement,
  id text not null,
  firstName text not null,
  lastName text not null,
  telephone text not null,
  email text not null,
  notes text not null
);

INSERT INTO friends (id, firstName, lastName, telephone, email, notes)
VALUES ('BFP', 'Big Fat', 'Panda', '574-213-0726', 'mike@eikonomega.com', 'My bestest friend in all the world.');

