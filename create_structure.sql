CREATE TABLE IF NOT EXISTS %s (
  id bigint NOT NULL AUTO_INCREMENT,
  AverageMark FLOAT NOT NULL,
  FullName varchar(100) NOT NULL,
  StuNumb bigint NOT NULL,
  GroupName varchar(100) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
