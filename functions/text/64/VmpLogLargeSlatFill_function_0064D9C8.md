# VmpLogLargeSlatFill

- RVA: `0x0064D9C8`–`0x0064DAD7` (길이 `271` bytes)
- VA: `0x000000014064D9C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A68C4`
- 디코드: `66`개 명령, `271/271` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064DA00` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0064DABC` → [tlgWriteEx_EtwWriteEx](../4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x0064DAC8` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_006EE22C](../6E/Unknown_function_006EE22C.md) at `0x006EE28F`

### Static image references
- `0x0064D9D6` → RVA `0x00E0A740` (`.data`; read)
- `0x0064D9E4` → RVA `0x00F02458` (`.data`; read)
- `0x0064DAAD` → RVA `0x00053853` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064D9C8  40 55                           push rbp
0064D9CA  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0064D9CF  48 81 EC 00 01 00 00            sub rsp, 0x100
0064D9D6  48 8B 05 63 CD 7B 00            mov rax, qword ptr [rip + 0x7bcd63]
0064D9DD  48 33 C4                        xor rax, rsp
0064D9E0  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0064D9E4  4C 8B 15 6D 4A 8B 00            mov r10, qword ptr [rip + 0x8b4a6d]
0064D9EB  4C 8B DA                        mov r11, rdx
0064D9EE  41 83 3A 05                     cmp dword ptr [r10], 5
0064D9F2  0F 86 C9 00 00 00               jbe 0x14064dac1
0064D9F8  BA 01 00 00 00                  mov edx, 1
0064D9FD  49 8B CA                        mov rcx, r10
0064DA00  E8 9B 10 DE FF                  call 0x14042eaa0
0064DA05  84 C0                           test al, al
0064DA07  0F 84 B4 00 00 00               je 0x14064dac1
0064DA0D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0064DA16  BA 04 00 00 00                  mov edx, 4
0064DA1B  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0064DA22  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
0064DA28  8D 4A 04                        lea ecx, [rdx + 4]
0064DA2B  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
0064DA2F  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
0064DA33  83 65 03 00                     and dword ptr [rbp + 3], 0
0064DA37  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0064DA3B  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0064DA3F  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0064DA43  89 45 87                        mov dword ptr [rbp - 0x79], eax
0064DA46  48 8D 45 87                     lea rax, [rbp - 0x79]
0064DA4A  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0064DA4E  48 8D 45 97                     lea rax, [rbp - 0x69]
0064DA52  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0064DA56  48 8D 45 9F                     lea rax, [rbp - 0x61]
0064DA5A  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0064DA5E  48 8D 45 8B                     lea rax, [rbp - 0x75]
0064DA62  48 89 45 07                     mov qword ptr [rbp + 7], rax
0064DA66  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0064DA6A  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0064DA6E  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064DA72  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0064DA76  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
0064DA79  89 45 8F                        mov dword ptr [rbp - 0x71], eax
0064DA7C  48 8D 45 8F                     lea rax, [rbp - 0x71]
0064DA80  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0064DA84  48 8D 45 B7                     lea rax, [rbp - 0x49]
0064DA88  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0064DA8D  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0064DA91  89 55 DF                        mov dword ptr [rbp - 0x21], edx
0064DA94  89 4D EF                        mov dword ptr [rbp - 0x11], ecx
0064DA97  89 4D FF                        mov dword ptr [rbp - 1], ecx
0064DA9A  44 89 4D 8B                     mov dword ptr [rbp - 0x75], r9d
0064DA9E  45 33 C9                        xor r9d, r9d
0064DAA1  89 55 0F                        mov dword ptr [rbp + 0xf], edx
0064DAA4  89 4D 1F                        mov dword ptr [rbp + 0x1f], ecx
0064DAA7  49 8B CA                        mov rcx, r10
0064DAAA  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0064DAAD  48 8D 15 9F 5D A0 FF            lea rdx, [rip - 0x5fa261]
0064DAB4  4C 89 5D 97                     mov qword ptr [rbp - 0x69], r11
0064DAB8  4C 89 45 9F                     mov qword ptr [rbp - 0x61], r8
0064DABC  E8 87 C8 E5 FF                  call 0x1404aa348
0064DAC1  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
0064DAC5  48 33 CC                        xor rcx, rsp
0064DAC8  E8 73 EB 05 00                  call 0x1406ac640
0064DACD  48 81 C4 00 01 00 00            add rsp, 0x100
0064DAD4  5D                              pop rbp
0064DAD5  C3                              ret
0064DAD6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpLogLargeSlatFill(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 8113507)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9128557))) <= 5) goto loc_0064DAC1;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 9128557), 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 4;
        a1 = *(unsigned __int64 *)(result + 184);
        result = *(unsigned int *)(a1 + 464);
        a1 = a2 + 4;
        v_stack_mC8 = (unsigned int)(result);
        result = v_stack_mC8;
        v_stack_m78 = result;
        result = v_stack_mB8;
        v_stack_m68 = result;
        result = v_stack_mB0;
        v_stack_m58 = result;
        result = v_stack_mC4;
        v_stack_m48 = result;
        result = a5;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m38 = result;
        result = a6;
        v_stack_mC0 = (unsigned int)(result);
        result = v_stack_mC0;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mD0 = result;
        v_stack_mD8 = (unsigned int)(a1);
        v_stack_m70 = (unsigned int)(a2);
        v_stack_m60 = (unsigned int)(a1);
        v_stack_m50 = (unsigned int)(a1);
        v_stack_mC4 = a4;
        a4 = 0;
        v_stack_m40 = (unsigned int)(a2);
        v_stack_m30 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9128557);
        v_stack_m20 = (unsigned int)(a2);
        a2 = v_rip - 6267489;
        v_stack_mB8 = a2;
        v_stack_mB0 = a3;
        result = tlgWriteEx_EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (256);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VmpLogLargeSlatFill(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x7BCD63)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B4A6D))) <= 5) goto loc_0064DAC1;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x8B4A6D), 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 4;
        Arg1 = *(uint64_t *)(result + 0xB8);
        result = *(uint32_t *)(Arg1 + 0x1D0);
        Arg1 = Arg2 + 4;
        v_stack_mC8 = (uint32_t)(result);
        result = v_stack_mC8;
        v_stack_m78 = result;
        result = v_stack_mB8;
        v_stack_m68 = result;
        result = v_stack_mB0;
        v_stack_m58 = result;
        result = v_stack_mC4;
        v_stack_m48 = result;
        result = Arg5;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m38 = result;
        result = Arg6;
        v_stack_mC0 = (uint32_t)(result);
        result = v_stack_mC0;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mD0 = result;
        v_stack_mD8 = (uint32_t)(Arg1);
        v_stack_m70 = (uint32_t)(Arg2);
        v_stack_m60 = (uint32_t)(Arg1);
        v_stack_m50 = (uint32_t)(Arg1);
        v_stack_mC4 = Arg4;
        Arg4 = 0;
        v_stack_m40 = (uint32_t)(Arg2);
        v_stack_m30 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x8B4A6D);
        v_stack_m20 = (uint32_t)(Arg2);
        Arg2 = v_rip - 6267489;
        v_stack_mB8 = Arg2;
        v_stack_mB0 = Arg3;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064D9C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064D9C8[BB_0064D9C8]
  bb_0064D9F8[BB_0064D9F8]
  bb_0064DA0D[BB_0064DA0D]
  bb_0064DAC1[BB_0064DAC1]
  bb_0064DAD6[BB_0064DAD6]
  bb_0064D9C8 -->|branch| bb_0064DAC1
  bb_0064D9C8 -->|fallthrough| bb_0064D9F8
  bb_0064D9F8 -->|branch| bb_0064DAC1
  bb_0064D9F8 -->|fallthrough| bb_0064DA0D
  bb_0064DA0D -->|flow| bb_0064DAC1
```
