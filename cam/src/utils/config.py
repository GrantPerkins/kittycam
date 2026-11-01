class Config:
    def __init__(self):
        self.team_domain = "fragrant-fire-8d83.cloudflareaccess.com"
        self.aud = "95589cc50d879a2e52b58ad59cf22be5149766b5e55519604b87e27f0af157fb"
        self.jwks_url = f"https://{self.team_domain}/cdn-cgi/access/certs"
        self.issuer = f"https://{self.team_domain}"