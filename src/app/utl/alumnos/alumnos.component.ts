import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import {AlumnoFilterPipe } from '../alumnos-filter.pipe';
import { CommonModule } from '@angular/common';
import { AlumnosUtl } from '../app.config';
import { ProyectoapiService } from '../proyectoapi.service';

@Component({
  selector: 'app-alumnos',
  imports: [FormsModule, RouterLink, AlumnoFilterPipe, CommonModule],
  templateUrl: './alumnos.component.html',
  styleUrls: ['./alumnos.component.css']
})


export default class AlumnosComponent{

  imageWidth:number=50;
  imageMargin:number=2;
  muestraImg:boolean=true;
  alumnoFilter:string=''
  alumnoTitle!:string
  dataSource:any=[];
  listFilter: any;

  constructor(public alumnosUtl:ProyectoapiService){}


  alumnosIric:AlumnosUtl[]=[
    {
      matricula:1234,
      nombre:'pedro',
      apaterno:'lopez',
      amaterno:'muñoz',
      correo:'pedro@gmail.com',

    },
  ]


  ngOnInit(): void {
  this.alumnosUtl.getAlumnos().subscribe(
    {
      next: (response: any) => {
        this.dataSource = response;
      },

      error: (error: any) => console.log(error)
    }
  );
}



}

