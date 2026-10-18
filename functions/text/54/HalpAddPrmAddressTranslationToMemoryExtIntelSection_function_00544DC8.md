# HalpAddPrmAddressTranslationToMemoryExtIntelSection

- RVA: `0x00544DC8`–`0x0054515F` (길이 `919` bytes)
- VA: `0x0000000140544DC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3C64`
- 디코드: `262`개 명령, `919/919` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00544DF2` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00544DFF` → [WheaPrmTranslatePhysicalAddress](../66/WheaPrmTranslatePhysicalAddress_function_00660AD0.md) (function, `0x00660AD0`)

### Direct callers
- [HalpCreateMcaMemoryErrorRecord](HalpCreateMcaMemoryErrorRecord_function_00540C78.md) at `0x00540FA8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00544DC8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00544DCD  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00544DD2  55                              push rbp
00544DD3  48 8D 6C 24 A0                  lea rbp, [rsp - 0x60]
00544DD8  48 81 EC 60 01 00 00            sub rsp, 0x160
00544DDF  48 8B FA                        mov rdi, rdx
00544DE2  48 8B D9                        mov rbx, rcx
00544DE5  33 D2                           xor edx, edx
00544DE7  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00544DEC  41 B8 34 01 00 00               mov r8d, 0x134
00544DF2  E8 49 1E 18 00                  call 0x1406c6c40
00544DF7  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00544DFC  48 8B CB                        mov rcx, rbx
00544DFF  E8 CC BC 11 00                  call 0x140660ad0
00544E04  44 8B C8                        mov r9d, eax
00544E07  85 C0                           test eax, eax
00544E09  0F 88 31 03 00 00               js 0x140545140
00544E0F  4C 8B 44 24 54                  mov r8, qword ptr [rsp + 0x54]
00544E14  49 83 CA FF                     or r10, 0xffffffffffffffff
00544E18  4D 3B C2                        cmp r8, r10
00544E1B  0F 84 FC 00 00 00               je 0x140544f1d
00544E21  48 8B 54 24 2C                  mov rdx, qword ptr [rsp + 0x2c]
00544E26  48 8D 4F 08                     lea rcx, [rdi + 8]
00544E2A  48 8B 01                        mov rax, qword ptr [rcx]
00544E2D  48 83 C8 01                     or rax, 1
00544E31  C7 47 10 01 00 00 00            mov dword ptr [rdi + 0x10], 1
00544E38  49 3B D2                        cmp rdx, r10
00544E3B  74 08                           je 0x140544e45
00544E3D  48 89 57 14                     mov qword ptr [rdi + 0x14], rdx
00544E41  48 83 C8 02                     or rax, 2
00544E45  48 8B 54 24 74                  mov rdx, qword ptr [rsp + 0x74]
00544E4A  49 3B D2                        cmp rdx, r10
00544E4D  74 08                           je 0x140544e57
00544E4F  48 89 57 2C                     mov qword ptr [rdi + 0x2c], rdx
00544E53  48 83 C8 10                     or rax, 0x10
00544E57  48 8B 55 94                     mov rdx, qword ptr [rbp - 0x6c]
00544E5B  49 3B D2                        cmp rdx, r10
00544E5E  74 08                           je 0x140544e68
00544E60  48 89 57 34                     mov qword ptr [rdi + 0x34], rdx
00544E64  48 83 C8 20                     or rax, 0x20
00544E68  48 8B 55 84                     mov rdx, qword ptr [rbp - 0x7c]
00544E6C  48 0F BA E8 07                  bts rax, 7
00544E71  48 89 01                        mov qword ptr [rcx], rax
00544E74  44 88 47 3D                     mov byte ptr [rdi + 0x3d], r8b
00544E78  49 3B D2                        cmp rdx, r10
00544E7B  74 0B                           je 0x140544e88
00544E7D  48 0F BA E8 0A                  bts rax, 0xa
00544E82  88 57 40                        mov byte ptr [rdi + 0x40], dl
00544E85  48 89 01                        mov qword ptr [rcx], rax
00544E88  48 8B 55 A4                     mov rdx, qword ptr [rbp - 0x5c]
00544E8C  49 3B D2                        cmp rdx, r10
00544E8F  74 0B                           je 0x140544e9c
00544E91  48 0F BA E8 0C                  bts rax, 0xc
00544E96  88 57 42                        mov byte ptr [rdi + 0x42], dl
00544E99  48 89 01                        mov qword ptr [rcx], rax
00544E9C  48 8B 55 B4                     mov rdx, qword ptr [rbp - 0x4c]
00544EA0  49 3B D2                        cmp rdx, r10
00544EA3  74 0B                           je 0x140544eb0
00544EA5  48 0F BA E8 0D                  bts rax, 0xd
00544EAA  88 57 43                        mov byte ptr [rdi + 0x43], dl
00544EAD  48 89 01                        mov qword ptr [rcx], rax
00544EB0  48 8B 55 EC                     mov rdx, qword ptr [rbp - 0x14]
00544EB4  49 3B D2                        cmp rdx, r10
00544EB7  74 0B                           je 0x140544ec4
00544EB9  48 0F BA E8 0F                  bts rax, 0xf
00544EBE  88 57 45                        mov byte ptr [rdi + 0x45], dl
00544EC1  48 89 01                        mov qword ptr [rcx], rax
00544EC4  48 8B 55 FC                     mov rdx, qword ptr [rbp - 4]
00544EC8  49 3B D2                        cmp rdx, r10
00544ECB  74 0B                           je 0x140544ed8
00544ECD  48 0F BA E8 10                  bts rax, 0x10
00544ED2  88 57 46                        mov byte ptr [rdi + 0x46], dl
00544ED5  48 89 01                        mov qword ptr [rcx], rax
00544ED8  48 8B 55 CC                     mov rdx, qword ptr [rbp - 0x34]
00544EDC  49 3B D2                        cmp rdx, r10
00544EDF  74 0B                           je 0x140544eec
00544EE1  48 0F BA E8 11                  bts rax, 0x11
00544EE6  89 57 47                        mov dword ptr [rdi + 0x47], edx
00544EE9  48 89 01                        mov qword ptr [rcx], rax
00544EEC  48 8B 55 DC                     mov rdx, qword ptr [rbp - 0x24]
00544EF0  49 3B D2                        cmp rdx, r10
00544EF3  74 0B                           je 0x140544f00
00544EF5  48 0F BA E8 12                  bts rax, 0x12
00544EFA  89 57 4B                        mov dword ptr [rdi + 0x4b], edx
00544EFD  48 89 01                        mov qword ptr [rcx], rax
00544F00  48 8B 55 2C                     mov rdx, qword ptr [rbp + 0x2c]
00544F04  49 3B D2                        cmp rdx, r10
00544F07  74 0B                           je 0x140544f14
00544F09  48 0F BA E8 17                  bts rax, 0x17
00544F0E  88 57 53                        mov byte ptr [rdi + 0x53], dl
00544F11  48 89 01                        mov qword ptr [rcx], rax
00544F14  48 8B 55 44                     mov rdx, qword ptr [rbp + 0x44]
00544F18  E9 05 01 00 00                  jmp 0x140545022
00544F1D  4C 8B 44 24 5C                  mov r8, qword ptr [rsp + 0x5c]
00544F22  4D 3B C2                        cmp r8, r10
00544F25  0F 84 0A 02 00 00               je 0x140545135
00544F2B  48 8B 54 24 34                  mov rdx, qword ptr [rsp + 0x34]
00544F30  48 8D 4F 08                     lea rcx, [rdi + 8]
00544F34  48 8B 01                        mov rax, qword ptr [rcx]
00544F37  48 83 C8 01                     or rax, 1
00544F3B  C7 47 10 02 00 00 00            mov dword ptr [rdi + 0x10], 2
00544F42  49 3B D2                        cmp rdx, r10
00544F45  74 08                           je 0x140544f4f
00544F47  48 89 57 14                     mov qword ptr [rdi + 0x14], rdx
00544F4B  48 83 C8 02                     or rax, 2
00544F4F  48 8B 54 24 7C                  mov rdx, qword ptr [rsp + 0x7c]
00544F54  49 3B D2                        cmp rdx, r10
00544F57  74 08                           je 0x140544f61
00544F59  48 89 57 2C                     mov qword ptr [rdi + 0x2c], rdx
00544F5D  48 83 C8 10                     or rax, 0x10
00544F61  48 8B 55 9C                     mov rdx, qword ptr [rbp - 0x64]
00544F65  49 3B D2                        cmp rdx, r10
00544F68  74 08                           je 0x140544f72
00544F6A  48 89 57 34                     mov qword ptr [rdi + 0x34], rdx
00544F6E  48 83 C8 20                     or rax, 0x20
00544F72  48 8B 55 8C                     mov rdx, qword ptr [rbp - 0x74]
00544F76  48 0F BA E8 07                  bts rax, 7
00544F7B  48 89 01                        mov qword ptr [rcx], rax
00544F7E  44 88 47 3D                     mov byte ptr [rdi + 0x3d], r8b
00544F82  49 3B D2                        cmp rdx, r10
00544F85  74 0B                           je 0x140544f92
00544F87  48 0F BA E8 0A                  bts rax, 0xa
00544F8C  88 57 40                        mov byte ptr [rdi + 0x40], dl
00544F8F  48 89 01                        mov qword ptr [rcx], rax
00544F92  48 8B 55 AC                     mov rdx, qword ptr [rbp - 0x54]
00544F96  49 3B D2                        cmp rdx, r10
00544F99  74 0B                           je 0x140544fa6
00544F9B  48 0F BA E8 0C                  bts rax, 0xc
00544FA0  88 57 42                        mov byte ptr [rdi + 0x42], dl
00544FA3  48 89 01                        mov qword ptr [rcx], rax
00544FA6  48 8B 55 BC                     mov rdx, qword ptr [rbp - 0x44]
00544FAA  49 3B D2                        cmp rdx, r10
00544FAD  74 0B                           je 0x140544fba
00544FAF  48 0F BA E8 0D                  bts rax, 0xd
00544FB4  88 57 43                        mov byte ptr [rdi + 0x43], dl
00544FB7  48 89 01                        mov qword ptr [rcx], rax
00544FBA  48 8B 55 F4                     mov rdx, qword ptr [rbp - 0xc]
00544FBE  49 3B D2                        cmp rdx, r10
00544FC1  74 0B                           je 0x140544fce
00544FC3  48 0F BA E8 0F                  bts rax, 0xf
00544FC8  88 57 45                        mov byte ptr [rdi + 0x45], dl
00544FCB  48 89 01                        mov qword ptr [rcx], rax
00544FCE  48 8B 55 04                     mov rdx, qword ptr [rbp + 4]
00544FD2  49 3B D2                        cmp rdx, r10
00544FD5  74 0B                           je 0x140544fe2
00544FD7  48 0F BA E8 10                  bts rax, 0x10
00544FDC  88 57 46                        mov byte ptr [rdi + 0x46], dl
00544FDF  48 89 01                        mov qword ptr [rcx], rax
00544FE2  48 8B 55 D4                     mov rdx, qword ptr [rbp - 0x2c]
00544FE6  49 3B D2                        cmp rdx, r10
00544FE9  74 0B                           je 0x140544ff6
00544FEB  48 0F BA E8 11                  bts rax, 0x11
00544FF0  89 57 47                        mov dword ptr [rdi + 0x47], edx
00544FF3  48 89 01                        mov qword ptr [rcx], rax
00544FF6  48 8B 55 E4                     mov rdx, qword ptr [rbp - 0x1c]
00544FFA  49 3B D2                        cmp rdx, r10
00544FFD  74 0B                           je 0x14054500a
00544FFF  48 0F BA E8 12                  bts rax, 0x12
00545004  89 57 4B                        mov dword ptr [rdi + 0x4b], edx
00545007  48 89 01                        mov qword ptr [rcx], rax
0054500A  48 8B 55 34                     mov rdx, qword ptr [rbp + 0x34]
0054500E  49 3B D2                        cmp rdx, r10
00545011  74 0B                           je 0x14054501e
00545013  48 0F BA E8 17                  bts rax, 0x17
00545018  88 57 53                        mov byte ptr [rdi + 0x53], dl
0054501B  48 89 01                        mov qword ptr [rcx], rax
0054501E  48 8B 55 4C                     mov rdx, qword ptr [rbp + 0x4c]
00545022  49 3B D2                        cmp rdx, r10
00545025  74 0B                           je 0x140545032
00545027  48 0F BA E8 19                  bts rax, 0x19
0054502C  88 57 55                        mov byte ptr [rdi + 0x55], dl
0054502F  48 89 01                        mov qword ptr [rcx], rax
00545032  48 8B 54 24 3C                  mov rdx, qword ptr [rsp + 0x3c]
00545037  49 3B D2                        cmp rdx, r10
0054503A  74 0B                           je 0x140545047
0054503C  48 83 C8 04                     or rax, 4
00545040  48 89 57 1C                     mov qword ptr [rdi + 0x1c], rdx
00545044  48 89 01                        mov qword ptr [rcx], rax
00545047  48 8B 54 24 44                  mov rdx, qword ptr [rsp + 0x44]
0054504C  49 3B D2                        cmp rdx, r10
0054504F  74 0B                           je 0x14054505c
00545051  48 83 C8 08                     or rax, 8
00545055  48 89 57 24                     mov qword ptr [rdi + 0x24], rdx
00545059  48 89 01                        mov qword ptr [rcx], rax
0054505C  48 8B 54 24 4C                  mov rdx, qword ptr [rsp + 0x4c]
00545061  49 3B D2                        cmp rdx, r10
00545064  74 0A                           je 0x140545070
00545066  48 83 C8 40                     or rax, 0x40
0054506A  88 57 3C                        mov byte ptr [rdi + 0x3c], dl
0054506D  48 89 01                        mov qword ptr [rcx], rax
00545070  48 8B 54 24 64                  mov rdx, qword ptr [rsp + 0x64]
00545075  49 3B D2                        cmp rdx, r10
00545078  74 0B                           je 0x140545085
0054507A  48 0F BA E8 08                  bts rax, 8
0054507F  88 57 3E                        mov byte ptr [rdi + 0x3e], dl
00545082  48 89 01                        mov qword ptr [rcx], rax
00545085  48 8B 54 24 6C                  mov rdx, qword ptr [rsp + 0x6c]
0054508A  49 3B D2                        cmp rdx, r10
0054508D  74 0B                           je 0x14054509a
0054508F  48 0F BA E8 09                  bts rax, 9
00545094  88 57 3F                        mov byte ptr [rdi + 0x3f], dl
00545097  48 89 01                        mov qword ptr [rcx], rax
0054509A  48 8B 55 C4                     mov rdx, qword ptr [rbp - 0x3c]
0054509E  49 3B D2                        cmp rdx, r10
005450A1  74 0B                           je 0x1405450ae
005450A3  48 0F BA E8 0E                  bts rax, 0xe
005450A8  88 57 44                        mov byte ptr [rdi + 0x44], dl
005450AB  48 89 01                        mov qword ptr [rcx], rax
005450AE  48 8B 55 0C                     mov rdx, qword ptr [rbp + 0xc]
005450B2  49 3B D2                        cmp rdx, r10
005450B5  74 0B                           je 0x1405450c2
005450B7  48 0F BA E8 13                  bts rax, 0x13
005450BC  88 57 4F                        mov byte ptr [rdi + 0x4f], dl
005450BF  48 89 01                        mov qword ptr [rcx], rax
005450C2  48 8B 55 14                     mov rdx, qword ptr [rbp + 0x14]
005450C6  49 3B D2                        cmp rdx, r10
005450C9  74 0B                           je 0x1405450d6
005450CB  48 0F BA E8 14                  bts rax, 0x14
005450D0  88 57 50                        mov byte ptr [rdi + 0x50], dl
005450D3  48 89 01                        mov qword ptr [rcx], rax
005450D6  48 8B 55 1C                     mov rdx, qword ptr [rbp + 0x1c]
005450DA  49 3B D2                        cmp rdx, r10
005450DD  74 0B                           je 0x1405450ea
005450DF  48 0F BA E8 15                  bts rax, 0x15
005450E4  88 57 51                        mov byte ptr [rdi + 0x51], dl
005450E7  48 89 01                        mov qword ptr [rcx], rax
005450EA  48 8B 55 24                     mov rdx, qword ptr [rbp + 0x24]
005450EE  49 3B D2                        cmp rdx, r10
005450F1  74 0B                           je 0x1405450fe
005450F3  48 0F BA E8 16                  bts rax, 0x16
005450F8  88 57 52                        mov byte ptr [rdi + 0x52], dl
005450FB  48 89 01                        mov qword ptr [rcx], rax
005450FE  48 8B 55 3C                     mov rdx, qword ptr [rbp + 0x3c]
00545102  49 3B D2                        cmp rdx, r10
00545105  74 39                           je 0x140545140
00545107  48 0F BA E8 18                  bts rax, 0x18
0054510C  88 57 54                        mov byte ptr [rdi + 0x54], dl
0054510F  48 89 01                        mov qword ptr [rcx], rax
00545112  48 8B 07                        mov rax, qword ptr [rdi]
00545115  48 83 C8 01                     or rax, 1
00545119  48 89 07                        mov qword ptr [rdi], rax
0054511C  4C 8D 9C 24 60 01 00 00         lea r11, [rsp + 0x160]
00545124  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00545128  41 8B C1                        mov eax, r9d
0054512B  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
0054512F  49 8B E3                        mov rsp, r11
00545132  5D                              pop rbp
00545133  C3                              ret
00545134  CC                              int3
00545135  48 8B 07                        mov rax, qword ptr [rdi]
00545138  41 B9 01 00 00 C0               mov r9d, 0xc0000001
0054513E  EB 19                           jmp 0x140545159
00545140  48 8B 07                        mov rax, qword ptr [rdi]
00545143  41 8B C9                        mov ecx, r9d
00545146  41 81 F9 BB 00 00 C0            cmp r9d, 0xc00000bb
0054514D  75 06                           jne 0x140545155
0054514F  48 83 C8 04                     or rax, 4
00545153  EB C4                           jmp 0x140545119
00545155  85 C9                           test ecx, ecx
00545157  79 BC                           jns 0x140545115
00545159  48 83 C8 02                     or rax, 2
0054515D  EB BA                           jmp 0x140545119
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAddPrmAddressTranslationToMemoryExtIntelSection(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m104;
    unsigned __int64 v_stack_m10C;
    unsigned __int64 v_stack_m114;
    unsigned __int64 v_stack_m11C;
    unsigned __int64 v_stack_m124;
    unsigned __int64 v_stack_m12C;
    unsigned __int64 v_stack_m134;
    unsigned __int64 v_stack_m13C;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m1C;
    unsigned __int64 v_stack_m24;
    unsigned __int64 v_stack_m2C;
    unsigned __int64 v_stack_m34;
    unsigned __int64 v_stack_m3C;
    unsigned __int64 v_stack_m44;
    unsigned __int64 v_stack_m4C;
    unsigned __int64 v_stack_m54;
    unsigned __int64 v_stack_m5C;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m6C;
    unsigned __int64 v_stack_m74;
    unsigned __int64 v_stack_m7C;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m84;
    unsigned __int64 v_stack_m8C;
    unsigned __int64 v_stack_m94;
    unsigned __int64 v_stack_m9C;
    unsigned __int64 v_stack_mA4;
    unsigned __int64 v_stack_mAC;
    unsigned __int64 v_stack_mB4;
    unsigned __int64 v_stack_mBC;
    unsigned __int64 v_stack_mC4;
    unsigned __int64 v_stack_mCC;
    unsigned __int64 v_stack_mD4;
    unsigned __int64 v_stack_mDC;
    unsigned __int64 v_stack_mE4;
    unsigned __int64 v_stack_mEC;
    unsigned __int64 v_stack_mF4;
    unsigned __int64 v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (352);
    a2 = 0;
    result = memset(v_stack_m148, a2, 308, a4);
    result = WheaPrmTranslatePhysicalAddress(a1, v_stack_m148, 308, a4);
    if (sign_flag) goto loc_00545140;
    v_r10 = (v_r10) | (-1);
    if (v_stack_m114 == v_r10) goto loc_00544F1D;
    result = (*(unsigned __int64 *)(a2 + 8)) | (1);
    *(unsigned int *)(a2 + 16) = 1;
    if (v_stack_m13C != v_r10) {
        *(unsigned __int64 *)(a2 + 20) = v_stack_m13C;
        result = (result) | (2);
    }
    if (v_stack_mF4 != v_r10) {
        *(unsigned __int64 *)(a2 + 44) = v_stack_mF4;
        result = (result) | (16);
    }
    if (v_stack_mD4 != v_r10) {
        *(unsigned __int64 *)(a2 + 52) = v_stack_mD4;
        result = (result) | (32);
    }
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned __int8 *)(a2 + 61) = (unsigned __int8)(v_stack_m114);
    if (v_stack_mE4 != v_r10) {
        *(unsigned __int8 *)(a2 + 64) = (unsigned __int8)(v_stack_mE4);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mC4 != v_r10) {
        *(unsigned __int8 *)(a2 + 66) = (unsigned __int8)(v_stack_mC4);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mB4 != v_r10) {
        *(unsigned __int8 *)(a2 + 67) = (unsigned __int8)(v_stack_mB4);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m7C != v_r10) {
        *(unsigned __int8 *)(a2 + 69) = (unsigned __int8)(v_stack_m7C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m6C != v_r10) {
        *(unsigned __int8 *)(a2 + 70) = (unsigned __int8)(v_stack_m6C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m9C != v_r10) {
        *(unsigned int *)(a2 + 71) = (unsigned int)(v_stack_m9C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m8C != v_r10) {
        *(unsigned int *)(a2 + 75) = (unsigned int)(v_stack_m8C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m3C != v_r10) {
        *(unsigned __int8 *)(a2 + 83) = (unsigned __int8)(v_stack_m3C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    goto loc_00545022;
loc_00544F1D:
    if (v_stack_m10C == v_r10) goto loc_00545135;
    result = (*(unsigned __int64 *)(a2 + 8)) | (1);
    *(unsigned int *)(a2 + 16) = 2;
    if (v_stack_m134 != v_r10) {
        *(unsigned __int64 *)(a2 + 20) = v_stack_m134;
        result = (result) | (2);
    }
    if (v_stack_mEC != v_r10) {
        *(unsigned __int64 *)(a2 + 44) = v_stack_mEC;
        result = (result) | (16);
    }
    if (v_stack_mCC != v_r10) {
        *(unsigned __int64 *)(a2 + 52) = v_stack_mCC;
        result = (result) | (32);
    }
    *(unsigned __int64 *)(a2 + 8) = result;
    *(unsigned __int8 *)(a2 + 61) = (unsigned __int8)(v_stack_m10C);
    if (v_stack_mDC != v_r10) {
        *(unsigned __int8 *)(a2 + 64) = (unsigned __int8)(v_stack_mDC);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mBC != v_r10) {
        *(unsigned __int8 *)(a2 + 66) = (unsigned __int8)(v_stack_mBC);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mAC != v_r10) {
        *(unsigned __int8 *)(a2 + 67) = (unsigned __int8)(v_stack_mAC);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m74 != v_r10) {
        *(unsigned __int8 *)(a2 + 69) = (unsigned __int8)(v_stack_m74);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m64 != v_r10) {
        *(unsigned __int8 *)(a2 + 70) = (unsigned __int8)(v_stack_m64);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m94 != v_r10) {
        *(unsigned int *)(a2 + 71) = (unsigned int)(v_stack_m94);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m84 != v_r10) {
        *(unsigned int *)(a2 + 75) = (unsigned int)(v_stack_m84);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m34 != v_r10) {
        *(unsigned __int8 *)(a2 + 83) = (unsigned __int8)(v_stack_m34);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
loc_00545022:
    if (v_stack_m1C != v_r10) {
        *(unsigned __int8 *)(a2 + 85) = (unsigned __int8)(v_stack_m1C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m12C != v_r10) {
        result = (result) | (4);
        *(unsigned __int64 *)(a2 + 28) = v_stack_m12C;
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m124 != v_r10) {
        result = (result) | (8);
        *(unsigned __int64 *)(a2 + 36) = v_stack_m124;
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m11C != v_r10) {
        result = (result) | (64);
        *(unsigned __int8 *)(a2 + 60) = (unsigned __int8)(v_stack_m11C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m104 != v_r10) {
        *(unsigned __int8 *)(a2 + 62) = (unsigned __int8)(v_stack_m104);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mFC != v_r10) {
        *(unsigned __int8 *)(a2 + 63) = (unsigned __int8)(v_stack_mFC);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_mA4 != v_r10) {
        *(unsigned __int8 *)(a2 + 68) = (unsigned __int8)(v_stack_mA4);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m5C != v_r10) {
        *(unsigned __int8 *)(a2 + 79) = (unsigned __int8)(v_stack_m5C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m54 != v_r10) {
        *(unsigned __int8 *)(a2 + 80) = (unsigned __int8)(v_stack_m54);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m4C != v_r10) {
        *(unsigned __int8 *)(a2 + 81) = (unsigned __int8)(v_stack_m4C);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m44 != v_r10) {
        *(unsigned __int8 *)(a2 + 82) = (unsigned __int8)(v_stack_m44);
        *(unsigned __int64 *)(a2 + 8) = result;
    }
    if (v_stack_m2C == v_r10) goto loc_00545140;
    *(unsigned __int8 *)(a2 + 84) = (unsigned __int8)(v_stack_m2C);
    *(unsigned __int64 *)(a2 + 8) = result;
loc_00545115:
    result = (*(unsigned __int64 *)(a2)) | (1);
loc_00545119:
    *(unsigned __int64 *)(a2) = result;
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00545135:
    goto loc_00545159;
loc_00545140:
    if (((unsigned int)((unsigned int)(0xC0000001ULL))) != 0xC00000BBULL) goto loc_00545155;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m8 + 24))) | (4);
    goto loc_00545119;
loc_00545155:
    if (!sign_flag) goto loc_00545115;
loc_00545159:
    result = (result) | (2);
    goto loc_00545119;
}
```

## 5. (Beta) C Style

```c
int64_t HalpAddPrmAddressTranslationToMemoryExtIntelSection(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m104;
    uint64_t v_stack_m10C;
    uint64_t v_stack_m114;
    uint64_t v_stack_m11C;
    uint64_t v_stack_m124;
    uint64_t v_stack_m12C;
    uint64_t v_stack_m134;
    uint64_t v_stack_m13C;
    uint64_t v_stack_m148;
    uint64_t v_stack_m1C;
    uint64_t v_stack_m24;
    uint64_t v_stack_m2C;
    uint64_t v_stack_m34;
    uint64_t v_stack_m3C;
    uint64_t v_stack_m44;
    uint64_t v_stack_m4C;
    uint64_t v_stack_m54;
    uint64_t v_stack_m5C;
    uint64_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m6C;
    uint64_t v_stack_m74;
    uint64_t v_stack_m7C;
    uint64_t v_stack_m8;
    uint64_t v_stack_m84;
    uint64_t v_stack_m8C;
    uint64_t v_stack_m94;
    uint64_t v_stack_m9C;
    uint64_t v_stack_mA4;
    uint64_t v_stack_mAC;
    uint64_t v_stack_mB4;
    uint64_t v_stack_mBC;
    uint64_t v_stack_mC4;
    uint64_t v_stack_mCC;
    uint64_t v_stack_mD4;
    uint64_t v_stack_mDC;
    uint64_t v_stack_mE4;
    uint64_t v_stack_mEC;
    uint64_t v_stack_mF4;
    uint64_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (352);
    Arg2 = 0;
    result = memset(v_stack_m148, Arg2, 308, a4);
    result = WheaPrmTranslatePhysicalAddress(Arg1, v_stack_m148, 308, a4);
    if (sign_flag) goto loc_00545140;
    local_r10 = (local_r10) | (-1);
    if (v_stack_m114 == local_r10) goto loc_00544F1D;
    result = (*(uint64_t *)(arg2 + 0x8)) | (1);
    *(uint32_t *)(arg2 + 0x10) = 1;
    if (v_stack_m13C != local_r10) {
        *(uint64_t *)(arg2 + 0x14) = v_stack_m13C;
        result = (result) | (2);
    }
    if (v_stack_mF4 != local_r10) {
        *(uint64_t *)(arg2 + 0x2C) = v_stack_mF4;
        result = (result) | (16);
    }
    if (v_stack_mD4 != local_r10) {
        *(uint64_t *)(arg2 + 0x34) = v_stack_mD4;
        result = (result) | (32);
    }
    *(uint64_t *)(arg2 + 0x8) = result;
    *(uint8_t *)(arg2 + 0x3D) = (uint8_t)(v_stack_m114);
    if (v_stack_mE4 != local_r10) {
        *(uint8_t *)(arg2 + 0x40) = (uint8_t)(v_stack_mE4);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mC4 != local_r10) {
        *(uint8_t *)(arg2 + 0x42) = (uint8_t)(v_stack_mC4);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mB4 != local_r10) {
        *(uint8_t *)(arg2 + 0x43) = (uint8_t)(v_stack_mB4);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m7C != local_r10) {
        *(uint8_t *)(arg2 + 0x45) = (uint8_t)(v_stack_m7C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m6C != local_r10) {
        *(uint8_t *)(arg2 + 0x46) = (uint8_t)(v_stack_m6C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m9C != local_r10) {
        *(uint32_t *)(arg2 + 0x47) = (uint32_t)(v_stack_m9C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m8C != local_r10) {
        *(uint32_t *)(arg2 + 0x4B) = (uint32_t)(v_stack_m8C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m3C != local_r10) {
        *(uint8_t *)(arg2 + 0x53) = (uint8_t)(v_stack_m3C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    goto loc_00545022;
loc_00544F1D:
    if (v_stack_m10C == local_r10) goto loc_00545135;
    result = (*(uint64_t *)(arg2 + 0x8)) | (1);
    *(uint32_t *)(arg2 + 0x10) = 2;
    if (v_stack_m134 != local_r10) {
        *(uint64_t *)(arg2 + 0x14) = v_stack_m134;
        result = (result) | (2);
    }
    if (v_stack_mEC != local_r10) {
        *(uint64_t *)(arg2 + 0x2C) = v_stack_mEC;
        result = (result) | (16);
    }
    if (v_stack_mCC != local_r10) {
        *(uint64_t *)(arg2 + 0x34) = v_stack_mCC;
        result = (result) | (32);
    }
    *(uint64_t *)(arg2 + 0x8) = result;
    *(uint8_t *)(arg2 + 0x3D) = (uint8_t)(v_stack_m10C);
    if (v_stack_mDC != local_r10) {
        *(uint8_t *)(arg2 + 0x40) = (uint8_t)(v_stack_mDC);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mBC != local_r10) {
        *(uint8_t *)(arg2 + 0x42) = (uint8_t)(v_stack_mBC);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mAC != local_r10) {
        *(uint8_t *)(arg2 + 0x43) = (uint8_t)(v_stack_mAC);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m74 != local_r10) {
        *(uint8_t *)(arg2 + 0x45) = (uint8_t)(v_stack_m74);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m64 != local_r10) {
        *(uint8_t *)(arg2 + 0x46) = (uint8_t)(v_stack_m64);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m94 != local_r10) {
        *(uint32_t *)(arg2 + 0x47) = (uint32_t)(v_stack_m94);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m84 != local_r10) {
        *(uint32_t *)(arg2 + 0x4B) = (uint32_t)(v_stack_m84);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m34 != local_r10) {
        *(uint8_t *)(arg2 + 0x53) = (uint8_t)(v_stack_m34);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
loc_00545022:
    if (v_stack_m1C != local_r10) {
        *(uint8_t *)(arg2 + 0x55) = (uint8_t)(v_stack_m1C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m12C != local_r10) {
        result = (result) | (4);
        *(uint64_t *)(arg2 + 0x1C) = v_stack_m12C;
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m124 != local_r10) {
        result = (result) | (8);
        *(uint64_t *)(arg2 + 0x24) = v_stack_m124;
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m11C != local_r10) {
        result = (result) | (64);
        *(uint8_t *)(arg2 + 0x3C) = (uint8_t)(v_stack_m11C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m104 != local_r10) {
        *(uint8_t *)(arg2 + 0x3E) = (uint8_t)(v_stack_m104);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mFC != local_r10) {
        *(uint8_t *)(arg2 + 0x3F) = (uint8_t)(v_stack_mFC);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_mA4 != local_r10) {
        *(uint8_t *)(arg2 + 0x44) = (uint8_t)(v_stack_mA4);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m5C != local_r10) {
        *(uint8_t *)(arg2 + 0x4F) = (uint8_t)(v_stack_m5C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m54 != local_r10) {
        *(uint8_t *)(arg2 + 0x50) = (uint8_t)(v_stack_m54);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m4C != local_r10) {
        *(uint8_t *)(arg2 + 0x51) = (uint8_t)(v_stack_m4C);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m44 != local_r10) {
        *(uint8_t *)(arg2 + 0x52) = (uint8_t)(v_stack_m44);
        *(uint64_t *)(arg2 + 0x8) = result;
    }
    if (v_stack_m2C == local_r10) goto loc_00545140;
    *(uint8_t *)(arg2 + 0x54) = (uint8_t)(v_stack_m2C);
    *(uint64_t *)(arg2 + 0x8) = result;
loc_00545115:
    result = (*(uint64_t *)(arg2)) | (1);
loc_00545119:
    *(uint64_t *)(arg2) = result;
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00545135:
    goto loc_00545159;
loc_00545140:
    if (((uint32_t)((uint32_t)(0xC0000001ULL))) != 0xC00000BBULL) goto loc_00545155;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m8 + 0x18))) | (4);
    goto loc_00545119;
loc_00545155:
    if (!sign_flag) goto loc_00545115;
loc_00545159:
    result = (result) | (2);
    goto loc_00545119;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `32` | `W` |
| `Arg2` | `+ 0x14` | `64` | `W` |
| `Arg2` | `+ 0x1C` | `64` | `W` |
| `Arg2` | `+ 0x24` | `64` | `W` |
| `Arg2` | `+ 0x2C` | `64` | `W` |
| `Arg2` | `+ 0x34` | `64` | `W` |
| `Arg2` | `+ 0x3C` | `8` | `W` |
| `Arg2` | `+ 0x3D` | `8` | `W` |
| `Arg2` | `+ 0x3E` | `8` | `W` |
| `Arg2` | `+ 0x3F` | `8` | `W` |
| `Arg2` | `+ 0x40` | `8` | `W` |
| `Arg2` | `+ 0x42` | `8` | `W` |
| `Arg2` | `+ 0x43` | `8` | `W` |
| `Arg2` | `+ 0x44` | `8` | `W` |
| `Arg2` | `+ 0x45` | `8` | `W` |
| `Arg2` | `+ 0x46` | `8` | `W` |
| `Arg2` | `+ 0x47` | `32` | `W` |
| `Arg2` | `+ 0x4B` | `32` | `W` |
| `Arg2` | `+ 0x4F` | `8` | `W` |
| `Arg2` | `+ 0x50` | `8` | `W` |
| `Arg2` | `+ 0x51` | `8` | `W` |
| `Arg2` | `+ 0x52` | `8` | `W` |
| `Arg2` | `+ 0x53` | `8` | `W` |
| `Arg2` | `+ 0x54` | `8` | `W` |
| `Arg2` | `+ 0x55` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00544DC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
