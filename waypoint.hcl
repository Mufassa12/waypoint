project = "waypoint"

app "waypoint-golf" {
  labels = {
    "service" = "waypoint-golf",
    "env"     = "dev"
  }

  build {
    use "docker" {}
  }

  deploy {
    use "docker" {
    }
  }
}
