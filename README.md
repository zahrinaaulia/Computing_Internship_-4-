<h1> Final Assignment Computing Laboratory </h1>

Di project ini, kami kelompok 4 akan menyelesaikan Final Assignment dari Computing Laboratory.
Di Project ini terdapat beberapa kasus yang harus diselesaikan :
            
            A. Membuat file pets.py
            
              Dalam file ini, kami ditugaskan untuk membuat kelas utama yaitu Pets dan Animal 
              dan Child class (inheritance dari kelas Animal). Untuk kelas Pets sendiri memiliki atribut
              global yaitu pet_list berupa list yang akan diisi dengan inputan dari user, untuk method di class
              ini terdapat dua method yaitu is_hungry() (untuk mengembalikan adakah pets yang lapar dalam pet_list) 
              dan whos_hungry() (untuk mengembalikan siapa saja yang lapar pada pet_list).
              
              Untuk kelas Animal, kelas ini memiliki atribut name, age, dan hungry(true). kelas ini akan menggunakan list pet_list
              yang ada pada kelas Pets. kelas ini mempunyai method yaitu method eat() yang bertujuan untuk mengganti 
              status hungry menjadi false.
              
              Untuk child class terdapat 3 kelas, yaitu Bird, Dog, dan Cat yang merupakan inheritance dari kelas Animal.
              disetiap kelas memiliki atribut species dan memiliki method sound() berdasarkan spesies/jenis kelas yang ada.
            
            B. Membuat figure2d.py
            
                Dalam file ini, terdapat 2 kelas utama yaitu kelas Segitiga dan kelas Segiempat. selain kelas utama, 
                terdapat juga beberapa child class seperti kelas Samasisi, Samakaki (yang merupakan inheritance dari kelas Segitiga) dan
                Persegi,Trapesium, dan Jajargenjang (yang merupakan inheritance dari kelas Segiempat).
                
                Untuk kelas Utama, kedua kelas tersebut memiliki atribut jumlah_sisi seperti untuk kelas Segitiga memiliki jumlah_sisi 3
                dan kelas Segiempat memiliki jumlah_sisi 4
                
                Untuk Child Class, keempat kelas tersebut memiliki atribut yang berbeda-beda sesuai dengan kelasnya seperti :
                    - Untuk kelas Samasisi memiliki atribut sisi,tinggi
                    - Untuk kelas Samakaki memiliki atribut alas, tinggi
                    - Untuk kelas Persegi memiliki atribut panjang, lebar
                    - Untuk kelas Trapesium memiliki atribut alas, tutup, tinggi
                    - Untuk kelas Jajargenjang memiliki atribut alas, tinggi 
                    
                Child Class juga memiliki method, yaitu method hitung_luas() untuk menghitung luas  dan hitung_keliling() untuk                         menghitung volume disetiap class tetapi memiliki formula yang berbeda tergantung dengan bentuk bidang. 
                    
                
                
               
            C. Membuat vehicle.py
            
                Dalam file ini, terdapat satu kelas utama yaitu kelas Vehicle yang memiliki atribut year dan price.
                Selain kelas utama, terdapat juga child class yaitu Car, Motorbike, dan Bicycle yang masing -masing memiliki atribut                     global wheel_count dan capacity.
                
                Untuk Child class, masing masing memiliki method pay_tax() dan method park(hour), untuk method pay_tax() memiliki                       ketentuan masing-masing yaitu apabila Car dikenai pajak 15% dari price, Motorbike 10%, dan Bicycle tidak dikenakan biaya                 apapun. Untuk park(hour) method, dikenakanbiaya 2500 untuk setiap roda pada kendaraan tiap jamnya. dan terdapat biaya                   tambahan 5000 untuk capacity > 5.
                
                
          
                
            D. Membuat figure3d.py
                
                Di file ini, terdapat 4 kelas, yaitu Kubus, Balok, Tabung dan Kerucut. Masing-masing dari kelas tersebut memiliki                       atribut global yaitu jumlah_sisi, dan atribut lain yang berbeda-beda seperti:
                    - Kubus memiliki atribut sisi
                    - Balok memiliki atribut panjang, lebar, tinggi 
                    - Tabung memiliki atribut  jari-jari, tinggi
                    - Kerucut memiliki atribut jari-jari , tinggi 
                    
                Keempat kelas tersebut memiliki method yang sama yaitu hitung_luas() untuk menghitung luas bangun dan hitung_volume()                   untuk menghitung volume yang memiliki formula yang berbeda-beda sesuai dengan bentuk bangun.
            
            
