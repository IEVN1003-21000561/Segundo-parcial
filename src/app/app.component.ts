import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { initFlowbite } from 'flowbite';

import { NavbarComponent } from './navbar/navbar.component';
import { DistanciaComponent } from './formularios/distancia/distancia.component';
import { ZodiacoComponent } from './zodiaco/zodiaco.component';
import { AporbComponent } from './aporb/aporb.component';
import { RouterOutlet } from "@angular/router";


@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [
    FormsModule,
    ReactiveFormsModule,
    NavbarComponent,
    ZodiacoComponent,
    DistanciaComponent,
    AporbComponent,
    RouterOutlet,

]
})
export class AppComponent implements OnInit {
  title = 'AngularSegundo03';

  ngOnInit(): void {
    initFlowbite();
  }
}

