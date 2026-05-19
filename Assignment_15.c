// race_condition.c
//without mutex


/*
#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define INCREMENTS 1000000

long long counter = 0;

void* increment_counter(void* arg)
{
    for(int i = 0; i < INCREMENTS; i++)
    {
        counter++;   // Critical section (unsafe)
    }

    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    // Create threads
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    // Wait for threads to finish
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    printf("Final Counter Value = %lld\n", counter);

    return 0;
}
*/


// mutex_counter.c

#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 4
#define INCREMENTS 1000000

long long counter = 0;

// Mutex declaration
pthread_mutex_t lock;

void* increment_counter(void* arg)
{
    for(int i = 0; i < INCREMENTS; i++)
    {
        // Lock the mutex
        pthread_mutex_lock(&lock);

        counter++;   // Critical section (safe)

        // Unlock the mutex
        pthread_mutex_unlock(&lock);
    }

    return NULL;
}

int main()
{
    pthread_t threads[NUM_THREADS];

    // Initialize mutex
    pthread_mutex_init(&lock, NULL);

    // Create threads
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_create(&threads[i], NULL, increment_counter, NULL);
    }

    // Wait for all threads
    for(int i = 0; i < NUM_THREADS; i++)
    {
        pthread_join(threads[i], NULL);
    }

    // Destroy mutex
    pthread_mutex_destroy(&lock);

    printf("Final Counter Value = %lld\n", counter);

    return 0;
}
