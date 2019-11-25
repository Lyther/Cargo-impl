# MySQL 8.0.16
use sustechbus;
##### stops #####
START TRANSACTION ;
INSERT INTO stops (id, name) VALUES (0, 'Joy Highland (JH)');
INSERT INTO stops (id, name) VALUES (1, 'Wisdom Valley (WV)');
INSERT INTO stops (id, name) VALUES (2, 'Innovation Park (IP)');
INSERT INTO stops (id, name) VALUES (3, 'Lychee Hill (LH)');
INSERT INTO stops (id, name) VALUES (4, 'New Student Dormitory (NSD)');
INSERT INTO stops (id, name) VALUES (5, 'Social Health Center (SHC)');
INSERT INTO stops (id, name) VALUES (6, 'Staff Restaurant (SR)');
INSERT INTO stops (id, name) VALUES (7, 'Expert Appartment (EA)');
INSERT INTO stops (id, name) VALUES (8, 'Gate 3 (G3)');
INSERT INTO stops (id, name) VALUES (9, 'IPark (IPARK)');
INSERT INTO stops (id, name) VALUES (10, 'Gate 1 (G1)');
INSERT INTO stops (id, name) VALUES (11, 'Administration Building (AB)');
INSERT INTO stops (id, name) VALUES (12, 'Gate 7 (G7)');
INSERT INTO stops (id, name) VALUES (13, 'Research Building (RB)');
COMMIT ;
##### lines #####
START TRANSACTION ;
INSERT INTO `lines` (id, start, end, name, type) VALUES (0, 0, 13, 'normal-JH2RB', 'normal');
INSERT INTO `lines` (id, start, end, name, type) VALUES (1, 13, 0, 'normal-RB2JH', 'normal');
INSERT INTO `lines` (id, start, end, name, type) VALUES (2, 0, 13, 'peak-JH2RB', 'peak');
INSERT INTO `lines` (id, start, end, name, type) VALUES (3, 13, 0, 'peak-RB2JH', 'peak');
COMMIT ;
##### lines details #####
START TRANSACTION ;
# normal-JH2RB
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 0, 0);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 1, 1);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 2, 2);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 3, 3);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 4, 4);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 5, 5);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 6, 6);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 7, 7);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 8, 8);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 10, 9);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 11, 10);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 12, 11);
INSERT INTO stopsinline (line, stop, ord) VALUES (0, 13, 12);
# normal-RB2JH
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 13, 0);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 12, 1);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 11, 2);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 10, 3);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 8, 4);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 7, 5);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 6, 6);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 5, 7);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 4, 8);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 1, 9);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 2, 10);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 3, 11);
INSERT INTO stopsinline (line, stop, ord) VALUES (1, 0, 12);
# peak-JH2RB
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 0, 0);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 1, 1);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 3, 2);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 4, 3);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 6, 4);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 12, 5);
INSERT INTO stopsinline (line, stop, ord) VALUES (2, 13, 6);
# peak-RB2JH
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 13, 0);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 12, 1);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 6, 2);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 4, 3);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 1, 4);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 3, 5);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 1, 6);
INSERT INTO stopsinline (line, stop, ord) VALUES (3, 0, 7);
COMMIT ;