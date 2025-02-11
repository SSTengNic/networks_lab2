# Identifying Idempotent Routes in the REST API

## What is Idempotency?

Idempotent methods are operations that can be executed multiple times without changing the intended outcome. This means that whether the request is sent once or multiple times, the result remains the same.

## Idempotent Routes in My REST API

In my REST API, the following routes are idempotent:

-   **GET Requests:** These retrieve data and do not modify any resources.
-   **DELETE Requests (for the same student):** Deleting a student multiple times does not alter the system beyond the first successful deletion.

## Proof of Idempotency

### **GET Requests**

To demonstrate idempotency, run the `test_requests.sh` file located in the `tests` folder. The test cases for GET requests (**TEST 1 - 4**) show that:

-   Regardless of how many times a GET request is sent, the response remains consistent, returning the same data for the same parameters.
-   The database state is never modified by these requests.

### **DELETE Requests**

Looking at **TEST 9** in `test_requests.sh`:

-   The first DELETE request removes the student record successfully.
-   A second DELETE request for the same student returns a `404 Not Found` error.
-   This confirms that after the initial deletion, subsequent DELETE requests do not affect the database, proving their idempotency.

## Conclusion

The GET and DELETE methods in this API exhibit idempotency because they do not cause unintended side effects when called multiple times. GET requests consistently return the same results, and DELETE requests ensure that a deleted resource remains deleted without additional changes to the system.
