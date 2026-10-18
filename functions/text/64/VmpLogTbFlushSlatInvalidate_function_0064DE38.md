# VmpLogTbFlushSlatInvalidate

- RVA: `0x0064DE38`–`0x0064DF47` (길이 `271` bytes)
- VA: `0x000000014064DE38`
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
- `0x0064DE70` → [tlgKeywordOn](../42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0064DF2C` → [tlgWriteEx_EtwWriteEx](../4A/tlgWriteEx_EtwWriteEx_function_004AA348.md) (function, `0x004AA348`)
- `0x0064DF38` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [VmpProcessInvalidateList](../42/VmpProcessInvalidateList_function_00428A54.md) at `0x00428BEB`

### Static image references
- `0x0064DE46` → RVA `0x00E0A740` (`.data`; read)
- `0x0064DE54` → RVA `0x00F02458` (`.data`; read)
- `0x0064DF1D` → RVA `0x00053728` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064DE38  40 55                           push rbp
0064DE3A  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
0064DE3F  48 81 EC 00 01 00 00            sub rsp, 0x100
0064DE46  48 8B 05 F3 C8 7B 00            mov rax, qword ptr [rip + 0x7bc8f3]
0064DE4D  48 33 C4                        xor rax, rsp
0064DE50  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0064DE54  4C 8B 15 FD 45 8B 00            mov r10, qword ptr [rip + 0x8b45fd]
0064DE5B  4C 8B DA                        mov r11, rdx
0064DE5E  41 83 3A 05                     cmp dword ptr [r10], 5
0064DE62  0F 86 C9 00 00 00               jbe 0x14064df31
0064DE68  BA 02 00 00 00                  mov edx, 2
0064DE6D  49 8B CA                        mov rcx, r10
0064DE70  E8 2B 0C DE FF                  call 0x14042eaa0
0064DE75  84 C0                           test al, al
0064DE77  0F 84 B4 00 00 00               je 0x14064df31
0064DE7D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0064DE86  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0064DE8D  8B 81 D0 01 00 00               mov eax, dword ptr [rcx + 0x1d0]
0064DE93  8D 4A 02                        lea ecx, [rdx + 2]
0064DE96  83 65 E3 00                     and dword ptr [rbp - 0x1d], 0
0064DE9A  8D 51 04                        lea edx, [rcx + 4]
0064DE9D  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
0064DEA1  83 65 03 00                     and dword ptr [rbp + 3], 0
0064DEA5  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0064DEA9  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0064DEAD  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0064DEB1  89 45 87                        mov dword ptr [rbp - 0x79], eax
0064DEB4  48 8D 45 87                     lea rax, [rbp - 0x79]
0064DEB8  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
0064DEBC  48 8D 45 97                     lea rax, [rbp - 0x69]
0064DEC0  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
0064DEC4  48 8D 45 8B                     lea rax, [rbp - 0x75]
0064DEC8  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0064DECC  48 8D 45 8F                     lea rax, [rbp - 0x71]
0064DED0  48 89 45 07                     mov qword ptr [rbp + 7], rax
0064DED4  48 8B 45 77                     mov rax, qword ptr [rbp + 0x77]
0064DED8  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
0064DEDC  48 8D 45 9F                     lea rax, [rbp - 0x61]
0064DEE0  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0064DEE4  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
0064DEE8  48 89 45 A7                     mov qword ptr [rbp - 0x59], rax
0064DEEC  48 8D 45 A7                     lea rax, [rbp - 0x59]
0064DEF0  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0064DEF4  48 8D 45 B7                     lea rax, [rbp - 0x49]
0064DEF8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0064DEFD  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
0064DF01  89 4D DF                        mov dword ptr [rbp - 0x21], ecx
0064DF04  89 55 EF                        mov dword ptr [rbp - 0x11], edx
0064DF07  89 4D FF                        mov dword ptr [rbp - 1], ecx
0064DF0A  44 89 4D 8F                     mov dword ptr [rbp - 0x71], r9d
0064DF0E  45 33 C9                        xor r9d, r9d
0064DF11  89 4D 0F                        mov dword ptr [rbp + 0xf], ecx
0064DF14  49 8B CA                        mov rcx, r10
0064DF17  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0064DF1A  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
0064DF1D  48 8D 15 04 58 A0 FF            lea rdx, [rip - 0x5fa7fc]
0064DF24  4C 89 5D 97                     mov qword ptr [rbp - 0x69], r11
0064DF28  44 89 45 8B                     mov dword ptr [rbp - 0x75], r8d
0064DF2C  E8 17 C4 E5 FF                  call 0x1404aa348
0064DF31  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
0064DF35  48 33 CC                        xor rcx, rsp
0064DF38  E8 03 E7 05 00                  call 0x1406ac640
0064DF3D  48 81 C4 00 01 00 00            add rsp, 0x100
0064DF44  5D                              pop rbp
0064DF45  C3                              ret
0064DF46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VmpLogTbFlushSlatInvalidate(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6)
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
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC4;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (256);
    result = (*(unsigned __int64 *)(v_rip + 8112371)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 9127421))) <= 5) goto loc_0064DF31;
    result = tlgKeywordOn(*(unsigned __int64 *)(v_rip + 9127421), 2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        result = *(unsigned int *)(a1 + 464);
        a1 = 2 + 2;
        a2 = a1 + 4;
        v_stack_mC8 = (unsigned int)(result);
        result = v_stack_mC8;
        v_stack_m78 = result;
        result = v_stack_mB8;
        v_stack_m68 = result;
        result = v_stack_mC4;
        v_stack_m58 = result;
        result = v_stack_mC0;
        v_stack_m48 = result;
        result = a5;
        v_stack_mB0 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = a6;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mD0 = result;
        v_stack_mD8 = (unsigned int)(a2);
        v_stack_m70 = (unsigned int)(a1);
        v_stack_m60 = (unsigned int)(a2);
        v_stack_m50 = (unsigned int)(a1);
        v_stack_mC0 = a4;
        a4 = 0;
        v_stack_m40 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9127421);
        v_stack_m30 = (unsigned int)(a2);
        v_stack_m20 = (unsigned int)(a2);
        a2 = v_rip - 6268924;
        v_stack_mB8 = a2;
        v_stack_mC4 = a3;
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
int64_t VmpLogTbFlushSlatInvalidate(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
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
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC4;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (256);
    result = (*(uint64_t *)(v_rip + 0x7BC8F3)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x8B45FD))) <= 5) goto loc_0064DF31;
    result = tlgKeywordOn(*(uint64_t *)(v_rip + 0x8B45FD), 2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        result = *(uint32_t *)(Arg1 + 0x1D0);
        Arg1 = 2 + 2;
        Arg2 = Arg1 + 4;
        v_stack_mC8 = (uint32_t)(result);
        result = v_stack_mC8;
        v_stack_m78 = result;
        result = v_stack_mB8;
        v_stack_m68 = result;
        result = v_stack_mC4;
        v_stack_m58 = result;
        result = v_stack_mC0;
        v_stack_m48 = result;
        result = Arg5;
        v_stack_mB0 = result;
        result = v_stack_mB0;
        v_stack_m38 = result;
        result = Arg6;
        v_stack_mA8 = result;
        result = v_stack_mA8;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mD0 = result;
        v_stack_mD8 = (uint32_t)(Arg2);
        v_stack_m70 = (uint32_t)(Arg1);
        v_stack_m60 = (uint32_t)(Arg2);
        v_stack_m50 = (uint32_t)(Arg1);
        v_stack_mC0 = Arg4;
        Arg4 = 0;
        v_stack_m40 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x8B45FD);
        v_stack_m30 = (uint32_t)(Arg2);
        v_stack_m20 = (uint32_t)(Arg2);
        Arg2 = v_rip - 6268924;
        v_stack_mB8 = Arg2;
        v_stack_mC4 = Arg3;
        result = tlgWriteEx_EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (256);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064DE38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064DE38[BB_0064DE38]
  bb_0064DE68[BB_0064DE68]
  bb_0064DE7D[BB_0064DE7D]
  bb_0064DF31[BB_0064DF31]
  bb_0064DF46[BB_0064DF46]
  bb_0064DE38 -->|branch| bb_0064DF31
  bb_0064DE38 -->|fallthrough| bb_0064DE68
  bb_0064DE68 -->|branch| bb_0064DF31
  bb_0064DE68 -->|fallthrough| bb_0064DE7D
  bb_0064DE7D -->|flow| bb_0064DF31
```
