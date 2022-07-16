import datetime

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, Http404, request
from inWhite.forms import CreateNewProperty
from .filters import PropertyFilter

from .models import Property, User


def home(request):
    return render(request, 'home.html')


@login_required
def account(request):
    return render(request, 'account.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = User
        fields = ['avatar', 'bio']


class PropertiesSearchView(ListView):
    model = Property
    context_object_name = "properties"
    template_name = 'properties_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        return Property.objects.filter(name__icontains=query).filter().order_by('-name')


class createForm(CreateView):
    model = Property

    fields = ['name', 'property_type', 'address', 'description', 'photo']
    success_url = ''

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def create(response):  # Creates and saves new Property from input form
    form = CreateNewProperty()
    context = {
        "form": form
    }

    if response.method == "POST":
        form = CreateNewProperty(response.POST, files=response.FILES)
        # fields = ('name', 'property_type', 'address', 'description', 'photo')

        if form.is_valid():
            name = form.cleaned_data.get('name')
            area = form.cleaned_data.get('area')
            property_type = form.cleaned_data.get('property_type')
            address = form.cleaned_data.get('address')
            description = form.cleaned_data.get('description')
            photo = form.cleaned_data.get('photo')
            registration_date = datetime.datetime.now()

            property_obj = Property.objects.create(name=name,
                                                   area=area,
                                                   property_type=property_type,
                                                   address=address,
                                                   description=description,
                                                   photo=photo,
                                                   registration_date=registration_date,
                                                   )

            property_obj.save()

            context['object'] = property_obj
            context['created'] = True

    return render(response, './create.html', context=context)


def properties(request):
    props = Property.objects.all()

    myFilter = PropertyFilter()

    context = {'properties': props, 'myFilter': myFilter}

    return render(request, 'properties.html', context)


def property_details(request, property_id):
    try:
        property_d = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        raise Http404('Property not found')
    return render(request, 'property_details.html', {
        'property': property_d,
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user_qs = User.objects.filter(username=username)

        if user_qs.count() == 0:
            print("No Such User")
            raise forms.ValidationError("The user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/profile')
        else:
            messages.error(request, "Username or Password not correct")
            return redirect('/login')
    messages.error(request, "Username or Password not correct")
    return redirect('/login')


class LoginInterfaceView(LoginView):
    template_name = 'registration/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'registration/logout.html'


class SignupInterfaceView:
    template_name = '/registration.html'


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def registration_request(request):
    args = {}
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/properties")
        else:
            args['form'] = form
            messages.error(request, "Registration Error! Try again")
            return redirect("/registration")

    form = NewUserForm()
    return render(request=request, template_name="registration.html", context={"register_form": form})


class MyPropertiesListView(LoginRequiredMixin, ListView):
    model = Property
    context_object_name = "property"
    template_name = 'properties.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.property.all()
