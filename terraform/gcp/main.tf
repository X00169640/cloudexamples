provider "google" {
  project     = "devops2021gcp"
  region      = "europe-west2"
}

resource "google_compute_network" "example_vpc" {
  name                    = "example-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "example_subnet" {
  name          = "example-subnet"
  ip_cidr_range = "10.0.0.0/24"
  network       = google_compute_network.example_vpc.id
}

resource "google_compute_instance" "example_server" {
  name         = "example-server"
  machine_type = "e2-medium"
  zone         = "europe-west2-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.example_subnet.id
  }
}