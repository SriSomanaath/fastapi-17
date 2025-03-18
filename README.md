# Community Job Portal API Endpoints

This document outlines the REST API endpoints for the Community Job Portal, supporting three types of users:
1. **Common Users** – Authentication, Profile, and Settings
2. **Job Seekers** – Resume management, job applications, AI recommendations
3. **Recruiters** – Job posting, applicant tracking, hiring analytics, notifications

## **1️⃣ Common User Endpoints**  

### **🛡️ Authentication & Profile Management**
- `POST /auth/register` → Register a new user  
- `POST /auth/login` → Login user  
- `POST /auth/logout` → Logout user  
- `GET /user/profile` → Fetch current user profile  
- `PUT /user/profile` → Update user profile details  
- `DELETE /user/delete` → Delete user account  

### **⚙️ User Settings**
- `GET /user/settings` → Fetch user settings  
- `PUT /user/settings` → Update user settings/preferences  

## **2️⃣ Job Seeker Endpoints**  

### **📄 Resume & Profile Management**
- `POST /jobseeker/resume/upload` → Upload resume  
- `GET /jobseeker/resume` → Fetch uploaded resume  
- `DELETE /jobseeker/resume` → Delete resume  
- `POST /jobseeker/profile` → Add professional details (skills, experience, education)  
- `PUT /jobseeker/profile` → Update professional details  

### **🔍 Job Search & Applications**
- `GET /jobs` → Fetch all available jobs  
- `GET /jobs?search=keyword` → Search jobs using keyword  
- `GET /job/{jobId}` → Get details of a specific job  
- `POST /jobseeker/apply/{jobId}` → Apply for a job  
- `GET /jobseeker/applications` → Get all applied jobs  
- `GET /jobseeker/application/{appId}` → Get details of a specific application  
- `DELETE /jobseeker/application/{appId}` → Withdraw application  

### **🤖 AI Job Recommendations**
- `GET /jobseeker/recommended-jobs` → Get AI-recommended jobs based on profile  
- `GET /jobseeker/matching-score/{jobId}` → Get job match score  

### **📊 Job Application Status**
- `GET /jobseeker/application-status/{appId}` → Fetch application status  
- `GET /jobseeker/hiring-progress` → Get hiring progress for all applied jobs  

## **3️⃣ Recruiter Endpoints**  

### **📌 Job Posting & Management**
- `POST /recruiter/job` → Create a new job  
- `GET /recruiter/jobs` → Fetch all jobs posted by recruiter  
- `GET /recruiter/job/{jobId}` → Get job details  
- `PUT /recruiter/job/{jobId}` → Update job  
- `DELETE /recruiter/job/{jobId}` → Delete job  

### **👥 Applicant Tracking**
- `GET /recruiter/job/{jobId}/applications` → Fetch applications for a job  
- `GET /recruiter/application/{appId}` → Get details of a specific application  
- `POST /recruiter/application/{appId}/status` → Update application status (`shortlisted/rejected/hired`)  
- `POST /recruiter/applications/bulk-status` → Bulk update statuses  
- `DELETE /recruiter/application/{appId}` → Remove an application  

### **🎯 Candidate Recommendations**
- `GET /recruiter/job/{jobId}/recommended-candidates` → Get AI-suggested candidates  
- `GET /recruiter/candidate/{candidateId}` → Get candidate profile  
- `POST /recruiter/candidate/{candidateId}/invite` → Send an interview invite  

### **📊 Hiring Analytics & Reports**
- `GET /recruiter/dashboard` → Fetch recruiter dashboard data  
- `GET /recruiter/hiring-analytics` → Get overall hiring analytics  
- `GET /recruiter/job/{jobId}/analytics` → Get job-specific analytics  
- `GET /recruiter/candidate-ranking/{jobId}` → AI-based candidate ranking  

### **🔔 Recruiter Notifications**
- `GET /recruiter/notifications` → Fetch all notifications  
- `POST /recruiter/notification/read/{notifId}` → Mark notification as read  

---

## **📌 Summary of Endpoints (40+ Total)**  
| **Category** | **Endpoint**  |
|-------------|--------------|
| **Common User** | `POST /auth/register`, `POST /auth/login`, `GET /user/profile`, `GET /user/settings`  |
| **Resume** | `POST /jobseeker/resume/upload`, `GET /jobseeker/resume`  |
| **Job Search** | `GET /jobs`, `GET /job/{jobId}`, `POST /jobseeker/apply/{jobId}`  |
| **AI Matching** | `GET /jobseeker/recommended-jobs`, `GET /jobseeker/matching-score/{jobId}`  |
| **Recruiter Dashboard** | `GET /recruiter/dashboard`, `GET /recruiter/hiring-analytics`  |
| **Job Posting** | `POST /recruiter/job`, `GET /recruiter/jobs`, `PUT /recruiter/job/{jobId}`  |
| **Candidate Tracking** | `GET /recruiter/job/{jobId}/applications`, `POST /recruiter/application/{appId}/status`  |
| **AI Suggestions** | `GET /recruiter/job/{jobId}/recommended-candidates`, `POST /recruiter/candidate/{candidateId}/invite`  |
| **Recruiter Notifications** | `GET /recruiter/notifications`, `POST /recruiter/notification/read/{notifId}`  |

This document provides **all essential endpoints** for a **full-fledged job portal**. 🚀
