# TtmiLogSessionRundown

- RVA: `0x0077B670`–`0x0077B7EF` (길이 `383` bytes)
- VA: `0x000000014077B670`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C861C`
- 디코드: `79`개 명령, `383/383` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077B6A8` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077B7D4` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077B7E0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSessionsRundown](TtmiSessionsRundown_function_007771BC.md) at `0x0077723E`

### Static image references
- `0x0077B67E` → RVA `0x00E0A740` (`.data`; read)
- `0x0077B68C` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077B6B8` → RVA `0x00052103` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077B6A8` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077B7D4` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077B7E0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077B670  40 55                           push rbp
0077B672  48 8D 6C 24 D0                  lea rbp, [rsp - 0x30]
0077B677  48 81 EC 30 01 00 00            sub rsp, 0x130
0077B67E  48 8B 05 BB F0 68 00            mov rax, qword ptr [rip + 0x68f0bb]
0077B685  48 33 C4                        xor rax, rsp
0077B688  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0077B68C  83 3D 35 D2 85 00 05            cmp dword ptr [rip + 0x85d235], 5
0077B693  4C 8B C1                        mov r8, rcx
0077B696  0F 86 3D 01 00 00               jbe 0x14077b7d9
0077B69C  BA 01 00 00 00                  mov edx, 1
0077B6A1  48 8D 0D 20 D2 85 00            lea rcx, [rip + 0x85d220]
0077B6A8  E8 F3 33 CB FF                  call 0x14042eaa0
0077B6AD  84 C0                           test al, al
0077B6AF  0F 84 24 01 00 00               je 0x14077b7d9
0077B6B5  41 8B 00                        mov eax, dword ptr [r8]
0077B6B8  48 8D 15 44 6A 8D FF            lea rdx, [rip - 0x7295bc]
0077B6BF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0077B6C3  48 8D 0D FE D1 85 00            lea rcx, [rip + 0x85d1fe]
0077B6CA  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0077B6CF  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
0077B6D7  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0077B6DB  45 33 C9                        xor r9d, r9d
0077B6DE  41 8B 40 04                     mov eax, dword ptr [r8 + 4]
0077B6E2  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
0077B6E6  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0077B6EB  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0077B6EF  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
0077B6F3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0077B6F7  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0077B6FC  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0077B700  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
0077B704  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
0077B708  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
0077B70D  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0077B711  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
0077B715  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0077B719  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0077B71E  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0077B722  41 8B 40 14                     mov eax, dword ptr [r8 + 0x14]
0077B726  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
0077B72A  48 8D 44 24 44                  lea rax, [rsp + 0x44]
0077B72F  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0077B733  41 8B 40 18                     mov eax, dword ptr [r8 + 0x18]
0077B737  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0077B73B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
0077B740  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0077B744  41 8B 40 1C                     mov eax, dword ptr [r8 + 0x1c]
0077B748  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
0077B74C  48 8D 44 24 4C                  lea rax, [rsp + 0x4c]
0077B751  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0077B755  41 8B 40 20                     mov eax, dword ptr [r8 + 0x20]
0077B759  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0077B75D  48 8D 44 24 50                  lea rax, [rsp + 0x50]
0077B762  48 89 45 00                     mov qword ptr [rbp], rax
0077B766  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
0077B76A  45 33 C0                        xor r8d, r8d
0077B76D  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
0077B771  48 8D 44 24 54                  lea rax, [rsp + 0x54]
0077B776  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0077B77A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
0077B77F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077B784  C7 44 24 20 0C 00 00 00         mov dword ptr [rsp + 0x20], 0xc
0077B78C  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
0077B794  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
0077B79C  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
0077B7A4  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
0077B7AC  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
0077B7B4  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
0077B7BC  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
0077B7C4  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
0077B7CC  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
0077B7D4  E8 07 A9 CA FF                  call 0x1404260e0
0077B7D9  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0077B7DD  48 33 CC                        xor rcx, rsp
0077B7E0  E8 5B 0E F3 FF                  call 0x1406ac640
0077B7E5  48 81 C4 30 01 00 00            add rsp, 0x130
0077B7EC  5D                              pop rbp
0077B7ED  C3                              ret
0077B7EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogSessionRundown(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m118;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
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
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned int v_stack_mFC;

    v_rsp = (v_rsp) - (304);
    result = (*(unsigned __int64 *)(v_rip + 6877371)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8770101)) <= 5) goto loc_0077B7D9;
    result = tlgKeywordOn(v_rip + 8770080, 1, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(a1);
        a2 = v_rip - 7509436;
        v_stack_m108 = (unsigned int)(result);
        a1 = v_rip + 8770046;
        result = v_stack_m108;
        v_stack_mB0 = 4;
        v_stack_mB8 = result;
        a4 = 0;
        result = *(unsigned int *)(a1 + 4);
        v_stack_m104 = (unsigned int)(result);
        result = v_stack_m104;
        v_stack_mA8 = result;
        result = *(unsigned int *)(a1 + 8);
        v_stack_m100 = (unsigned int)(result);
        result = v_stack_m100;
        v_stack_m98 = result;
        result = *(unsigned int *)(a1 + 12);
        v_stack_mFC = (unsigned int)(result);
        result = v_stack_mFC;
        v_stack_m88 = result;
        result = *(unsigned int *)(a1 + 16);
        v_stack_mF8 = (unsigned int)(result);
        result = v_stack_mF8;
        v_stack_m78 = result;
        result = *(unsigned int *)(a1 + 20);
        v_stack_mF4 = (unsigned int)(result);
        result = v_stack_mF4;
        v_stack_m68 = result;
        result = *(unsigned int *)(a1 + 24);
        v_stack_mF0 = (unsigned int)(result);
        result = v_stack_mF0;
        v_stack_m58 = result;
        result = *(unsigned int *)(a1 + 28);
        v_stack_mEC = (unsigned int)(result);
        result = v_stack_mEC;
        v_stack_m48 = result;
        result = *(unsigned int *)(a1 + 32);
        v_stack_mE8 = (unsigned int)(result);
        result = v_stack_mE8;
        v_stack_m38 = result;
        result = *(unsigned int *)(a1 + 36);
        a3 = 0;
        v_stack_mE4 = (unsigned int)(result);
        result = v_stack_mE4;
        v_stack_m28 = result;
        result = v_stack_mD8;
        v_stack_m110 = result;
        v_stack_m118 = 12;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (304);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogSessionRundown(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m118;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
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
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint32_t v_stack_mFC;

    local_rsp = (local_rsp) - (304);
    result = (*(uint64_t *)(v_rip + 0x68F0BB)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85D235)) <= 5) goto loc_0077B7D9;
    result = tlgKeywordOn(v_rip + 8770080, 1, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(Arg1);
        Arg2 = v_rip - 7509436;
        v_stack_m108 = (uint32_t)(result);
        Arg1 = v_rip + 8770046;
        result = v_stack_m108;
        v_stack_mB0 = 4;
        v_stack_mB8 = result;
        Arg4 = 0;
        result = *(uint32_t *)(Arg1 + 0x4);
        v_stack_m104 = (uint32_t)(result);
        result = v_stack_m104;
        v_stack_mA8 = result;
        result = *(uint32_t *)(Arg1 + 0x8);
        v_stack_m100 = (uint32_t)(result);
        result = v_stack_m100;
        v_stack_m98 = result;
        result = *(uint32_t *)(Arg1 + 0xC);
        v_stack_mFC = (uint32_t)(result);
        result = v_stack_mFC;
        v_stack_m88 = result;
        result = *(uint32_t *)(Arg1 + 0x10);
        v_stack_mF8 = (uint32_t)(result);
        result = v_stack_mF8;
        v_stack_m78 = result;
        result = *(uint32_t *)(Arg1 + 0x14);
        v_stack_mF4 = (uint32_t)(result);
        result = v_stack_mF4;
        v_stack_m68 = result;
        result = *(uint32_t *)(Arg1 + 0x18);
        v_stack_mF0 = (uint32_t)(result);
        result = v_stack_mF0;
        v_stack_m58 = result;
        result = *(uint32_t *)(Arg1 + 0x1C);
        v_stack_mEC = (uint32_t)(result);
        result = v_stack_mEC;
        v_stack_m48 = result;
        result = *(uint32_t *)(Arg1 + 0x20);
        v_stack_mE8 = (uint32_t)(result);
        result = v_stack_mE8;
        v_stack_m38 = result;
        result = *(uint32_t *)(Arg1 + 0x24);
        Arg3 = 0;
        v_stack_mE4 = (uint32_t)(result);
        result = v_stack_mE4;
        v_stack_m28 = result;
        result = v_stack_mD8;
        v_stack_m110 = result;
        v_stack_m118 = 12;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (304);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077B670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077B670[BB_0077B670]
  bb_0077B69C[BB_0077B69C]
  bb_0077B6B5[BB_0077B6B5]
  bb_0077B7D9[BB_0077B7D9]
  bb_0077B7EE[BB_0077B7EE]
  bb_0077B670 -->|branch| bb_0077B7D9
  bb_0077B670 -->|fallthrough| bb_0077B69C
  bb_0077B69C -->|branch| bb_0077B7D9
  bb_0077B69C -->|fallthrough| bb_0077B6B5
  bb_0077B6B5 -->|flow| bb_0077B7D9
```
