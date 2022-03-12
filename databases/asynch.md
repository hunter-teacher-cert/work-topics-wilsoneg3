Challenge 1

 SELECT Teacher, COUNT(Attendance) AS total
    FROM (SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, Date, CourseSection, Attendance, Teacher, Period
    FROM scan AS s
    INNER JOIN periodAtt AS p
    ON s.studentID = p.studentID
    AND substr(ScanTime,1,instr(s.scanTime, ' ')-1) = p.Date
    WHERE p.Attendance = 'A'
    ORDER BY s.Last, s.First ASC) AS allCuts
    GROUP BY Teacher
    ORDER BY TotalCuts DESC
   
