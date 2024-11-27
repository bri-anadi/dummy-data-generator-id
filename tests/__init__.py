"""
Rangkaian Pengujian untuk Dummy Data Generator.

Modul ini menyediakan inisialisasi untuk kasus uji dan utilitas
atau konfigurasi pengujian bersama.
"""

import unittest
import sys
import os

# Tambahkan direktori induk ke path Python untuk memastikan paket dapat diimpor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Opsional: Anda dapat mendefinisikan konfigurasi atau utilitas pengujian global di sini
class BaseTestCase(unittest.TestCase):
    """
    Kasus uji dasar dengan metode setup dan teardown umum
    yang dapat diwariskan oleh kelas uji spesifik.
    """
    def setUp(self):
        """
        Metode yang dipanggil sebelum setiap metode uji.
        Dapat digunakan untuk inisialisasi umum.
        """
        pass

    def tearDown(self):
        """
        Metode yang dipanggil setelah setiap metode uji.
        Dapat digunakan untuk operasi pembersihan.
        """
        pass

# Anda juga dapat mendefinisikan fixture atau fungsi pembantu global
def tearUpModule():
    """
    Fungsi opsional yang dipanggil sekali sebelum pengujian apa pun di modul.
    Berguna untuk setup tingkat modul.
    """
    print("Menyiapkan modul pengujian...")

def tearDownModule():
    """
    Fungsi opsional yang dipanggil sekali setelah semua pengujian di modul selesai.
    Berguna untuk pembersihan tingkat modul.
    """
    print("Membongkar modul pengujian...")
