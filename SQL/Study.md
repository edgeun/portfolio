# SQL 튜닝 수업 노트

안녕하세요, 여러분!  🌟

초보자도 쉽게 배울 수 있도록 오라클 SQL 튜닝 내용을 정리하였습니다.

<img src="https://github.com/edgeun/portfolio-2024/blob/main/001.png" width="600" height="400">

&nbsp;

## 수업 자료( ☀️ 2024년 3월 23일 updated)


- **튜닝 예제 1. SELECT 문의 실행과정 3단계**:  📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#8b876c439d4044d1bbd88315e0623fab)
  
- **튜닝 예제 2. OPTIMIZER**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 3. 실행 계획의 종류 2가지**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 4. WHERE절에 인덱스 컬럼을 가공하지 마세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 5. HAVING절에 일반 검색 조건을 쓰지 마세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 6. WHERE에 인덱스 컬럼 가공이 불가피하다면 함수 기반 인덱스를 생성하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 7. 암시적 형변환에 주의하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 8. ORDER BY절을 통한 과도한 정렬 작업을 피하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 9. 그룹함수 대신에 인덱스를 사용해서 SQL을 튜닝하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 10. 인덱스를 엑세스 하지 못하는 검색조건을 알아야해요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 11. FULL TABLE SCAN을 할 수 밖에 없다면 FULL TABLE SCAN이 빠르게 되도록 튜닝하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 12. 인덱스를 탈 수 있도록 힌트를 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 13. 훌륭한 인덱스 2개를 같이 사용하여 시너지 효과를 볼 수 있어요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 14. 테이블 랜덤 엑세스를 줄이기 위해 결합 컬럼 엑세스를 활용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

- **튜닝 예제 15. 결합 컬럼 인덱스 구성시 컬럼순서가 중요합니다.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 16. INDEX SKIP SCAN 을 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 17. INDEX FULL SCAN을 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 18. INDEX FAST FULL SCAN을 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 19. INDEX BITMAP MERGE SCAN을 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 20. INDEX UNIQUE SCAN을 사용하세요.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)

**튜닝 예제 21. 조인 문장을 튜닝 할 때 조인 순서 튜닝이 중요합니다.**: 📝[노트](https://edgeun.notion.site/0614_SQL-_SELECT-3-ORDER-BY-31af5d2c9de3408aab685a9d020ff7e1#85c82d79b47e47b88182486629d43609)
