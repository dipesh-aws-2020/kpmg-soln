resource "aws_instance" "web_server1" {
  ami           = "ami-xxxxx"
  instance_type = "t2.medium"
  key_name = aws_key_pair.keypair.key_name

  subnet_id = "subnet-xxxxx"
  vpc_security_group_ids = ["sg-xxxxx"]

  tags = {
    Name ="web_server1"
  }
}

resource "aws_eip" "ip" {
    vpc = true
    instance = aws_instance.web_server1.id
}

resource "aws_key_pair" "keypair" {
  key_name = "web_server1-keypair"
  public_key = file("./kp/web_server1-keypair.pub")
}
