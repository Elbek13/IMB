from django.urls import path
from information.views import (
    category_list, m_category_list, global_search1, global_search2, global_search3,
    dissertatsiya_list, dissertatsiya_create, dissertatsiya_edit, dissertatsiya_delete,
    m_dissertatsiya_list, m_dissertatsiya_create, m_dissertatsiya_edit, m_dissertatsiya_delete,
    u1_dissertatsiya_list, u1_dissertatsiya_detail,
    monografiya_list, monografiya_create, monografiya_edit, monografiya_delete,
    m_monografiya_list, m_monografiya_create, m_monografiya_edit, m_monografiya_delete,
    u1_monografiya_list, u1_monografiya_detail,
    risola_list, risola_create, risola_edit, risola_delete,
    m_risola_list, m_risola_create, m_risola_edit, m_risola_delete,
    u1_risola_list, u1_risola_detail,
    darslik_list, darslik_create, darslik_edit, darslik_delete,
    m_darslik_list, m_darslik_create, m_darslik_edit, m_darslik_delete,
    u1_darslik_list, u1_darslik_detail,
    qollanma_list, qollanma_create, qollanma_edit, qollanma_delete,
    m_qollanma_list, m_qollanma_create, m_qollanma_edit, m_qollanma_delete,
    u1_qollanma_list, u1_qollanma_detail,
    loyiha_list, loyiha_create, loyiha_edit, loyiha_delete,
    m_loyiha_list, m_loyiha_create, m_loyiha_edit, m_loyiha_delete,
    u1_loyiha_list, u1_loyiha_detail,
    jurnal_list, jurnal_create, jurnal_edit, jurnal_delete,
    m_jurnal_list, m_jurnal_create, m_jurnal_edit, m_jurnal_delete,
    u1_jurnal_list, u1_jurnal_detail,
    maqola_list, maqola_create, maqola_edit, maqola_delete,
    m_maqola_list, m_maqola_create, m_maqola_edit, m_maqola_delete,
    u1_maqola_list, u1_maqola_detail,
    other_list, other_create, other_edit, other_delete,
    m_other_list, m_other_create, m_other_edit, m_other_delete,
    u1_other_list, u1_other_detail,
    tajriba_list, tajriba_create, tajriba_edit, tajriba_delete,
    m_tajriba_list, m_tajriba_create, m_tajriba_edit, m_tajriba_delete,
    u1_tajriba_list, u1_tajriba_detail, U2DissertatsiyaListView, U2DissertatsiyaDetailView, U2MonografiyaListView,
    U2MonografiyaDetailView, U2RisolaListView, U2RisolaDetailView, U2DarslikListView, U2DarslikDetailView,
    U2QollanmaListView, U2QollanmaDetailView, U2LoyihaListView, U2LoyihaDetailView, U2JurnalListView,
    U2JurnalDetailView, U2MaqolaListView,
    U2MaqolaDetailView, U2TajribaListView, U2TajribaDetailView, U2OtherListView, U2OtherDetailView,
    U3DissertatsiyaListView, U3DissertatsiyaDetailView, U3MonografiyaListView, U3MonografiyaDetailView,
    U3RisolaDetailView, U3RisolaListView, U3DarslikListView, U3DarslikDetailView, U3QollanmaListView,
    U3QollanmaDetailView, U3LoyihaListView, U3LoyihaDetailView, U3JurnalListView, U3JurnalDetailView, U3MaqolaListView,
    U3MaqolaDetailView, U3OtherListView, U3OtherDetailView, U3TajribaDetailView,
)

urlpatterns = [
    path('category/', category_list, name='category_list'),
    path('m_category/', m_category_list, name='m_category_list'),
    path('global-search1/', global_search1, name='global_search1'),
    path('global-search2/', global_search2, name='global_search2'),
    path('global-search3/', global_search3, name='global_search3'),

    # Dissertatsiya
    path('dissertatsiya_list/', dissertatsiya_list, name='dissertatsiya_list'),
    path('m_dissertatsiya_list/', m_dissertatsiya_list, name='m_dissertatsiya_list'),
    path('u1_dissertatsiya_list/', u1_dissertatsiya_list, name='u1_dissertatsiya_list'),
    path('u2_dissertatsiya_list/', U2DissertatsiyaListView.as_view(), name='u2_dissertatsiya_list'),
    path('u3_dissertatsiya_list/', U3DissertatsiyaListView.as_view(), name='u3_dissertatsiya_list'),
    path('dissertatsiya_list/create/', dissertatsiya_create, name='dissertatsiya_create'),
    path('m_dissertatsiya_list/create/', m_dissertatsiya_create, name='m_dissertatsiya_create'),
    path('dissertatsiya/edit/<int:dissertatsiya_id>/', dissertatsiya_edit, name='dissertatsiya_edit'),
    path('m_dissertatsiya/edit/<int:dissertatsiya_id>/', m_dissertatsiya_edit, name='m_dissertatsiya_edit'),
    path('dissertatsiya/delete/<int:dissertatsiya_id>/', dissertatsiya_delete, name='dissertatsiya_delete'),
    path('m_dissertatsiya/delete/<int:dissertatsiya_id>/', m_dissertatsiya_delete, name='m_dissertatsiya_delete'),
    path('u1_dissertatsiya/<int:dissertatsiya_id>/', u1_dissertatsiya_detail, name='u1_dissertatsiya_detail'),
    path('u2_dissertatsiya/<int:pk>/', U2DissertatsiyaDetailView.as_view(), name='u2_dissertatsiya_detail'),
    path('u3_dissertatsiya/<int:pk>/', U3DissertatsiyaDetailView.as_view(), name='u3_dissertatsiya_detail'),

    # Monografiya
    path('monografiya_list/', monografiya_list, name='monografiya_list'),
    path('m_monografiya_list/', m_monografiya_list, name='m_monografiya_list'),
    path('u1_monografiya_list/', u1_monografiya_list, name='u1_monografiya_list'),
    path('u2_monografiya_list/', U2MonografiyaListView.as_view(), name='u2_monografiya_list'),
    path('u3_monografiya_list/', U3MonografiyaListView.as_view(), name='u3_monografiya_list'),
    path('monografiya_list/create/', monografiya_create, name='monografiya_create'),
    path('m_monografiya_list/create/', m_monografiya_create, name='m_monografiya_create'),
    path('monografiya/edit/<int:monografiya_id>/', monografiya_edit, name='monografiya_edit'),
    path('m_monografiya/edit/<int:monografiya_id>/', m_monografiya_edit, name='m_monografiya_edit'),
    path('monografiya/delete/<int:monografiya_id>/', monografiya_delete, name='monografiya_delete'),
    path('m_monografiya/delete/<int:monografiya_id>/', m_monografiya_delete, name='m_monografiya_delete'),
    path('u1_monografiya/<int:monografiya_id>/', u1_monografiya_detail, name='u1_monografiya_detail'),
    path('u2_monografiya/<int:pk>/', U2MonografiyaDetailView.as_view(), name='u2_monografiya_detail'),
    path('u3_monografiya/<int:pk>/', U3MonografiyaDetailView.as_view(), name='u3_monografiya_detail'),

    # Risola
    path('risola_list/', risola_list, name='risola_list'),
    path('m_risola_list/', m_risola_list, name='m_risola_list'),
    path('u1_risola_list/', u1_risola_list, name='u1_risola_list'),
    path('u2_risola_list/', U2RisolaListView.as_view(), name='u2_risola_list'),
    path('u3_risola_list/', U3RisolaListView.as_view(), name='u3_risola_list'),
    path('risola_list/create/', risola_create, name='risola_create'),
    path('m_risola_list/create/', m_risola_create, name='m_risola_create'),
    path('risola/edit/<int:risola_id>/', risola_edit, name='risola_edit'),
    path('m_risola/edit/<int:risola_id>/', m_risola_edit, name='m_risola_edit'),
    path('risola/delete/<int:risola_id>/', risola_delete, name='risola_delete'),
    path('m_risola/delete/<int:risola_id>/', m_risola_delete, name='m_risola_delete'),
    path('u1_risola/<int:risola_id>/', u1_risola_detail, name='u1_risola_detail'),
    path('u2_risola/<int:pk>/', U2RisolaDetailView.as_view(), name='u2_risola_detail'),
    path('u3_risola/<int:pk>/', U3RisolaDetailView.as_view(), name='u3_risola_detail'),

    # Darslik
    path('darslik_list/', darslik_list, name='darslik_list'),
    path('m_darslik_list/', m_darslik_list, name='m_darslik_list'),
    path('u1_darslik_list/', u1_darslik_list, name='u1_darslik_list'),
    path('u2_darslik_list/', U2DarslikListView.as_view(), name='u2_darslik_list'),
    path('u3_darslik_list/', U3DarslikListView.as_view(), name='u3_darslik_list'),
    path('darslik_list/create/', darslik_create, name='darslik_create'),
    path('m_darslik_list/create/', m_darslik_create, name='m_darslik_create'),
    path('darslik/edit/<int:darslik_id>/', darslik_edit, name='darslik_edit'),
    path('m_darslik/edit/<int:darslik_id>/', m_darslik_edit, name='m_darslik_edit'),
    path('darslik/delete/<int:darslik_id>/', darslik_delete, name='darslik_delete'),
    path('m_darslik/delete/<int:darslik_id>/', m_darslik_delete, name='m_darslik_delete'),
    path('u1_darslik/<int:darslik_id>/', u1_darslik_detail, name='u1_darslik_detail'),
    path('u2_darslik/<int:pk>/', U2DarslikDetailView.as_view(), name='u2_darslik_detail'),
    path('u3_darslik/<int:pk>/', U3DarslikDetailView.as_view(), name='u3_darslik_detail'),

    # Qollanma
    path('qollanma_list/', qollanma_list, name='qollanma_list'),
    path('m_qollanma_list/', m_qollanma_list, name='m_qollanma_list'),
    path('u1_qollanma_list/', u1_qollanma_list, name='u1_qollanma_list'),
    path('u2_qollanma_list/', U2QollanmaListView.as_view(), name='u2_qollanma_list'),
    path('u3_qollanma_list/', U3QollanmaListView.as_view(), name='u3_qollanma_list'),
    path('qollanma_list/create/', qollanma_create, name='qollanma_create'),
    path('m_qollanma_list/create/', m_qollanma_create, name='m_qollanma_create'),
    path('qollanma/edit/<int:qollanma_id>/', qollanma_edit, name='qollanma_edit'),
    path('m_qollanma/edit/<int:qollanma_id>/', m_qollanma_edit, name='m_qollanma_edit'),
    path('qollanma/delete/<int:qollanma_id>/', qollanma_delete, name='qollanma_delete'),
    path('m_qollanma/delete/<int:qollanma_id>/', m_qollanma_delete, name='m_qollanma_delete'),
    path('u1_qollanma/<int:qollanma_id>/', u1_qollanma_detail, name='u1_qollanma_detail'),
    path('u2_qollanma/<int:pk>/', U2QollanmaDetailView.as_view(), name='u2_qollanma_detail'),
    path('u3_qollanma/<int:pk>/', U3QollanmaDetailView.as_view(), name='u3_qollanma_detail'),

    # Loyiha
    path('loyiha_list/', loyiha_list, name='loyiha_list'),
    path('m_loyiha_list/', m_loyiha_list, name='m_loyiha_list'),
    path('u1_loyiha_list/', u1_loyiha_list, name='u1_loyiha_list'),
    path('u2_loyiha_list/', U2LoyihaListView.as_view(), name='u2_loyiha_list'),
    path('u3_loyiha_list/', U3LoyihaListView.as_view(), name='u3_loyiha_list'),
    path('loyiha_list/create/', loyiha_create, name='loyiha_create'),
    path('m_loyiha_list/create/', m_loyiha_create, name='m_loyiha_create'),
    path('loyiha/edit/<int:loyiha_id>/', loyiha_edit, name='loyiha_edit'),
    path('m_loyiha/edit/<int:loyiha_id>/', m_loyiha_edit, name='m_loyiha_edit'),
    path('loyiha/delete/<int:loyiha_id>/', loyiha_delete, name='loyiha_delete'),
    path('m_loyiha/delete/<int:loyiha_id>/', m_loyiha_delete, name='m_loyiha_delete'),
    path('u1_loyiha/<int:loyiha_id>/', u1_loyiha_detail, name='u1_loyiha_detail'),
    path('u2_loyiha/<int:pk>/', U2LoyihaDetailView.as_view(), name='u2_loyiha_detail'),
    path('u3_loyiha/<int:pk>/', U3LoyihaDetailView.as_view(), name='u3_loyiha_detail'),

    # Jurnal
    path('jurnal_list/', jurnal_list, name='jurnal_list'),
    path('m_jurnal_list/', m_jurnal_list, name='m_jurnal_list'),
    path('u1_jurnal_list/', u1_jurnal_list, name='u1_jurnal_list'),
    path('u2_jurnal_list/', U2JurnalListView.as_view(), name='u2_jurnal_list'),
    path('u3_jurnal_list/', U3JurnalListView.as_view(), name='u3_jurnal_list'),
    path('jurnal_list/create/', jurnal_create, name='jurnal_create'),
    path('m_jurnal_list/create/', m_jurnal_create, name='m_jurnal_create'),
    path('jurnal/edit/<int:jurnal_id>/', jurnal_edit, name='jurnal_edit'),
    path('m_jurnal/edit/<int:jurnal_id>/', m_jurnal_edit, name='m_jurnal_edit'),
    path('jurnal/delete/<int:jurnal_id>/', jurnal_delete, name='jurnal_delete'),
    path('m_jurnal/delete/<int:jurnal_id>/', m_jurnal_delete, name='m_jurnal_delete'),
    path('u1_jurnal/<int:jurnal_id>/', u1_jurnal_detail, name='u1_jurnal_detail'),
    path('u2_jurnal/<int:pk>/', U2JurnalDetailView.as_view(), name='u2_jurnal_detail'),
    path('u3_jurnal/<int:pk>/', U3JurnalDetailView.as_view(), name='u3_jurnal_detail'),

    # Maqola
    path('maqola_list/', maqola_list, name='maqola_list'),
    path('m_maqola_list/', m_maqola_list, name='m_maqola_list'),
    path('u1_maqola_list/', u1_maqola_list, name='u1_maqola_list'),
    path('u2_maqola_list/', U2MaqolaListView.as_view(), name='u2_maqola_list'),
    path('u3_maqola_list/', U3MaqolaListView.as_view(), name='u3_maqola_list'),
    path('maqola_list/create/', maqola_create, name='maqola_create'),
    path('m_maqola_list/create/', m_maqola_create, name='m_maqola_create'),
    path('maqola/edit/<int:maqola_id>/', maqola_edit, name='maqola_edit'),
    path('m_maqola/edit/<int:maqola_id>/', m_maqola_edit, name='m_maqola_edit'),
    path('maqola/delete/<int:maqola_id>/', maqola_delete, name='maqola_delete'),
    path('m_maqola/delete/<int:maqola_id>/', m_maqola_delete, name='m_maqola_delete'),
    path('u1_maqola/<int:maqola_id>/', u1_maqola_detail, name='u1_maqola_detail'),
    path('u2_maqola/<int:pk>/', U2MaqolaDetailView.as_view(), name='u2_maqola_detail'),
    path('u3_maqola/<int:pk>/', U3MaqolaDetailView.as_view(), name='u3_maqola_detail'),

    # Other
    path('other_list/', other_list, name='other_list'),
    path('m_other_list/', m_other_list, name='m_other_list'),
    path('u1_other_list/', u1_other_list, name='u1_other_list'),
    path('u2_other_list/', U2OtherListView.as_view(), name='u2_other_list'),
    path('u3_other_list/', U3OtherListView.as_view(), name='u3_other_list'),
    path('other_list/create/', other_create, name='other_create'),
    path('m_other_list/create/', m_other_create, name='m_other_create'),
    path('other/edit/<int:other_id>/', other_edit, name='other_edit'),
    path('m_other/edit/<int:other_id>/', m_other_edit, name='m_other_edit'),
    path('other/delete/<int:other_id>/', other_delete, name='other_delete'),
    path('m_other/delete/<int:other_id>/', m_other_delete, name='m_other_delete'),
    path('u1_other/<int:other_id>/', u1_other_detail, name='u1_other_detail'),
    path('u2_other/<int:pk>/', U2OtherDetailView.as_view(), name='u2_other_detail'),
    path('u3_other/<int:pk>/', U3OtherDetailView.as_view(), name='u3_other_detail'),

    # Tajriba
    path('tajriba_list/', tajriba_list, name='tajriba_list'),
    path('m_tajriba_list/', m_tajriba_list, name='m_tajriba_list'),
    path('u1_tajriba_list/', u1_tajriba_list, name='u1_tajriba_list'),
    path('u2_tajriba_list/', U2TajribaListView.as_view(), name='u2_tajriba_list'),
    path('u3_tajriba_list/', U2TajribaListView.as_view(), name='u3_tajriba_list'),
    path('tajriba_list/create/', tajriba_create, name='tajriba_create'),
    path('m_tajriba_list/create/', m_tajriba_create, name='m_tajriba_create'),
    path('tajriba/edit/<int:tajriba_id>/', tajriba_edit, name='tajriba_edit'),
    path('m_tajriba/edit/<int:tajriba_id>/', m_tajriba_edit, name='m_tajriba_edit'),
    path('tajriba/delete/<int:tajriba_id>/', tajriba_delete, name='tajriba_delete'),
    path('m_tajriba/delete/<int:tajriba_id>/', m_tajriba_delete, name='m_tajriba_delete'),
    path('u1_tajriba/<int:tajriba_id>/', u1_tajriba_detail, name='u1_tajriba_detail'),
    path('u2_tajriba/<int:pk>/', U2TajribaDetailView.as_view(), name='u2_tajriba_detail'),
    path('u3_tajriba/<int:pk>/', U3TajribaDetailView.as_view(), name='u3_tajriba_detail'),

]
