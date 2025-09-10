# Beacon
Beacon is a modern Django-based platform for classroom management, assignment tracking, and project discovery. It supports both instructors and students, providing dashboards, assignment submission, feedback with a clean, user-friendly interface.

## Features
- Instructor and student dashboards
- Assignment and project management
- Classroom and student management
- Submission tracking and feedback
- Profile management
- CSV export for instructors
- Modern sidebar navigation

## Screenshots
![Student Dashboard](https://res.cloudinary.com/dvhwvkip4/image/upload/v1757483174/Screenshot_2025-09-10_084210_ioe7k2.png)
![Student Profile](https://res.cloudinary.com/dvhwvkip4/image/upload/v1757486357/Screenshot_2025-09-10_093914_fkvawc.png)

**Note:** These screenshots are just a sneak peek of Beacon. Explore the full app live here: [Beacon Website]()

## Common Paths
| Path                      | Description                       |
|-------------------------- |-----------------------------------|
| `/auth/login/`            | Login page                        |
| `/dashboard/`             | Student dashboard                  |
| `/instructor-dashboard/`  | Instructor dashboard               |
| `/profile/`               | User profile                       |
| `/discover/`              | Discover projects                   |
| `/auth/logout/`           | Logout                             |

## Instructor Paths
| Path                              | Description                       |
|-----------------------------------|-----------------------------------|
| `/students/`                      | List all students                 |
| `/students/add/`                  | Add a new student                 |
| `/students/<id>/`                 | View student profile              |
| `/students/<id>/delete/`          | Delete a student                  |
| `/assignments/`                   | List assignments                  |
| `/assignments/add/`               | Add assignment                    |
| `/assignments/<id>/`              | Assignment details                |
| `/assignments/<id>/edit/`         | Edit assignment                   |
| `/assignments/<id>/delete/`       | Delete assignment                 |
| `/classrooms/`                    | List classrooms                   |
| `/classrooms/add/`                | Add classroom                     |
| `/classrooms/<id>/delete/`        | Delete classroom                  |
| `/classrooms/<id>/manage/`        | Manage classroom students         |
| `/students/export/csv/`           | Export students & submissions CSV |

## Student Paths
| Path                              | Description                       |
|-----------------------------------|-----------------------------------|
| `/dashboard/`                     | Student dashboard                 |
| `/discover/`                      | Discover projects                 |
| `/profile/`                       | Student profile                   |
| `/profile/edit/`                  | Edit profile                      |
| `/profile/change-password/`       | Change password                   |
| `/assignments/`                   | List assignments                  |
| `/assignments/<id>/`              | Assignment details                |
| `/assignments/<id>/submit/`       | Submit assignment                 |

## Future Enhancements
- **Notifications**: Real-time alerts for assignment deadlines and feedback.
- **Collaboration Tools**: Group assignments, project discussions, and peer reviews.
- **Bookmark Projects**: Students can save and revisit interesting projects from the discover page.