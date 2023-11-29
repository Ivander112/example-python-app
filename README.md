## Update app.py dan pembuatan Dockerfile

### 1. Update app.py

 Saya menambahkan 2 routing baru yaitu '/nama' dan '/secret' serta mengubah portnya menjadi 4321

	from  flask  import  Flask
	app  =  Flask(__name__)

	@app.route('/')
	def  hello_world():
	return  'Hello, Docker!'

	@app.route('/nama')
	def  hello_moder():
	return  'Di update oleh ivan'
	
	@app.route('/secret')
	def  hello_secret():
	return  'gk ad secret'

	if  __name__  ==  '__main__':
		app.run(debug=True,host='0.0.0.0', port="4321")
		
### 2. Dockerfile

Saya menggunakan python:3.8 serta memastikan bahwa portnya 4321. Digunakan command cmd agar program langsung berjalan. Isi Dockerfile

	FROM python:3.8
	LABEL Name="ansible_st2_ivan"
	LABEL Version="0.1.0"
	EXPOSE 4321
	WORKDIR /app
	COPY . .
	RUN pip install -r requirements.txt
	CMD ["python", "app.py"]

## Penggunaan ansible ke VM


### 1. Isi inventory.yaml

Isi file ini adalah nama image yang akan di build dan path dari vm untuk username saya serta IP dari VM target.

	all:
	  vars:
	    image_p: python-custom-i:0.1.0
	    dir_path: /home/ivanderiaw/test_ansible
	  hosts:
	    container-test-i:
	      ansible_host: 10.184.0.100

### 2. Isi playbook.yaml
	
	  - name: uji coba menjalankan docker container
	    hosts: container-test-i
	    become: false
	    tasks:
	    - name: Copy file to remote host
	      copy:
	        src: /home/ivanz/Coding/btj-academy/raw_file/
	        dest: "{{dir_path}}"
	    - name: Build container image
	      docker_image:
	        name: "{{image_p}}"
	        source: "build"
	        build:
	          path: "{{dir_path}}"
	        state: present
	    - name: Deploy container
	      docker_container:
	        name: simple-task-ansible-i
	        image: "{{image_p}}"
	        interactive: true
	        tty: true
	        published_ports:
	          - "4321:4321"
	        publish_all_ports: true

### 3. Copy file ke local

Task ini merupakan task pertama. Saya meng-*copy* semua isi directory raw_file ke directory test_ansible. Isi raw_file adalah file yang diperlukan untuk mem-*build* docker image yaitu app.py, Dockerfile, requirement.txt, inventory.yaml dan playbook.yaml.

 
### 4. Build image

Task kedua adalah mem-*build* docker image. Pada task ini diperlukan nama image dan directory target. Keduanya ditulis di variabel "image_p" dan "dir_path".

### 5. Menjalankan Docker container

Task ketiga adalah memjalankan docker conatiner. Pada task ini diperlukan iamge yang tadi digunakan. Pastikan container interactive lalu declarasikan juga port yang digunakan dengan dengan command ports:ports.

### 6. Uji coba curl

![Uji coba Curl](/curl-test.png)

Dapat terlihat bahwa curl berhasil dilakukan