# TtmiLogDeviceAssignedTerminalEvent

- RVA: `0x00779648`–`0x0077972F` (길이 `231` bytes)
- VA: `0x0000000140779648`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00078F20`
- 디코드: `54`개 명령, `231/231` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077968A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007796A3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00779708` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00779714` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpPublishDeviceEvent](TtmpPublishDeviceEvent_function_00776718.md) at `0x0077677D`

### Static image references
- `0x0077965F` → RVA `0x00E0A740` (`.data`; read)
- `0x0077966D` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x007796EE` → RVA `0x00051A02` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0077968A` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007796A3` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00779708` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00779714` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00779648  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0077964D  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00779652  55                              push rbp
00779653  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00779658  48 81 EC A0 00 00 00            sub rsp, 0xa0
0077965F  48 8B 05 DA 10 69 00            mov rax, qword ptr [rip + 0x6910da]
00779666  48 33 C4                        xor rax, rsp
00779669  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077966D  83 3D 54 F2 85 00 05            cmp dword ptr [rip + 0x85f254], 5
00779674  8B DA                           mov ebx, edx
00779676  8B F9                           mov edi, ecx
00779678  0F 86 8F 00 00 00               jbe 0x14077970d
0077967E  BA 01 00 00 00                  mov edx, 1
00779683  48 8D 0D 3E F2 85 00            lea rcx, [rip + 0x85f23e]
0077968A  E8 11 54 CB FF                  call 0x14042eaa0
0077968F  84 C0                           test al, al
00779691  74 7A                           je 0x14077970d
00779693  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0077969C  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
007796A3  E8 48 62 AB FF                  call 0x14022f8f0
007796A8  83 65 23 00                     and dword ptr [rbp + 0x23], 0
007796AC  48 8D 0D 15 F2 85 00            lea rcx, [rip + 0x85f215]
007796B3  83 65 33 00                     and dword ptr [rbp + 0x33], 0
007796B7  BA 04 00 00 00                  mov edx, 4
007796BC  83 65 43 00                     and dword ptr [rbp + 0x43], 0
007796C0  45 33 C9                        xor r9d, r9d
007796C3  89 45 E7                        mov dword ptr [rbp - 0x19], eax
007796C6  45 33 C0                        xor r8d, r8d
007796C9  48 8D 45 E7                     lea rax, [rbp - 0x19]
007796CD  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
007796D0  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007796D4  48 8D 45 EB                     lea rax, [rbp - 0x15]
007796D8  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007796DC  48 8D 45 EF                     lea rax, [rbp - 0x11]
007796E0  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007796E4  48 8D 45 F7                     lea rax, [rbp - 9]
007796E8  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
007796EB  89 55 3F                        mov dword ptr [rbp + 0x3f], edx
007796EE  48 8D 15 0D 83 8D FF            lea rdx, [rip - 0x727cf3]
007796F5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007796FA  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00779702  89 7D EB                        mov dword ptr [rbp - 0x15], edi
00779705  89 5D EF                        mov dword ptr [rbp - 0x11], ebx
00779708  E8 D3 C9 CA FF                  call 0x1404260e0
0077970D  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00779711  48 33 CC                        xor rcx, rsp
00779714  E8 27 2F F3 FF                  call 0x1406ac640
00779719  4C 8D 9C 24 A0 00 00 00         lea r11, [rsp + 0xa0]
00779721  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00779725  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
00779729  49 8B E3                        mov rsp, r11
0077972C  5D                              pop rbp
0077972D  C3                              ret
0077972E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogDeviceAssignedTerminalEvent(int a1, int a2, int a3, int a4)
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
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6885594)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8778324)) <= 5) goto loc_0077970D;
    result = tlgKeywordOn(v_rip + 8778302, 1, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(a1 + 184);
        result = PsGetProcessSessionIdEx(a1, 1, a3, a4);
        a1 = v_rip + 8778261;
        a2 = 4;
        a4 = 0;
        v_stack_m78 = (unsigned int)(result);
        a3 = 0;
        result = v_stack_m78;
        v_stack_m40 = a2;
        v_stack_m48 = result;
        result = v_stack_m74;
        v_stack_m38 = result;
        result = v_stack_m70;
        v_stack_m28 = result;
        result = v_stack_m68;
        v_stack_m30 = a2;
        v_stack_m20 = a2;
        a2 = v_rip - 7503091;
        v_stack_m80 = result;
        v_stack_m88 = 5;
        v_stack_m74 = (unsigned int)((unsigned int)(a1));
        v_stack_m70 = (unsigned int)((unsigned int)(a2));
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogDeviceAssignedTerminalEvent(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
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
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m74;
    uint32_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6910DA)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85F254)) <= 5) goto loc_0077970D;
    result = tlgKeywordOn(v_rip + 8778302, 1, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(Arg1 + 0xB8);
        result = PsGetProcessSessionIdEx(Arg1, 1, Arg3, Arg4);
        Arg1 = v_rip + 8778261;
        Arg2 = 4;
        Arg4 = 0;
        v_stack_m78 = (uint32_t)(result);
        Arg3 = 0;
        result = v_stack_m78;
        v_stack_m40 = Arg2;
        v_stack_m48 = result;
        result = v_stack_m74;
        v_stack_m38 = result;
        result = v_stack_m70;
        v_stack_m28 = result;
        result = v_stack_m68;
        v_stack_m30 = Arg2;
        v_stack_m20 = Arg2;
        Arg2 = v_rip - 7503091;
        v_stack_m80 = result;
        v_stack_m88 = 5;
        v_stack_m74 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m70 = (uint32_t)((uint32_t)(Arg2));
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00779648&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00779648[BB_00779648]
  bb_0077967E[BB_0077967E]
  bb_00779693[BB_00779693]
  bb_0077970D[BB_0077970D]
  bb_0077972E[BB_0077972E]
  bb_00779648 -->|branch| bb_0077970D
  bb_00779648 -->|fallthrough| bb_0077967E
  bb_0077967E -->|branch| bb_0077970D
  bb_0077967E -->|fallthrough| bb_00779693
  bb_00779693 -->|flow| bb_0077970D
```
