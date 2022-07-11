project = "waygolf"

app "waygolf" {
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
