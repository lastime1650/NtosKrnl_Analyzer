# PcwRegister

- RVA: `0x00A61180`–`0x00A611D8` (길이 `88` bytes)
- VA: `0x0000000140A61180`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076818`
- 디코드: `26`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A61197` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00A611AA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A611B8` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x00A611CF` → [ExpPcwDisabledStatus](ExpPcwDisabledStatus_function_00A611E0.md) (function, `0x00A611E0`)

### Direct callers
- [ExpRegisterCounterSet](../7D/ExpRegisterCounterSet_function_007D156C.md) at `0x007D157C`
- [ExpRegisterCounterSet](../7D/ExpRegisterCounterSet_function_007D156C.md) at `0x007D1594`

### Static image references
- `0x00A61190` → RVA `0x00FD8080` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A61197` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00A611AA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A611B8` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A61180  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A61185  57                              push rdi
00A61186  48 83 EC 20                     sub rsp, 0x20
00A6118A  48 8B D9                        mov rbx, rcx
00A6118D  48 8B FA                        mov rdi, rdx
00A61190  48 8B 0D E9 6E 57 00            mov rcx, qword ptr [rip + 0x576ee9]
00A61197  E8 78 76 9C FF                  call 0x140428814
00A6119C  48 85 C0                        test rax, rax
00A6119F  74 2A                           je 0x140a611cb
00A611A1  48 8B 00                        mov rax, qword ptr [rax]
00A611A4  48 8B D7                        mov rdx, rdi
00A611A7  48 8B CB                        mov rcx, rbx
00A611AA  E8 21 99 C5 FF                  call 0x1406baad0
00A611AF  48 8B 0D CA 6E 57 00            mov rcx, qword ptr [rip + 0x576eca]
00A611B6  8B D8                           mov ebx, eax
00A611B8  E8 03 5C 9F FF                  call 0x140456dc0
00A611BD  8B C3                           mov eax, ebx
00A611BF  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A611C4  48 83 C4 20                     add rsp, 0x20
00A611C8  5F                              pop rdi
00A611C9  C3                              ret
00A611CA  CC                              int3
00A611CB  48 83 23 00                     and qword ptr [rbx], 0
00A611CF  E8 0C 00 00 00                  call 0x140a611e0
00A611D4  8B D8                           mov ebx, eax
00A611D6  EB E5                           jmp 0x140a611bd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PcwRegister(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 5730025), a2, a3, a4);
    if (result == 0) goto loc_00A611CB;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    result = ExReleaseExtensionTable(*(unsigned __int64 *)(v_rip + 5729994), a2, a3, a4);
loc_00A611BD:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A611CB:
    result = ExpPcwDisabledStatus(*(unsigned __int64 *)(v_rip + 5729994), a2, a3, a4);
    goto loc_00A611BD;
}
```

## 5. (Beta) C Style

```c
int64_t PcwRegister(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x576EE9), Arg2, a3, a4);
    if (result == 0) goto loc_00A611CB;
    result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    result = ExReleaseExtensionTable(*(uint64_t *)(v_rip + 0x576ECA), Arg2, a3, a4);
loc_00A611BD:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A611CB:
    result = ExpPcwDisabledStatus(*(uint64_t *)(v_rip + 0x576ECA), Arg2, a3, a4);
    goto loc_00A611BD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A61180&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A61180[BB_00A61180]
  bb_00A611A1[BB_00A611A1]
  bb_00A611BD[BB_00A611BD]
  bb_00A611CA[BB_00A611CA]
  bb_00A611CB[BB_00A611CB]
  bb_00A61180 -->|branch| bb_00A611CB
  bb_00A61180 -->|fallthrough| bb_00A611A1
  bb_00A611A1 -->|flow| bb_00A611BD
  bb_00A611CA -->|flow| bb_00A611CB
  bb_00A611CB -->|branch| bb_00A611BD
```
