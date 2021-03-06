# Generated by Django 3.0.3 on 2020-07-24 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('tombo', models.CharField(max_length=50, verbose_name='Tombo :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Armários',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Bancada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('tombo', models.CharField(max_length=50, verbose_name='Tombo :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Estantes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Gaveta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('armario_gaveta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_gaveta', to='app.Armario')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Origem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Origem',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Outros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Reagente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome :')),
                ('formula_q', models.CharField(max_length=50, verbose_name='Formula Química :')),
                ('grau_p', models.CharField(max_length=50, verbose_name='Gráu de Pureza :')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade :')),
                ('data_validade', models.DateField(verbose_name='Data de Validade')),
                ('controle_pfex', models.CharField(max_length=50, verbose_name='Controle PF / Exercito :')),
                ('ficha_tec', models.ImageField(upload_to='images', verbose_name='Anexar PDF ou imagem :')),
                ('massamolecular', models.CharField(max_length=50, verbose_name='Massa Molecular :')),
                ('densidade', models.CharField(max_length=50, verbose_name='Densidade :')),
                ('disponibilidade', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NÃO')], max_length=3)),
                ('obs', models.TextField(verbose_name='Observação :')),
                ('armario_reagente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Reagente', to='app.Armario')),
                ('bancada_reagente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Reagente', to='app.Bancada')),
                ('estante_reagente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_Reagente', to='app.Estante')),
                ('gaveta_reagente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gaveta_Reagente', to='app.Gaveta')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reagente', to='app.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('obs', models.TextField(verbose_name='Observação')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
            ],
        ),
        migrations.CreateModel(
            name='Vidraria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome :')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade :')),
                ('ficha_tec', models.ImageField(upload_to='images', verbose_name='Ficha Técnica :')),
                ('especficacao_t', models.TextField(verbose_name='Especificação Técnica')),
                ('obs', models.TextField(verbose_name='Observação')),
                ('armario_vidraria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Vidraria', to='app.Armario')),
                ('bancada_vidraria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Vidraria', to='app.Bancada')),
                ('estante_vidraria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_Vidraria', to='app.Estante')),
                ('gaveta_vidraria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gaveta_Vidraria', to='app.Gaveta')),
                ('sala_vidraria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Vidraria', to='app.Sala')),
            ],
        ),
        migrations.CreateModel(
            name='Solucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('concetracao', models.CharField(max_length=50)),
                ('data_producao', models.DateField(verbose_name='data_Producao')),
                ('obs', models.TextField(verbose_name='Observação :')),
                ('armario_solucao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Solucao', to='app.Armario')),
                ('bancada_solucao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Solucao', to='app.Bancada')),
                ('estante_solucao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_Solucao', to='app.Estante')),
                ('gaveta_solucao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gaveta_Solucao', to='app.Gaveta')),
                ('reagente', models.ManyToManyField(to='app.Reagente')),
                ('sala_solucao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Solucao', to='app.Sala')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Soluções',
                'ordering': ['nome'],
            },
        ),
        migrations.AddField(
            model_name='reagente',
            name='sala_reagente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Reagente', to='app.Sala'),
        ),
        migrations.AddField(
            model_name='reagente',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='unidade', to='app.Unidade'),
        ),
        migrations.CreateModel(
            name='Prateleira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome :')),
                ('sigla', models.CharField(max_length=50, verbose_name='SIGLA :')),
                ('armario_prateleira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Prateleira', to='app.Armario')),
                ('bancada_prateleira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Prateleira', to='app.Bancada')),
                ('estante_prateleira', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_prateleira', to='app.Estante')),
            ],
        ),
        migrations.AddField(
            model_name='estante',
            name='sala_estante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_esteante', to='app.Sala'),
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome :')),
                ('tombo', models.CharField(max_length=20, verbose_name='Tombo :')),
                ('data_compra', models.DateField(verbose_name='Data da Compra')),
                ('data_u_m', models.DateField(verbose_name='Data da Última Manutenção')),
                ('origem', models.ImageField(upload_to='images', verbose_name='Anexar PDF ou imagem :')),
                ('ficha_tec', models.ImageField(upload_to='images', verbose_name='Ficha Técnica :')),
                ('especficacao_t', models.TextField(verbose_name='Especificação Técnica')),
                ('calibragem', models.CharField(choices=[('SIM', 'SIM'), ('NAO', 'NÃO')], max_length=3)),
                ('obs', models.TextField(verbose_name='Observação :')),
                ('armario_equipamentos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Equipamentos', to='app.Armario')),
                ('bancada_equipamentos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Equipamentos', to='app.Bancada')),
                ('estante_equipamentos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_Equipamentos', to='app.Estante')),
                ('gaveta_equipamentos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gaveta_Equipamentos', to='app.Gaveta')),
                ('marca_Equipamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Marca', to='app.Marca')),
                ('sala_equipamentos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Equipamentos', to='app.Sala')),
            ],
        ),
        migrations.CreateModel(
            name='Diverso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome :')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade :')),
                ('ficha_tec', models.ImageField(upload_to='images', verbose_name='Ficha Técnica :')),
                ('especficacao_t', models.TextField(verbose_name='Especificação Técnica')),
                ('obs', models.TextField(verbose_name='Observação')),
                ('armario_diversos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Armario_Diversos', to='app.Armario')),
                ('bancada_diversos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Bancada_Diversos', to='app.Bancada')),
                ('estante_diversos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Estante_Diversos', to='app.Estante')),
                ('gaveta_diversos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Gaveta_Diversos', to='app.Gaveta')),
                ('sala_diversos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Diversos', to='app.Sala')),
                ('u_md', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Unidade', to='app.Unidade')),
            ],
        ),
        migrations.AddField(
            model_name='bancada',
            name='sala_bancada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_Bancada', to='app.Sala'),
        ),
        migrations.CreateModel(
            name='Aulasprontas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('quantidade_reagente', models.IntegerField(verbose_name='Quant_Reagente :')),
                ('quantidade_solucao', models.IntegerField(verbose_name='Quant_solucao :')),
                ('obs_aula_pronta', models.TextField(verbose_name='Observação :')),
                ('diverso_ap', models.ManyToManyField(to='app.Diverso')),
                ('equepamentos_ap', models.ManyToManyField(to='app.Equipamento')),
                ('reagente_ap', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Reagente_Aula', to='app.Reagente')),
                ('solucao_ap', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Solução_Aula', to='app.Solucao')),
                ('vidraria_ap', models.ManyToManyField(to='app.Vidraria')),
            ],
            options={
                'verbose_name': 'Aulasprontas',
                'verbose_name_plural': 'Modelos de Aulas Práticas Prontas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='AulaPratica_COM_Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_solicitacao', models.DateField(verbose_name='Data da Solicitação')),
                ('turno', models.CharField(choices=[('MANHA', 'MANHÃ'), ('TARDE', 'TARDE'), ('NOITE', 'NOITE')], max_length=5)),
                ('data_H_inicio', models.DateTimeField(verbose_name='Data Inicio')),
                ('data_H_final', models.DateTimeField(verbose_name='Data Fim')),
                ('quant_aluno', models.IntegerField(verbose_name='Quantidade de Alunos:')),
                ('obs1', models.TextField(verbose_name='Observação :')),
                ('apsala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='salaap', to='app.Sala', verbose_name='Sala')),
                ('aulas_prontas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Aulasprontas', to='app.Aulasprontas', verbose_name='Modelos de Aulas Prontas')),
            ],
            options={
                'verbose_name': 'AulaPratica',
                'verbose_name_plural': 'Aula Prática Com Modelo',
                'ordering': ['apsala'],
            },
        ),
        migrations.AddField(
            model_name='armario',
            name='sala_armario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Sala_armario', to='app.Sala'),
        ),
    ]
