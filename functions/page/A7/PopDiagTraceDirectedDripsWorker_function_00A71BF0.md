# PopDiagTraceDirectedDripsWorker

- RVA: `0x00A71BF0`–`0x00A71CA3` (길이 `179` bytes)
- VA: `0x0000000140A71BF0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B540C`
- 디코드: `43`개 명령, `179/179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x00A71C22` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A71C8B` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A71C97` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopDirectedDripsWorkerRoutine](../75/PopDirectedDripsWorkerRoutine_function_00757DF0.md) at `0x00757E26`

### Static image references
- `0x00A71BFD` → RVA `0x00E0A740` (`.data`; read)
- `0x00A71C0B` → RVA `0x00E67858` (`.data`; read)
- `0x00A71C14` → RVA `0x00F0B408` (`.data`; read)
- `0x00A71C1B` → RVA `0x0001AF78` (`.rdata`; read)
- `0x00A71C2B` → RVA `0x00F0B6B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A71C22` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A71C8B` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A71C97` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A71BF0  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00A71BF5  55                              push rbp
00A71BF6  48 8B EC                        mov rbp, rsp
00A71BF9  48 83 EC 70                     sub rsp, 0x70
00A71BFD  48 8B 05 3C 8B 39 00            mov rax, qword ptr [rip + 0x398b3c]
00A71C04  48 33 C4                        xor rax, rsp
00A71C07  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00A71C0B  80 3D 46 5C 3F 00 00            cmp byte ptr [rip + 0x3f5c46], 0
00A71C12  74 7C                           je 0x140a71c90
00A71C14  48 8B 0D ED 97 49 00            mov rcx, qword ptr [rip + 0x4997ed]
00A71C1B  48 8D 15 56 93 5A FF            lea rdx, [rip - 0xa56caa]
00A71C22  E8 29 08 92 FF                  call 0x140392450
00A71C27  84 C0                           test al, al
00A71C29  74 65                           je 0x140a71c90
00A71C2B  8A 05 7F 9A 49 00               mov al, byte ptr [rip + 0x499a7f]
00A71C31  48 8D 15 40 93 5A FF            lea rdx, [rip - 0xa56cc0]
00A71C38  83 65 D4 00                     and dword ptr [rbp - 0x2c], 0
00A71C3C  B9 08 00 00 00                  mov ecx, 8
00A71C41  83 65 E4 00                     and dword ptr [rbp - 0x1c], 0
00A71C45  45 33 C0                        xor r8d, r8d
00A71C48  83 65 F4 00                     and dword ptr [rbp - 0xc], 0
00A71C4C  88 45 C0                        mov byte ptr [rbp - 0x40], al
00A71C4F  48 8D 45 C0                     lea rax, [rbp - 0x40]
00A71C53  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00A71C57  44 8D 49 FB                     lea r9d, [rcx - 5]
00A71C5B  48 8D 45 10                     lea rax, [rbp + 0x10]
00A71C5F  89 4D E0                        mov dword ptr [rbp - 0x20], ecx
00A71C62  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00A71C66  48 8D 05 43 9A 49 00            lea rax, [rip + 0x499a43]
00A71C6D  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00A71C71  48 8D 45 C8                     lea rax, [rbp - 0x38]
00A71C75  89 4D F0                        mov dword ptr [rbp - 0x10], ecx
00A71C78  48 8B 0D 89 97 49 00            mov rcx, qword ptr [rip + 0x499789]
00A71C7F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A71C84  C7 45 D0 01 00 00 00            mov dword ptr [rbp - 0x30], 1
00A71C8B  E8 90 AA 9A FF                  call 0x14041c720
00A71C90  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00A71C94  48 33 CC                        xor rcx, rsp
00A71C97  E8 A4 A9 C3 FF                  call 0x1406ac640
00A71C9C  48 83 C4 70                     add rsp, 0x70
00A71CA0  5D                              pop rbp
00A71CA1  C3                              ret
00A71CA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceDirectedDripsWorker(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 3771196)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned __int8 *)(v_rip + 4152390)) == 0) goto loc_00A71C90;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 4823021), v_rip - 10841258, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int8 *)(v_rip + 4823679);
        a2 = v_rip - 10841280;
        a1 = 8;
        a3 = 0;
        v_stack_m48 = (unsigned __int8)(result);
        result = v_stack_m48;
        v_stack_m40 = result;
        a4 = a1 - 5;
        result = v_stack_p8;
        v_stack_m28 = (unsigned int)(a1);
        v_stack_m30 = result;
        result = v_rip + 4823619;
        v_stack_m20 = result;
        result = v_stack_m40;
        v_stack_m18 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 4822921);
        v_stack_m58 = result;
        v_stack_m38 = 1;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceDirectedDripsWorker(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint8_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x398B3C)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint8_t *)(v_rip + 0x3F5C46)) == 0) goto loc_00A71C90;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4997ED), v_rip - 10841258, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = *(uint8_t *)(v_rip + 0x499A7F);
        Arg2 = v_rip - 10841280;
        Arg1 = 8;
        Arg3 = 0;
        v_stack_m48 = (uint8_t)(result);
        result = v_stack_m48;
        v_stack_m40 = result;
        a4 = Arg1 - 5;
        result = v_stack_p8;
        v_stack_m28 = (uint32_t)(Arg1);
        v_stack_m30 = result;
        result = v_rip + 4823619;
        v_stack_m20 = result;
        result = v_stack_m40;
        v_stack_m18 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x499789);
        v_stack_m58 = result;
        v_stack_m38 = 1;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A71BF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A71BF0[BB_00A71BF0]
  bb_00A71C14[BB_00A71C14]
  bb_00A71C2B[BB_00A71C2B]
  bb_00A71C90[BB_00A71C90]
  bb_00A71CA2[BB_00A71CA2]
  bb_00A71BF0 -->|branch| bb_00A71C90
  bb_00A71BF0 -->|fallthrough| bb_00A71C14
  bb_00A71C14 -->|branch| bb_00A71C90
  bb_00A71C14 -->|fallthrough| bb_00A71C2B
  bb_00A71C2B -->|flow| bb_00A71C90
```
