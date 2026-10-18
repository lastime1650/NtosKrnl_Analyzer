# TtmiLogDeviceRundown

- RVA: `0x00779D00`–`0x00779E4F` (길이 `335` bytes)
- VA: `0x0000000140779D00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073684`
- 디코드: `69`개 명령, `335/335` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00779D38` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00779E34` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779E40` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiDevicesRundown](TtmiDevicesRundown_function_00775AFC.md) at `0x00775B7B`

### Static image references
- `0x00779D0E` → RVA `0x00E0A740` (`.data`; read)
- `0x00779D1C` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x00779D48` → RVA `0x00051F79` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00779D38` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00779E34` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779E40` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779D00  40 55                           push rbp
00779D02  48 8D 6C 24 F0                  lea rbp, [rsp - 0x10]
00779D07  48 81 EC 10 01 00 00            sub rsp, 0x110
00779D0E  48 8B 05 2B 0A 69 00            mov rax, qword ptr [rip + 0x690a2b]
00779D15  48 33 C4                        xor rax, rsp
00779D18  48 89 45 00                     mov qword ptr [rbp], rax
00779D1C  83 3D A5 EB 85 00 05            cmp dword ptr [rip + 0x85eba5], 5
00779D23  4C 8B C1                        mov r8, rcx
00779D26  0F 86 0D 01 00 00               jbe 0x140779e39
00779D2C  BA 01 00 00 00                  mov edx, 1
00779D31  48 8D 0D 90 EB 85 00            lea rcx, [rip + 0x85eb90]
00779D38  E8 63 4D CB FF                  call 0x14042eaa0
00779D3D  84 C0                           test al, al
00779D3F  0F 84 F4 00 00 00               je 0x140779e39
00779D45  41 8B 00                        mov eax, dword ptr [r8]
00779D48  48 8D 15 2A 82 8D FF            lea rdx, [rip - 0x727dd6]
00779D4F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00779D53  48 8D 0D 6E EB 85 00            lea rcx, [rip + 0x85eb6e]
00779D5A  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00779D5F  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
00779D67  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00779D6B  45 33 C9                        xor r9d, r9d
00779D6E  41 8B 40 04                     mov eax, dword ptr [r8 + 4]
00779D72  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00779D76  48 8D 44 24 34                  lea rax, [rsp + 0x34]
00779D7B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
00779D7F  41 8B 40 08                     mov eax, dword ptr [r8 + 8]
00779D83  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00779D87  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00779D8C  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00779D90  49 8B 40 18                     mov rax, qword ptr [r8 + 0x18]
00779D94  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00779D99  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00779D9E  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
00779DA2  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00779DA6  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
00779DAA  48 8D 44 24 3C                  lea rax, [rsp + 0x3c]
00779DAF  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00779DB3  41 8B 40 10                     mov eax, dword ptr [r8 + 0x10]
00779DB7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00779DBB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00779DC0  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00779DC4  49 8B 40 20                     mov rax, qword ptr [r8 + 0x20]
00779DC8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00779DCD  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00779DD2  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00779DD6  41 8B 40 14                     mov eax, dword ptr [r8 + 0x14]
00779DDA  45 33 C0                        xor r8d, r8d
00779DDD  89 44 24 44                     mov dword ptr [rsp + 0x44], eax
00779DE1  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00779DE6  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00779DEA  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00779DEF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00779DF4  C7 44 24 20 0A 00 00 00         mov dword ptr [rsp + 0x20], 0xa
00779DFC  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
00779E04  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
00779E0C  48 C7 45 B8 08 00 00 00         mov qword ptr [rbp - 0x48], 8
00779E14  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
00779E1C  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
00779E24  48 C7 45 E8 08 00 00 00         mov qword ptr [rbp - 0x18], 8
00779E2C  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
00779E34  E8 A7 C2 CA FF                  call 0x1404260e0
00779E39  48 8B 4D 00                     mov rcx, qword ptr [rbp]
00779E3D  48 33 CC                        xor rcx, rsp
00779E40  E8 FB 27 F3 FF                  call 0x1406ac640
00779E45  48 81 C4 10 01 00 00            add rsp, 0x110
00779E4C  5D                              pop rbp
00779E4D  C3                              ret
00779E4E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceRundown(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
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
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;

    v_rsp = (v_rsp) - (272);
    result = (*(unsigned __int64 *)(v_rip + 6883883)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8776613)) <= 5) goto loc_00779E39;
    result = tlgKeywordOn(v_rip + 8776592, 1, a1, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned int *)(a1);
        a2 = v_rip - 7503318;
        v_stack_mE8 = (unsigned int)(result);
        a1 = v_rip + 8776558;
        result = v_stack_mE8;
        v_stack_m90 = 4;
        v_stack_m98 = result;
        a4 = 0;
        result = *(unsigned int *)(a1 + 4);
        v_stack_mE4 = (unsigned int)(result);
        result = v_stack_mE4;
        v_stack_m88 = result;
        result = *(unsigned int *)(a1 + 8);
        v_stack_mE0 = (unsigned int)(result);
        result = v_stack_mE0;
        v_stack_m78 = result;
        result = *(unsigned __int64 *)(a1 + 24);
        v_stack_mD0 = result;
        result = v_stack_mD0;
        v_stack_m68 = result;
        result = *(unsigned int *)(a1 + 12);
        v_stack_mDC = (unsigned int)(result);
        result = v_stack_mDC;
        v_stack_m58 = result;
        result = *(unsigned int *)(a1 + 16);
        v_stack_mD8 = (unsigned int)(result);
        result = v_stack_mD8;
        v_stack_m48 = result;
        result = *(unsigned __int64 *)(a1 + 32);
        v_stack_mC8 = result;
        result = v_stack_mC8;
        v_stack_m38 = result;
        result = *(unsigned int *)(a1 + 20);
        a3 = 0;
        v_stack_mD4 = (unsigned int)(result);
        result = v_stack_mD4;
        v_stack_m28 = result;
        result = v_stack_mB8;
        v_stack_mF0 = result;
        v_stack_mF8 = 10;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 8;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (272);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceRundown(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
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
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;

    local_rsp = (local_rsp) - (272);
    result = (*(uint64_t *)(v_rip + 0x690A2B)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85EBA5)) <= 5) goto loc_00779E39;
    result = tlgKeywordOn(v_rip + 8776592, 1, Arg1, Arg4);
    if ((uint8_t)(result) != 0) {
        result = *(uint32_t *)(Arg1);
        Arg2 = v_rip - 7503318;
        v_stack_mE8 = (uint32_t)(result);
        Arg1 = v_rip + 8776558;
        result = v_stack_mE8;
        v_stack_m90 = 4;
        v_stack_m98 = result;
        Arg4 = 0;
        result = *(uint32_t *)(Arg1 + 0x4);
        v_stack_mE4 = (uint32_t)(result);
        result = v_stack_mE4;
        v_stack_m88 = result;
        result = *(uint32_t *)(Arg1 + 0x8);
        v_stack_mE0 = (uint32_t)(result);
        result = v_stack_mE0;
        v_stack_m78 = result;
        result = *(uint64_t *)(Arg1 + 0x18);
        v_stack_mD0 = result;
        result = v_stack_mD0;
        v_stack_m68 = result;
        result = *(uint32_t *)(Arg1 + 0xC);
        v_stack_mDC = (uint32_t)(result);
        result = v_stack_mDC;
        v_stack_m58 = result;
        result = *(uint32_t *)(Arg1 + 0x10);
        v_stack_mD8 = (uint32_t)(result);
        result = v_stack_mD8;
        v_stack_m48 = result;
        result = *(uint64_t *)(Arg1 + 0x20);
        v_stack_mC8 = result;
        result = v_stack_mC8;
        v_stack_m38 = result;
        result = *(uint32_t *)(Arg1 + 0x14);
        Arg3 = 0;
        v_stack_mD4 = (uint32_t)(result);
        result = v_stack_mD4;
        v_stack_m28 = result;
        result = v_stack_mB8;
        v_stack_mF0 = result;
        v_stack_mF8 = 10;
        v_stack_m80 = 4;
        v_stack_m70 = 4;
        v_stack_m60 = 8;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        v_stack_m30 = 8;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (272);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779D00[BB_00779D00]
  bb_00779D2C[BB_00779D2C]
  bb_00779D45[BB_00779D45]
  bb_00779E39[BB_00779E39]
  bb_00779E4E[BB_00779E4E]
  bb_00779D00 -->|branch| bb_00779E39
  bb_00779D00 -->|fallthrough| bb_00779D2C
  bb_00779D2C -->|branch| bb_00779E39
  bb_00779D2C -->|fallthrough| bb_00779D45
  bb_00779D45 -->|flow| bb_00779E39
```
