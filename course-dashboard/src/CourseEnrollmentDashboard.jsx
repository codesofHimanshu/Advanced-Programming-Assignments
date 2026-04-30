import React, { useMemo, useState } from "react";

export default function CourseEnrollmentDashboard() {

  // ---------- STATE ----------
  const [studentsMap, setStudentsMap] = useState(
    new Map([
      [1, { id: 1, name: "Aman", enrolledCourses: new Set(["Java", "DSA"]), gpa: 8.7 }],
      [2, { id: 2, name: "Riya", enrolledCourses: new Set(["Python", "Java"]), gpa: 9.1 }],
      [3, { id: 3, name: "Kunal", enrolledCourses: new Set(["DSA"]), gpa: 7.5 }]
    ])
  );

  const [filterCourse, setFilterCourse] = useState("");

  // 🔥 NEW FORM STATE
  const [name, setName] = useState("");
  const [gpa, setGpa] = useState("");
  const [courses, setCourses] = useState("");

  // ---------- ADD STUDENT ----------
  const addStudent = () => {
    if (!name || !gpa || !courses) {
      alert("Fill all fields");
      return;
    }

    if (isNaN(gpa)) {
      alert("Enter valid GPA");
      return;
    }

    const newStudent = {
      id: Date.now(),
      name,
      gpa: parseFloat(gpa),
      enrolledCourses: new Set(
        courses.split(",").map(c => c.trim()).filter(c => c)
      )
    };

    setStudentsMap(prev => {
      const newMap = new Map(prev); // no mutation
      newMap.set(newStudent.id, newStudent);
      return newMap;
    });

    // clear inputs
    setName("");
    setGpa("");
    setCourses("");
  };

  // ---------- REMOVE STUDENT ----------
  const removeStudent = (id) => {
    setStudentsMap(prev => {
      const newMap = new Map(prev);
      newMap.delete(id);
      return newMap;
    });
  };

  // ---------- SORT BY GPA ----------
  const sortedStudents = useMemo(() => {
    return [...studentsMap.values()].sort((a, b) => b.gpa - a.gpa);
  }, [studentsMap]);

  // ---------- UNIQUE COURSES ----------
  const uniqueCourses = useMemo(() => {
    return [...studentsMap.values()].reduce((acc, student) => {
      student.enrolledCourses.forEach(c => acc.add(c));
      return acc;
    }, new Set());
  }, [studentsMap]);

  // ---------- FILTER ----------
  const filteredStudents = useMemo(() => {
    if (!filterCourse) return sortedStudents;

    return sortedStudents.filter(student =>
      student.enrolledCourses.has(filterCourse)
    );
  }, [filterCourse, sortedStudents]);

  // ---------- RENDER ----------
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>Course Enrollment Dashboard</h2>

      {/* 🔥 INPUT FORM */}
      <div style={{ marginBottom: "15px" }}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          style={{ marginRight: "5px" }}
        />

        <input
          type="number"
          placeholder="GPA"
          value={gpa}
          onChange={(e) => setGpa(e.target.value)}
          style={{ marginRight: "5px" }}
        />

        <input
          type="text"
          placeholder="Courses (comma separated)"
          value={courses}
          onChange={(e) => setCourses(e.target.value)}
          style={{ marginRight: "5px" }}
        />

        <button onClick={addStudent}>Add Student</button>
      </div>

      {/* FILTER */}
      <input
        type="text"
        placeholder="Filter by course"
        value={filterCourse}
        onChange={(e) => setFilterCourse(e.target.value)}
        style={{ marginBottom: "10px" }}
      />

      {/* UNIQUE COURSES */}
      <h3>Unique Courses</h3>
      <ul>
        {[...uniqueCourses].map(course => (
          <li key={course}>{course}</li>
        ))}
      </ul>

      {/* STUDENTS */}
      <h3>Students (Sorted by GPA)</h3>
      <ul>
        {filteredStudents.map(student => (
          <li key={student.id}>
            <b>{student.name}</b> (GPA: {student.gpa}) — Courses:{" "}
            {[...student.enrolledCourses].join(", ")}
            <button
              onClick={() => removeStudent(student.id)}
              style={{ marginLeft: "10px" }}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>

      {/* COMPLEXITY */}
      <h4>Complexity</h4>
      <p>Filtering students by course: O(N)</p>
      <p>Reason: We check each student once, Set lookup is O(1)</p>
    </div>
  );
}