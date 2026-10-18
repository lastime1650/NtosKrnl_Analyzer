# RtlpMuiRegFreeRegistryInfo

- RVA: `0x0083DE14`–`0x0083E067` (길이 `595` bytes)
- VA: `0x000000014083DE14`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F978`
- 디코드: `191`개 명령, `595/595` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **12**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0083DE62` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DE85` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DEA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DECB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DF08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DF3F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DF76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DFAC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083DFE4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083E00B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0083E02E` → [RtlpMuiRegFreeRegistryInfo](RtlpMuiRegFreeRegistryInfo_function_0083DE14.md) (function, `0x0083DE14`)
- `0x0083E03E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [RtlpMuiRegCreateKernelRegistryInfo](../../text/6A/RtlpMuiRegCreateKernelRegistryInfo_function_006A908C.md) at `0x006A9220`
- [RtlpMuiRegFreeRegistryInfo](RtlpMuiRegFreeRegistryInfo_function_0083DE14.md) at `0x0083E02E`
- [RtlpMuiRegLoadRegistryInfo](RtlpMuiRegLoadRegistryInfo_function_0083EDC4.md) at `0x0083EE0A`
- [RtlpMuiRegLoadInstalled](RtlpMuiRegLoadInstalled_function_0083FB1C.md) at `0x0083FB97`
- [RtlpMuiRegLoadInstalled](RtlpMuiRegLoadInstalled_function_0083FB1C.md) at `0x0083FC26`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x0083DE62` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DE85` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DEA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DECB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DF08` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DF3F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DF76` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DFAC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083DFE4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083E00B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0083E03E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0083DE14  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0083DE19  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0083DE1E  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0083DE23  41 56                           push r14
0083DE25  48 83 EC 20                     sub rsp, 0x20
0083DE29  33 FF                           xor edi, edi
0083DE2B  48 8B D9                        mov rbx, rcx
0083DE2E  48 85 C9                        test rcx, rcx
0083DE31  0F 84 12 02 00 00               je 0x14083e049
0083DE37  85 D2                           test edx, edx
0083DE39  0F 84 0A 02 00 00               je 0x14083e049
0083DE3F  0F BA E2 0A                     bt edx, 0xa
0083DE43  BE FF 0F 00 00                  mov esi, 0xfff
0083DE48  0F 43 F2                        cmovae esi, edx
0083DE4B  40 F6 C6 01                     test sil, 1
0083DE4F  74 1D                           je 0x14083de6e
0083DE51  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
0083DE55  48 85 C9                        test rcx, rcx
0083DE58  74 11                           je 0x14083de6b
0083DE5A  8B 03                           mov eax, dword ptr [rbx]
0083DE5C  A8 01                           test al, 1
0083DE5E  74 07                           je 0x14083de67
0083DE60  33 D2                           xor edx, edx
0083DE62  E8 09 4A 34 00                  call 0x140b82870
0083DE67  48 89 7B 18                     mov qword ptr [rbx + 0x18], rdi
0083DE6B  83 23 FE                        and dword ptr [rbx], 0xfffffffe
0083DE6E  40 F6 C6 02                     test sil, 2
0083DE72  74 1D                           je 0x14083de91
0083DE74  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
0083DE78  48 85 C9                        test rcx, rcx
0083DE7B  74 11                           je 0x14083de8e
0083DE7D  8B 03                           mov eax, dword ptr [rbx]
0083DE7F  A8 02                           test al, 2
0083DE81  74 07                           je 0x14083de8a
0083DE83  33 D2                           xor edx, edx
0083DE85  E8 E6 49 34 00                  call 0x140b82870
0083DE8A  48 89 7B 20                     mov qword ptr [rbx + 0x20], rdi
0083DE8E  83 23 FD                        and dword ptr [rbx], 0xfffffffd
0083DE91  40 F6 C6 04                     test sil, 4
0083DE95  74 1D                           je 0x14083deb4
0083DE97  48 8B 4B 28                     mov rcx, qword ptr [rbx + 0x28]
0083DE9B  48 85 C9                        test rcx, rcx
0083DE9E  74 11                           je 0x14083deb1
0083DEA0  8B 03                           mov eax, dword ptr [rbx]
0083DEA2  A8 04                           test al, 4
0083DEA4  74 07                           je 0x14083dead
0083DEA6  33 D2                           xor edx, edx
0083DEA8  E8 C3 49 34 00                  call 0x140b82870
0083DEAD  48 89 7B 28                     mov qword ptr [rbx + 0x28], rdi
0083DEB1  83 23 FB                        and dword ptr [rbx], 0xfffffffb
0083DEB4  40 F6 C6 08                     test sil, 8
0083DEB8  74 1D                           je 0x14083ded7
0083DEBA  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0083DEBE  48 85 C9                        test rcx, rcx
0083DEC1  74 11                           je 0x14083ded4
0083DEC3  8B 03                           mov eax, dword ptr [rbx]
0083DEC5  A8 08                           test al, 8
0083DEC7  74 07                           je 0x14083ded0
0083DEC9  33 D2                           xor edx, edx
0083DECB  E8 A0 49 34 00                  call 0x140b82870
0083DED0  48 89 7B 30                     mov qword ptr [rbx + 0x30], rdi
0083DED4  83 23 F7                        and dword ptr [rbx], 0xfffffff7
0083DED7  41 BE BF FF FF FF               mov r14d, 0xffffffbf
0083DEDD  40 F6 C6 10                     test sil, 0x10
0083DEE1  74 31                           je 0x14083df14
0083DEE3  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
0083DEE7  48 85 C9                        test rcx, rcx
0083DEEA  74 25                           je 0x14083df11
0083DEEC  8B 03                           mov eax, dword ptr [rbx]
0083DEEE  A8 10                           test al, 0x10
0083DEF0  74 1B                           je 0x14083df0d
0083DEF2  44 21 71 28                     and dword ptr [rcx + 0x28], r14d
0083DEF6  48 8B 4B 38                     mov rcx, qword ptr [rbx + 0x38]
0083DEFA  48 85 C9                        test rcx, rcx
0083DEFD  74 0E                           je 0x14083df0d
0083DEFF  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0083DF02  A8 40                           test al, 0x40
0083DF04  75 07                           jne 0x14083df0d
0083DF06  33 D2                           xor edx, edx
0083DF08  E8 63 49 34 00                  call 0x140b82870
0083DF0D  48 89 7B 38                     mov qword ptr [rbx + 0x38], rdi
0083DF11  83 23 EF                        and dword ptr [rbx], 0xffffffef
0083DF14  40 F6 C6 20                     test sil, 0x20
0083DF18  74 31                           je 0x14083df4b
0083DF1A  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
0083DF1E  48 85 C9                        test rcx, rcx
0083DF21  74 25                           je 0x14083df48
0083DF23  8B 03                           mov eax, dword ptr [rbx]
0083DF25  A8 20                           test al, 0x20
0083DF27  74 1B                           je 0x14083df44
0083DF29  44 21 71 28                     and dword ptr [rcx + 0x28], r14d
0083DF2D  48 8B 4B 40                     mov rcx, qword ptr [rbx + 0x40]
0083DF31  48 85 C9                        test rcx, rcx
0083DF34  74 0E                           je 0x14083df44
0083DF36  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0083DF39  A8 40                           test al, 0x40
0083DF3B  75 07                           jne 0x14083df44
0083DF3D  33 D2                           xor edx, edx
0083DF3F  E8 2C 49 34 00                  call 0x140b82870
0083DF44  48 89 7B 40                     mov qword ptr [rbx + 0x40], rdi
0083DF48  83 23 DF                        and dword ptr [rbx], 0xffffffdf
0083DF4B  40 F6 C6 40                     test sil, 0x40
0083DF4F  74 31                           je 0x14083df82
0083DF51  48 8B 4B 58                     mov rcx, qword ptr [rbx + 0x58]
0083DF55  48 85 C9                        test rcx, rcx
0083DF58  74 25                           je 0x14083df7f
0083DF5A  8B 03                           mov eax, dword ptr [rbx]
0083DF5C  A8 40                           test al, 0x40
0083DF5E  74 1B                           je 0x14083df7b
0083DF60  44 21 71 28                     and dword ptr [rcx + 0x28], r14d
0083DF64  48 8B 4B 58                     mov rcx, qword ptr [rbx + 0x58]
0083DF68  48 85 C9                        test rcx, rcx
0083DF6B  74 0E                           je 0x14083df7b
0083DF6D  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0083DF70  A8 40                           test al, 0x40
0083DF72  75 07                           jne 0x14083df7b
0083DF74  33 D2                           xor edx, edx
0083DF76  E8 F5 48 34 00                  call 0x140b82870
0083DF7B  48 89 7B 58                     mov qword ptr [rbx + 0x58], rdi
0083DF7F  44 21 33                        and dword ptr [rbx], r14d
0083DF82  40 84 F6                        test sil, sil
0083DF85  79 32                           jns 0x14083dfb9
0083DF87  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0083DF8B  48 85 C9                        test rcx, rcx
0083DF8E  74 25                           je 0x14083dfb5
0083DF90  8B 03                           mov eax, dword ptr [rbx]
0083DF92  84 C0                           test al, al
0083DF94  79 1B                           jns 0x14083dfb1
0083DF96  44 21 71 28                     and dword ptr [rcx + 0x28], r14d
0083DF9A  48 8B 4B 50                     mov rcx, qword ptr [rbx + 0x50]
0083DF9E  48 85 C9                        test rcx, rcx
0083DFA1  74 0E                           je 0x14083dfb1
0083DFA3  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0083DFA6  A8 40                           test al, 0x40
0083DFA8  75 07                           jne 0x14083dfb1
0083DFAA  33 D2                           xor edx, edx
0083DFAC  E8 BF 48 34 00                  call 0x140b82870
0083DFB1  48 89 7B 50                     mov qword ptr [rbx + 0x50], rdi
0083DFB5  0F BA 33 07                     btr dword ptr [rbx], 7
0083DFB9  0F BA E6 09                     bt esi, 9
0083DFBD  73 32                           jae 0x14083dff1
0083DFBF  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
0083DFC3  48 85 C9                        test rcx, rcx
0083DFC6  74 25                           je 0x14083dfed
0083DFC8  0F BA 23 09                     bt dword ptr [rbx], 9
0083DFCC  73 1B                           jae 0x14083dfe9
0083DFCE  44 21 71 28                     and dword ptr [rcx + 0x28], r14d
0083DFD2  48 8B 4B 60                     mov rcx, qword ptr [rbx + 0x60]
0083DFD6  48 85 C9                        test rcx, rcx
0083DFD9  74 0E                           je 0x14083dfe9
0083DFDB  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0083DFDE  A8 40                           test al, 0x40
0083DFE0  75 07                           jne 0x14083dfe9
0083DFE2  33 D2                           xor edx, edx
0083DFE4  E8 87 48 34 00                  call 0x140b82870
0083DFE9  48 89 7B 60                     mov qword ptr [rbx + 0x60], rdi
0083DFED  0F BA 33 09                     btr dword ptr [rbx], 9
0083DFF1  0F BA E6 0B                     bt esi, 0xb
0083DFF5  73 24                           jae 0x14083e01b
0083DFF7  48 8B 8B 88 00 00 00            mov rcx, qword ptr [rbx + 0x88]
0083DFFE  48 85 C9                        test rcx, rcx
0083E001  74 14                           je 0x14083e017
0083E003  0F BA 23 0B                     bt dword ptr [rbx], 0xb
0083E007  73 07                           jae 0x14083e010
0083E009  33 D2                           xor edx, edx
0083E00B  E8 60 48 34 00                  call 0x140b82870
0083E010  48 89 BB 88 00 00 00            mov qword ptr [rbx + 0x88], rdi
0083E017  0F BA 33 0B                     btr dword ptr [rbx], 0xb
0083E01B  F7 C6 FF 0F 00 00               test esi, 0xfff
0083E021  74 2B                           je 0x14083e04e
0083E023  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
0083E027  48 85 C9                        test rcx, rcx
0083E02A  74 22                           je 0x14083e04e
0083E02C  8B D6                           mov edx, esi
0083E02E  E8 E1 FD FF FF                  call 0x14083de14
0083E033  48 8B 4B 68                     mov rcx, qword ptr [rbx + 0x68]
0083E037  48 85 C9                        test rcx, rcx
0083E03A  74 07                           je 0x14083e043
0083E03C  33 D2                           xor edx, edx
0083E03E  E8 2D 48 34 00                  call 0x140b82870
0083E043  48 89 7B 68                     mov qword ptr [rbx + 0x68], rdi
0083E047  EB 05                           jmp 0x14083e04e
0083E049  BF 0D 00 00 C0                  mov edi, 0xc000000d
0083E04E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0083E053  8B C7                           mov eax, edi
0083E055  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0083E05A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0083E05F  48 83 C4 20                     add rsp, 0x20
0083E063  41 5E                           pop r14
0083E065  C3                              ret
0083E066  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpMuiRegFreeRegistryInfo(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    if (a1 == 0) goto loc_0083E049;
    if (a2 == 0) goto loc_0083E049;
    v_rsi = (unsigned int)(0xFFFULL);
    if (condition_is_above_or_equal) { v_rsi = a2; }
    if ((((unsigned __int8)(v_rsi)) & (1)) == 0) goto loc_0083DE6E;
    if (*(unsigned __int64 *)(a1 + 24) == 0) goto loc_0083DE6B;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (1)) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 24) = 0;
loc_0083DE6B:
loc_0083DE6E:
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_0083DE91;
    if (*(unsigned __int64 *)(a1 + 32) == 0) goto loc_0083DE8E;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (2)) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 32) = 0;
loc_0083DE8E:
loc_0083DE91:
    if ((((unsigned __int8)(v_rsi)) & (4)) == 0) goto loc_0083DEB4;
    if (*(unsigned __int64 *)(a1 + 40) == 0) goto loc_0083DEB1;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (4)) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 40) = 0;
loc_0083DEB1:
loc_0083DEB4:
    if ((((unsigned __int8)(v_rsi)) & (8)) == 0) goto loc_0083DED7;
    if (*(unsigned __int64 *)(a1 + 48) == 0) goto loc_0083DED4;
    result = (unsigned int)(*(unsigned int *)(a1));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (8)) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 48), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 48) = 0;
loc_0083DED4:
loc_0083DED7:
    if ((((unsigned __int8)(v_rsi)) & (16)) == 0) goto loc_0083DF14;
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_0083DF11;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (16)) == 0) goto loc_0083DF0D;
    if (*(unsigned __int64 *)(a1 + 56) == 0) goto loc_0083DF0D;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 40)))) & (64)) == 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 56), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 56) = 0;
loc_0083DF11:
loc_0083DF14:
    if ((((unsigned __int8)(v_rsi)) & (32)) == 0) goto loc_0083DF4B;
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_0083DF48;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (32)) == 0) goto loc_0083DF44;
    if (*(unsigned __int64 *)(a1 + 64) == 0) goto loc_0083DF44;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)))) & (64)) == 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 64), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 64) = 0;
loc_0083DF48:
loc_0083DF4B:
    if ((((unsigned __int8)(v_rsi)) & (64)) == 0) goto loc_0083DF82;
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_0083DF7F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1)))) & (64)) == 0) goto loc_0083DF7B;
    if (*(unsigned __int64 *)(a1 + 88) == 0) goto loc_0083DF7B;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 88) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 88) + 40)))) & (64)) == 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 88), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 88) = 0;
loc_0083DF7F:
loc_0083DF82:
    if (!sign_flag) goto loc_0083DFB9;
    if (*(unsigned __int64 *)(a1 + 80) == 0) goto loc_0083DFB5;
    if (!sign_flag) goto loc_0083DFB1;
    if (*(unsigned __int64 *)(a1 + 80) == 0) goto loc_0083DFB1;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 80) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 80) + 40)))) & (64)) == 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 80), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 80) = 0;
loc_0083DFB5:
loc_0083DFB9:
    if (condition_is_above_or_equal) goto loc_0083DFF1;
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_0083DFED;
    if (condition_is_above_or_equal) goto loc_0083DFE9;
    if (*(unsigned __int64 *)(a1 + 96) == 0) goto loc_0083DFE9;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 96) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 96) + 40)))) & (64)) == 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 96), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 96) = 0;
loc_0083DFED:
loc_0083DFF1:
    if (condition_is_above_or_equal) goto loc_0083E01B;
    if (*(unsigned __int64 *)(a1 + 136) == 0) goto loc_0083E017;
    if (!(condition_is_above_or_equal)) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 136), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 136) = 0;
loc_0083E017:
loc_0083E01B:
    if ((((unsigned int)(v_rsi)) & (0xFFFULL)) == 0) goto loc_0083E04E;
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_0083E04E;
    result = RtlpMuiRegFreeRegistryInfo(*(unsigned __int64 *)(a1 + 104), (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    if (*(unsigned __int64 *)(a1 + 104) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 104), a2, a3, a4);
    }
    *(unsigned __int64 *)(a1 + 104) = 0;
    goto loc_0083E04E;
loc_0083E049:
loc_0083E04E:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t RtlpMuiRegFreeRegistryInfo(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    if (Arg1 == NULL) goto loc_0083E049;
    if (Arg2 == 0) goto loc_0083E049;
    local_rsi = (uint32_t)(0xFFFULL);
    if (condition_is_above_or_equal) { local_rsi = Arg2; }
    if ((((uint8_t)(local_rsi)) & (1)) == 0) goto loc_0083DE6E;
    if (*(uint64_t *)(arg1 + 0x18) == 0) goto loc_0083DE6B;
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (1)) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x18), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x18) = 0;
loc_0083DE6B:
loc_0083DE6E:
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_0083DE91;
    if (*(uint64_t *)(arg1 + 0x20) == 0) goto loc_0083DE8E;
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (2)) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x20), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x20) = 0;
loc_0083DE8E:
loc_0083DE91:
    if ((((uint8_t)(local_rsi)) & (4)) == 0) goto loc_0083DEB4;
    if (*(uint64_t *)(arg1 + 0x28) == 0) goto loc_0083DEB1;
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (4)) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x28), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x28) = 0;
loc_0083DEB1:
loc_0083DEB4:
    if ((((uint8_t)(local_rsi)) & (8)) == 0) goto loc_0083DED7;
    if (*(uint64_t *)(arg1 + 0x30) == 0) goto loc_0083DED4;
    result = (uint32_t)(*(uint32_t *)(arg1));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (8)) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x30), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x30) = 0;
loc_0083DED4:
loc_0083DED7:
    if ((((uint8_t)(local_rsi)) & (16)) == 0) goto loc_0083DF14;
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_0083DF11;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (16)) == 0) goto loc_0083DF0D;
    if (*(uint64_t *)(arg1 + 0x38) == 0) goto loc_0083DF0D;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x28)))) & (64)) == 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x38), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x38) = 0;
loc_0083DF11:
loc_0083DF14:
    if ((((uint8_t)(local_rsi)) & (32)) == 0) goto loc_0083DF4B;
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_0083DF48;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (32)) == 0) goto loc_0083DF44;
    if (*(uint64_t *)(arg1 + 0x40) == 0) goto loc_0083DF44;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)))) & (64)) == 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x40), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x40) = 0;
loc_0083DF48:
loc_0083DF4B:
    if ((((uint8_t)(local_rsi)) & (64)) == 0) goto loc_0083DF82;
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_0083DF7F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1)))) & (64)) == 0) goto loc_0083DF7B;
    if (*(uint64_t *)(arg1 + 0x58) == 0) goto loc_0083DF7B;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x58) + 0x28)))) & (64)) == 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x58), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x58) = 0;
loc_0083DF7F:
loc_0083DF82:
    if (!sign_flag) goto loc_0083DFB9;
    if (*(uint64_t *)(arg1 + 0x50) == 0) goto loc_0083DFB5;
    if (!sign_flag) goto loc_0083DFB1;
    if (*(uint64_t *)(arg1 + 0x50) == 0) goto loc_0083DFB1;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x50) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x50) + 0x28)))) & (64)) == 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x50), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x50) = 0;
loc_0083DFB5:
loc_0083DFB9:
    if (condition_is_above_or_equal) goto loc_0083DFF1;
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_0083DFED;
    if (condition_is_above_or_equal) goto loc_0083DFE9;
    if (*(uint64_t *)(arg1 + 0x60) == 0) goto loc_0083DFE9;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x60) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x60) + 0x28)))) & (64)) == 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x60), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x60) = 0;
loc_0083DFED:
loc_0083DFF1:
    if (condition_is_above_or_equal) goto loc_0083E01B;
    if (*(uint64_t *)(arg1 + 0x88) == 0) goto loc_0083E017;
    if (!(condition_is_above_or_equal)) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x88), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x88) = 0;
loc_0083E017:
loc_0083E01B:
    if ((((uint32_t)(local_rsi)) & (0xFFFULL)) == 0) goto loc_0083E04E;
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_0083E04E;
    result = RtlpMuiRegFreeRegistryInfo(*(uint64_t *)(arg1 + 0x68), (uint32_t)((uint32_t)(local_rsi)), a3, a4);
    if (*(uint64_t *)(arg1 + 0x68) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x68), Arg2, a3, a4);
    }
    *(uint64_t *)(arg1 + 0x68) = 0;
    goto loc_0083E04E;
loc_0083E049:
loc_0083E04E:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `W` |
| `Arg1` | `+ 0x50` | `64` | `R` |
| `Arg1` | `+ 0x50` | `64` | `W` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `W` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `W` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `W` |
| `Arg1` | `+ 0x88` | `64` | `R` |
| `Arg1` | `+ 0x88` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0083DE14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
