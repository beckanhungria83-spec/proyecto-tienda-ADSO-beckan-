from app import db

class Producto(db.Model):
    __tablename__ = "productos"
    idProducto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    proCodigo = db.Column(db.String(30), nullable=False, unique=True)
    proNombre = db.Column(db.String(100), nullable=False)
    proPrecio = db.Column(db.Float, nullable=False)
    proCategoria = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "idProducto": self.idProducto,
            "proCodigo": self.proCodigo,
            "proNombre": self.proNombre,
            "proPrecio": self.proPrecio,
            "proCategoria": self.proCategoria
        }