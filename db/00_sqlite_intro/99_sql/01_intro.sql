-- 주석
/* SQL구문은 대소문자 구분x(중요)
  기본 문법(변하지 않는 부분 - 대문자)
  변하는 부분 - 소문자
*/
-- 데이터 전체 조회
SELECT * FROM examples;
select * from examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제 (테이블 자체를 삭제, 내용 삭제는 truncate)
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES
('홍길동', 25, '서울'),
('김철수', 24, '대전'),
('이싸피', 23, '광주'),
('박삼성', 28, '구미'),
('최전자', 27, '부산');

SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='부산';
SELECT DISTINCT age FROM classmates;

SELECT rowid, * FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

INSERT INTO classmates VALUES ('최전자', 28, '부산');

-- 데이터 수정
UPDATE classmates SET
name='홍길동',
address='제주도'
WHERE rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age >= 30;
SELECT first_name FROM users WHERE age >= 30;
SELECT * FROM users WHERE age >= 30 AND last_name="김";

-- Sqlite Functions
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%-5114-%';

-- ORDER BY
SELECT rowid, * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age, balance DESC; -- 같은 age에 대해 balance로 내림차순
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age ASC, last_name ASC LIMIT 10;

-- GROUP BY
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name; -- 나중에 서브쿼리떄 많이 쓴다.

-- ALTER TABLE
CREATE TABLE articles(
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번 내용');

ALTER TABLE articles RENAME TO news;
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL; -- Error: Cannot add a NOT NULL column with default value NULL

ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES ('제목', '내용', datetime('now'));
SELECT * FROM news;

ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '임시제목';
SELECT * FROM news;


-- 210914 HW
CREATE TABLE test (
name TEXT,
age INT,
address TEXT
);

INSERT INTO test (name, age, address) VALUES('홍길동', 20, 'seoul');
INSERT INTO test VALUES('홍길동', 20, 'seoul');
insert into test values(address='seoul', age=20, name='홍길동'); -- 에러
insert into test (address, age, name) values('seoul', 20, '홍길동');

-- 210914 Workshop
--1)
CREATE TABLE countries (
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

--2)
INSERT INTO countries VALUES('B203', '2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries VALUES('1102', '2020-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries VALUES('303', '2020-01-01', '2020-01-03', 'deluxe', 500);
INSERT INTO countries VALUES('807', '2020-01-04', '2020-01-07', 'superior', 300 );

--3)
ALTER TABLE countries RENAME TO hotels;

--4)
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

--5)
SELECT grade, COUNT(*) AS grade_count FROM hotels GROUP BY grade ORDER BY grade_count;

--6)
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade="deluxe";

--7)
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in="2020-01-04" ORDER BY price;