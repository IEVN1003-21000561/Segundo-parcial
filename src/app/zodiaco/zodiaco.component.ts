import { Component, OnInit } from '@angular/core'
import { FormGroup, FormControl, ReactiveFormsModule } from '@angular/forms'
import { CommonModule } from '@angular/common'
import { Persona, ResultadoZodiaco } from './zodiaco'

@Component({
  selector: 'app-zodiaco',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './zodiaco.component.html',
  styleUrls: ['./zodiaco.component.css']
})
export class ZodiacoComponent implements OnInit {
  form!: FormGroup
  persona = new Persona()
  resultado = new ResultadoZodiaco()
  mostrarResultado = false

  signos = [
    'rata', 'buey', 'tigre', 'conejo', 'dragon', 'serpiente',
    'caballo', 'cabra', 'mono', 'gallo', 'perro', 'cerdo'
  ]

  imagenes: { [key: string]: string } = {
    rata: 'https://i.imgur.com/RzsPKjT.png',
    buey: 'https://i.imgur.com/MuATcnC.png',
    tigre: 'https://i.imgur.com/9l9kzXO.png',
    conejo: 'https://i.imgur.com/DDTHKH8.png',
    dragon: 'https://i.imgur.com/0Z6wZmr.png',
    serpiente: 'https://i.imgur.com/wC6weoa.png',
    caballo: 'https://i.imgur.com/phOOMqm.png',
    cabra: 'https://i.imgur.com/G6lGifG.png',
    mono: 'https://i.imgur.com/wwZ7PkW.png',
    gallo: 'https://i.imgur.com/pKYnkAT.png',
    perro: 'https://i.imgur.com/7CiBzVv.png',
    cerdo: 'https://i.imgur.com/MZCIWek.png'
  }

  fechaAnoActual = new Date().getFullYear()
  fechaMesActual = new Date().getMonth() + 1
  fechaDiaActual = new Date().getDate()

  ngOnInit(): void {
    this.form = new FormGroup({
      nombre: new FormControl(''),
      apellidoPaterno: new FormControl(''),
      apellidoMaterno: new FormControl(''),
      diaNacimiento: new FormControl(null),
      mesNacimiento: new FormControl(null),
      anioNacimiento: new FormControl(null),
      sexo: new FormControl('')
    })
  }

  calcularZodiaco(): void {
    this.persona.nombre = this.form.value.nombre
    this.persona.apellidoPaterno = this.form.value.apellidoPaterno
    this.persona.apellidoMaterno = this.form.value.apellidoMaterno
    this.persona.diaNacimiento = +this.form.value.diaNacimiento
    this.persona.mesNacimiento = +this.form.value.mesNacimiento
    this.persona.anioNacimiento = +this.form.value.anioNacimiento
    this.persona.sexo = this.form.value.sexo

    this.resultado.edad = this.calcularEdad()
    this.resultado.signoZodiacal = this.obtenerSigno()
    this.resultado.imagenSigno = this.imagenes[this.resultado.signoZodiacal]
    this.resultado.nombre = `${this.persona.nombre} ${this.persona.apellidoPaterno} ${this.persona.apellidoMaterno}`

    this.mostrarResultado = true
  }

  calcularEdad(): number {
    this.resultado.edad = this.fechaAnoActual - this.persona.anioNacimiento

    if (this.fechaMesActual < this.persona.mesNacimiento) {
      this.resultado.edad--
    } else if (this.fechaMesActual === this.persona.mesNacimiento) {
      if (this.fechaDiaActual < this.persona.diaNacimiento) {
        this.resultado.edad--
      }
    }

    return this.resultado.edad
  }

  obtenerSigno(): string {
    return this.signos[((this.persona.anioNacimiento - 4) + 12) % 12]
  }
}

