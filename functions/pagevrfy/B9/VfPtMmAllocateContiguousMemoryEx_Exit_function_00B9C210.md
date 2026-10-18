# VfPtMmAllocateContiguousMemoryEx_Exit

- RVA: `0x00B9C210`–`0x00B9C24A` (길이 `58` bytes)
- VA: `0x0000000140B9C210`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B9C219` → [VfIsKernelVerificationOn](../../text/4F/VfIsKernelVerificationOn_function_004FCC90.md) (function, `0x004FCC90`)
- `0x00B9C23E` → [VfPtMiscPoolNotification](../../text/3F/VfPtMiscPoolNotification_function_003FF310.md) (function, `0x003FF310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B9C219` → [VfIsKernelVerificationOn](../../text/4F/VfIsKernelVerificationOn_function_004FCC90.md) (`PAGEVRFY` → `.text`)
  - `0x00B9C23E` → [VfPtMiscPoolNotification](../../text/3F/VfPtMiscPoolNotification_function_003FF310.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9C210  40 53                           push rbx
00B9C212  48 83 EC 20                     sub rsp, 0x20
00B9C216  48 8B D9                        mov rbx, rcx
00B9C219  E8 72 0A 96 FF                  call 0x1404fcc90
00B9C21E  84 C0                           test al, al
00B9C220  75 21                           jne 0x140b9c243
00B9C222  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00B9C226  48 8B 08                        mov rcx, qword ptr [rax]
00B9C229  48 85 C9                        test rcx, rcx
00B9C22C  74 15                           je 0x140b9c243
00B9C22E  48 8B 53 40                     mov rdx, qword ptr [rbx + 0x40]
00B9C232  45 33 C9                        xor r9d, r9d
00B9C235  41 B8 43 6F 6E 54               mov r8d, 0x546e6f43
00B9C23B  48 8B 12                        mov rdx, qword ptr [rdx]
00B9C23E  E8 CD 30 86 FF                  call 0x1403ff310
00B9C243  48 83 C4 20                     add rsp, 0x20
00B9C247  5B                              pop rbx
00B9C248  C3                              ret
00B9C249  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfPtMmAllocateContiguousMemoryEx_Exit(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = VfIsKernelVerificationOn(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B9C243;
    result = *(unsigned __int64 *)(a1 + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 64);
        a4 = 0;
        a3 = 0x546E6F43ULL;
        a2 = *(unsigned __int64 *)(a2);
        result = VfPtMiscPoolNotification(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfPtMmAllocateContiguousMemoryEx_Exit(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = VfIsKernelVerificationOn(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B9C243;
    result = *(uint64_t *)(arg1 + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) != 0) {
        Arg2 = *(uint64_t *)(arg1 + 0x40);
        Arg4 = 0;
        Arg3 = 0x546E6F43ULL;
        Arg2 = *(uint64_t *)(Arg2);
        result = VfPtMiscPoolNotification(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8)), Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9C210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9C210[BB_00B9C210]
  bb_00B9C222[BB_00B9C222]
  bb_00B9C22E[BB_00B9C22E]
  bb_00B9C243[BB_00B9C243]
  bb_00B9C249[BB_00B9C249]
  bb_00B9C210 -->|branch| bb_00B9C243
  bb_00B9C210 -->|fallthrough| bb_00B9C222
  bb_00B9C222 -->|branch| bb_00B9C243
  bb_00B9C222 -->|fallthrough| bb_00B9C22E
  bb_00B9C22E -->|flow| bb_00B9C243
```
