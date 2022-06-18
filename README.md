# FlaskArticleApp

<h3>Models</h3>

<ul>
  <li>
    <h4>Article model</h4>
    <ul>
      <li>id - serial</li>
      <li>post_uri - unique string up to 50 chars</li>
      <li>ToDo author - related to user model</li>
      <li>title - string up to 255 chars</li>
      <li>body - text</li>
    </ul>
  </li>
  <li>
    <h4>ToDo: User model</h4>
    <ul>
      <li>id - serial</li>
      <li>username - unique string up to 50 chars</li>
      <li>email - unique string up to 50 chars </li>
      <li>password - string up to 16 chars</li>
    </ul>
  </li>
</ul>

<h3>Features</h3>
<ul>
  <li>
    <h4>Main Page '/'</h4>
    <ul>
      <li>List all articles</li>
    </ul>
  </li>
  <li>
    <h4>Single Article Page '/article/:post_uri'</h4>
    <ul>
      <li>Single Article View</li>
    </ul>
  </li>
  <li>
    <h4>Search page '/search/'</h4>
    <ul>
      <li>Search in title form</li>
    </ul>
  </li>
  <li>
    <h4>Search in article's title '/search/:term'</h4>
    <ul>
      <li>Display all the articles which contains the searched term in their titles</li>
    </ul>
  </li>
  <li>
    <h4>ToDo Login Page '/login/'</h4>
    <ul>
      <li>Login Form</li>
    </ul>
  </li>
  <li>
    <h4>ToDo SignUp Page '/signup/'</h4>
    <ul>
      <li>SignUp Form</li>
    </ul>
  </li>
</ul>
