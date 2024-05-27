{% block content %}
<!DOCTYPE html>
<html lang="tr">
  <head>
    <title>FitLife'a Giriş Yap</title>

    <style>
      * {
        box-sizing: border-box;
      }

      body {
        font-family: "Nunito Sans", sans-serif;
        background-color: rgba(94, 0, 45, 0.2);
        color: #fff;
        margin: 0;
        padding: 0;
      }

      h2 {
        text-align: center;
        margin-top: 30px;
        letter-spacing: 2px;
      }

      table {
        margin: 0 auto;
        padding: 20px;
        border: 2px solid rgba(94, 0, 45, 0.9);
        border-radius: 10px;
        width: 50%;
      }

      input {
        width: calc(100% - 20px);
        padding: 10px;
        margin: 5px 0;
        box-sizing: border-box;
        border: 1px solid rgba(94, 0, 45, 0.9);
        border-radius: 5px;
      }

      button {
        background-color: rgba(94, 0, 45, 0.5);
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }

      button:hover {
        background-color: #fff;
        color: #000202;
      }

      a {
        display: block;
        text-align: center;
        color: #000202;
        text-decoration: none;
        margin-top: 10px;
      }

      a:hover {
        text-decoration: underline;
      }
      .error {
        font-size: large;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h2>FitLife'a Giriş Yap</h2>
    <form method="post" action="{% url 'giris_yap_view' %}">
      {% csrf_token %}
      <table>
        <tr>
          <td>
            <input type="email" name="email" placeholder="E-posta" />
          </td>
        </tr>
        <tr>
          <td>
            <input type="password" name="sifre" placeholder="Şifre" />
          </td>
        </tr>
        <tr>
          <td>
            <button type="submit">Giriş Yap</button>
          </td>
          <td>
            {% if error_message %}
            <p class="error" style="color: #000202">{{ error_message }}</p>
            {% endif %}
          </td>
        </tr>
        <tr>
          <td>
            <a href="">Şifreni mi unuttun?</a>
          </td>
        </tr>
      </table>
    </form>
  </body>
</html>
{% endblock content %}
