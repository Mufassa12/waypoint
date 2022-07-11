project = "waygolf"

app "example-python" {
  labels = {
    "service" = "waygolf",
    "env"     = "dev"
  }

  build {
    use "docker" {}
  }

  deploy {
    use "docker" {
      service_port = 8080
    }
  }
}
