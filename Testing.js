const { exec } = require('child_process');
const { expect } = require('chai');

describe('Sistema de Gestión Escolar', function() {
  this.timeout(10000); // Aumentar el tiempo de espera para pruebas que pueden tardar más

  it('debería registrar un nuevo estudiante', function(done) {
    exec('python ruta/a/tu/script_registrar_estudiante.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Estudiante registrado exitosamente');
      done();
    });
  });

  it('debería actualizar los datos de un estudiante', function(done) {
    exec('python ruta/a/tu/script_actualizar_estudiante.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Datos del estudiante actualizados');
      done();
    });
  });

  it('debería registrar un nuevo profesor', function(done) {
    exec('python ruta/a/tu/script_registrar_profesor.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Profesor registrado exitosamente');
      done();
    });
  });

  it('debería asignar horarios y materias a un profesor', function(done) {
    exec('python ruta/a/tu/script_asignar_horarios.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Horarios y materias asignados');
      done();
    });
  });

  it('debería enviar una notificación importante', function(done) {
    exec('python ruta/a/tu/script_enviar_notificacion.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Notificación enviada');
      done();
    });
  });

  it('debería generar un reporte de asistencia', function(done) {
    exec('python ruta/a/tu/script_generar_reporte_asistencia.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Reporte de asistencia generado');
      done();
    });
  });

  it('debería gestionar inscripciones y matrículas', function(done) {
    exec('python ruta/a/tu/script_gestionar_inscripciones.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Inscripciones y matrículas gestionadas');
      done();
    });
  });

  it('debería acceder a la biblioteca digital', function(done) {
    exec('python ruta/a/tu/script_acceder_biblioteca.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Acceso a la biblioteca digital');
      done();
    });
  });

  it('debería generar un reporte de rendimiento académico', function(done) {
    exec('python ruta/a/tu/script_generar_reporte_rendimiento.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Reporte de rendimiento académico generado');
      done();
    });
  });

  it('debería gestionar permisos y roles de usuario', function(done) {
    exec('python ruta/a/tu/script_gestionar_permisos.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Permisos y roles de usuario gestionados');
      done();
    });
  });

  it('debería evaluar a los estudiantes', function(done) {
    exec('python ruta/a/tu/script_evaluar_estudiantes.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Estudiantes evaluados');
      done();
    });
  });

  it('debería integrar elementos de gamificación', function(done) {
    exec('python ruta/a/tu/script_integrar_gamificacion.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Elementos de gamificación integrados');
      done();
    });
  });

  it('debería proporcionar soporte técnico', function(done) {
    exec('python ruta/a/tu/script_proporcionar_soporte.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Soporte técnico proporcionado');
      done();
    });
  });

  it('debería soportar múltiples idiomas', function(done) {
    exec('python ruta/a/tu/script_soportar_idiomas.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Soporte para múltiples idiomas');
      done();
    });
  });

  it('debería facilitar la educación inclusiva', function(done) {
    exec('python ruta/a/tu/script_educacion_inclusiva.py', (error, stdout, stderr) => {
      if (error) {
        done(error);
        return;
      }
      expect(stdout.trim()).to.equal('Educación inclusiva facilitada');
      done();
    });
  });
});
