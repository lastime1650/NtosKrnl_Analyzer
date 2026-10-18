# TtmiLogProximityBlockedRequest

- RVA: `0x0077A6D0`–`0x0077A7E7` (길이 `279` bytes)
- VA: `0x000000014077A6D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CDD2C`
- 디코드: `64`개 명령, `279/279` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077A717` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077A734` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x0077A7C0` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077A7CC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSetPendingOnOffRequest](TtmiSetPendingOnOffRequest_function_0077D074.md) at `0x0077D0E0`

### Static image references
- `0x0077A6EB` → RVA `0x00E0A740` (`.data`; read)
- `0x0077A6F9` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077A797` → RVA `0x0005290C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077A717` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077A734` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x0077A7C0` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077A7CC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077A6D0  48 8B C4                        mov rax, rsp
0077A6D3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0077A6D7  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0077A6DB  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
0077A6DF  55                              push rbp
0077A6E0  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0077A6E4  48 81 EC C0 00 00 00            sub rsp, 0xc0
0077A6EB  48 8B 05 4E 00 69 00            mov rax, qword ptr [rip + 0x69004e]
0077A6F2  48 33 C4                        xor rax, rsp
0077A6F5  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077A6F9  83 3D C8 E1 85 00 05            cmp dword ptr [rip + 0x85e1c8], 5
0077A700  8B DA                           mov ebx, edx
0077A702  40 8A F9                        mov dil, cl
0077A705  0F 86 BA 00 00 00               jbe 0x14077a7c5
0077A70B  BA 01 00 00 00                  mov edx, 1
0077A710  48 8D 0D B1 E1 85 00            lea rcx, [rip + 0x85e1b1]
0077A717  E8 84 43 CB FF                  call 0x14042eaa0
0077A71C  84 C0                           test al, al
0077A71E  0F 84 A1 00 00 00               je 0x14077a7c5
0077A724  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077A72D  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
0077A734  E8 B7 51 AB FF                  call 0x14022f8f0
0077A739  83 65 03 00                     and dword ptr [rbp + 3], 0
0077A73D  48 8D 0D 84 E1 85 00            lea rcx, [rip + 0x85e184]
0077A744  83 65 13 00                     and dword ptr [rbp + 0x13], 0
0077A748  BA 04 00 00 00                  mov edx, 4
0077A74D  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0077A751  45 33 C9                        xor r9d, r9d
0077A754  83 65 33 00                     and dword ptr [rbp + 0x33], 0
0077A758  45 33 C0                        xor r8d, r8d
0077A75B  83 65 43 00                     and dword ptr [rbp + 0x43], 0
0077A75F  89 45 CB                        mov dword ptr [rbp - 0x35], eax
0077A762  48 8D 45 CB                     lea rax, [rbp - 0x35]
0077A766  48 89 45 F7                     mov qword ptr [rbp - 9], rax
0077A76A  48 8D 45 C7                     lea rax, [rbp - 0x39]
0077A76E  48 89 45 07                     mov qword ptr [rbp + 7], rax
0077A772  48 8D 45 CF                     lea rax, [rbp - 0x31]
0077A776  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077A77A  48 8D 45 3F                     lea rax, [rbp + 0x3f]
0077A77E  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077A782  48 8D 45 77                     lea rax, [rbp + 0x77]
0077A786  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077A78A  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077A78E  89 55 FF                        mov dword ptr [rbp - 1], edx
0077A791  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0077A794  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
0077A797  48 8D 15 6E 81 8D FF            lea rdx, [rip - 0x727e92]
0077A79E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077A7A3  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
0077A7AB  40 88 7D C7                     mov byte ptr [rbp - 0x39], dil
0077A7AF  C7 45 0F 01 00 00 00            mov dword ptr [rbp + 0xf], 1
0077A7B6  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
0077A7B9  C7 45 2F 02 00 00 00            mov dword ptr [rbp + 0x2f], 2
0077A7C0  E8 1B B9 CA FF                  call 0x1404260e0
0077A7C5  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077A7C9  48 33 CC                        xor rcx, rsp
0077A7CC  E8 6F 1E F3 FF                  call 0x1406ac640
0077A7D1  4C 8D 9C 24 C0 00 00 00         lea r11, [rsp + 0xc0]
0077A7D9  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0077A7DD  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
0077A7E1  49 8B E3                        mov rsp, r11
0077A7E4  5D                              pop rbp
0077A7E5  C3                              ret
0077A7E6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogProximityBlockedRequest(unsigned __int8 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rdi;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6881358)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    if ((*(unsigned int *)(v_rip + 8774088)) <= 5) goto loc_0077A7C5;
    result = tlgKeywordOn(v_rip + 8774065, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8774020;
        a2 = 4;
        a4 = 0;
        a3 = 0;
        *(unsigned int *)(v_rsp - 95 - 53) = (unsigned int)(result);
        result = v_rsp - 95 - 53;
        *(unsigned __int64 *)(v_rsp - 95 - 9) = result;
        result = v_rsp - 95 - 57;
        *(unsigned __int64 *)(v_rsp - 95 + 7) = result;
        result = v_rsp - 95 - 49;
        *(unsigned __int64 *)(v_rsp - 95 + 23) = result;
        result = v_rsp - 95 + 63;
        *(unsigned __int64 *)(v_rsp - 95 + 39) = result;
        result = v_rsp - 95 + 119;
        *(unsigned __int64 *)(v_rsp - 95 + 55) = result;
        result = v_rsp - 95 - 41;
        *(unsigned int *)(v_rsp - 95 - 1) = a2;
        *(unsigned int *)(v_rsp - 95 + 31) = a2;
        *(unsigned int *)(v_rsp - 95 + 63) = a2;
        a2 = v_rip - 7503506;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        *(unsigned __int8 *)(v_rsp - 95 - 57) = a1;
        *(unsigned int *)(v_rsp - 95 + 15) = 1;
        *(unsigned int *)(v_rsp - 95 - 49) = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 95 + 47) = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogProximityBlockedRequest(uint8_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m8;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rdi;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x69004E)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    if ((*(uint32_t *)(v_rip + 0x85E1C8)) <= 5) goto loc_0077A7C5;
    result = tlgKeywordOn(v_rip + 8774065, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8774020;
        Arg2 = 4;
        Arg4 = 0;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x5F - 0x35) = (uint32_t)(result);
        result = local_rsp - 95 - 53;
        *(uint64_t *)(local_rsp - 0x5F - 0x9) = result;
        result = local_rsp - 95 - 57;
        *(uint64_t *)(local_rsp - 0x5F + 0x7) = result;
        result = local_rsp - 95 - 49;
        *(uint64_t *)(local_rsp - 0x5F + 0x17) = result;
        result = local_rsp - 95 + 63;
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = result;
        result = local_rsp - 95 + 119;
        *(uint64_t *)(local_rsp - 0x5F + 0x37) = result;
        result = local_rsp - 95 - 41;
        *(uint32_t *)(local_rsp - 0x5F - 0x1) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x1F) = Arg2;
        *(uint32_t *)(local_rsp - 0x5F + 0x3F) = Arg2;
        Arg2 = v_rip - 7503506;
        v_stack_mA0 = result;
        v_stack_mA8 = 7;
        *(uint8_t *)(local_rsp - 0x5F - 0x39) = Arg1;
        *(uint32_t *)(local_rsp - 0x5F + 0xF) = 1;
        *(uint32_t *)(local_rsp - 0x5F - 0x31) = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077A6D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077A6D0[BB_0077A6D0]
  bb_0077A70B[BB_0077A70B]
  bb_0077A724[BB_0077A724]
  bb_0077A7C5[BB_0077A7C5]
  bb_0077A7E6[BB_0077A7E6]
  bb_0077A6D0 -->|branch| bb_0077A7C5
  bb_0077A6D0 -->|fallthrough| bb_0077A70B
  bb_0077A70B -->|branch| bb_0077A7C5
  bb_0077A70B -->|fallthrough| bb_0077A724
  bb_0077A724 -->|flow| bb_0077A7C5
```
