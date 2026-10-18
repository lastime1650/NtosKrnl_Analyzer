# HalpPutAcpiHacksInRegistry

- RVA: `0x0070BC04`–`0x0070BE1F` (길이 `539` bytes)
- VA: `0x000000014070BC04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4870`
- 디코드: `121`개 명령, `539/539` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x0070BCB3` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x0070BCE9` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x0070BD3F` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x0070BD4A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0070BD81` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0070BDAB` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0070BDDD` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0070BE06` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (function, `0x006ADCD0`)
- `0x0070BE0F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [HaliInitPowerManagement](HaliInitPowerManagement_function_0070BAE0.md) at `0x0070BB26`

### Static image references
- `0x0070BC18` → RVA `0x00F8FE40` (`.data`; read)
- `0x0070BC41` → RVA `0x00024FE0` (`.rdata`; read)
- `0x0070BC4C` → RVA `0x000259E8` (`.rdata`; read)
- `0x0070BC57` → RVA `0x00025A00` (`.rdata`; read)
- `0x0070BC62` → RVA `0x00025A58` (`.rdata`; read)
- `0x0070BC6D` → RVA `0x00025A68` (`.rdata`; read)
- `0x0070BC78` → RVA `0x00025A38` (`.rdata`; read)
- `0x0070BD57` → RVA `0x00FC1AC8` (`.data`; read)
- `0x0070BD86` → RVA `0x00FC1AB0` (`.data`; read)
- `0x0070BDB0` → RVA `0x00FC1AC0` (`.data`; read)
- `0x0070BDC7` → RVA `0x00FC1ACC` (`.data`; read)
- `0x0070BDE2` → RVA `0x00FC1AC4` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **9**
  - `0x0070BCB3` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x0070BCE9` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x0070BD3F` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x0070BD4A` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0070BD81` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0070BDAB` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0070BDDD` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0070BE06` → [ZwSetValueKey](../../text/6A/ZwSetValueKey_function_006ADCD0.md) (`PAGE` → `.text`)
  - `0x0070BE0F` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070BC04  40 55                           push rbp
0070BC06  53                              push rbx
0070BC07  48 8D 6C 24 B1                  lea rbp, [rsp - 0x4f]
0070BC0C  48 81 EC D8 00 00 00            sub rsp, 0xd8
0070BC13  48 83 65 7F 00                  and qword ptr [rbp + 0x7f], 0
0070BC18  48 8D 0D 21 42 88 00            lea rcx, [rip + 0x884221]
0070BC1F  83 65 6F 00                     and dword ptr [rbp + 0x6f], 0
0070BC23  33 C0                           xor eax, eax
0070BC25  21 45 33                        and dword ptr [rbp + 0x33], eax
0070BC28  45 33 C9                        xor r9d, r9d
0070BC2B  48 83 65 77 00                  and qword ptr [rbp + 0x77], 0
0070BC30  45 33 C0                        xor r8d, r8d
0070BC33  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0070BC39  33 D2                           xor edx, edx
0070BC3B  89 45 1B                        mov dword ptr [rbp + 0x1b], eax
0070BC3E  21 45 1B                        and dword ptr [rbp + 0x1b], eax
0070BC41  48 8D 05 98 93 91 FF            lea rax, [rip - 0x6e6c68]
0070BC48  48 89 45 BF                     mov qword ptr [rbp - 0x41], rax
0070BC4C  48 8D 05 95 9D 91 FF            lea rax, [rip - 0x6e626b]
0070BC53  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
0070BC57  48 8D 05 A2 9D 91 FF            lea rax, [rip - 0x6e625e]
0070BC5E  48 89 45 DF                     mov qword ptr [rbp - 0x21], rax
0070BC62  48 8D 05 EF 9D 91 FF            lea rax, [rip - 0x6e6211]
0070BC69  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
0070BC6D  48 8D 05 F4 9D 91 FF            lea rax, [rip - 0x6e620c]
0070BC74  48 89 45 FF                     mov qword ptr [rbp - 1], rax
0070BC78  48 8D 05 B9 9D 91 FF            lea rax, [rip - 0x6e6247]
0070BC7F  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
0070BC83  48 C7 45 B7 6C 00 6E 00         mov qword ptr [rbp - 0x49], 0x6e006c
0070BC8B  48 C7 45 C7 16 00 18 00         mov qword ptr [rbp - 0x39], 0x180016
0070BC93  48 C7 45 D7 0A 00 0C 00         mov qword ptr [rbp - 0x29], 0xc000a
0070BC9B  48 C7 45 E7 0A 00 0C 00         mov qword ptr [rbp - 0x19], 0xc000a
0070BCA3  48 C7 45 F7 12 00 14 00         mov qword ptr [rbp - 9], 0x140012
0070BCAB  48 C7 45 07 18 00 1A 00         mov qword ptr [rbp + 7], 0x1a0018
0070BCB3  E8 F8 29 B0 FF                  call 0x14020e6b0
0070BCB8  48 83 65 1F 00                  and qword ptr [rbp + 0x1f], 0
0070BCBD  48 8D 45 B7                     lea rax, [rbp - 0x49]
0070BCC1  0F 57 C0                        xorps xmm0, xmm0
0070BCC4  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0070BCC8  BB 30 00 00 00                  mov ebx, 0x30
0070BCCD  C7 45 2F 40 00 00 00            mov dword ptr [rbp + 0x2f], 0x40
0070BCD4  4C 8D 45 17                     lea r8, [rbp + 0x17]
0070BCD8  89 5D 17                        mov dword ptr [rbp + 0x17], ebx
0070BCDB  BA 19 00 02 00                  mov edx, 0x20019
0070BCE0  48 8D 4D 7F                     lea rcx, [rbp + 0x7f]
0070BCE4  F3 0F 7F 45 37                  movdqu xmmword ptr [rbp + 0x37], xmm0
0070BCE9  E8 22 16 FA FF                  call 0x1406ad310
0070BCEE  85 C0                           test eax, eax
0070BCF0  0F 88 1E 01 00 00               js 0x14070be14
0070BCF6  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0070BCFA  4C 8D 45 17                     lea r8, [rbp + 0x17]
0070BCFE  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
0070BD02  48 8D 4D 77                     lea rcx, [rbp + 0x77]
0070BD06  48 8D 45 C7                     lea rax, [rbp - 0x39]
0070BD0A  89 5D 17                        mov dword ptr [rbp + 0x17], ebx
0070BD0D  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0070BD11  0F 57 C0                        xorps xmm0, xmm0
0070BD14  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0070BD18  C7 45 2F 40 00 00 00            mov dword ptr [rbp + 0x2f], 0x40
0070BD1F  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0070BD24  45 33 C9                        xor r9d, r9d
0070BD27  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0070BD2F  BA 19 00 02 00                  mov edx, 0x20019
0070BD34  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
0070BD3A  F3 0F 7F 45 37                  movdqu xmmword ptr [rbp + 0x37], xmm0
0070BD3F  E8 2C 17 FA FF                  call 0x1406ad470
0070BD44  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0070BD48  8B D8                           mov ebx, eax
0070BD4A  E8 61 15 FA FF                  call 0x1406ad2b0
0070BD4F  85 DB                           test ebx, ebx
0070BD51  0F 88 BD 00 00 00               js 0x14070be14
0070BD57  0F B6 05 6A 5D 8B 00            movzx eax, byte ptr [rip + 0x8b5d6a]
0070BD5E  48 8D 55 D7                     lea rdx, [rbp - 0x29]
0070BD62  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0070BD66  BB 04 00 00 00                  mov ebx, 4
0070BD6B  89 45 67                        mov dword ptr [rbp + 0x67], eax
0070BD6E  44 8B CB                        mov r9d, ebx
0070BD71  48 8D 45 67                     lea rax, [rbp + 0x67]
0070BD75  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0070BD79  45 33 C0                        xor r8d, r8d
0070BD7C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0070BD81  E8 4A 1F FA FF                  call 0x1406adcd0
0070BD86  0F B6 05 23 5D 8B 00            movzx eax, byte ptr [rip + 0x8b5d23]
0070BD8D  48 8D 55 E7                     lea rdx, [rbp - 0x19]
0070BD91  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0070BD95  44 8B CB                        mov r9d, ebx
0070BD98  89 45 67                        mov dword ptr [rbp + 0x67], eax
0070BD9B  45 33 C0                        xor r8d, r8d
0070BD9E  48 8D 45 67                     lea rax, [rbp + 0x67]
0070BDA2  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0070BDA6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0070BDAB  E8 20 1F FA FF                  call 0x1406adcd0
0070BDB0  8B 05 0A 5D 8B 00               mov eax, dword ptr [rip + 0x8b5d0a]
0070BDB6  48 8D 55 F7                     lea rdx, [rbp - 9]
0070BDBA  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0070BDBE  44 8B CB                        mov r9d, ebx
0070BDC1  C1 E0 10                        shl eax, 0x10
0070BDC4  45 33 C0                        xor r8d, r8d
0070BDC7  0B 05 FF 5C 8B 00               or eax, dword ptr [rip + 0x8b5cff]
0070BDCD  89 45 67                        mov dword ptr [rbp + 0x67], eax
0070BDD0  48 8D 45 67                     lea rax, [rbp + 0x67]
0070BDD4  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0070BDD8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0070BDDD  E8 EE 1E FA FF                  call 0x1406adcd0
0070BDE2  8B 05 DC 5C 8B 00               mov eax, dword ptr [rip + 0x8b5cdc]
0070BDE8  48 8D 55 07                     lea rdx, [rbp + 7]
0070BDEC  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0070BDF0  44 8B CB                        mov r9d, ebx
0070BDF3  89 45 67                        mov dword ptr [rbp + 0x67], eax
0070BDF6  45 33 C0                        xor r8d, r8d
0070BDF9  48 8D 45 67                     lea rax, [rbp + 0x67]
0070BDFD  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
0070BE01  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0070BE06  E8 C5 1E FA FF                  call 0x1406adcd0
0070BE0B  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
0070BE0F  E8 9C 14 FA FF                  call 0x1406ad2b0
0070BE14  48 81 C4 D8 00 00 00            add rsp, 0xd8
0070BE1B  5B                              pop rbx
0070BE1C  5D                              pop rbp
0070BE1D  C3                              ret
0070BE1E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpPutAcpiHacksInRegistry(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (216);
    result = 0;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    v_stack_m44 = 0;
    v_stack_mA0 = v_rip - 7236712;
    v_stack_m90 = v_rip - 7234155;
    v_stack_m80 = v_rip - 7234142;
    v_stack_m70 = v_rip - 7234065;
    v_stack_m60 = v_rip - 7234060;
    v_stack_m50 = v_rip - 7234119;
    v_stack_mA8 = 0x6E006CULL;
    v_stack_m98 = 0x180016ULL;
    v_stack_m88 = 0xC000AULL;
    v_stack_m78 = 0xC000AULL;
    v_stack_m68 = 0x140012ULL;
    v_stack_m58 = 0x1A0018ULL;
    result = KeWaitForSingleObject(v_rip + 8929825, a2, a3, a4);
    v_stack_m38 = v_stack_mA8;
    v_stack_m30 = 64;
    v_stack_m48 = 48;
    v_stack_m28 = v_xmm0;
    result = ZwOpenKey(v_stack_p20, (unsigned int)(0x20019ULL), v_stack_m48, a4);
    if (sign_flag) goto loc_0070BE14;
    v_stack_m40 = v_stack_p20;
    v_stack_m48 = 48;
    v_stack_m38 = v_stack_m98;
    v_stack_m30 = 64;
    v_stack_mB8 = v_stack_p10;
    a4 = 0;
    v_stack_mC0 = 1;
    v_stack_m28 = v_xmm0;
    result = ZwCreateKey(v_stack_p18, (unsigned int)(0x20019ULL), v_stack_m48, a4);
    result = ZwClose(v_stack_p20, (unsigned int)(0x20019ULL), v_stack_m48, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = *(unsigned __int8 *)(v_rip + 9133418);
        a2 = v_stack_m88;
        a1 = v_stack_p18;
        v_rbx = 4;
        v_stack_p8 = (unsigned int)(result);
        a4 = (unsigned int)(v_rbx);
        result = v_stack_p8;
        v_stack_mC0 = (unsigned int)(v_rbx);
        a3 = 0;
        v_stack_mC8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        result = *(unsigned __int8 *)(v_rip + 9133347);
        a2 = v_stack_m78;
        a1 = v_stack_p18;
        a4 = (unsigned int)(v_rbx);
        v_stack_p8 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_p8;
        v_stack_mC0 = (unsigned int)(v_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        result = *(unsigned int *)(v_rip + 9133322);
        a2 = v_stack_m68;
        a1 = v_stack_p18;
        a4 = (unsigned int)(v_rbx);
        result = (unsigned int)((result) << (16));
        a3 = 0;
        result = (unsigned int)((result) | (*(unsigned int *)(v_rip + 9133311)));
        v_stack_p8 = (unsigned int)(result);
        result = v_stack_p8;
        v_stack_mC0 = (unsigned int)(v_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        result = *(unsigned int *)(v_rip + 9133276);
        a2 = v_stack_m58;
        a1 = v_stack_p18;
        a4 = (unsigned int)(v_rbx);
        v_stack_p8 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_p8;
        v_stack_mC0 = (unsigned int)(v_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(a1, a2, a3, a4);
        a1 = v_stack_p18;
        result = ZwClose(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (216);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpPutAcpiHacksInRegistry(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (216);
    result = 0;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m44 = 0;
    v_stack_mA0 = v_rip - 7236712;
    v_stack_m90 = v_rip - 7234155;
    v_stack_m80 = v_rip - 7234142;
    v_stack_m70 = v_rip - 7234065;
    v_stack_m60 = v_rip - 7234060;
    v_stack_m50 = v_rip - 7234119;
    v_stack_mA8 = 0x6E006CULL;
    v_stack_m98 = 0x180016ULL;
    v_stack_m88 = 0xC000AULL;
    v_stack_m78 = 0xC000AULL;
    v_stack_m68 = 0x140012ULL;
    v_stack_m58 = 0x1A0018ULL;
    result = KeWaitForSingleObject(v_rip + 8929825, Arg2, Arg3, Arg4);
    v_stack_m38 = v_stack_mA8;
    v_stack_m30 = 64;
    v_stack_m48 = 48;
    v_stack_m28 = v_xmm0;
    result = ZwOpenKey(v_stack_p20, (uint32_t)(0x20019ULL), v_stack_m48, Arg4);
    if (sign_flag) goto loc_0070BE14;
    v_stack_m40 = v_stack_p20;
    v_stack_m48 = 48;
    v_stack_m38 = v_stack_m98;
    v_stack_m30 = 64;
    v_stack_mB8 = v_stack_p10;
    Arg4 = 0;
    v_stack_mC0 = 1;
    v_stack_m28 = v_xmm0;
    result = ZwCreateKey(v_stack_p18, (uint32_t)(0x20019ULL), v_stack_m48, Arg4);
    result = ZwClose(v_stack_p20, (uint32_t)(0x20019ULL), v_stack_m48, Arg4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = *(uint8_t *)(v_rip + 0x8B5D6A);
        Arg2 = v_stack_m88;
        Arg1 = v_stack_p18;
        local_rbx = 4;
        v_stack_p8 = (uint32_t)(result);
        Arg4 = (uint32_t)(local_rbx);
        result = v_stack_p8;
        v_stack_mC0 = (uint32_t)(local_rbx);
        Arg3 = 0;
        v_stack_mC8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        result = *(uint8_t *)(v_rip + 0x8B5D23);
        Arg2 = v_stack_m78;
        Arg1 = v_stack_p18;
        Arg4 = (uint32_t)(local_rbx);
        v_stack_p8 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_p8;
        v_stack_mC0 = (uint32_t)(local_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        result = *(uint32_t *)(v_rip + 0x8B5D0A);
        Arg2 = v_stack_m68;
        Arg1 = v_stack_p18;
        Arg4 = (uint32_t)(local_rbx);
        result = (uint32_t)((result) << (16));
        Arg3 = 0;
        result = (uint32_t)((result) | (*(uint32_t *)(v_rip + 0x8B5CFF)));
        v_stack_p8 = (uint32_t)(result);
        result = v_stack_p8;
        v_stack_mC0 = (uint32_t)(local_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        result = *(uint32_t *)(v_rip + 0x8B5CDC);
        Arg2 = v_stack_m58;
        Arg1 = v_stack_p18;
        Arg4 = (uint32_t)(local_rbx);
        v_stack_p8 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_p8;
        v_stack_mC0 = (uint32_t)(local_rbx);
        v_stack_mC8 = result;
        result = ZwSetValueKey(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_p18;
        result = ZwClose(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (216);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070BC04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070BC04[BB_0070BC04]
  bb_0070BCF6[BB_0070BCF6]
  bb_0070BD57[BB_0070BD57]
  bb_0070BE14[BB_0070BE14]
  bb_0070BE1E[BB_0070BE1E]
  bb_0070BC04 -->|branch| bb_0070BE14
  bb_0070BC04 -->|fallthrough| bb_0070BCF6
  bb_0070BCF6 -->|branch| bb_0070BE14
  bb_0070BCF6 -->|fallthrough| bb_0070BD57
  bb_0070BD57 -->|flow| bb_0070BE14
```
