# PiDqObjectActionQueueEntryCreate

- RVA: `0x00A44138`–`0x00A441A1` (길이 `105` bytes)
- VA: `0x0000000140A44138`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006383C`
- 디코드: `30`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4415D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PiDqObjectManagerHandleObjectEvent](PiDqObjectManagerHandleObjectEvent_function_00A4402C.md) at `0x00A44080`

### Static image references
- `0x00A44174` → RVA `0x00F8B390` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4415D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A44138  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A4413D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00A44142  57                              push rdi
00A44143  48 83 EC 20                     sub rsp, 0x20
00A44147  48 8B DA                        mov rbx, rdx
00A4414A  48 8B F1                        mov rsi, rcx
00A4414D  33 FF                           xor edi, edi
00A4414F  B9 00 01 00 00                  mov ecx, 0x100
00A44154  41 B8 50 6E 70 58               mov r8d, 0x58706e50
00A4415A  8D 57 20                        lea edx, [rdi + 0x20]
00A4415D  E8 8E DF 13 00                  call 0x140b820f0
00A44162  48 89 03                        mov qword ptr [rbx], rax
00A44165  48 8B C8                        mov rcx, rax
00A44168  48 85 C0                        test rax, rax
00A4416B  74 2D                           je 0x140a4419a
00A4416D  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00A44171  8D 47 01                        lea eax, [rdi + 1]
00A44174  F0 48 0F C1 05 13 72 54 00      lock xadd qword ptr [rip + 0x547213], rax
00A4417D  48 FF C0                        inc rax
00A44180  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
00A44184  F0 FF 06                        lock inc dword ptr [rsi]
00A44187  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A4418C  8B C7                           mov eax, edi
00A4418E  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00A44193  48 83 C4 20                     add rsp, 0x20
00A44197  5F                              pop rdi
00A44198  C3                              ret
00A44199  CC                              int3
00A4419A  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A4419F  EB E6                           jmp 0x140a44187
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqObjectActionQueueEntryCreate(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    result = ExAllocatePool2(256, v_rdi + 32, (unsigned int)(0x58706E50ULL), a4);
    *(unsigned __int64 *)(a2) = result;
    if (result == 0) goto loc_00A4419A;
    *(unsigned __int64 *)(result + 16) = a1;
    result = (v_rdi + 1) + 1;
    *(unsigned __int64 *)(result + 24) = result;
loc_00A44187:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_00A4419A:
    goto loc_00A44187;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqObjectActionQueueEntryCreate(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    result = ExAllocatePool2(256, local_rdi + 32, (uint32_t)(0x58706E50ULL), a4);
    *(uint64_t *)(arg2) = result;
    if (result == 0) goto loc_00A4419A;
    *(void **)(result + 0x10) = Arg1;
    result = (local_rdi + 1) + 1;
    *(uint64_t *)(result + 0x18) = result;
loc_00A44187:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_00A4419A:
    goto loc_00A44187;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A44138&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A44138[BB_00A44138]
  bb_00A4416D[BB_00A4416D]
  bb_00A44187[BB_00A44187]
  bb_00A44199[BB_00A44199]
  bb_00A4419A[BB_00A4419A]
  bb_00A44138 -->|branch| bb_00A4419A
  bb_00A44138 -->|fallthrough| bb_00A4416D
  bb_00A4416D -->|flow| bb_00A44187
  bb_00A44199 -->|flow| bb_00A4419A
  bb_00A4419A -->|branch| bb_00A44187
```
