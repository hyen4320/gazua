# 베이스 이미지로 우분투를 사용합니다.
FROM ubuntu:latest

# 사용자 계정을 추가합니다. 여기서는 예시로 'user1'과 'user2'를 추가합니다.
RUN useradd -ms /bin/bash user1
RUN useradd -ms /bin/bash user2

# 사용자 계정 'user1'과 'user2'의 비밀번호를 설정합니다.
RUN echo 'user1:password1' | chpasswd
RUN echo 'user2:password2' | chpasswd

# 필요한 패키지를 설치할 수 있습니다.
RUN apt-get update && apt-get install -y vim

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# 사용자 계정을 변경합니다.
USER user1

# 컨테이너 실행 시 실행할 명령을 지정합니다.
CMD ["bash"]