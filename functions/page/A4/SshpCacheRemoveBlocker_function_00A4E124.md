# SshpCacheRemoveBlocker

- RVA: `0x00A4E124`–`0x00A4E153` (길이 `47` bytes)
- VA: `0x0000000140A4E124`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097934`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A4E148` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (function, `0x003EE750`)

### Direct callers
- [SleepstudyHelperDestroyLibrary](../77/SleepstudyHelperDestroyLibrary_function_00774720.md) at `0x007747E4`
- [SshpUnlinkBlockerFromLibrary](SshpUnlinkBlockerFromLibrary_function_00A4E0C8.md) at `0x00A4E0EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4E148` → [RtlDeleteElementGenericTableAvl](../../text/3E/RtlDeleteElementGenericTableAvl_function_003EE750.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4E124  48 8B C4                        mov rax, rsp
00A4E127  48 83 EC 38                     sub rsp, 0x38
00A4E12B  83 79 2C 00                     cmp dword ptr [rcx + 0x2c], 0
00A4E12F  74 1C                           je 0x140a4e14d
00A4E131  83 60 EC 00                     and dword ptr [rax - 0x14], 0
00A4E135  48 83 C1 30                     add rcx, 0x30
00A4E139  48 89 50 F0                     mov qword ptr [rax - 0x10], rdx
00A4E13D  48 8D 50 E8                     lea rdx, [rax - 0x18]
00A4E141  C7 40 E8 01 00 00 00            mov dword ptr [rax - 0x18], 1
00A4E148  E8 03 06 9A FF                  call 0x1403ee750
00A4E14D  48 83 C4 38                     add rsp, 0x38
00A4E151  C3                              ret
00A4E152  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpCacheRemoveBlocker(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    result = v_rsp;
    if ((*(unsigned int *)(a1 + 44)) != 0) {
        a1 = (a1) + (48);
        *(unsigned __int64 *)(v_rsp - 16) = a2;
        a2 = v_rsp - 24;
        *(unsigned int *)(v_rsp - 24) = 1;
        result = RtlDeleteElementGenericTableAvl(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SshpCacheRemoveBlocker(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    result = local_rsp;
    if ((*(uint32_t *)(arg1 + 0x2C)) != 0) {
        Arg1 = (Arg1) + (48);
        *(uint64_t *)(local_rsp - 0x10) = Arg2;
        Arg2 = local_rsp - 24;
        *(uint32_t *)(local_rsp - 0x18) = 1;
        result = RtlDeleteElementGenericTableAvl(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2C` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4E124&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4E124[BB_00A4E124]
  bb_00A4E131[BB_00A4E131]
  bb_00A4E14D[BB_00A4E14D]
  bb_00A4E152[BB_00A4E152]
  bb_00A4E124 -->|branch| bb_00A4E14D
  bb_00A4E124 -->|fallthrough| bb_00A4E131
  bb_00A4E131 -->|flow| bb_00A4E14D
```
