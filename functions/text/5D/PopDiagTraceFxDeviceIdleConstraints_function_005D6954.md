# PopDiagTraceFxDeviceIdleConstraints

- RVA: `0x005D6954`–`0x005D6A2E` (길이 `218` bytes)
- VA: `0x00000001405D6954`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CC818`
- 디코드: `48`개 명령, `218/218` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x005D699A` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005D6A0B` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005D6A17` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPluginRequestDeviceIdleConstraints](../4D/PopPluginRequestDeviceIdleConstraints_function_004D2660.md) at `0x004D26C8`

### Static image references
- `0x005D696E` → RVA `0x00E0A740` (`.data`; read)
- `0x005D697C` → RVA `0x00E67858` (`.data`; read)
- `0x005D698C` → RVA `0x00F0B408` (`.data`; read)
- `0x005D6993` → RVA `0x000217F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D6954  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
005D6959  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
005D695E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
005D6963  55                              push rbp
005D6964  48 8B EC                        mov rbp, rsp
005D6967  48 81 EC 80 00 00 00            sub rsp, 0x80
005D696E  48 8B 05 CB 3D 83 00            mov rax, qword ptr [rip + 0x833dcb]
005D6975  48 33 C4                        xor rax, rsp
005D6978  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005D697C  80 3D D5 0E 89 00 00            cmp byte ptr [rip + 0x890ed5], 0
005D6983  48 8B DA                        mov rbx, rdx
005D6986  0F 84 84 00 00 00               je 0x1405d6a10
005D698C  48 8B 0D 75 4A 93 00            mov rcx, qword ptr [rip + 0x934a75]
005D6993  48 8D 15 56 AE A4 FF            lea rdx, [rip - 0x5b51aa]
005D699A  E8 B1 BA DB FF                  call 0x140392450
005D699F  84 C0                           test al, al
005D69A1  74 6D                           je 0x1405d6a10
005D69A3  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
005D69A7  48 8D 45 10                     lea rax, [rbp + 0x10]
005D69AB  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
005D69AF  48 8D 15 3A AE A4 FF            lea rdx, [rip - 0x5b51c6]
005D69B6  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
005D69BA  45 33 C9                        xor r9d, r9d
005D69BD  48 8B 0D 44 4A 93 00            mov rcx, qword ptr [rip + 0x934a44]
005D69C4  45 33 C0                        xor r8d, r8d
005D69C7  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
005D69CB  48 8D 45 20                     lea rax, [rbp + 0x20]
005D69CF  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005D69D3  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
005D69D6  C1 E0 02                        shl eax, 2
005D69D9  89 45 E8                        mov dword ptr [rbp - 0x18], eax
005D69DC  48 8D 45 C0                     lea rax, [rbp - 0x40]
005D69E0  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005D69E5  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
005D69ED  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005D69F3  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005D69F9  C7 45 C8 08 00 00 00            mov dword ptr [rbp - 0x38], 8
005D6A00  C7 45 D8 04 00 00 00            mov dword ptr [rbp - 0x28], 4
005D6A07  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
005D6A0B  E8 C0 86 C8 FF                  call 0x14025f0d0
005D6A10  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
005D6A14  48 33 CC                        xor rcx, rsp
005D6A17  E8 24 5C 0D 00                  call 0x1406ac640
005D6A1C  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
005D6A24  48 81 C4 80 00 00 00            add rsp, 0x80
005D6A2B  5D                              pop rbp
005D6A2C  C3                              ret
005D6A2D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceFxDeviceIdleConstraints(__int64 a1, __int64 a2, int a3, int a4)
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
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 8601035)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 8982229)) == 0) goto loc_005D6A10;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9652853), v_rip - 5984682, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a2 = v_rip - 5984710;
        a4 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 9652804);
        a3 = 0;
        v_stack_m48 = result;
        result = v_stack_p18;
        v_stack_m38 = result;
        result = v_stack_p18;
        result = (unsigned int)((result) << (2));
        v_stack_m20 = (unsigned int)(result);
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m40 = 8;
        v_stack_m30 = 4;
        v_stack_m28 = a2;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceFxDeviceIdleConstraints(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x833DCB)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x890ED5)) == 0) goto loc_005D6A10;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x934A75), v_rip - 5984682, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg2 = v_rip - 5984710;
        Arg4 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x934A44);
        Arg3 = 0;
        v_stack_m48 = result;
        result = v_stack_p18;
        v_stack_m38 = result;
        result = v_stack_p18;
        result = (uint32_t)((result) << (2));
        v_stack_m20 = (uint32_t)(result);
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m40 = 8;
        v_stack_m30 = 4;
        v_stack_m28 = Arg2;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D6954&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D6954[BB_005D6954]
  bb_005D698C[BB_005D698C]
  bb_005D69A3[BB_005D69A3]
  bb_005D6A10[BB_005D6A10]
  bb_005D6A2D[BB_005D6A2D]
  bb_005D6954 -->|branch| bb_005D6A10
  bb_005D6954 -->|fallthrough| bb_005D698C
  bb_005D698C -->|branch| bb_005D6A10
  bb_005D698C -->|fallthrough| bb_005D69A3
  bb_005D69A3 -->|flow| bb_005D6A10
```
