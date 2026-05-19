#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define ITEMS_TO_PRODUCE 10

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

sem_t empty;
sem_t full;

pthread_mutex_t mutex;

void* producer(void* arg)
{
    int item;

    for(item = 1; item <= ITEMS_TO_PRODUCE; item++)
    {
        // Wait if buffer is full
        sem_wait(&empty);

        // Lock critical section
        pthread_mutex_lock(&mutex);

        buffer[in] = item;
        printf("Producer produced item %d at position %d\n", item, in);

        in = (in + 1) % BUFFER_SIZE;

        // Unlock critical section
        pthread_mutex_unlock(&mutex);

        // Signal that buffer has new item
        sem_post(&full);

        sleep(1);
    }

    pthread_exit(NULL);
}

void* consumer(void* arg)
{
    int item;

    for(int i = 1; i <= ITEMS_TO_PRODUCE; i++)
    {
        // Wait if buffer is empty
        sem_wait(&full);

        // Lock critical section
        pthread_mutex_lock(&mutex);

        item = buffer[out];
        printf("Consumer consumed item %d from position %d\n", item, out);

        out = (out + 1) % BUFFER_SIZE;

        // Unlock critical section
        pthread_mutex_unlock(&mutex);

        // Signal that buffer has empty slot
        sem_post(&empty);

        sleep(2);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t producerThread, consumerThread;

    // Initialize semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    // Initialize mutex
    pthread_mutex_init(&mutex, NULL);

    // Create threads
    pthread_create(&producerThread, NULL, producer, NULL);
    pthread_create(&consumerThread, NULL, consumer, NULL);

    // Wait for threads to finish
    pthread_join(producerThread, NULL);
    pthread_join(consumerThread, NULL);

    // Destroy synchronization tools
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    printf("\nExecution completed successfully.\n");

    return 0;
}