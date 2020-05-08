CREATE DATABASE IF NOT EXISTS cnt_gossip;

CREATE TABLE cnt_gossip.recent_peers(
    recent_peers_id SERIAL,
    peer_id varchar(64) default null,
    host varchar(64) not null,
    port tinyint not null,
    table_ts  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(recent_peers_id),
    KEY bypid(peer_id),
    KEY byhost(host),
    KEY byport(port),
    KEY bytts(table_ts)
) ENGINE=MYISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;