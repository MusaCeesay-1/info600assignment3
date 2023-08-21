FROM openjdk:11
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN javac Main.java
CMD ["java", "Main"]
