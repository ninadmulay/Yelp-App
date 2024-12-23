import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <header>
      <h1>Yelp</h1>
      <nav>
        <a routerLink="/businesses">Businesses</a> |
        <a routerLink="/reviews">Reviews</a> |
        <a routerLink="/testdb">TestDB</a>
      </nav>
    </header>

    <main>
      <router-outlet></router-outlet>
    </main>
  `,
  styles: [`
    header {
      background-color: #d32323; /* Yelp red */
      color: white;
      padding: 10px;
      text-align: center;
    }

    nav a {
      color: white;
      margin: 0 10px; 
      text-decoration: none; 
    }
  `]
})
export class AppComponent { }