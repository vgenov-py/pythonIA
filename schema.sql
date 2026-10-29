CREATE TABLE users (id integer primary key autoincrement, email text unique, pwd text, token text);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE logs (id integer primary key autoincrement, timestamp text not null, msg text);
