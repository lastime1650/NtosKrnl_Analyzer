# EtwTraceWin32kFreezeChangeNotifyStart

- RVA: `0x007B8410`–`0x007B84C3` (길이 `179` bytes)
- VA: `0x00000001407B8410`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B9BCC`
- 디코드: `37`개 명령, `179/179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007B8445` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007B84A5` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007B84B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PspPostFreezeOperationWorker](../A9/PspPostFreezeOperationWorker_function_00A94CB0.md) at `0x00A94F97`
- [PspWin32kProcessFreezeNotify](../AA/PspWin32kProcessFreezeNotify_function_00AA3A88.md) at `0x00AA3B2F`

### Static image references
- `0x007B8417` → RVA `0x00E0A740` (`.data`; read)
- `0x007B8429` → RVA `0x00E091A0` (`.data`; read)
- `0x007B848D` → RVA `0x00054938` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007B8445` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007B84A5` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007B84B5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B8410  48 81 EC 98 00 00 00            sub rsp, 0x98
007B8417  48 8B 05 22 23 65 00            mov rax, qword ptr [rip + 0x652322]
007B841E  48 33 C4                        xor rax, rsp
007B8421  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
007B8429  83 3D 70 0D 65 00 05            cmp dword ptr [rip + 0x650d70], 5
007B8430  44 0F B7 C2                     movzx r8d, dx
007B8434  44 8B C9                        mov r9d, ecx
007B8437  76 71                           jbe 0x1407b84aa
007B8439  BA 04 00 00 00                  mov edx, 4
007B843E  48 8D 0D 5B 0D 65 00            lea rcx, [rip + 0x650d5b]
007B8445  E8 56 66 C7 FF                  call 0x14042eaa0
007B844A  84 C0                           test al, al
007B844C  74 5C                           je 0x1407b84aa
007B844E  83 64 24 6C 00                  and dword ptr [rsp + 0x6c], 0
007B8453  48 8D 44 24 34                  lea rax, [rsp + 0x34]
007B8458  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
007B845D  48 8D 0D 3C 0D 65 00            lea rcx, [rip + 0x650d3c]
007B8464  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007B8469  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007B846E  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007B8473  48 8D 44 24 40                  lea rax, [rsp + 0x40]
007B8478  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007B847D  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
007B8481  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
007B8486  45 33 C9                        xor r9d, r9d
007B8489  89 54 24 68                     mov dword ptr [rsp + 0x68], edx
007B848D  48 8D 15 A4 C4 89 FF            lea rdx, [rip - 0x763b5c]
007B8494  66 44 89 44 24 30               mov word ptr [rsp + 0x30], r8w
007B849A  45 33 C0                        xor r8d, r8d
007B849D  C7 44 24 78 02 00 00 00         mov dword ptr [rsp + 0x78], 2
007B84A5  E8 36 DC C6 FF                  call 0x1404260e0
007B84AA  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
007B84B2  48 33 CC                        xor rcx, rsp
007B84B5  E8 86 41 EF FF                  call 0x1406ac640
007B84BA  48 81 C4 98 00 00 00            add rsp, 0x98
007B84C1  C3                              ret
007B84C2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceWin32kFreezeChangeNotifyStart(int a1, unsigned __int16 a2)
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
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;

    v_rsp = (v_rsp) - (152);
    result = (*(unsigned __int64 *)(v_rip + 6628130)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6622576)) <= 5) goto loc_007B84AA;
    result = tlgKeywordOn(v_rip + 6622555, 4, a2, (unsigned int)(a1));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m64;
        a1 = v_rip + 6622524;
        v_stack_m38 = result;
        result = v_stack_m68;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = 4;
        v_stack_m64 = (unsigned int)((unsigned int)(a1));
        a4 = 0;
        v_stack_m30 = 4;
        a2 = v_rip - 7748444;
        v_stack_m68 = a2;
        a3 = 0;
        v_stack_m20 = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (152);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceWin32kFreezeChangeNotifyStart(int32_t Arg1, uint16_t Arg2)
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
    uint64_t v_stack_m58;
    uint64_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;

    local_rsp = (local_rsp) - (152);
    result = (*(uint64_t *)(v_rip + 0x652322)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x650D70)) <= 5) goto loc_007B84AA;
    result = tlgKeywordOn(v_rip + 6622555, 4, Arg2, (uint32_t)(Arg1));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m64;
        Arg1 = v_rip + 6622524;
        v_stack_m38 = result;
        result = v_stack_m68;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m70 = result;
        v_stack_m78 = 4;
        v_stack_m64 = (uint32_t)((uint32_t)(Arg1));
        a4 = 0;
        v_stack_m30 = 4;
        Arg2 = v_rip - 7748444;
        v_stack_m68 = Arg2;
        a3 = 0;
        v_stack_m20 = 2;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (152);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B8410&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B8410[BB_007B8410]
  bb_007B8439[BB_007B8439]
  bb_007B844E[BB_007B844E]
  bb_007B84AA[BB_007B84AA]
  bb_007B84C2[BB_007B84C2]
  bb_007B8410 -->|branch| bb_007B84AA
  bb_007B8410 -->|fallthrough| bb_007B8439
  bb_007B8439 -->|branch| bb_007B84AA
  bb_007B8439 -->|fallthrough| bb_007B844E
  bb_007B844E -->|flow| bb_007B84AA
```
