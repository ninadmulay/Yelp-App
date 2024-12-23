import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p>Welcome to the Yelp App!</p>
  `,
  styles: [`
    /* Add styles if needed */
  `]
})
export class HomeComponent { }