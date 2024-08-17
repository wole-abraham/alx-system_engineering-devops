# Postmortem Report: API Service Outage on July 10, 2024

## Issue Summary
- **Duration:** The outage lasted for 2 hours and 15 minutes, from 14:30 to 16:45 UTC on July 10, 2024.
- **Impact:** The primary API service was down, resulting in a 503 Service Unavailable error for approximately 80% of users. During this period, users were unable to access core functionalities, including game searches and library management.
- **Root Cause:** The root cause was an unhandled exception in the API’s rate-limiting middleware, which led to a cascading failure across the load balancers.

## Timeline
- **14:30 UTC:** The issue was detected by an automated monitoring alert indicating a sharp increase in 503 errors across the API endpoints.
- **14:32 UTC:** The DevOps team was notified via Slack. Initial assumption was that it was a load balancer issue, as the errors were widespread and typically associated with traffic management.
- **14:35 UTC:** The team began investigating the load balancers and network infrastructure, suspecting a configuration error.
- **14:50 UTC:** Further monitoring indicated that the API server logs were filled with exceptions related to rate-limiting.
- **15:00 UTC:** Focus shifted to the API’s rate-limiting middleware. The issue was escalated to the backend engineering team.
- **15:15 UTC:** The backend team identified an unhandled edge case in the rate-limiting middleware that triggered the failure.
- **15:30 UTC:** The team attempted a hotfix to bypass the faulty rate-limiting logic.
- **16:00 UTC:** The hotfix was deployed, but the issue persisted, leading the team to investigate further.
- **16:20 UTC:** It was discovered that the middleware failure caused a memory leak in the load balancers, leading to the cascading failure.
- **16:30 UTC:** The affected services were restarted, and the faulty middleware was temporarily disabled.
- **16:45 UTC:** All services were restored, and normal operations resumed.

## Root Cause and Resolution
- **Root Cause:** The API’s rate-limiting middleware had an unhandled edge case when processing a surge of requests from a specific IP range. This caused the middleware to throw exceptions, which were not properly caught or logged. As the exceptions accumulated, they caused the API servers to become unresponsive, leading to the load balancers failing due to memory overload.
- **Resolution:** The immediate resolution involved disabling the faulty middleware and restarting the affected services. A hotfix was then applied to handle the edge case in the rate-limiting logic, ensuring that exceptions would be properly caught and logged without disrupting the service.

## Corrective and Preventative Measures
### Improvements Needed
- Enhance exception handling and logging within the rate-limiting middleware to prevent similar failures.
- Improve monitoring to detect memory leaks and other resource-related issues earlier.
- Implement a fallback mechanism in the API service to maintain partial functionality even during middleware failures.

### Task List
1. **Patch Rate-Limiting Middleware:** Modify the middleware to handle edge cases and log exceptions properly. *(Due: July 12, 2024)*
2. **Add Monitoring on Middleware Exceptions:** Integrate monitoring tools to track exceptions and memory usage in real-time. *(Due: July 13, 2024)*
3. **Implement API Fallback Mechanism:** Develop and test a fallback mechanism to ensure minimal functionality is maintained during service disruptions. *(Due: July 20, 2024)*
4. **Load Balancer Configuration Review:** Conduct a review of load balancer configurations to optimize for better handling of memory leaks. *(Due: July 15, 2024)*
5. **Postmortem Review Meeting:** Schedule a meeting with the DevOps and Backend teams to discuss the incident and preventive strategies. *(Due: July 11, 2024)*

This incident has highlighted the need for robust exception handling and improved monitoring within critical middleware components. The outlined corrective actions will help prevent similar issues in the future and ensure the reliability of our services.

