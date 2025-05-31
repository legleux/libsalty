#include <sodium.h>
#include <stdio.h>
#include <string.h>

#define MESSAGE (const unsigned char *)"test"
#define MESSAGE_LEN 4
#define CIPHERTEXT_LEN (crypto_box_MACBYTES + MESSAGE_LEN)

int main()
{
    if (sodium_init() < 0)
    {
        // panic! libsodium couldn't initialize
        return 1;
    }
    unsigned char alice_publickey[crypto_box_PUBLICKEYBYTES];
    unsigned char alice_secretkey[crypto_box_SECRETKEYBYTES];
    crypto_box_keypair(alice_publickey, alice_secretkey);

    unsigned char bob_publickey[crypto_box_PUBLICKEYBYTES];
    unsigned char bob_secretkey[crypto_box_SECRETKEYBYTES];
    crypto_box_keypair(bob_publickey, bob_secretkey);

    unsigned char nonce[crypto_box_NONCEBYTES];
    unsigned char ciphertext[CIPHERTEXT_LEN];

    randombytes_buf(nonce, sizeof nonce);

    if (crypto_box_easy(ciphertext, MESSAGE, MESSAGE_LEN, nonce,
                        bob_publickey, alice_secretkey) != 0)
    {
        fprintf(stderr, "Encryption failed\n");
        return 1;
    }

    unsigned char decrypted[MESSAGE_LEN];

    if (crypto_box_open_easy(decrypted, ciphertext, CIPHERTEXT_LEN, nonce,
                             alice_publickey, bob_secretkey) != 0)
    {
        fprintf(stderr, "Decryption failed or message forged\n");
        return 1;
    }

    printf("Decrypted message: %.*s\n", MESSAGE_LEN, decrypted);
    return 0;
}
